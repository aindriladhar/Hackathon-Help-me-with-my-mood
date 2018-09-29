import sys

num = sys.argv[1];

if num % 2 == 0:
	print('even')
	sys.stdout.flush()
else:
	print('odd')
	sys.stdout.flush()