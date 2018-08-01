import itertools
import hashlib

f = open('rainbow-table.txt', 'w')

letters = ['a', 'b', 'c']
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
generator = itertools.product(letters, repeat = 8)

for combo in generator:
	keyword = ''.join(combo)
	hashed = hashlib.md5(keyword.encode('utf-8')).hexdigest()
	f.write(hashed + ' | ' + keyword + '\n')
