import os, time

f = os.popen('ls -l')
records = f.readlines()
for record in records:
  print record
  time.sleep(1)
