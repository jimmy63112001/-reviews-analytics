data = []
count = 0#計數

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1 #count = count + 1
		if count % 1000 == 0: #%用來求餘數 if後面記得加冒號！！ 
			print(len(data)) #每讀1000行就把長度印給你（print對電腦而言很花時間）
print('file is completely read total', len(data), 'data!')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	print('average is', sum_len/len(data))#len(data)=1000000

new = []
new2 = []
for d in data:
	if len(d) < 100:
		new.append(d)
	else:
		new2.append(d)
print('一共有', len(new), '長度少於100')
print('一共有', len(new2), '長度多於100')