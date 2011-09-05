#!/usr/bin/env python
# encoding: utf-8
"""
 COPYRIGHT (C) Ozay Civelek <ozay.civelek@gmail.com>
 
 This file is a part of pyEventPlugins software package
 Some rights reserved

 Author 	: Ozay Civelek <ozay.civelek@testurk.com>
 Date		: $__date__$

 Version	: $__version__$
 
 $__file__$
 
 Framework entry point example.

 Demonstrate burst usage of plugin system. Please note 
 all event calls are done through Events object.
"""
from Library.EventManager import Events

if __name__ == '__main__':
	Events().fire('ON_CLEAR',"selaaaaam", " ", "naber?", func="eveeet")
	#print Events().list_types()
	#print Events().list_plugins()

