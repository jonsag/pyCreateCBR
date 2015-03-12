#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Encoding: UTF-8

import ConfigParser, os, sys, zipfile

try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED

modes = { zipfile.ZIP_DEFLATED: 'deflated',
          zipfile.ZIP_STORED:   'stored',
          }

config = ConfigParser.ConfigParser()  # define config file
config.read("%s/config.ini" % os.path.dirname(os.path.realpath(__file__)))  # read config file

imageTypes = (config.get('fileTypes', 'imageTypes').replace(" ", "")).split(',')  # allowed image types

def onError(errorCode, extra):
    print "\nError:"
    if errorCode == 1:
        print extra
        usage(errorCode)
    elif errorCode == 2:
        print "No options given"
        usage(errorCode)
        
def usage(exitCode):
    print "\nUsage:"
    print "----------------------------------------"
    print "%s " % sys.argv[0]

    sys.exit(exitCode)
    
def findDirs(searchPath, verbose):   
    dirs = []      
    print "\n--- Searching %s for directories" % (searchPath)
    for myFile in os.listdir(searchPath):
        if os.path.isdir(os.path.join(str(searchPath), myFile)) and not os.path.islink(os.path.join(str(searchPath), myFile)):  # check if myFile matches criteria
            print "%s" % myFile
            dirs.append(os.path.join(str(searchPath), myFile))
                
    print "--- Number of directories in %s: %d\n" % (searchPath, len(dirs))

    return sorted(dirs)

def findImages(searchPath, verbose):   
    images = []      
    print "\n--- Searching %s for directories" % (searchPath)
    for myFile in os.listdir(searchPath):
        if os.path.isfile(os.path.join(str(searchPath), myFile)) and not os.path.islink(os.path.join(str(searchPath), myFile)):  # check if myFile matches criteria
            extension = os.path.splitext(myFile)[1].lstrip(".").lower()
            for imageType in imageTypes:
                if extension == imageType.lower():
                    print "%s" % myFile
                    images.append(os.path.join(str(searchPath), myFile))
                
    print "--- Number of images in %s: %d\n" % (searchPath, len(images))

    return sorted(images)

def createCBR(path, zipName, images, verbose):
    zf = zipfile.ZipFile(os.path.join(path, '%s.cbr' % zipName), mode='w')
    
    for image in images:
        print "Adding %s ..." % image
        try:
            zf.write(image, compress_type=compression)
        except:
            print "Error"
    
    print "Closing..."
    zf.close()

    
    
    
    