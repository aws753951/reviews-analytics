data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		count += 1
		data.append(line)
		if count % 100000 == 0:
			print(data[count-1])

