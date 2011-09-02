from PluginMount import MountPoint

class Events(object):
	__metaclass__ = MountPoint
	__hookpoints__ = {}
	
	def fire(self,event):
		for action in self.plugins:
			if event in action().hook_points():
				action().execute(event)
	
	def hook_points(self):
		"""Return a list of hooked events"""
		return self.__hookpoints__.keys()
	
	def execute(self, hook_point):
		"""Execute the given method for an event"""
		methodname = self.__hookpoints__[hook_point]
		method = getattr(self, methodname)
		method()
	
	def list_types(self):
		event_list = []
		for action in self.plugins:
			[event_list.append(el) for el in action().hook_points() if el not in event_list]
		return event_list
	
	def list_plugins(self):
		plugins = {}
		for action in self.plugins:
			plugins[action().__pluginname__] = action().hook_points()
		return plugins