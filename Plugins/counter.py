"""
 COPYRIGHT (C) Ozay Civelek <ozay.civelek@gmail.com>
 
 This file is a part of pyEventPlugins software package
 Some rights reserved

 Author 	: Ozay Civelek <ozay.civelek@testurk.com>
 Date		: $__date__$

 Version	: $__version__$
 
 $__file__$
 
 Singleton Plugin Example

 Demonstrate Singleton usage of plugin system.
"""
from .Library.EventManager import Events

class counter(Events):
	
	__hookpoints__ = {'COUNT' : 'perform'}
	__Instance = None
	
	def __new__(cls, *args, **kw):
		if not cls.__Instance:
			cls.__Instance = super(counter, cls).__new__(cls,*args, **kw)
		return cls.__Instance
	
	__counter__ = 0
	
	def perform(self, *args, **kw):
		self.__counter__ += 1
		print self.__counter__