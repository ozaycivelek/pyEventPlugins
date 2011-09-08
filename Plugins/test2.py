"""
 COPYRIGHT (C) Ozay Civelek <ozay.civelek@gmail.com>
 
 This file is a part of pyEventPlugins software package
 Some rights reserved

 Author 	: Ozay Civelek <ozay.civelek@testurk.com>
 Date		: $__date__$

 Version	: $__version__$
 
 $__file__$
 
 Plugin Example

 Demonstrate burst usage of plugin system. Please note plugins
 may also fire events, thus plugins can be chained to perform
 more complex tasks upon a fired single event
"""
from .Library.EventManager import Events

class example_plugin(Events):
	
	__hookpoints__ = {'ON_CLEAR' : 'per6orm'}
	
	def per6orm(self, *args, **kw):
		print "wa sdfgsdfgsdfgsdfg!"