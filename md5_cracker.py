import sys
import hashlib
try:
	hash=sys.argv[1]
	file=sys.argv[2]
	if len(hash) != 32:
		print 'Invalid hash!'
	lines = open(file).read().splitlines()
	for line in lines:
		h=hashlib.md5(line).hexdigest()
		if hash==h:
			print 'Hash ->', line
			break
except:
	print 'Usage:',sys.argv[0],'[hash] [filename]'