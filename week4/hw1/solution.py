import os
import tempfile
from random import randint

class File:
    def __init__(self, filename):
        self.name = filename
        if not os.path.exists(filename):
            with open(filename, "w"):
                pass
    
    def __add__(self, obj):
        path = os.path.join(tempfile.gettempdir(), str(randint(0, 1000000000)))
        while os.path.exists(path):
            path = os.path.join(tempfile.gettempdir(), str(randint(0, 1000000000)))
        f = File(path)
        f.write(self.read() + obj.read())
        return f

    def __str__(self):
        return os.path.abspath(self.name)

    def __iter__(self):
        self.it = self.read()
        self.it = [x+'\n' for x in self.it.split('\n')[:-1]]
        
        self.cur = 0
        self.end = len(self.it)
        return self

    def __next__(self):
        if self.cur < self.end:
            res = self.it[self.cur]
            self.cur += 1
            return res
        else:
            raise StopIteration
                   

    def read(self):
        with open(self.name, "r") as f:
            return f.read()

    def write(self, s):
        with open(self.name, "w") as f:
            f.write(s)
        return(len(s))
        
