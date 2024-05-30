#!/usr/bin/env python3
'''Lab 3 Inv 3 script - free disk space'''
# Author ID: [seneca_id]

import subprocess

def free_space():
    # Launch the Linux command as a new process
    p = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
    p1 = subprocess.Popen(['grep', '/$'], stdin=p.stdout, stdout=subprocess.PIPE)
    p.stdout.close()
    output = subprocess.check_output(['awk', '{print $4}'], stdin=p1.stdout).decode('utf-8').strip()
    p1.stdout.close()
    return output

if __name__ == '__main__':
    print(free_space())

