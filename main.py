import pydirectinput
import time


time.sleep(3)


def reset():



    pydirectinput.moveTo(1095, 1050)
    pydirectinput.mouseDown()
    time.sleep(0.05)
    pydirectinput.mouseUp()

    time.sleep(0.5) 


    pydirectinput.press('esc')
    time.sleep(0.5)


    pydirectinput.moveTo(950, 850)
    pydirectinput.mouseDown()
    time.sleep(0.15) 
    pydirectinput.mouseUp()


    pydirectinput.moveTo(850, 450)
    pydirectinput.moveTo(850, 451)
    pydirectinput.mouseDown()
    time.sleep(0.15) 
    pydirectinput.mouseUp()

def canhao():
    #1 "w"
    pydirectinput.keyDown("w")
    time.sleep(3)
    pydirectinput.keyUp("w")

    #2 "d"
    pydirectinput.keyDown("d")
    time.sleep(9)
    pydirectinput.keyUp("d")

    pydirectinput.press('space')

    #3 "d"
    pydirectinput.keyDown("d")
    time.sleep(3)
    pydirectinput.keyUp("d")

    pydirectinput.press('space')

    #4 "d"
    pydirectinput.keyDown("d")
    time.sleep(0.5)
    pydirectinput.keyUp("d")

    pydirectinput.press('e')

def treat():
    pydirectinput.keyDown("a")
    time.sleep(4.3)
    pydirectinput.keyUp("a")

    pydirectinput.keyDown("w")
    time.sleep(2.5)
    pydirectinput.keyUp("w")

    pydirectinput.press('e')

def blueberry():
    pydirectinput.keyDown("a")
    time.sleep(3.6)
    pydirectinput.keyUp("a")

    pydirectinput.keyDown("w")
    time.sleep(14)
    pydirectinput.keyUp("w")

    pydirectinput.keyDown("a")
    time.sleep(4)
    pydirectinput.keyUp("a")

    pydirectinput.keyDown("s")
    time.sleep(3)
    pydirectinput.keyUp("s")

    pydirectinput.keyDown("d")
    time.sleep(0.5)
    pydirectinput.keyUp("d")

    pydirectinput.keyDown("s")
    time.sleep(0.5)
    pydirectinput.keyUp("s")

    pydirectinput.keyDown("a")
    time.sleep(10)
    pydirectinput.keyUp("a")

    pydirectinput.keyDown("w")
    time.sleep(2)
    pydirectinput.keyUp("w")

    pydirectinput.keyDown("d")
    time.sleep(1)
    pydirectinput.keyUp("d")

    pydirectinput.keyDown("w")
    time.sleep(0.5)
    pydirectinput.keyUp("w")
    pydirectinput.press('e')

def strawberry():
        #1 "w"
    pydirectinput.keyDown("w")
    time.sleep(2)
    pydirectinput.keyUp("w")

    #2 "d"
    pydirectinput.keyDown("d")
    time.sleep(9)
    pydirectinput.keyUp("d")

    pydirectinput.keyDown("s")
    time.sleep(10)
    pydirectinput.keyUp("s")

    pydirectinput.keyDown("d")
    time.sleep(4)
    pydirectinput.keyUp("d")

    pydirectinput.keyDown("s")
    time.sleep(2)
    pydirectinput.keyUp("s")

    pydirectinput.keyDown("d")
    time.sleep(2)
    pydirectinput.keyUp("d")

    pydirectinput.press('space')

    pydirectinput.keyDown("d")
    time.sleep(4.3)
    pydirectinput.keyUp("d")

    pydirectinput.keyDown("w")
    time.sleep(4)
    pydirectinput.keyUp("w")

    pydirectinput.keyDown("a")
    time.sleep(1.5)
    pydirectinput.keyUp("a")

    pydirectinput.keyDown("s")
    time.sleep(0.1)
    pydirectinput.keyUp("s")

    pydirectinput.press('e')




reset()   
canhao()
time.sleep(5)
treat()
reset()   
canhao()
time.sleep(5)
blueberry()
reset()
strawberry()