from ast import AST, NodeVisitor, For, If, While
from typing import Generator, Any, Tuple, Type, List

import importlib.metadata as importlib_metadata


class Visitor(NodeVisitor):
    def __init__(self):
        self.errors: List[set] = []

    def find_child_nodes(self, node: Any, node_type_obj: Any) -> List[If]:
        had_node_type: List[bool] = [isinstance(child, node_type_obj) for child in node.body]
        if not any(had_node_type):
            return []
        return list(filter(lambda x: isinstance(x, node_type_obj), node.body)) or []

    def append_error(self, node_list, err_msg):
        for node in node_list:
            self.errors.append((
                node.lineno,
                node.col_offset,
                err_msg
            ))

    def find_nested_nodes(self, node):
        if_nodes: List[If] = self.find_child_nodes(node=node, node_type_obj=If)
        for_nodes: List[For] = self.find_child_nodes(node=node, node_type_obj=For)
        while_nodes: List[While] = self.find_child_nodes(node=node, node_type_obj=While)

        self.append_error(if_nodes, 'FNN100 nested if found')
        self.append_error(for_nodes, 'FNN101 nested for loop found')
        self.append_error(while_nodes, 'FNN102 nested while loop found')

    def visit_For(self, node: For) -> Any:
        self.find_nested_nodes(node)
        self.generic_visit(node)

    def visit_If(self, node: If) -> Any:
        self.find_nested_nodes(node)
        self.generic_visit(node)

    def visit_While(self, node: While) -> Any:
        self.find_nested_nodes(node)
        self.generic_visit(node)


class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: AST) -> None:
        self.tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self.tree)

        for error in visitor.errors:
            yield error + (type(self),)
