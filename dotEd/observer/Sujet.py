# -*- coding: utf-8 -*-

class Sujet:
	'''
    classdocs
	'''
	
	def __init__(self):
		'''
		Constructor
		'''
		self.observateurs = []
		
	def addObservateur(self, observateur):
		'''
		addObservateur (to complete)
		'''
		self.observateurs.append(observateur)
		
	def notify(self):
		'''
		notify (to complete)
		'''
		for obs in self.observateurs:
			obs.actualise() 