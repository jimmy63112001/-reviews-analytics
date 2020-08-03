data = []
count = 0#計數
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1 #count = count + 1
		if count % 1000 == 0: #%用來求餘數 if後面記得加冒號！！ 
			print(len(data)) #每讀1000行就把長度印給你（print對電腦而言很花時間）
print(len(data))
print(data[0])
print('-------------')
print(data[1])