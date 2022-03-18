word = ['qwerty', 'asdf', 'zxcv', 'yuio', 'hjk', 'vbnm']
with open('new_file.txt', "w") as f:
    for x in word:
        f.write("%s\n" % x)

content = open('new_file.txt')
print(content.read())