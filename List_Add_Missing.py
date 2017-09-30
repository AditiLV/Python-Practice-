file_name = raw_input("Enter file: ")

lines = [line.strip('\n') for line in open(file_name, 'r')]

word_list = []

for line in lines:
    words = line.split()
    for word in words:
        word = word.lower()
        if word in word_list:
            pass
        else:
            word_list.append(word)

print sorted(word_list)
