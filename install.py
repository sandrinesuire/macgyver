import os
os.system("pip install virtualenv")
os.system("virtualenv -p python3 env")
os.system("source env/bin/activate")
os.system("pip install -r requirements.txt")
