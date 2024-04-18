import shlex
import shutil
import subprocess
import sys
from pathlib import Path
from tomllib import loads


class Colr:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


class PyProjectConfig:
    cwd: Path
    pyproject: Path
    vt_config: dict

    npm_exec: str
    npx_exec: str
    serve_app: str
    vite_apps: list

    def __init__(self):
        self.cwd = Path.cwd()
        self.pyproject = self.cwd / "pyproject.toml"
        self.load_pyproject()

    def load_pyproject(self):
        if not self.pyproject.exists():
            raise FileNotFoundError("pyproject.toml not found.")

        pyproject_raw = loads(str(self.pyproject.read_text()))
        self.vt_config = pyproject_raw.get("tool", {}).get("vite_transporter", {})
        self.npm_exec = self.vt_config.get("npm_exec", "npm")
        self.npx_exec = self.vt_config.get("npx_exec", "npx")
        self.serve_app = self.vt_config.get("serve_app", "app")
        self.vite_apps = self.vt_config.get("vite_apps", [])

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return None


class NPXCommander:
    def __init__(self, workdir: Path, npx_binary: str = "npx"):
        self.npx_binary = npx_binary
        self.workdir = workdir

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return None

    def run(self, command: str):
        subprocess.run([self.npx_binary, *shlex.split(command)], cwd=self.workdir)


class NPMCommander:
    def __init__(self, workdir: Path, npm_binary: str = "npm"):
        self.npm_binary = npm_binary
        self.workdir = workdir

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return None

    def run(self, command: str):
        subprocess.run([self.npm_binary, *shlex.split(command)], cwd=self.workdir)


def _compile(pypro: PyProjectConfig, vite_apps: list[dict], replace: bool = False):
    pc: PyProjectConfig = pypro

    print("Compiling Vite apps...")
    vt_dir = pc.cwd / pc.serve_app / "vt"

    # Delete contents of vt_dir
    if vt_dir.exists():
        if not replace:
            prompt = input(
                f"Continuing will replace the contents of \n\r"
                f"{vt_dir} \n\r"
                f"Do you want to continue? (Y/n): "
            )
        else:
            prompt = "y"

        if prompt.lower() == "y" or prompt == "":
            for item in vt_dir.iterdir():
                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    item.unlink()

        else:
            print("Operation aborted.")
            sys.exit(0)

    else:
        vt_dir.mkdir()

    # Create directories for vite apps
    for app in vite_apps:
        va_path = pc.cwd / app.get("vite_app")
        va_node_modules = va_path / "node_modules"
        va_dist = va_path / "dist"
        va_assets = va_dist / "assets"

        va_vt_path = vt_dir / app.get("vite_app")

        if not va_vt_path.exists():
            va_vt_path.mkdir()

        if not va_node_modules.exists():
            with NPMCommander(va_path, pc.npm_exec) as npm:
                npm.run("install")

        with NPXCommander(va_path, pc.npx_exec) as npx:
            npx.run("vite build --mode production")

        for item in va_assets.iterdir():
            print(f"{Colr.OKGREEN}Copying {item.name} to {va_vt_path}{Colr.END}")

            if item.suffix == ".js":
                with open(va_vt_path / item.name, "w") as f:
                    content = item.read_text()
                    f.write(content.replace("assets/", f"__vt/{app.get('vite_app')}/"))
            else:
                shutil.copy(item, va_vt_path / item.name)

        shutil.rmtree(va_dist)

    print("Compilation complete.")
