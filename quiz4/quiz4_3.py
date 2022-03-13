def file_read():
    with open('words.txt', 'r') as file:
        while(True):
            line = file.readline()
            if line =='':
                break
            yield line.strip()

for i in file_read():
    print(i)
