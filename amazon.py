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

new = []
for i in data:
	if len(i) < 100:
		new.append(i)

print('一共有 ', len(new), '筆留言小於100字')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)

print('一共有', len(good), '筆提到 good')