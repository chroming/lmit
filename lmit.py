#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

def lmitmain():
    print("lmitmain")

def lmitchoice():
    print("lmitchoice")


def main():
    try:
        sys.argv[1]
        lmichoice()
    except:
        lmitmain()

if __name__ == "__main__":
    main()
