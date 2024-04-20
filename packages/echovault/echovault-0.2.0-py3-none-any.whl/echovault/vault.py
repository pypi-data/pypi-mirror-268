from dulwich.objects import Tree, Commit
from echovault.table import Table
from base64 import b64decode, b64encode
from socket import getfqdn, gethostname
from os import getpid, getuid, getgid, getlogin, name as operating_system_name
from sys import argv
from typing import Optional
from time import time
from stat import S_IFDIR

class Vault:
    @staticmethod
    def encode(string):
        return string.encode('utf-8')

    @staticmethod
    def decode(value):
        return b64decode(value).decode('utf-8')
    
    def __init__(self, object_store, refs, *, tree:Tree=None, ref=None):
        self.object_store = object_store
        self.refs = refs
        self.ref = ref

        if ref is not None:
            if ('refs/heads/' + ref) in self.refs and tree is None:
                tree = self.object_store[self.refs['refs/heads/' + ref]]
        
        if tree is None:
            self._tree = Tree()
        else:
            self._tree = tree

    def _update(self):
        if not self._tree.id in self.object_store:
            self.object_store.add_object(self._tree)
            
    def __getitem__(self, name:str):
        identifier = self.encode(name)
        _, oid = self._tree[identifier]
        tree = self.object_store[oid]
        return Table(self.object_store,
                     self,
                     identifier,
                     tree=tree)

    def __setitem__(self, name:str, iterable):
        identifier = self.encode(name)
        table = Table(self.object_store, self, identifier, iterable)
        self._tree[identifier] = S_IFDIR, table.tree.id
        self._update()

    def __delitem__(self, name:str):
        del self._tree[self.encode(name)]
        self._update()

    def __iter__(self):
        return (self.decode(raw_key)
                for raw_key
                in iter(self._tree))

    def commit(self,
               ref:Optional[str]=None,
               message:Optional[str]='',
               author:Optional[str]=None,
               committer:Optional[str]=None,
               time_:Optional[int]=None,
               timezone:Optional[int]=None,
               ):
        if ref is None:
            ref = self.ref
            
        ref = ('refs/heads/' + ref).encode('utf-8')
        commit = Commit()
        
        commit.message = message.encode('utf-8')
        commit.tree = self._tree

        if committer is None:
            committer = ('_'.join((getfqdn(), gethostname(),
                                   operating_system_name,
                                   repr(getgid()),
                                   repr(getuid()), repr(getpid())))
                         + ': '
                         + ' '.join(argv))
            
        if author is None:
            author = getlogin()

        commit.committer = committer.encode('utf-8')
        commit.author = author.encode('utf-8')

        if time_ is None:
            time_ = int(time())

        if timezone is None:
            timezone = 0

        commit.commit_time = time_
        commit.commit_timezone = timezone
        commit.author_time = time_
        commit.author_timezone = timezone

        try:
            parents = (self.refs[ref],)
        except:
            parents = ()
            
        commit.parents = parents
        
        if not commit.id in self.object_store:
            self.object_store.add_object(commit)

        self.refs[ref] = commit.id
