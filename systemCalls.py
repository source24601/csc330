import os

print("Before exec")
os.execl("/bin/ls", "ls", "-l")

# This line is never reached if exec succeeds
print("After exec")
