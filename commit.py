import os
import sys

file = sys.argv[1]
cmd = 'git add %s; git commit -m \'Add %s\'' % (file, file)
print(cmd)
fp = os.popen(cmd)
print(fp.read())
status = fp.close()
print('status code ' + str(status))
