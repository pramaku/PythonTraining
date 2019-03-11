import urllib

sock = urllib.urlopen(r'http://www.google.com/')

html = sock.read()

sock.close()

print html
