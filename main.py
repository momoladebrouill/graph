import random,tkinter

from dessins import *
from grap import *
class drag():
    def __init__(s):
        s.restart()
        s.dico={}
        for elem in g:
            res=c.create_oval(elem.x-10,elem.y-10,elem.x+10,elem.y+10,fill=elem.coul,tags=('toma',))
            s.dico[res]=elem
            res=c.create_text(elem.x,elem.y+10,text=elem.name,tags=("LINEEEE",))
            s.dico[res]=elem
            for ng in elem.ng:
                c.create_line(elem.x,elem.y,ng.x,ng.y,tags=("LINEEEE",))
    def restart(s,e=None):
        s.obj,s.x,s.y=None,0,0
        
                
    def start(s,event):
        s.obj=c.find_closest(event.x,event.y)[0]
        s.x=event.x
        s.y=event.y
    
    def depl(s,event):
        dx=event.x-s.x
        dy=event.y-s.y
        c.move(s.obj,dx,dy)
        sommet=s.dico[s.obj]
        c.delete("LINEEEE")
        s.x=event.x
        s.y=event.y
        sommet.x,sommet.y=s.x,s.y
        s.update()
        
    def update(this):
        c.delete("LINEEEE")
        for elem in g:
            res=c.create_text(elem.x,elem.y+10,text=elem.dessin,font="courrier 1",tags=("LINEEEE",))
            this.dico[res]=elem
            for ng in elem.ng:
                c.create_line(elem.x,elem.y,ng.x,ng.y,tags=("LINEEEE",))


class Doggy():
    def __init__(this):
        this.lieu=mais
        this.x,this.y=this.lieu.x,this.lieu.y
        this.dess=c.create_text(this.lieu.x,this.lieu.y,text=chien,font="courrier 1",tags=('doggy,'))
    def move(this,event=None,draw=True):
        prob=0
        lieu=random.random()
        for elem in this.lieu.ng:
            prob+=this.lieu.probTo(elem)
            if lieu<prob:
                this.lieu=elem
                break
        if draw:
            this.draw()
    def draw(this):
        c.move(this.dess,this.lieu.x-this.x,this.lieu.y-this.y)
        this.x,this.y=this.lieu.x,this.lieu.y
        

  
mais=S("Maison",maison)
mais.x,mais.y=250,50
bouc=S("boucherie",saucisse)
bouc.x,bouc.y=50,450
boul=S("boulangerie",pain)
boul.x,boul.y=450,450
mais.addPonderated(bouc,2/3)
mais.addPonderated(boul,1/3)
boul.addPonderated(bouc,2/3)
boul.addPonderated(mais,1/3)
bouc.addPonderated(boul,1/2)
bouc.addPonderated(mais,1/2)
g=Graph([mais,bouc,boul])

f=tkinter.Tk()
c=tkinter.Canvas(f)
c.config(width=500,height=500)

c.pack()
drag=drag()
drag.update()
medor=Doggy()
medor.draw()
f.bind("<space>",medor.move)
c.tag_bind("toma","<ButtonPress>",drag.start)
c.tag_bind("toma","<ButtonRelease>",drag.restart)
c.tag_bind("toma","<B1-Motion>",drag.depl)

def throw(nb):
    count=0
    for i in range(nb):
        medor.lieu=mais
        for j in range(7):
            medor.move(draw=False)
        count+=medor.lieu==bouc
    return count/nb

