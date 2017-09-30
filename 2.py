try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except Exception:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
