from dulwich.objects import Tree, Blob
from pickle import dumps, loads
from base64 import b64decode, b64encode
from stat import S_IFREG, S_IFDIR
from uuid import uuid4

class Entry:
    @staticmethod
    def encode(value):
        return b64encode(dumps(value))


    @staticmethod
    def decode(value):
        return loads(b64decode(value))
    
    def __init__(self, object_store, table, identifier, items=(), *, tree=None):
        self.object_store = object_store
        self.table = table
        self.identifier = identifier
        
        if tree is None:
            tree = Tree()

        self.tree = tree
        
        for key, value in (items.items()
                           if isinstance(items, dict)
                           else items):
            self[key] = value

        if not b'_' in self.tree:
            blob = Blob()
            
            if not blob.id in self.object_store:
                self.object_store.add_object(blob)
            
            self.tree[b'_'] = S_IFREG | 0o755, blob.id

        self._update()

    def _update(self):
        if not self.tree.id in self.object_store:
            self.object_store.add_object(self.tree)

        self.table.tree[self.identifier] = S_IFDIR, self.tree.id
            
        self.table._update()

    def __getitem__(self, key):
        _, id_ = self.tree[self.encode(key)]
        return loads(self.object_store[id_].data)

    def __setitem__(self, key, value):
        blob = Blob()
        blob.data = dumps(value)
        
        if not blob.id in self.object_store:
            self.object_store.add_object(blob)
            
        self.tree[self.encode(key)] = S_IFREG | 0o755, blob.id

        self._update()

    def __delitem__(self, key):
        del self.tree[self.encode(key)]
        
        self._update()
            
    def __iter__(self):
        return (self.decode(raw_key)
                for raw_key
                in iter(self.tree)
                if raw_key != b'_')

    def keys(self):
        yield from iter(self)

    def items(self):
        for key in self.keys():
            yield (key, self[key])

    def values(self):
        for _, value in self.items():
            yield value

    def __repr__(self):
        return repr(dict(self.items()))
            
class Table:
    def __init__(self, object_store, vault, identifier, values=(), *, tree=None):
        self.object_store = object_store
        self.vault = vault
        self.identifier = identifier
        
        if tree is None:
            tree = Tree()

        self.tree = tree
        self.extend(values)


        if not b'_' in self.tree:
            blob = Blob()
            
            if not blob.id in self.object_store:
                self.object_store.add_object(blob)
            
            self.tree[b'_'] = S_IFREG | 0o755, blob.id

        self._update()

    def _update(self):
        if not self.tree.id in self.object_store:
            self.object_store.add_object(self.tree)

        self.vault._tree[self.identifier] = S_IFDIR, self.tree.id
            
        self.vault._update()
            
    def __iter__(self):
        for key in self.tree:
            if key == b'_':
                continue
            
            _, id_ = self.tree[key]
            yield Entry(self.object_store,
                        self,
                        key,
                        tree=self.object_store[id_])
            

    def extend(self, iterable):
        for item in iterable:
            entry = Entry(self.object_store,
                          self,
                          str(uuid4()).encode('utf-8'),
                          item)
            self.tree[entry.identifier] = S_IFDIR, entry.tree.id

        self._update()
            
    def remove(self, entry):
        del self.tree[entry.identifier]
        
        self._update()
