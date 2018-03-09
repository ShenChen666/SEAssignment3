# -*- coding: utf-8 -*-

"""Main module."""
import sys
import click
import re
import urllib.request
import requests

def parseFile(input):
	if input.startswith('http'):
		req = urllib.request.urlopen(input)
		buffer = req.read().decode('utf-8')
	else:
		buffer = open(input).read()
	return buffer

def relex(cmd):
	pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
	m = re.findall(pattern, str(cmd))
	return m


class LightTester:
	def __init__(self,N):
		N = int(N)
		self.N = N
		self.lights = [ [0]*N for _ in range(N) ]


	def apply(self,m):
		a = int(m[1])
		b = int(m[2])
		c = int(m[3])
		d = int(m[4])
		if a > c:
			a,b = b,a
		if b > d:
			b,d = d,b
		if a < 0:
			a = 0
		if b <0:
			b = 0
		if c >=self.N:
			c = (self.N) -1
		if d >=self.N:
			d = (self.N) -1
		if(m[0]=='switch'):
			for i in range(a,c+1):
				for j in range(b,d+1):
					if(self.lights[i][j]==1):
						self.lights[i][j]=0
					elif(self.lights[i][j]==0):
						self.lights[i][j]=1
			
		elif (m[0]=='turn on'):
			for i in range(a,c+1):
				for j in range(b,d+1):
					self.lights[i][j] = 1
			
		elif(m[0]=='turn off'):
			for i in range(a,c+1):
				for j in range(b,d+1):
					self.lights[i][j] = 0
			
	def count(self):
		count = 0
		for i in range(len(self.lights)):
			for j in range(len(self.lights)):
				if(self.lights[i][j] == 1):
					count += 1

		return count


def main():
	insturctions = parseFile(input)
	firstLine = insturctions.split('\n')[0]
	lights = LightTester(firstLine)
	insturctions = relex(insturctions)
	for i in insturctions:
		lights.apply(i)
	print("#occupied: ", lights.count())	

if(__name__ =='__main__'):
	main()
