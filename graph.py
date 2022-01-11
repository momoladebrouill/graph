import random,tkinter,time
from colorsys import hsv_to_rgb

class drag():
    def __init__(s,e=None):
        s.obj,s.x,s.y=None,0,0
    def start(s,event):
        s.obj=c.find_closest(event.x,event.y)[0]
        s.x=event.x
        s.y=event.y
    
    def drag(s,event):
        dx=event.x-s.x
        dy=event.y-s.y
        c.move(s.obj,dx,dy)
        sommet=dico[s.obj]
        c.delete("LINEEEE")
        s.x=event.x
        s.y=event.y
        sommet.x,sommet.y=s.x,s.y
        s.update()
    def update(yuobala):
        for elem in g:
            c.create_text(elem.x,elem.y+10,text=elem.name,tags=("LINEEEE",))
            for ng in elem.ng:
                c.create_line(elem.x,elem.y,ng.x,ng.y,tags=("LINEEEE",))
        dico={}
        for elem in g:
            res=c.create_oval(elem.x-10,elem.y-10,elem.x+10,elem.y+10,fill=elem.coul,tags=('toma',))
            dico[res]=elem
            c.create_text(elem.x,elem.y+10,text=elem.name,tags=("LINEEEE",))
            for ng in elem.ng:
                c.create_line(elem.x,elem.y,ng.x,ng.y,tags=("LINEEEE",)) 
class S():
    def __init__(this):
        this.name=''.join(chr(random.randrange(65,90)) for i in range(3));
        this.coul="#%02x%02x%02x" % tuple([int(c) for c in hsv_to_rgb(random.random(),1,255)]);
        this.x,this.y=random.randrange(10,490),random.randrange(10,490)
        this.ng=list();
        this.visited=0;
        this.p=[];
        
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
        visitsession=hash(time.time())
        self.visited=visitsession
        for k in range(n):
            nl=list();
            for yota in liste:
                nl+=[elem for elem in yota.ng if elem.visited!=visitsession]
                for elem in nl: elem.visited=vistsession
            liste=nl[:];
        return liste;
    
    def dist(self,other):
        liste=[self];
        visitsession=hash(time.time())
        self.visited=visitsession
        dist=0
        for elem in g:g.p=[]
        while liste:
            nl=list();
            for yota in liste:
                if yota==other:
                        return dist,yota.p+[yota]
                for elem in yota.ng:
                    if elem.visited-visitsession:
                        nl.append(elem)
                        elem.p=yota.p+[yota]
                for elem in nl:
                    elem.visited=visitsession
            liste=nl[:];
            dist+=1
        return -1;
    
    __repr__=lambda this:this.name

class Graph():
    def __init__(s,ls):
        s.ls=ls
    def __getitem__(this,arg):
        if type(arg)==int:
            return self.ls[arg]
        if type(arg)==str:
            arg=arg.upper()
            for elem in this.ls:
                if elem.name==arg:
                    return elem
            raise KeyError(arg)
        raise TypeError
    def doforall(this,func):
        for elem in this:func(this)
        
    __repr__=lambda self:self.ls.__repr__()
    __iter__=lambda self:self.ls.__iter__()
    __next__=lambda self:self.ls.__next__()
    __len__=lambda this:len(this.ls)
    
def random_graph(nb_points:int,nb_links=3):
    walah=[S() for i in range(nb_points)]
    for elem in walah[::random.randint(1,3)]:
        for i in range(nb_links):
            random.choice(walah).add(elem)
    return walah

def complete_graph(nb_points):
    walah=[]
    for i in range(nb_points):
        walah.append(S())
        for elem in walah[:-1]:
            elem.add(walah[-1])
    return walah

def complete_graph_recur(nb_points,ls=[]):
    if nb_points==0:return ls
    new=S()
    for elem in ls:
        elem.add(new)
    ls.append(new)
    return complete_graph_recur(nb_points-1,ls)

    

g=Graph(random_graph(10,3))
drag=drag()

f=tkinter.Tk()
c=tkinter.Canvas(f)
c.config(width=500,height=500)
c.tag_bind("toma","<ButtonPress>",drag.start)
c.tag_bind("toma","<ButtonRelease>",drag.__init__)
c.tag_bind("toma","<B1-Motion>",drag.drag)
c.pack()



