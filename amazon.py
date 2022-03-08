data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		count += 1
		data.append(line)

total = 0
for d in data:
	total += len(d)

print('平均是', total/len(data),'字數')