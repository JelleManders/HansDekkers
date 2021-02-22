# Specs:
# - The user should input two numbers
# - Then print out numbers from 0 to 1000
# - When a number is divisible by the smaller input number, instead print "HANS"
# - When a number is divisible by the larger input number, instead print "DEKKERS"
# - When a number is divisible by both, instead print "HANS DEKKERS"

def HDtest(nr1, nr2):
	for i in range(1001):
		divBy1 = i % nr1 == 0
		divBy2 = i % nr2 == 0
		if divBy1 and divBy2:
			print("HANS DEKKERS")
		elif divBy1:
			print("HANS")
		elif divBy2:
			print("DEKKERS")

def HDtest2(x, y):
	xList = [x * i for i in range(1001) if x*i <= 1000]
	yList = [y * i for i in range(1001) if y*i <= 1000]
	bothList = [i for i in xList if i in yList]
	for elem in xList:
		if elem not in bothList:
			print("HANS")
		else:
			print("HANS DEKKERS")
	for elem in yList:
		if elem not in bothList:
			print("DEKKERS")

def HDtest3(x, y):
	xList = []
	yList = []
	i = 0
	j = 0
	while i <= 1000:
		i += x
		xList += [i]
	while j <= 1000:
		j += y
		yList += [j]
	bothList = [0]
	for elem in xList:
		if elem in yList:
			xList.remove(elem)
			yList.remove(elem)
			bothList += [elem]
	for elem in xList:
		print("HANS")
	for elem in yList:
		print("DEKKERS")
	for elem in bothList:
		print("HANS DEKKERS")

def HDtest4(x, y):
	inputs = [x for x in range(1001)]
	print(inputs)
	# idea was to go over all indices that are divisible by x and replace these with hans, then go over all indices divisble by Y, and replace these with dekkers unless there is already a Hans, then replace with Hans dekkers. Then print all elements that are not integers.

HDtest4(200, 500)
