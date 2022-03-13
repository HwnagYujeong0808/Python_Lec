infile1 = open('Justices.txt', 'r')
pre = [line.rstrip() for line in infile1]
infile1.close()

for i in range(len(pre)):
        pre[i] = pre[i].split((','))

pre
