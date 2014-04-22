__author__ = ['tim.postlewaite', 'kyleh']

import argparse
import urllib.request
from bs4 import BeautifulSoup

def main(args):

	responseFile = 'response.html'
	site = 'http://prime.paxsite.com/registration'
	response = urllib.request.urlopen(site)
	html = response.read()

	f = open(responseFile, 'w')

	f.write(str(html))

if __name__ == '__main__':
	parser = argparse.ArgumentParser(prog="Script to check a website for event tickets to be released.")
	parser.add_argument('-n', '--negate', type=bool, help='Negates the check (checks for absence of the pattern instead of presence)')
	parser.add_argument('-o', help='Output file?')
	parser.add_argument('-p', help='Regex pattern to match against')
	parser.add_argument('-u', help='URL to check for a regex pattern')
	args = parser.parse_args()
	main(args)
