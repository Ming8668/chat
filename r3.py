# 取出人名 # 清單分割

lines = []
with open('3.txt', 'r', encoding='utf-8') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][:5]
	name = s[0][5:]
	# print(s)
	# print(time)
	print(name)

