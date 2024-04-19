from __future__ import annotations

import sys
import re

from typing import TypedDict, Optional
from collections import deque
from copy import copy

if sys.version_info.major == 3 and sys.version_info.minor >= 9:
    from collections.abc import Generator, Iterable
else:
    from typing import Generator, Iterable


class Root(TypedDict):
    name: str
    version: str
    children: list[Node]
    stubs: list[str]
    delimiter: str


class Node(TypedDict):
    name: str
    parent: Node | Root
    children: list[Node]
    stubs: list[str]
    path: str
    is_closed: bool
    is_inactive: bool
    is_protected: bool


def unstrict_compare(left: list[str], right: list[str]) -> bool:
    """
    Function compares the two lists and returns True whether they are equal.
    For every list element, an extra argument is accounted for to cover cases
        when these elements are inactive and/or protected.
    """
    if len(left) != len(right):
        return False
    dleft = deque(left)
    dright = deque(right)
    extra_pattern = r'(?:inactive: |protect: ){1,2}'
    while True:
        lml = dleft.popleft()
        lmr = dright.popleft()
        if lml == lmr or re.match(extra_pattern + lml, lmr) or re.match(extra_pattern + lmr, lml):
            if dleft or dright:
                continue
            return True
        return False


def parser(data: list[str], path: str, *, delimiter='^', is_greedy=False) -> tuple[list[str], list[str]]:
    sections: list[str] = []
    params: list[str] = []
    container: list[str] = []
    parts: list[str] = path.split(delimiter) if path else []
    plen = len(parts)
    start: int = 0
    end: int = 0
    for number, line in enumerate(data):
        stripped = line.strip()
        if '{' in stripped and '}' not in stripped and ';' not in stripped:
            sections.append(stripped)
        elif '}' in stripped and '{' not in stripped and ';' not in stripped:
            if len(parts) == len(sections) and unstrict_compare(parts, [x[:-2] for x in sections]):
                if container:
                    container.append('}')
                    end = number
                if is_greedy:
                    del data[start : end + 1]
                return container, params
            sections.pop()
        elif ';' in stripped and '{' not in stripped and '}' not in stripped:
            if len(parts) == len(sections) and unstrict_compare(parts, [x[:-2] for x in sections]):
                params.append(stripped)
        else:
            continue
        if len(sections) >= len(parts) and unstrict_compare(parts, [x[:-2] for x in sections[:plen]]):
            if stripped and not ('{' in stripped and '}' in stripped):
                if not start:
                    start = number
                container.append(stripped)
    return container, params


def lazy_parser(data: Iterable[str], path: str, delimiter='^') -> Generator[str, None, None]:
    sections: list[str] = []
    parts: list[str] = path.split(delimiter) if path else []
    plen = len(parts)
    for line in data:
        stripped = line.strip()
        if '{' in stripped and '}' not in stripped and ';' not in stripped:
            sections.append(stripped)
        elif '}' in stripped and '{' not in stripped and ';' not in stripped:
            if len(parts) == len(sections) and unstrict_compare(parts, [x[:-2] for x in sections]):
                return
            sections.pop()
        if len(sections) >= plen and unstrict_compare(parts, [x[:-2] for x in sections[:plen]]):
            if stripped and not ('{' in stripped and '}' in stripped):
                yield stripped


def wc_parser(
    data: list[str], path: str, pattern: str, delimiter='^'
) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    if pattern.startswith('^'):
        pattern = pattern[1:]
        if not pattern:
            return {}, {}
    pattern = r'^(?:inactive: |protect: ){1,2}' + pattern
    sections: list[str] = []
    container: dict[str, list[str]] = {}
    params: dict[str, list[str]] = {}
    parts = path.split(delimiter) if path else []
    plen = len(parts)
    for line in data:
        stripped = line.strip()
        if '{' in stripped and '}' not in stripped and ';' not in stripped:
            sections.append(stripped)
            if parts == [x[:-2] for x in sections[:-1]]:
                if re.match(pattern, sections[-1], re.I):
                    key = sections[-1][:-2]
                    container[key] = []
                    params[key] = []
        elif '}' in stripped and '{' not in stripped and ';' not in stripped:
            if parts == [x[:-2] for x in sections[:-1]]:
                if re.match(pattern, sections[-1], re.I):
                    key = sections[-1][:-2]
                    if r := container.get(key):
                        r.append('}')
                    return container, params
            sections.pop()
        elif ';' in stripped and '{' not in stripped and '}' not in stripped:
            if (
                len(sections) == plen + 1
                and parts == [x[:-2] for x in sections[:plen]]
                and re.match(pattern, sections[plen], re.I)
            ):
                key = sections[plen][:-2]
                params[key].append(stripped)
        if stripped and parts == [x[:-2] for x in sections[:plen]]:
            if len(sections) > plen and re.match(pattern, sections[plen], re.I):
                container[sections[plen][:-2]].append(stripped)
    return container, params


def lazy_wc_parser(data: Iterable[str], path: str, pattern: str, delimiter='^') -> Generator[str, None, None]:
    if pattern.startswith('^'):
        pattern = pattern[1:]
        if not pattern:
            return
    pattern = r'^(?:inactive: |protect: ){1,2}' + pattern
    sections: list[str] = []
    parts: list[str] = path.split(delimiter) if path else []
    plen = len(parts)
    for line in data:
        stripped = line.strip()
        if '{' in stripped and '}' not in stripped and ';' not in stripped:
            sections.append(stripped)
        elif '}' in stripped and '{' not in stripped and ';' not in stripped:
            if parts == [x[:-2] for x in sections[:-1]]:
                if re.match(pattern, sections[-1][:-2], re.S):
                    yield '}'
            sections.pop()
        if stripped and parts == [x[:-2] for x in sections[:plen]]:
            if len(sections) > plen and re.match(pattern, sections[plen][:-2], re.S):
                yield stripped


def provide_config(data: Iterable[str], block=' ' * 2) -> str:
    depth = 0
    result = ''
    flag = False
    for line in data:
        stripped = line.strip()
        if '{' in stripped and ';' not in stripped:
            depth += 1
            flag = True
        elif '}' in stripped and ';' not in stripped:
            if depth:
                depth -= 1
        prepend = block * depth
        if flag:
            prepend = block * (depth - 1)
            flag = False
        result += f'{prepend}{stripped}\n'
    return result


def lazy_provide_config(data: Iterable[str], block=' ' * 2) -> Generator[str, None, None]:
    depth = 0
    flag = False
    for line in data:
        stripped = line.strip()
        if '{' in stripped and '}' not in stripped and ';' not in stripped:
            depth += 1
            flag = True
        elif '}' in stripped and '{' not in stripped and ';' not in stripped:
            if depth:
                depth -= 1
        prepend = block * depth
        if flag:
            prepend = block * (depth - 1)
            flag = False
        yield f'{prepend}{stripped}'


def construct_path(node: Node, delimiter='^') -> str:
    name = node.get('name')
    if not name:
        raise Exception('This node is without a name.')
    while True:
        parent = node.get('parent')
        if not parent:
            break
        extra = construct_path(parent, delimiter)
        return f'{extra}{delimiter}{name}'
    return name


def construct_tree(data: list[str], delimiter='^') -> Root:
    """
    This function goes through the config file and constructs the tree every leaf of which is a config section.
    """
    root = Root(name='root', version='', children=[], stubs=[], delimiter=delimiter)
    current_node: Root | Node = root
    section_regexp = r'^([^{]+)\s{'
    stub_regexp = r'^([^;]+;)'
    bom_symbol = '\ufeff'
    for line in data:
        if bom_symbol in line:
            # in case, when file is UTF-8 encoded with BOM
            # but opened with UTF-8 encoding and errors ignoring mode
            line = line.replace(bom_symbol, '')
        stripped = line.strip()
        if '{' in stripped and '}' not in stripped and ';' not in stripped:
            m = re.search(section_regexp, stripped)
            if not m:
                raise Exception('Incorrect configuration format detected.')
            section_name = m.group(1)
            if 'inactive: ' in section_name:
                section_name = section_name.replace('inactive: ', '', 1)
            if 'protect: ' in section_name:
                section_name = section_name.replace('protect: ', '', 1)
            section_name = section_name.strip()
            node = Node(
                name=section_name,
                parent=current_node,
                children=[],
                stubs=[],
                path='',
                is_closed=False,
                is_inactive='inactive: ' in m.group(1),
                is_protected='protect: ' in m.group(1),
            )
            node['path'] = construct_path(node, delimiter).replace(f'root{delimiter}', '')
            current_node['children'].append(node)
            current_node = node
        elif '}' in stripped and '{' not in stripped and ';' not in stripped:
            current_node['is_closed'] = True
            current_node = current_node['parent']
        elif ';' in stripped and '{' not in stripped and '}' not in stripped:
            m = re.search(stub_regexp, stripped)
            if not m:
                raise Exception('Incorrect configuration format detected. Wrong stub.')
            stub = m.group(1)
            current_node['stubs'].append(stub)
            if stub.startswith('version ') and current_node['name'] == 'root':
                parts = stub.split()
                if len(parts) == 2:
                    root['version'] = parts[1]
    return root


def search_node(path: deque[str], node: Root | Node) -> Optional[Node]:
    step = path.popleft()
    step = step.lower()
    if '.' in step and node['name'] == 'interfaces':
        try:
            ifd, ifl = step.split('.')
        except ValueError:
            return None
        if not ifl.isdigit():
            return None
        step = ifd
        path.appendleft(f'unit {ifl}')
    children = node.get('children', [])
    if not children:
        return None
    for child in children:
        name = child['name']
        name = name.lower()
        if name == step:
            if not path:
                return child
            return search_node(path, child)
    else:
        if not path:
            return None
        extra_step = path.popleft()
        path.appendleft(f'{step} {extra_step}')
        return search_node(path, node)


def compare_nodes(target: Root | Node, peer: Root | Node) -> Root | Node:
    def copy_node(type: str, origin: Node, parent: Root | Node) -> Node:
        node: Node = copy(origin)
        node['type'] = type
        node['parent'] = parent
        node['children'] = []
        return node

    if target['name'] != peer['name']:
        raise Exception('Nodes are not on the same level.')
    new_target = copy(target)
    new_target['children'] = []
    new_target['type'] = 'common'
    peers_children = copy(peer['children'])
    for child in target['children']:
        for peer_child in peer['children']:
            if child['name'] == peer_child['name']:
                peers_children.remove(peer_child)
                if next_node := compare_nodes(child, peer_child):
                    next_node['parent'] = new_target
                    new_target['children'].append(next_node)
                break
        else:
            copied_child = copy_node('new', child, new_target)
            new_target['children'].append(copied_child)
    for child in peers_children:
        copied_child = copy_node('lost', child, new_target)
        new_target['children'].append(copied_child)
    if new_target['name'] != 'root':
        if new_target['is_protected'] != peer['is_protected']:
            if new_target['is_protected']:
                new_target['name'] = 'protect:(-) ' + new_target['name']
            else:
                new_target['name'] = 'protect:(+): ' + new_target['name']
        if new_target['is_inactive'] != peer['is_inactive']:
            if new_target['is_inactive']:
                new_target['name'] = 'inactive:(-) ' + new_target['name']
            else:
                new_target['name'] = 'inactive:(+): ' + new_target['name']
    ts = set(target['stubs'])
    ps = set(peer['stubs'])
    new_target['diff'] = []
    new_target['diff'].extend([('+', x) for x in ts - ps])
    new_target['diff'].extend([('-', x) for x in ps - ts])
    if not new_target['diff'] and not new_target['children']:
        return {}
    return new_target


def search_inactives(tree: Root | Node) -> Root | Node:
    new_tree = copy(tree)
    new_tree['children'] = []
    for child in tree['children']:
        if node := search_inactives(child):
            new_tree['children'].append(node)
            node['parent'] = new_tree
    inactives = [x for x in filter(lambda x: x.startswith('inactive: '), tree['stubs'])]
    if tree['name'] != 'root' and not tree['is_inactive'] and not inactives:
        if new_tree['children']:
            return new_tree
        return {}
    new_tree['inactives'] = inactives
    return new_tree


def draw_diff_tree(tree: Root | Node, start: str) -> Generator[str, None, None]:
    if tree['name'] != start:
        if tree['type'] in ('new', 'lost'):
            sign = '+' if tree['type'] == 'new' else '-'
            yield f'{sign} {tree["name"]} {{'
            yield '...'
        else:
            yield f'{tree["name"]} {{'
    for child in tree['children']:
        for x in draw_diff_tree(child, start):
            yield x
    if 'diff' in tree and tree['diff']:
        for x, y in tree['diff']:
            yield f'{x} {y}'
    if tree['type'] in ('new', 'lost'):
        sign = '+' if tree['type'] == 'new' else '-'
        yield f'{sign} }}'
    else:
        if tree['name'] != start:
            yield '}'


def draw_inactive_tree(tree: Root | Node, start: str) -> Generator[str, None, None]:
    if tree['name'] != start:
        if tree['name'] == 'root':
            yield tree['name']
        elif tree['is_inactive']:
            yield f'inactive: {tree["name"]} {{'
        else:
            yield f'{tree["name"]} {{'
    for child in tree['children']:
        for x in draw_inactive_tree(child, start):
            yield x
    for stub in tree.get('inactives', []):
        yield stub
    if tree['name'] != start:
        yield '}'


def make_path(line_path: str) -> deque[str]:
    return deque(line_path.split())
