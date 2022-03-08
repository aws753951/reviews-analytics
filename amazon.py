data = []
count = 0
total = 0
avg = 0
with open('reviews.txt','r') as f:
	for line in f:
		count += 1
		data.append(line)
		total += len(data[count-1])

avg = total / count

print(avg)

