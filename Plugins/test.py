from .Library.EventManager import Events

class example_plugin2(Events):
	
	__hookpoints__ = {'ON_CLEAR' : 'perform'}
	
	def perform(self):
		print "wa yee!"