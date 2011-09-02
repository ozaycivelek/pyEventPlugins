from .Library.EventManager import Events

class example_plugin2(Events):
	
	__hookpoints__ = {'ON_CLEAR' : 'perform'}
	
	def perform(self, *args, **kw):
		print "ON_CLEAR", ''.join(args)