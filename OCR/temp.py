a = file('KNN.csv','r')
for line in a:
	s = ""
	for item in line:
		item = item.strip()
		s = s + item
	print s
