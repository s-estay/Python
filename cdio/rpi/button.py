import gpiozero

button_1 = gpiozero.Button(17) #connected to GPIO17 pin 11, pull-up
button_2 = gpiozero.Button(27) #connected to GPIO27 pin 13, pull-up
button_3 = gpiozero.Button(22) #connected to GPIO22 pin 15, pull-up
button_4 = gpiozero.Button(23) #connected to GPIO23 pin 16, pull-up
button_5 = gpiozero.Button(24) #connected to GPIO24 pin 18, pull-up

def say_one():
    print("one")

def say_two():
    print("two")

def say_three():
    print("three")

def say_four():
    print("four")

def say_five():
    print("five")

button_1.when_pressed = say_one
button_2.when_pressed = say_two
button_3.when_pressed = say_three
button_4.when_pressed = say_four
button_5.when_pressed = say_five
