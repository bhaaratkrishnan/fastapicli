from typer import Typer,Option,Exit,secho,colors
import os
from utis import install_package,create_default_project_files,create_ssr_project_files

app = Typer()

@app.command("create_project")
def create_project(name:str, ssr:bool = Option(...,prompt="Do you want SSR enabled")):
    
    secho("Creating Project",fg=colors.BRIGHT_GREEN)
    if name not in os.listdir():
        os.mkdir(name)
    else:
        secho("Project Name Already Exists!",fg=colors.RED)
        raise Exit()
    
    secho("Installing Dependencies", fg=colors.BRIGHT_GREEN)
    install_package("fastapi[all]")
    install_package("uvicorn")
    install_package("pipreqs")
    
    secho("FastAPI Installed Successfully", fg=colors.BRIGHT_GREEN)
    
    if ssr:
        create_ssr_project_files(name)
    else:
        create_default_project_files(name)
        os.system(f"pipreqs {name}")

@app.command("run")
def run():
    if "main.py" in os.listdir():
        os.system(f"uvicorn main:app --reload")
    else:
        secho("main.py File Not Found",fg=colors.BRIGHT_RED)
        raise Exit()

@app.command("deploy")
def deploy():
    print("Deploying")

if __name__ == "__main__":
    app()