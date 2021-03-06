#!/usr/bin/python
import sys
from collections import deque

class Stack:
    def __init__(self):
        self.stack = []
        self.len = 0

    def push(self, x):
        self.stack.append(x)
        self.len += 1

    def pop(self):
        if self.len > 0:
            self.len -= 1
            return self.stack.pop()
        else:
            print "ERROR: Stack is Empty!"
            return -1

    def size(self):
        return self.len

    def empty(self):
        return self.size() == 0

class Queue:
    def __init__(self):
        self.queue = deque()
        self.len = 0

    def push(self, x):
        self.queue.appendleft(x)
        self.len += 1

    def pop(self):
        if self.len > 0:
            self.len -= 1
            return self.queue.pop()
        else:
            print "ERROR: Queue is Empty"
            return -1
    
    def size(self):
        return self.len

    def empty(self):
        return self.size() == 0

class Point:
    def __init__(self, _w, _h, _p):
        self.width = _w
        self.height = _h
        self.path = _p
