#print('hello')

#a = '1'
#print(a)

#pyText
##b = 23
##print(b)
##
##import sys
##
##def fxn(x):
##    y = x + 3
##    return y
##
##def fxn2():
##    print('hello')


##import argparse
##parser = argparse.ArgumentParser()
##parser.add_argument("echo")
##args = parser.parse_args()
##print(args.echo)

##import argparse
##parser = argparse.ArgumentParser()
##parser.add_argument("x", help = "increment given number by 2", type = int)
##args = parser.parse_args()
##print(args.x + 2)

def foo():
    return 3

def main():
    if argv[0] == "foo":
        foo()

if __name__ == "__main__":
    main()
