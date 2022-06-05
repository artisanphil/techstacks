from collections import Counter

f = open("data.txt", "r")
stacks = f.read().splitlines() 
f.close()
  
print(Counter(stacks))