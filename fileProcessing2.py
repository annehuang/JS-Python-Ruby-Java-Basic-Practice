# for parsing

infile = open('output', 'r')

outfile = open('parsed', 'w')

# parse a file to find time measurements I logged

for line in infile:
    l = line.split("word ")
    for i in range(0, len(l)):
        if i%2 == 1:
            outfile.write(l[i])

outfile.close()
