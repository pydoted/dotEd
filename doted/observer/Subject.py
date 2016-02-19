# -*- coding: utf-8 -*-


class Subject(object):
	'''Represent a subject.
	
	
	Argument(s):
	observers (List[Observer]): All observers
	'''
	
	
	def __init__(self):
		self.observers = []
		
	def addObserver(self, obs):
		'''Add an observer.
		
		Argument(s):
		obs (Observer): A controller
		'''
		self.observers.append(obs)
		
	def notify(self):
		'''Notify all observers.'''
		for obs in self.observers:
			obs.update() 
