import subprocess
import sys 
import os
import importlib.util 

def install_package(name):
    if importlib.util.find_spec(name) is None:
        subprocess.check_call([sys.executable, "-m", "pip", "install",name])

def create_default_project_files(dir):
    #creating main.py
    with open(f"{dir}/main.py","w") as file:
        content = [
            "from fastapi import FastAPI\n\n",
            "app = FastAPI()\n\n"
            "@app.get('/')\n",
            "async def index():\n"
            "   return {'status':200}\n"

        ]
        file.writelines(content)
def create_ssr_project_files(dir):
    create_default_project_files(dir)
    #create directories
    os.mkdir(f"{dir}/static")
    os.mkdir(f"{dir}/static/img")
    os.mkdir(f"{dir}/templates")
    #create index.html
    with open(f"{dir}/templates/index.html","w") as file:
        content = [
            """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>""",
        ]  
        file.writelines(content)
    #create style.css
    with open(f"{dir}/static/styles.css","w") as f:
        pass
    