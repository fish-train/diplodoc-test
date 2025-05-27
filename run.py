# coding : utf-8

import subprocess
import time

def autobuild():
	cmd = "npx -y @diplodoc/cli -i . -o ./builds --output-format html && npx http-server ./builds -p 5005"
	subprocess.Popen(cmd, shell = True)

autobuild()
