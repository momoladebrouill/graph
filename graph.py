import random
'''class LL():
    def __init__(self):
        self.ls=list()
    def append(self,e):
        if e not in self.ls:
            self.ls.append(e)
            return 0
        return -1
    __repr__=lambda self:self.ls.__repr__()
    __iter__=lambda self:self.ls.__iter__()
    __next__=lambda self:self.ls.__next__()
    __getitem__=lambda self,v:self.ls.__getitem__(v)
'''
class S():
    def __init__(this,name:str):
        this.name=name;
        this.ng=list();
        this.entier=True;
        
    def addmany(self,others:iter):
        for elem in others:
            self.add(elem);
            
    def add(self,other):
        if type(other) is type(self):
            self.ng.append(other);
            other.ng.append(self);
        else:
            self.add(self.__class__(str(other)));

    def parcours(self,n):
        liste=[self];
        self.entier=False
        for k in range(n):
            nl=list();
            for yota in liste:
                for elem in yota.ng:
                    if elem.entier:
                        nl.append(elem);
                        elem.entier=False
            liste=nl;
        return liste;
    __repr__=lambda this:this.name;

walah=list()
word=lambda : ''.join(chr(random.randrange(65,90)) for i in range(10))
for i in range(20):
    walah.append(S(word()))
for elem in walah:
    for i in range(1,3):
        random.choice(walah).add(elem)