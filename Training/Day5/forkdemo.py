import os, time

print 'Hello'

c = os.fork()

if c == 0:
  print 'child started with pid ', os.getpid()
  for i in range(10):
    print 'child value is ', i
    time.sleep(1)
#  os._exit(0)
else:
  os.wait()

print 'paret started with pid ', os.getpid()
for j in range(10):
    print 'parent value is ', j
    time.sleep(1)
os._exit(0)
