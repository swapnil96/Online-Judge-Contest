import sys

print 1
sys.stdout.flush()
print 3, 1, 2, 3
sys.stdout.flush()
print 2, 4, 5
sys.stdout.flush()
	
d1 = int(raw_input())

if d1 == 0:

	print 1
	sys.stdout.flush()
	print 1, 4
	sys.stdout.flush()
	print 1, 5
	sys.stdout.flush()

	d11 = int(raw_input())
	if d11 == -1:

		print 2
		sys.stdout.flush()
		print 5
		sys.stdout.flush()

	elif d11== 1:

		print 2
		sys.stdout.flush()
		print 4
		sys.stdout.flush()
	

if d1 == 2:

	print 1
	sys.stdout.flush()
	print 2, 1, 2
	sys.stdout.flush()
	print 1, 3
	sys.stdout.flush()

	d2 = int(raw_input())

	if d2 == 0:

		print 2
		sys.stdout.flush()
		print 3
		sys.stdout.flush()

	elif d2 == 2:

		print 1
		sys.stdout.flush()
		print 1, 1
		sys.stdout.flush()
		print 1, 2
		sys.stdout.flush()

		d22 = int(raw_input())

		if d22 == -1:

			print 2
			sys.stdout.flush()
			print 2
			sys.stdout.flush()

		elif d22 == 1:
			
			print 2
			sys.stdout.flush()
			print 1	
			sys.stdout.flush()


