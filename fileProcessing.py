infile = open('cuatro.txt', 'r')

print infile

lst = []
for line in infile:
    lst.append(line)

outfile = open('fromcuatro.txt', 'w')

for i in range(1, len(lst)):
	prev = lst[i-1]
	curr = lst[i]
	if 'substr' in curr:
		outfile.write(prev)

outfile.close()
