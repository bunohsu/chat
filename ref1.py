#練習 對話紀錄格式轉換
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f: 
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None #如果person沒有值(預設值)
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		if line == 'Tom':
			person = 'Tom'
			continue
		if person: #如果person有值的話，才執行下一行
			new.append(person + ': ' + line)
	return new


def write_file(filename, lines):
	with open(filename, 'w', 'utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')



def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()
