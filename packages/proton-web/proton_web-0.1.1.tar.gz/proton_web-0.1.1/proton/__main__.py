import rich.style
import typer, os
from rich.progress import Progress, SpinnerColumn, TextColumn
import subprocess as sp
import shutil
from rich.panel import Panel
from rich import print as rprint
import rich
app = typer.Typer()
projectapp = typer.Typer(help="Project management.")
app.add_typer(projectapp, name="project")

@projectapp.command()
def init(dir:str="."):
    """Initalizes a new project."""
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task("Creating project...")
        os.mkdir(dir + "/" + "src")
        os.mkdir(dir + "/" + "web")
        with open(dir + "/" + "src/main.py", "w") as f:
            f.write("import proton as pt\nwin = pt.Window('A Proton webapp', '../web')\nwin.start(debug=True)\ndocument=pt.Document(win)")
        with open(dir + "/" + "web/index.html", "w") as f:
            f.write("<!DOCTYPE html>\n<body>\n  <h1>Hello, World!</h1>\n</body>\n</html>")

def error(text:str):
    rprint(Panel(text, title="[red]Error", title_align="left", style=rich.style.Style(color = "red")))

@app.command()
def build(mode:str):
    """Build your project."""
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        progress.add_task("Building...", total = 2)
        print("")
        print("")
        if mode == "debug":
            p = sp.Popen("python -m nuitka src/main.py --standalone --nofollow-import-to=cefpython3 --enable-console", shell=True)
        elif mode == "release":
            p = sp.Popen("python -m nuitka src/main.py --standalone --nofollow-import-to=cefpython3 --disable-console", shell=True)
        else:
            error("[white]Mode " + mode + " does not exist, quitting.\nUse build debug or build release. (debug enables the console, while release doesn't.)")
            
            exit()
        print("")
        print("")
        p.wait()
        
        #try:
        #    os.mkdir("dist")
        #except FileExistsError:
        #    pass
        shutil.rmtree("main.build")
        shutil.move("main.dist", "dist")
        shutil.copytree("web", "dist/web")
        
    print("Done!")
        
if __name__ == "__main__":
    app()