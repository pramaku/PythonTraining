import os

print 'Hello'

os.execvp('ls', ['ls', '-l'])

print 'Done'
