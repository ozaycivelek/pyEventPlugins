from .Library.EventManager import Events

class example_plugin(Events):
	
	__hookpoints__ = {'ON_CLEAR' : 'per6orm'}
	
	def per6orm(self):
		print "wa sdfgsdfgsdfgsdfg!"