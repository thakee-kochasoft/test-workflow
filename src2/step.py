
# step i, N

import sys, os, random, string
from time import sleep

i = int(sys.argv[1])
N = int(sys.argv[2])
t = 10

letters = string.ascii_letters + string.digits+ string.punctuation

print(f"step {i}/{N}")
for j in range(random.randint(2, 6)):
  print ('  ' + ''.join(random.choice(letters) for _ in range(random.randint(30, 40))))
print()
sleep(t)
