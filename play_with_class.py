#!/usr/bin/python
import sys

class Stack:
    def p(self):
        print "Hello World"

    @staticmethod
    def _print():
        print "HELLO WORLD"
    


def main():
    s = Stack()
    s.p()
    print '--'
    Stack._print()

if __name__ == "__main__":
    main()
