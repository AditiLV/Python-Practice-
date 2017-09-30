list_one = [x for x in range(1,10)]
print(list_one)


file_name = raw_input("Enter a file name: ")
lines = [line.strip("\n") for line in open(file_name, 'r')
         if line.startswith("From") and not line.startswith("From:")]

count = 0
for line in lines:
    words = line.split()
    print(words[1])
    count += 1
print( "There were %s lines in the file with From as the first word", count)


