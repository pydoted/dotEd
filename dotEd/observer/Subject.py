# -*- coding: utf-8 -*-

class Subject:
	'''
    classdocs
	'''
	
	def __init__(self):
		'''
		Constructor
		'''
		self.observators = []
		
	def addObservator(self, obs):
		'''
		addObservateur (to complete)
		'''
		self.observators.append(obs)
		
	def notify(self):
		'''
		notify (to complete)
		'''
		for obs in self.observators:
			obs.actualise() 