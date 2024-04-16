from pathlib import Path


def die(msg: str, code: str):
    print(msg)
    exit(code)



class Project:
    def __init__(self, dir: Path, name: str = 'proj', runner: str = None, editor: str = 'nvim', multi: bool = False):
        self.name: str = name
        self.dir: Path = dir
        self.editor: str = editor
        self.runner: str = runner
        self.multi: bool = multi

    def __str__(self):
        return f"{self.name} ->\n\tpath -> {self.dir}\n\teditor -> {self.editor}\n\trunner -> {self.runner}"

