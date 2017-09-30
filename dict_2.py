file_name = 'mbox-short.txt'
lines = [line.strip('\n') for line in open(file_name, 'r')
         if line.startswith("From ")]
date_dict = {}

for line in lines:
    words = line.split()
    date_dict[words[2]] = date_dict.get(words[2], 0) + 1

print date_dict
