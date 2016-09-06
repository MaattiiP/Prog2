#! /usr/bin/python3.4
# -*- encoding: utf-8 -*-

def domino():
	dom1 = 1
	dom2 = 1
	while dom1 < 7 and dom2 < 7:
		print ("[ " + str(dom1) + " | " + str (dom2) + " ]")
		dom1 = dom1 + 1
		dom2 = dom2
domino()
