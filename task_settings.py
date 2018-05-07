#!/usr/bin/env python2
import getpass, os

def get_path():
    path = '/home/'+getpass.getuser()+'/.taskmanager/'
    try:
        open(path+'database')
        #means settings file exists
        pass
    except IOError:
        os.mkdir(path)
    
    return path
