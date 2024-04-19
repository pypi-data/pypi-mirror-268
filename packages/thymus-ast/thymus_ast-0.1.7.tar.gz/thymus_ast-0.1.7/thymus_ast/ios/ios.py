from __future__ import annotations

import sys
import re

from dataclasses import dataclass
from typing import Optional, Any
from collections import deque

if sys.version_info.major == 3 and sys.version_info.minor >= 9:
    from collections.abc import Generator, Callable
else:
    from typing import Generator, Callable


STOP_LIST = (
    'exit-address-family',
    'end',
)
SA_REGEXP = r'^route-map\s|^interface\s'
SA_SECTIONS = (
    'route-map',
    'interface',
)


@dataclass
class Root:
    name: str
    version: str
    delimiter: str
    path: str
    children: list[Node]
    heuristics: list[Node]
    stubs: list[str]
    begin: int
    end: int
    is_accessible: bool


@dataclass
class Node:
    name: str
    path: str
    parent: Node | Root
    children: list[Node]
    heuristics: list[Node]
    stubs: list[str]
    begin: int
    end: int
    is_accessible: bool


def read_config(filename: str, encoding='utf-8-sig') -> list[str]:
    try:
        with open(filename, encoding=encoding) as f:
            return f.readlines()
    except FileNotFoundError:
        return []


def get_spaces(line: str) -> int:
    if m := re.search(r'^(\s+)', line):
        return len(m.group(1))
    return 0


def check_child(name: str, children: list[Node]) -> Optional[Node]:
    for child in children:
        if child.name == name:
            return child
    return None


def make_nodes(path: str, parent: Root | Node, delimiter: str) -> Node:
    parts = path.split()
    current: Root | Node = parent
    for number, elem in enumerate(parts):
        child = check_child(elem, current.children)
        if not child:
            xpath = f'{delimiter}'.join(parts[: number + 1])
            if parent.name != 'root':
                xpath = f'{parent.path}{delimiter}{xpath}'
            new_node = Node(elem, xpath, current, [], [], [], 0, 0, False)
            current.children.append(new_node)
            current = new_node
        else:
            current = child
    current.is_accessible = True
    return current


def step_back(node: Node, config: list[str], steps: int) -> Optional[Root | Node]:
    current: Node | Root = node
    while True:
        if type(current) is Root:
            break
        assert type(current) is Node
        current = current.parent
        if current.is_accessible:
            line = config[current.begin - 1][:-1]
            spaces = get_spaces(line)
            if steps > spaces:
                return current
    return None


def chop_tree(node: Node) -> None:
    marked: list[int] = []
    for number, child in enumerate(node.heuristics):
        if len(child.stubs) <= 1:
            marked.append(number)
    for number in reversed(marked):
        del node.heuristics[number]


def heuristics_parse(node: Root | Node, delimiter: str, is_crop: bool) -> None:
    if not node.stubs:
        return
    for stub in node.stubs:
        parts: list[str] = []
        if stub.startswith('no '):
            parts = stub[3:].split()
        elif re.match(r'^\d+\s', stub):
            parts = re.sub(r'^\d+\s', '', stub).split()
        else:
            parts = stub.split()
        current = node
        # a little bit the same as the make_nodes()
        # but I don't want to mix them together for clarity purposes
        for number, elem in enumerate(parts):
            child = check_child(elem, current.heuristics)
            if not child:
                xpath = f'{delimiter}'.join(parts[: number + 1])
                if node.name != 'root':
                    xpath = f'{node.path}{delimiter}{xpath}'
                new_node = Node(elem, xpath, current, [], [], [], 0, 0, False)
                if is_crop:
                    new_node.stubs.append(' '.join(parts[number + 1 :]))
                else:
                    new_node.stubs.append(stub)
                current.heuristics.append(new_node)
                current = new_node
            else:
                if is_crop:
                    child.stubs.append(' '.join(parts[number + 1 :]))
                else:
                    child.stubs.append(stub)
                current = child
    chop_tree(node)


def recursive_node_lookup(
    node: Root | Node, is_child: bool, callback: Callable[[Node, Any], None], **kwargs: Any
) -> None:
    target: list[Node] = node.children if is_child else node.heuristics
    for child in target:
        inner_target: list[Node] = child.children if is_child else child.heuristics
        if inner_target:
            recursive_node_lookup(child, is_child, callback, **kwargs)
        callback(child, **kwargs)


def lazy_provide_config(
    config: list[str], node: Root | Node, *, alignment: int, is_started: bool = False
) -> Generator[str, None, None]:
    if not node.is_accessible:
        return
    try:
        begin: int = 0
        end: int = node.end + 1
        if node.name != 'root':
            begin = node.begin - 1
        if config[end - 1].strip() != '!' and not config[end - 1].strip().startswith('exit-'):
            # some sections don't stop at '!' or 'exit-...' lines
            # they can overlap with the next section
            end -= 1
        depth: int = 0
        prev_spaces: int = 0
        for pos in range(begin, end):
            if not config[pos]:
                continue
            elif config[pos] == '\n':
                yield config[pos]
                continue
            spaces = get_spaces(config[pos])
            if not is_started:
                if spaces > 0:
                    yield config[pos].strip()
                elif spaces == 0:
                    is_started = True
                    yield config[pos].strip()
            else:
                if spaces > prev_spaces:
                    depth += 1
                    prev_spaces = spaces
                    yield f'{" " * alignment * depth}{config[pos].strip()}'
                elif spaces == prev_spaces:
                    yield f'{" " * alignment * depth}{config[pos].strip()}'
                else:
                    if spaces > 0:
                        depth -= 1
                        yield f'{" " * alignment * depth}{config[pos].strip()}'
                        prev_spaces = spaces
                    else:
                        depth = 0
                        prev_spaces = 0
                        yield config[pos].strip()
    except IndexError:
        return


def search_node(path: deque[str], node: Root | Node) -> Optional[Node]:
    """
    This function searches for a node based on the path argument.
    It also eats the path from its head.
    """
    step = path.popleft()
    for child in node.children:
        if child.name.lower() == step.lower():
            if not path:
                if child.is_accessible:
                    return child
                else:
                    return None
            return search_node(path, child)
    return None


def search_h_node(path: deque[str], node: Root | Node) -> Optional[Node]:
    """
    This function searches for a heuristic node based on the path argument.
    It also eats the path from its head.
    """
    step = path.popleft()
    for child in node.heuristics:
        if child.name.lower() == step.lower():
            if not path:
                return child
            return search_h_node(path, child)
    return None


def analyze_heuristics(root: Root, delimiter: str, is_crop: bool) -> None:
    """
    This function analyzes all stubs lists from the root down to the bottom and aggregates common parts
        to new sections inside heuristics list.
    `is_crop` allows a user to save only the unique parts of a stub string.
    """
    heuristics_parse(root, delimiter=delimiter, is_crop=is_crop)
    recursive_node_lookup(root, is_child=False, callback=chop_tree)
    recursive_node_lookup(root, is_child=True, callback=heuristics_parse, delimiter=delimiter, is_crop=is_crop)


def analyze_sections(root: Root, delimiter: str, cache: list[tuple[int, str]]) -> None:
    def __get_begin_end(children: list[Node]) -> tuple[int, int]:
        begin: int = -1
        end: int = -1
        for child in children:
            if child.is_accessible:
                if begin == -1:
                    begin = child.begin
                else:
                    begin = min(begin, child.begin)
                end = max(end, child.end)
            else:
                x, y = __get_begin_end(child.children)
                if begin == -1:
                    begin = x
                else:
                    begin = min(begin, x)
                end = max(end, y)
        return begin, end

    if root.name != 'root':
        return
    for number, line in cache:
        node = make_nodes(line, root, delimiter)
        node.begin = number
        node.end = number
    for child in root.children:
        if child.name in SA_SECTIONS:
            begin, end = __get_begin_end(child.children)
            child.begin = begin
            child.end = end
            child.is_accessible = True
            if child.name == 'route-map':
                for rm in child.children:
                    begin, end = __get_begin_end(rm.children)
                    rm.begin = begin
                    rm.end = end
                    rm.is_accessible = True


def construct_tree(
    config: list[str],
    *,
    delimiter: str = '^',
    is_heuristics: bool = False,
    is_base_heuristics: bool = False,
    is_crop: bool = False,
    is_promisc: bool = False,
) -> Optional[Root]:
    current: Root | Node = Root(
        name='root',
        version='',
        delimiter=delimiter,
        path='',
        children=[],
        heuristics=[],
        stubs=[],
        begin=0,
        end=0,
        is_accessible=True,
    )
    root = current
    bom_symbol = '\ufeff'
    prev_line: str = ''
    step: int = 0  # step tells how deep the next section is
    final: int = 0
    if not is_promisc:
        for index in range(len(config) - 1, 0, -1):
            if config[index] == '\n':
                continue
            elif config[index].strip() == 'end':
                break
        else:
            return None
    config.append('!\n')  # for the cases when the last section is not properly closed
    s_cache: list[tuple[int, str]] = []
    skip_mode: bool = True  # to skip lines preceding the version keyword
    c_block: bool = False  # to stop adding stubs and start accumulating c_buffer
    c_buffer: str = ''
    # LOOKAHEAD ALGO
    for number, line in enumerate(config):
        final = number
        if bom_symbol in line:
            # in case, when file is UTF-8 encoded with BOM
            # but opened with UTF-8 encoding and errors ignoring mode
            line = line.replace(bom_symbol, '')
        if skip_mode and line.startswith('version '):
            skip_mode = False
        if skip_mode:
            continue
        line = line.rstrip()
        if not line:
            continue
        if not prev_line:
            prev_line = line
            continue
        prev_spaces = get_spaces(prev_line)
        spaces = get_spaces(line)
        if spaces > prev_spaces:
            step = spaces - prev_spaces
            current = make_nodes(prev_line.strip(), current, delimiter)
            current.begin = number
        elif spaces < prev_spaces:
            if not step:
                continue
            stripped = prev_line.strip()
            if not c_block and not stripped.startswith('!') and stripped not in STOP_LIST:
                current.stubs.append(stripped)
            # If the last line of a section is found during inside_block
            # it must contain ^C
            if c_block:
                if stripped.endswith('^C'):
                    c_buffer += stripped
                    current.stubs.append(c_buffer)
                    c_buffer = ''
                    c_block = False
                else:
                    return None
            current.end = number
            temp = current
            if current.name == 'root':
                return None
            if not spaces:
                # We are definitely heading the root
                current = root
            else:
                current = step_back(current, config, prev_spaces - step)
            if not current:
                return None
            if current.name == 'root':
                last_end = temp.end
                while temp.name != 'root':
                    if temp.is_accessible and not temp.end:
                        temp.end = last_end
                    temp = temp.parent
        else:
            stripped = prev_line.strip()
            if not c_block:
                if not stripped.startswith('!') and stripped not in STOP_LIST:
                    if stripped.endswith('^C'):
                        c_block = True
                        c_buffer = stripped
                    else:
                        current.stubs.append(stripped)
                        if current.name == 'root' and is_base_heuristics and re.search(SA_REGEXP, stripped):
                            s_cache.append((number, stripped))
                            current.stubs = current.stubs[:-1]
                if current.name == 'root' and stripped.startswith('version '):
                    parts = stripped.split()
                    if len(parts) == 2:
                        current.version = parts[1]
            else:
                if stripped.endswith('^C'):
                    c_buffer += '\n'
                    c_buffer += stripped
                    current.stubs.append(c_buffer)
                    c_buffer = ''
                    c_block = False
                else:
                    c_buffer += '\n'
                    c_buffer += stripped
        prev_line = line
    if skip_mode:
        # If all passes through the config don't turn this flag off
        # That means the tree is empty.
        return None
    current.end = final
    if current.name != 'root':
        return None
    if is_heuristics:
        analyze_heuristics(current, delimiter, is_crop)
    if is_base_heuristics:
        analyze_sections(current, delimiter, s_cache)
    return current
