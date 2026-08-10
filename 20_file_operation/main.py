

file_content = open("./test.txt", 'r')
content = file_content.read()

print(content)
file_content.close()


with open("./test.txt", 'a') as f:
    f.write("\n\nnew line added..")


with open("./test.txt", 'r') as f:
    print(f.read())


