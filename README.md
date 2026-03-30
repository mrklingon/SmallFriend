# SmallFriend
NeoTrinkey Morse code blinker 

Project files to copy to your neotrinkey:

* friend.py - Program - rename as code.py to run on neotrinkey
* morse.py - encodes text to Morse code, prints it and blinks via neopixels
* tolkien - a batch of Tolkien quotes
* wise.py - code to select a random line from tolkien file

I was revisiting my earlier project ["Teach your NeoTrinkey Morse code!"](https://adafruit-playground.com/u/mrklingon/pages/teach-your-neotrinkey-morse-code) and thought it would be fun to add to it, coding a "small friend" that delivers messages in [Morse code](https://en.wikipedia.org/wiki/Morse_code). 

Project blinks some colors, then blinks out Morse for "hello." 
Then, touch #2 and two blue neopixels blink on and off, followed by blinking one of these words at random:

```
message1 = "friend"
message2 = "love"
message3 = "joy"
message4 = "peace"
message5 = "hi"
message6 = "hello"
```


If you touch #1 the blue "eyes" will wink and then one of the Tolkien quotes will be blinked out in code.

If you run the program while running an IDE like Mu or Thonny, it will print the text and the morse code.

You can replace the quotes in "tolkien" or create a new file with the text you want to have blinked out. If you create a new file, then change this line:

```
        docode(getWD("tolkien"))
```
to name the new file.


