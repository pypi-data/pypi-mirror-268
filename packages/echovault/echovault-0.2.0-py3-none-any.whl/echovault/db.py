from dulwich.objects import Tree

class Database:
    def __init__(self, tree:Tree=None):
        if tree is None:
            self._tree = Tree()
        else:
            self._tree = tree
        
    def __getitem__(self, name:str):
        return Table.from_tree(self._tree[name])

    def __setitem__(self, name:str, iterable):
        table = Table(*iterable)
        self.tree[name] = table._tree

    def __delitem__(self, name:str):
        del self._tree[name]
