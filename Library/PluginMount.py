class MountPoint(type):
	def __init__(cls, name, bases, attrs):
		if not hasattr(cls, 'plugins'):
			'''This section only runs when processing the mount point itself'''
			cls.plugins = []
		else:
			'''It must be a plugin implementation if we're here'''
			cls.plugins.append(cls)
			cls.__pluginname__ = name
	
