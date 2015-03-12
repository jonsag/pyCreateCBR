#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Encoding: UTF-8

import sys, getopt

from modules import (findDirs, findImages, createCBR, 
                     onError, usage)

try:
    myopts, args = getopt.getopt(sys.argv[1:],
                                 'p:vh',
                                 ['path=', 'verbose', 'help'])

except getopt.GetoptError as e:
    onError(1, str(e))

if len(sys.argv) == 1:  # no options passed
    onError(2, 2)
    
searchPath = "."
verbose = False
    
for option, argument in myopts:
    if option in ('-p', '--path'):
        searchPath = argument
    elif option in ('-v', '--verbose'):  # verbose output
        verbose = True
    elif option in ('-h', '--help'):  # display help text
        usage(0)    
        
dirs = findDirs(searchPath, verbose)
for myDir in dirs:
    print myDir
    images = findImages(myDir, verbose)
    createCBR(searchPath, myDir, images, verbose)