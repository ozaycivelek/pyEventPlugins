"""
 COPYRIGHT (C) Ozay Civelek <ozay.civelek@gmail.com>
 
 This file is a part of pyEventPlugins software package
 Some rights reserved

 Author 	: Ozay Civelek <ozay.civelek@testurk.com>
 Date		: $__date__$

 Version	: $__version__$
 
 $__file__$
 
 Event Manager Class

 Generic Event/Plugin interface providing all the functionality
 required to be performed on plugins being loaded.

"""
from PluginMount import MountPoint
from Exceptions import EventManagerException

class Events(object):
	"""Event specific logic interface for plugins"""
	
	__metaclass__ = MountPoint
	__hookpoints__ = {}
	
	def fire(self, event, *args, **kw):
		"""Fire and event"""
		for action in self.plugins:
			if event in action().hook_points():
				try:
					action().execute(event, *args, **kw)
				except EventManagerException:
					message_tmpl = "%s could not invoke %s hook\nAvailable hooks are %s"
					message_data = (action().__pluginname__, event, str(action().__hookpoints__))
					raise EventManagerException( message_tmpl % message_data)
				
	
	def hook_points(self):
		"""Return a list of hooked events"""
		return self.__hookpoints__.keys()
	
	def execute(self, hook_point, *args, **kw):
		"""Execute the given method for an event"""
		try:
			methodname = self.__hookpoints__[hook_point]
			method = getattr(self, methodname)
			method(*args, **kw)
		except:
			raise EventManagerException("%s failed\n%s" % hook_point)
		
	
	def list_types(self):
		"""Return all event types to be caught by plugins"""
		event_list = []
		for action in self.plugins:
			[event_list.append(el) for el in action().hook_points() if el not in event_list]
		return event_list
	
	def list_plugins(self):
		"""Return a dictionary of plugin names and events hooked into"""
		plugins = {}
		for action in self.plugins:
			plugins[action().__pluginname__] = action().hook_points()
		return plugins
