#!/usr/bin/env python3.8

def sayit(this):
    print(this)

message = input("What message do you have? ")
messcount = input("How many times should I say that? ")
if not messcount:
    messcount = 1
messcount = int(messcount)
i=0
while i < messcount:
    sayit(message)
    i += 1

