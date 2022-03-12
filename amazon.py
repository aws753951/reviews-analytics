data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		count += 1
		data.append(line)

total = 0
for d in data:
	total += len(d)


print(data[0])

print('平均每一則留言有', total/len(data),'字數')

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

#list comprehension

good = []
good = [d for d in data if 'good' in d] # 第一個d為要放入good list的元素，可更換
print(good[100])

bad = ['bad' in d for d in data] # 為布林值，是否有bad值在d字串元素裡面，有則True
print(bad[100])
 

# 文字計數

wc = {}
for d in data:
	words = d.strip().split()  #split() 都沒寫，預設把所有空白鍵給刪掉
	for word in words:
		if word not in wc:
			wc[word] = 1
		else:
			wc[word] += 1
	


for word in wc:
	if wc[word] >= 10000:
		print(word, wc[word])

print(len(wc)) # 印出有幾個字
print(wc['marc']) # 查出現多少次

while True:
	word = input('請輸入要查找的字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過')   # 避免找字時不存在而當掉

print('感謝使用本查詢功能')




















