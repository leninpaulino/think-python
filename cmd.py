import os

cmd = 'ls -l'
fp = os.popen(cmd)
print(fp.read())
status = fp.close()
print('status code ' + str(status))
