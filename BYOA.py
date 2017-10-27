#Just Click the start....

import os
import turtle
import time
import sys

wn = turtle.Screen()
cx = None
cy = None

scene_1 = True
scene_2 = scene_3 = scene_4 = alt = END = False


def traclear():
    global wn
    trace = turtle.Turtle()
    trace.shape("blank")
    trace.speed(0)
    for taar in range(100):
        trace.forward(.1)
        trace.backward(.1)


def click(x1, y1):
    global cx, cy
    cx = x1
    cy = y1


def detectClick(x1, y1, x2, y2):
    global wn, cx, cy
    wn.onclick(click)
    if x1 < cx < x2 and y1 < cy < y2:
        return True
    else:
        return False


def write(words, color, fontsize, xpos, ypos):
    global wn
    wr = turtle.Turtle()
    wr.speed(0)
    wr.tracer(10)
    wr.shape("blank")
    wr.color(color)
    wr.up()
    wr.goto(xpos, ypos)
    wr.write(words, move = False, align = "center", font = ("Times New Roman", fontsize, "normal"))


def addimage(image):
    global wn
    wn.addshape(os.path.expanduser(image))
    ima = turtle.Turtle()
    ima.tracer(4)
    ima.up()
    ima.shape(os.path.expanduser(image))
    return ima


def startUpScreen():
    global wn
    wn.tracer(4)
    wn.setworldcoordinates(0, 0, 10000, 10000)
    write("The Adventures of your Average, and Ordinary Salaryman", "black", 50, 5000, 6500)
    write("Click to Start", "black", 100, 5000, 4500)
    time.sleep(.5)
    while True:
        write("Click to Start", "white", 100, 5000, 4500)
        write("Click to Start", "white", 100, 5000, 4500)
        write("Click to Start", "white", 100, 5000, 4500)
        write("Click to Start", "white", 100, 5000, 4500)
        write("Click to Start", "white", 100, 5000, 4500)
        write("Click to Start", "white", 100, 5000, 4500)
        write("Click to Start", "white", 100, 5000, 4500)
        write("Click to Start", "white", 100, 5000, 4500)
        if detectClick(0, 0, 10000, 10000):
            break
        time.sleep(.5)
        write("Click to Start", "black", 100, 5000, 4500)
        if detectClick(0, 0, 10000, 10000):
            break
        time.sleep(.5)
    wn.clear()
    turtleFirst()


def turtleFirst():
    crabla = addimage("Crablante.gif")
    sept = addimage("salaryman_1899.gif")
    sept.goto(2000, 1000)
    crabla.goto(6000, 3000)
    write("You see a giant Crabman, leering at you.\n Knowing that you are bored of your life, what do you do?", "black", 50, 5000, 8000)
    time.sleep(.5)
    write("1) You attack the Crabman\n\n2) You run away to a job interview\n\n3) You walk and try to ignore him", "black", 50, 3000, 5000)
    time.sleep(.25)


def cyoa(x, y):
    global scene_1, scene_2, scene_3, scene_4, alt, END
    if scene_1:
        scene_1 = False
        if 150 < x < 4619 and 7216 < y < 7679:
            wn.clear()
            scene_2 = True
            scene1()
        elif 150 < x < 5921 and 6084 < y < 6556:
            alt = True
            wn.clear()
            scene1a()
        elif 150 < x < 5691 and 4905 < y < 5518:
            wn.clear()
            scene1b()
    elif alt:
        alt = False
        if 849 < x < 4476 and 7094 < y < 7735:
            wn.clear()
            scenealt()
        elif 817 < x < 9198 and 6018 < y < 6622:
            wn.clear()
            scene_3 = True
            scene2()
    elif scene_2:
        scene_2 = False
        if 1714 < x < 7452 and 5179 < y < 5688:
            wn.clear()
            scene2()
            scene_3 = True
        elif 1690 < x < 8277 and 3971 < y < 4584:
            wn.clear()
            scene1h()
    elif scene_3:
        scene_3 = False
        if 1706 < x < 8246 and 5886 < y < 6349:
            wn.clear()
            scene3()
            scene_4 = True
        elif 1777 < x < 8150 and 5018 < y < 5462:
            wn.clear()
            scene3a()
    elif scene_4:
        scene_4 = False
        END = True
        if 0 < x < 10000 and 0 < y < 10000:
            wn.clear()
            end()
    elif END:
        if 0 < x < 10000 and 0 < y < 10000:
            sys.exit()
    wn.onscreenclick(cyoa)


def scene1h():
    write("You arrive late at your interview\n You don't get hired\n You suicide after giving up.\n\n\n\n END", "black", 50, 5000, 5000)


def scenealt():
    write("You work for the company\n You grow bored\n You sigh and resign yourself to fate\n You leap off a building\n Crabman yells PSYCH!! and kills you.", "black", 50, 5000, 5000)
    write("END", "black", 50, 5000, 3000)


def end():
    sept = addimage("onepunchagain.gif")
    sept.goto(5000, 5000)
    traclear()
    time.sleep(1)
    write("THE \nEND", "gold", 400, 5000, 1000)


def scene3():
    sept = addimage("notonepunched.gif")
    sept.goto(5000, 5000)
    write("You found an opponent who could \nwithstand a normal punch of yours.\nClick for your destiny", "black", 50, 5000, 7500)


def scene3a():
    write("You indulge in anime, and other things.\nSociety falls from threats of monsters.\n You are the only human left.\n You run out of anime.\n You suicide by throwing yourself into a black hole.", "black", 40, 5000, 5000)
    write("END", "black", 100, 5000, 3000)


def scene2():
    op = addimage("Saitama.gif")
    op.goto(5000, 5000)
    write("After training for 3 years you become unnecessarily overpowered.\n You now one shot every monster, and you are bored with life", "black", 40, 5000, 8000)
    time.sleep(.5)
    write("1) You search for an enemy worthy of facing you\n\n2) You become a weeaboo, obsessed with anime", "white", 40, 5000, 5000)
    traclear()


def scene1():
    hero = addimage("Crabydie.gif")
    hero.goto(5000, 4000)
    write("You have defeated the Crabman, \nYou have realized your true dream", "black", 50, 5000, 8000)
    write("1) You train vigorously for 3 years\n\n2) You go to your job interview anyway", "white", 50, 5000, 4000)
    traclear()


def scene1a():
    write("You attend to your job interview, \nand succeed in getting your job.", "black", 50, 5000, 8000)
    write("1) Continue working\n\n2) Ditch your job and train vigourously for 3 years", "black", 50, 5000, 6000)


def scene1b():
    write("When you walk past him the Crabman\n reaches over with his razor sharp claws\n and snips your head off.", "black", 50, 5000, 5000)
    write("END", "black", 100, 5000, 3000)
    turtle.done()


def main():
    startUpScreen()

    wn.onscreenclick(cyoa)
    turtle.done()

main()
