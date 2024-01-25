import os, sys
os.system("git pull")
try:
    __import__("Share").Younisxyzbot()
except Exception as e:
    exit(str(e))
 
