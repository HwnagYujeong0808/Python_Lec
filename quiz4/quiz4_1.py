infile1 = open('Pre1990.txt', 'r')
infile2 = open('Retired.txt', 'r')
infile3 = open('Added.txt', 'r')

pre = {line.rstrip() for line in infile1}
retired = {line.rstrip() for line in infile2}
added = {line.rstrip() for line in infile3}
infile1.close()
infile2.close()
infile3.close()
colorset = pre.difference(retired)
colorset = colorset.union(added)
colorset = sorted(colorset)
outfile = open('newcolor.txt', 'w')
outfile.writelines('\n'.join(colorset))
outfile.close()
