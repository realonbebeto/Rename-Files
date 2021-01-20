#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:30:32 2021

@author: nyamwamu
"""

import os

def main():
    for count, filename in enumerate(os.listdir("/home/nyamwamu/Downloads/WQU Data Science")):
        old_name = str(filename)
        new_name = old_name.strip("yt1s.com -")
        fin_name = new_name.replace("_1080p", "")
        src = "/home/nyamwamu/Downloads/WQU Data Science/" + filename
        dst = "/home/nyamwamu/Downloads/WQU Data Science/" + fin_name
        print(fin_name)
        os.rename(src, dst)

if __name__ == '__main__':
    main()