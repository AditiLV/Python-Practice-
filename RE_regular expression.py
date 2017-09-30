user_input = raw_input("Enter a regular expression: ")
file_name = 'mbox.txt'
data_list = [line.strip('\n') for line in open(file_name, 'r')]

pattern = re.compile(user_input)

count = 0
for line in data_list:
    result = re.search(pattern, line)
    if result:
        count += 1

print "%s had %d lines that matched %s" % (file_name, count, user_input)
