import os
import subprocess
import sys

from subprocess import Popen, PIPE
try:
     os.system("alpr -c us webcam")
except:
        pass

#os.system('pdv -t %s > /home/tac/Desktop/123.txt' % epoch_name)


#cmd = ['alpr -c us webcam']

#with open('/home/tac/Desktop/output.txt', 'w') as out:
 #   return_code = subprocess.call(cmd, stdout=out)
f = open("/home/tac/Desktop/test.txt", 'w')

sys.stdout = f
try:
     print os.system("alpr -c us webcam")
except:
      pass
f.close()

