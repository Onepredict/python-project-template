from pathlib import Path
import shutil


from pathlib import Path


def remove(path_: Path):
    if path_.is_file():
        path_.unlink()
    elif path_.is_dir():
        for sub_path in path_.rglob("*"):
            remove(sub_path)
        path_.rmdir()


if "{{cookiecutter.use_docker}}" == "no":
    remove(Path("./build"))
    remove(Path("./docker-compose.yml"))
