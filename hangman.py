import turtle
import time
import random

logs = turtle.Screen()
logs.screensize(canvwidth=600, canvheight=500, bg=None)
logs.title("Hangman by Filips Vaicis") 
logs.bgcolor("#90EA82")
kursors = turtle.Turtle("classic")
pildspalva = turtle.Turtle()
pildspalva.pen(pencolor="red", speed=0)
pildspalva.hideturtle() # paslēpt kursoru
pildspalva.penup()
burtsminets = turtle.Turtle()
burtsminets.pen(pencolor="green", speed=0)
result= turtle.Turtle()
result.speed(100)
result.hideturtle()
result.penup()
result.goto(-200,-300)
result.pendown()
burtsminets.hideturtle()
hangman= turtle.Turtle()
hangman.hideturtle()
hangman.pen(pencolor="black", pensize=10, speed=2)
# pildspalva.goto(-200,-200)
# turtle.write(...) - teksta izvāds
def centrasdzivibas():
    hangman.penup()
    hangman.goto(-380,-150)
    hangman.pendown()
    hangman.forward(400)
    hangman.penup()
    hangman.goto(-310,-150)
    hangman.pendown()
    hangman.left(90)
    hangman.forward(400)
    hangman.right(90)
def trisdzivibas():
    hangman.goto(-310,250)
    hangman.pendown()
    hangman.forward(250)
    hangman.penup()
    hangman.goto(-310,170)
    hangman.pendown()
    hangman.left(40)
    hangman.forward(120)
    hangman.penup()
    hangman.right(40)
def divasdzivibas():
    hangman.goto(-100,250)
    hangman.pendown()
    hangman.right(90)
    hangman.forward(50)
    hangman.penup()
    hangman.goto(-130,170)
    hangman.pendown()
    hangman.fillcolor("white")
    hangman.begin_fill()
    hangman.circle(30)
    hangman.end_fill()
    hangman.penup()
    hangman.left(90)
def vienadziviba():
    hangman.goto(-100,140)
    hangman.right(90)
    hangman.pendown()
    hangman.forward(100)
    hangman.penup()
    hangman.goto(-100,120)
    hangman.right(40)
    hangman.pendown()
    hangman.forward(60)
    hangman.penup()
    hangman.goto(-100,120)
    hangman.left(80)
    hangman.pendown()
    hangman.forward(60)
    hangman.penup()
    hangman.left(50)
vards = ""
def spele(vards):
    sakums = turtle.textinput("Paziņojums","Izvēlaties vārdu ievadīt paši, vai arī izvilkt no faila. es/fails: ")
    vards= ""
    if sakums == "es":
        vards = turtle.textinput("Minējamais vārds","Ievadiet minējamo vārdu vai vārdu savienojumu: ")
    elif sakums == "fails":
        with open(r"C:\Users\filip\Desktop\hangman\vardi.txt", "r", encoding="utf-8") as file:
            fails= file.read()
            vards = fails.split()
            vards = random.choice(vards)
    punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for ele in vards:
        if ele in punct:
            vards = vards.replace(ele, "")
    vards = vards.lower()
    izlietoti = [" "]
    vardsbezzimem = vards
    latviesuburti = {"ā": "a", "č": "c", "ē": "e", "ģ": "g", "ī": "i", "ķ": "k", "ļ": "l", "ņ": "n", "š": "s", "ū": "u", "ž": "z"}
    for a in latviesuburti.keys():
        if a in vardsbezzimem:
            vardsbezzimem =vardsbezzimem.replace(a,latviesuburti[a])   
    loop=True
    dzivibas= 5
    while loop:
        burtsminets.clear()
        result.clear()
        minejums = turtle.textinput("Paziņojums","Jums ir "+str(dzivibas)+" dzīvības, ievadi minējamo burtu: ")
        # minejums = turtle.textinput()
        if minejums in izlietoti:
            burtsminets.clear()
            burtsminets.penup()
            burtsminets.goto(220,220)
            burtsminets.pendown()
            result.clear()
            burtsminets.color("red")
            burtsminets.write("Burts jau ir izlietots,\n miniet velreiz.", font=("Arial",30,"italic"), align="center")
            burtsminets.penup()
        else:
            if minejums not in vardsbezzimem:
                dzivibas= int(dzivibas)-1
        if dzivibas == 4:
            centrasdzivibas()
        if dzivibas==3:
            trisdzivibas()
        if dzivibas==2:
            divasdzivibas()
        if dzivibas==1:
            vienadziviba()
        if dzivibas==0:
            hangman.penup()
            hangman.goto(-100,40)
            hangman.right(60)
            hangman.pendown()
            hangman.forward(80)
            hangman.penup()
            hangman.goto(-100,40)
            hangman.right(60)
            hangman.pendown()
            hangman.forward(80)
            time.sleep(3)
            hangman.clear()
            hangman.reset()
            hangman.pen(pencolor="black", pensize=10, speed=2)
            hangman.hideturtle()
            break
        izlietoti.append(minejums)
        paslepts_vards = ""
        for burts in vardsbezzimem:
            if burts in izlietoti:
                # pildspalva.write(burts)
                paslepts_vards = paslepts_vards+burts+" "
            elif burts == " ":
                paslepts_vards += "   "
            else:
                # pildspalva.write("_")
                paslepts_vards += " _ "
        pildspalva.color("black")
        pildspalva.clear()
        pildspalva.penup()
        pildspalva.goto(0,-350)
        pildspalva.pendown()
        pildspalva.write(paslepts_vards, font=("Calibri",50, "bold"), align="center")
        truefalse=[]
        for x in vardsbezzimem:
            saglaba= x in izlietoti
            truefalse.append(saglaba)
            parbaude = all(truefalse)
        if not parbaude:
            pabeigt= turtle.textinput("Paziņojums","Vai jūs vēlaties pabeigt spēli? 'ja': ")
            if pabeigt == "ja":
                break
            else:
                continue
        loop=False
        for burts in vardsbezzimem:
            if burts not in izlietoti:
                loop = True
    if not loop:
        burtsminets.clear()
        result.clear()
        result.penup()
        result.goto(0,0)
        result.pendown()
        pildspalva.clear()
        result.write("Jūs uzminējāt- "+vards , font=("Arial",40,"italic"), align="center")
        hangman.clear()
    else:
        burtsminets.clear()
        result.clear()
        result.penup()
        result.goto(0,0)
        result.pendown()
        pildspalva.clear()
        result.write("Jūs neuzminējāt- "+vards , font=("Arial",40,"italic"), align="center")
        hangman.clear()
spele(vards)
forever = True
while forever:
    time.sleep(3)
    result.clear()
    pildspalva.clear()
    atkalspelet= turtle.textinput("Paziņojums","Vai jūs gribat atkal spēlēt? 'ja': ")
    if atkalspelet == "ja":
        spele(vards)
    else:
        result.clear()
        pildspalva.clear()
        pildspalva.penup()
        pildspalva.goto(0,0)
        pildspalva.pendown()
        pildspalva.write("Paldies, ka paspēlējāt", font=("Arial",40,"italic"), align="center")
        time.sleep(2)
        break
