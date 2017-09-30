file_name = 'mbox-short.txt'
lines = [line.strip('\n') for line in open(file_name, 'r')
         if line.startswith("From ")]
who_from_dict = {}

for line in lines:
    words = line.split()
    who_from_dict[words[1]] = who_from_dict.get(words[1], 0) + 1

print who_from_dict
