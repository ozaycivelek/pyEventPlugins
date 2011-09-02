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