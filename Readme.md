## Proto Board
Our proposal for proto board consisted of input push button with a built-in pull up and an output LED. Both the interfaces will be connected via the breakout StemmaQT connector.
The developed board looks like following

![proto2](https://user-images.githubusercontent.com/57740824/202589853-92b8ad52-7ad0-4ed9-a2bd-0b2d9c397d31.jpeg)

![proto3](https://user-images.githubusercontent.com/57740824/202589880-909e1686-0149-49f3-9244-c410d96a5d4d.jpeg)

![proto1](https://user-images.githubusercontent.com/57740824/202589834-9d895ff1-f0e9-4df0-a794-76e643723384.jpeg)

Hooking up the board is fairly simple, Look for the marking on the back, the black marking shows where you need to connect the red(positive) and the rest of the wires as follows

![protoboardmarking](https://user-images.githubusercontent.com/57740824/202590479-c7f8e049-5e43-4f63-92a6-fb7e2b9f4e63.jpeg)

```
J6-> Red(+3.3V)
J7 -> Black(Gnd)
J8 -> Blue(SDA,GPIO 22)
J9 -> Yellow(SCL,GPIO 23)
```
We also created custom library for the board, you can find the files pushbutton.c and pushbutton.h


# Interface with Sequencer
Using the PIO sequencer we interfaced the board with our protoboard using the StemmaQT connector and recorded the SDA(GPIO22) pin and replayed the data on SCL(GPIO23) pin. Similar to the sequencer we can log the data on the computer using a python script.

https://user-images.githubusercontent.com/57740824/202590917-f27e2335-ada0-4679-92b8-cb75daf38c63.mp4


