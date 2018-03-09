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

