#!/usr/bin/env python
# encoding: utf-8
"""
plugin.py

Created by Ozay Civelek on 2011-09-02.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
from Library.EventManager import Events
from Plugins import *



if __name__ == '__main__':
	Events().fire('ON_CLEAR')
	print Events().list_types()
	print Events().list_plugins()

