from morse import *
from wise import *


message1 = "friend"
message2 = "love"
message3 = "joy"
message4 = "peace"
message5 = "hi"
message6 = "hello"

texts = [message1,message2,message3,message4,message5,message6]

def blink():
    for i in range(6):
        b = i *10 +10
        pixels[1] = ((0,0,b))
        pixels[2] = ((0,0,b))
        pixels.show()
        time.sleep(.2)
        pixels.fill((0,0,0))
        pixels.show()
        time.sleep(.2)


def wink():
    c = (0,0,20)
    pixels[1] = c
    pixels[2] = blank
    pixels.show()
    for i in range(6):
        pixels[1] = c
        pixels[2] = blank
        pixels.show()
        time.sleep(.2)
        pixels[1] = blank
        pixels[2] = c
        pixels.show()
        time.sleep(.4)
    pixels.fill(blank)
    pixels.show()
Done  = False

count = 0

compthink() #computer thinking
docode("hello") #say hello
blinknum(1,blue)
blink()


while not Done:
    val = 0

    if touch1.value:
        val = val + 1

    if touch2.value:
        val = val + 2


    if val == 1: #advance through messages touching "1"
        blink()
        docode(getWD("tolkien"))
        compthink()

    if val == 2: #display message in Morse when touching "2"
        wink()
        docode(random.choice(texts))
        compthink() #indicates end of message

    time.sleep(.2)
