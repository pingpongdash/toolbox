import shutil
import subprocess
import sys

def get_compose_command():
    if shutil.which("docker-compose"):
        return ["docker-compose"]
    elif shutil.which("docker"):
        result = subprocess.run(["docker", "compose", "version"],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            return ["docker", "compose"]
    print("Error: Neither 'docker-compose' nor 'docker compose' is available.", file=sys.stderr)
    sys.exit(1)

def run_compose_command(args, check=True):
    cmd = get_compose_command()
    subprocess.run(cmd + args, check=check)
