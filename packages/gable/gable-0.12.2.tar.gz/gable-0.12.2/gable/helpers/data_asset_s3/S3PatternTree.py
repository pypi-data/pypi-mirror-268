class S3PatternTree:
    def __init__(self):
        self.root = S3PatternTree.Node("root")

    def print(self):
        self._print(self.root, 0)

    def _print(self, node: "S3PatternTree.Node", level: int):
        print("  " * level, node.name)
        for child in node.children:
            self._print(child, level + 1)

    def add_filepath(self, filepath: str):
        raise NotImplementedError

    def add_pattern(self, pattern: str):
        raise NotImplementedError

    class Node:
        children: set["S3PatternTree.Node"]

        def __init__(self, name):
            self.name = name
            self.children = set()

        def __hash__(self) -> int:
            return hash(self.name)
