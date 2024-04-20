import os
import click
import toml
from packaging import version

@click.command()
@click.option("--type", type=click.Choice(["stable", "beta"]))
def update(type = None):
    with open("pyproject.toml", "r") as f:
        pyproject = toml.load(f)

    # get current version
    ver = version.parse(pyproject["project"]["version"])
    # is beta
    verbeta = ver.is_prerelease

    if type is None:
        # get cli mtime
        cli_mtime = os.path.getmtime("cli.py")

        # pyproject last update time
        pyproject_mtime = os.path.getmtime("pyproject.toml")

        gap = cli_mtime - pyproject_mtime 
        # if gap larger than a month
        if gap > 60 * 60 * 24 * 30:
            click.prompt("pyproject.toml is not updated in a month, please update it manually", default="y", type=click.Choice(["y", "n"]))
            exit()

        # if gap larger than 3 weeks
        # prompt whether to make it stable
        if gap > 60 * 60 * 24 * 21:
            res = click.prompt("pyproject.toml is not updated in 3 weeks, do you want it stable", default="y", type=click.Choice(["y", "n"]))
            if res == "y":
                type= "stable"
            else:
                type= "beta"
        
        # if less than a week
        if gap < 60 * 60 * 24 * 7:
            input("pyproject.toml is updated less than a week, please update it manually")
            exit()

        type= "beta"
    
    if verbeta and pyproject["project"]["version"][-1].isdigit() and int(pyproject["project"]["version"][-1]) >= 4:
        type= "stable"

    oldver = pyproject["project"]["version"] 
    if type == "stable":
        pyproject["project"]["version"] = f"{ver.major}.{ver.minor}.{ver.micro}"
    elif verbeta:
        pyproject["project"]["version"] = f"{pyproject["project"]["version"][:-2]}b{int(pyproject["project"]["version"][-1]) + 1}"
    else:
        pyproject["project"]["version"] = f"{ver.major}.{ver.minor+1}.{ver.micro}b1"

    input(f"update {oldver} to {pyproject['project']['version']}?")

    with open("pyproject.toml", "w") as f:
        toml.dump(pyproject, f)

if __name__ == "__main__":
    update()

# 1