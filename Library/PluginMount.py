"""
 COPYRIGHT (C) Ozay Civelek <ozay.civelek@gmail.com>
 
 This file is a part of pyEventPlugins software package
 Some rights reserved

 Author 	: Ozay Civelek <ozay.civelek@testurk.com>
 Date		: $__date__$

 Version	: $__version__$
 
 $__file__$
 
 Plugins mount point object

 MountPoint is an object derived from type object
 acting as a metaclass for Event Manager.
"""
class MountPoint(type):
	"""Plugin mount point object designed to act as a meta class for ?Event Manager. 
	   If initiated directly creates the plugins list, all other objects inheriting
	   MountPoint will be added as plugins."""
	
	def __init__(cls, name, bases, attrs):
		if not hasattr(cls, 'plugins'):
			'''This section only runs when processing the mount point itself'''
			cls.plugins = []
		else:
			'''It must be a plugin implementation if we're here'''
			cls.plugins.append(cls)
			cls.__pluginname__ = name
	
