import sys

num = int(sys.argv[1]);

if num % 2 == 0:
	print('even')
else:
	print('odd')
sys.stdout.flush()
