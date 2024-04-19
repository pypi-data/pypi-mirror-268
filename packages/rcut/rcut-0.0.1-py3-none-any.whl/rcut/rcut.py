#!/usr/bin/env python3

import getopt
import sys

def usage():
	print('''
rcut.py USAGE:
    rcut [FLAGS] [OPTIONS] [input]

FLAGS:
    -h  Prints help information
    -n  Show count number (one-indexed) with each field. -f will be ignored
    -v  Activate verbose mode

OPTIONS:
    -d <delim>     [default: \\t]
    -f <fields>    [default: 1] (can be a comma separated list)

ARGS:
    <input>    Input file (default will be stdin)
    ''')


def process_line(line, fields, delim, show_indexes,verbose):
	parts = line.split(delim)
	parts_chosen = []

	if show_indexes == True:
		for i in range(len(parts)):
			print(f'[{i+1}]{parts[i]}', end=' ')
		print()

		return

	for f in fields:
		try:
			parts_chosen.append(parts[f-1])
		except IndexError:
			parts_chosen.append('')
	counter = 0
	for p in parts_chosen:
		print(p, end='')
		counter += 1
		if counter < len(parts_chosen):
			print(delim, end='')

		# print(delim, end='')
	print()


def main():

	opts, args = getopt.getopt(sys.argv[1:], "hf:d:n")

	verbose = False
	fields = [1]
	show_indexes = False
	delim = "\t" # default delim
	file_input = sys.stdin

	for o, a in opts:
			if o == "-v":
				verbose = True
			elif o == "-h":
				usage()
				exit()
			if o == "-f":
				fields = [int(x) for x in a.split(',')]
			if o == "-d":
				delim = a
			if o == "-n":
				show_indexes = True

	if len(args) > 0:
		filename = args[0]

		with open(filename, 'r') as f:
			for line in f:
				line = line.strip()
				process_line(line, fields, delim, show_indexes, verbose)

	else:
		while True:
			try:
				line = input()
				process_line(line, fields, delim, show_indexes, verbose)
			except EOFError:
				break


if __name__ == '__main__':
	main()