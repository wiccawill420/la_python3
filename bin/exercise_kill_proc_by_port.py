#!/usr/bin/env python3.6

#import sys
import os
import argparse
import subprocess

parser = argparse.ArgumentParser(description='Kills process keeping port blocked')
parser.add_argument('portnumber', help='The port number to scan for')
args = parser.parse_args()

try:
    lsofCom = subprocess.run(['lsof', '-n', '-i4TCP:' + args.portnumber], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
except:
    print("There was an error")

comOutput = lsofCom.stdout.decode()
lines = comOutput.splitlines()
foundit = 0
for line in lines:
    if 'LISTEN' in line:
        pid = int(line.split()[1])
        print(f"Process {pid} found on port {args.portnumber}, attempting to kill it")
        try:
            os.kill(pid, 9)
        except:
            print(f"Failed to kill pid {pid}")
        foundit = 1
if foundit != 1:
    print(F"No process found on {args.portnumber} or permission denied")
