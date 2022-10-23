
import os, random, string
from time import sleep

N = 10
t = 10

letters = string.ascii_letters + string.digits+ string.punctuation

os.system('')
print ("Starting ... \033[32mSuccess!\033[0m")
for i in range(N+1):
  print(f"step {i}/{N}")
  for j in range(random.randint(2, 6)):
    print ('  ' + ''.join(random.choice(letters) for _ in range(random.randint(30, 40))))
  print()
  sleep(t)

print ("Completing ... \033[32mSuccess!\033[0m")
