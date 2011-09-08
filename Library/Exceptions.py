"""
 COPYRIGHT (C) Ozay Civelek <ozay.civelek@gmail.com>
 
 This file is a part of pyEventPlugins software package
 Some rights reserved

 Author		: Ozay Civelek <ozay.civelek@testurk.com>
 Date		: $__date__$

 Version	: $__version__$
 
 $__file__$
 
 Event Manager Exception(s)

 Generic event exception class

"""

class EventManagerException(Exception):
	"""Event manager exception"""
	
	def __init__(self, message):
		self.value = message
	
	def __str__(self):
		return self.value
