import os
import yaml
import re
import sys
import subprocess


def load_settings(settings_file):
    if not os.path.isfile(settings_file):
        print("Yo, where's that settings.yml at?")
        sys.exit(1)

    with open(settings_file, 'r') as f:
        settings = yaml.safe_load(f)
    return settings

def replace_shell_commands(value):
    pattern = r'\$\((.*?)\)'
    while re.search(pattern, value):
        match = re.search(pattern, value)
        if match:
            command = match.group(1)
            command_output = execute_shell_command(command)
            value = value.replace(f"$({command})", command_output, 1)
    return value

def execute_shell_command(command):
    try:
        result = subprocess.check_output(command, shell=True, text=True).strip()
        return result
    except subprocess.CalledProcessError as e:
        print(f"Command '{command}' failed with error: {e}")
        sys.exit(1)

def generate_env_file(settings, env_file_path):
    with open(env_file_path, 'w') as f:
        for key, value in settings.items():
            if key not in ["environment_variables", "shared_directories", "service_options"]:
                value = replace_shell_commands(value)
                f.write(f"{key.upper()}={value}\n")

        f.write("\n# Environment Variables\n")
        for key, value in settings.get("environment_variables", {}).items():
            value = replace_shell_commands(value)
            f.write(f"{key.upper()}={value}\n")
