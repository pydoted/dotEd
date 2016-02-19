# -*- coding: utf-8 -*-


class Subject(object):
	'''Represent a subject.
	
	
	Argument(s):
	observators (List[Observator]): All observators
	'''
	
	
	def __init__(self):
		self.observators = []
		
	def addObservator(self, obs):
		'''Add an observator.
		
		Argument(s):
		obs (Observator): A controller
		'''
		self.observators.append(obs)
		
	def notify(self):
		'''Notify all observators.'''
		for obs in self.observators:
			obs.updateView() 
