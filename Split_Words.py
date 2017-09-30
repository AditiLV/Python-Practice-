f = open('mbox.txt')
count = 0
a = 0.0
for line in f:
    if line.startswith('X-DSPAM-Confidence:'):
        c,b = line.rsplit(':')
        a = float(b) + a
        count = count + 1
print(a/count)
    
   
    
