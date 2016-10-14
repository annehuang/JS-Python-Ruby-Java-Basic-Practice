# for parsing

infile = open('output values q2', 'r')

outfile = open('parsed', 'w')

lst = []

for line in infile:
    l = line.split("word ")
    for i in range(0, len(l)):
        if i%2 == 1:
            outfile.write(l[i])

outfile.close()
