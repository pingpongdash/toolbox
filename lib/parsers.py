import os
import sys
import yaml
import subprocess
import re

def execute_shell_command(command):
    try:
        result = subprocess.check_output(command, shell=True, text=True).strip()
        return result
    except subprocess.CalledProcessError as e:
        print(f"Command '{command}' failed with error: {e}")
        sys.exit(1)

def replace_shell_commands(value):
    pattern = r'\$\((.*?)\)'
    while re.search(pattern, value):
        match = re.search(pattern, value)
        if match:
            command = match.group(1)
            command_output = execute_shell_command(command)
            value = value.replace(f"$({command})", command_output, 1)
    return value

def load_settings(settings_file):
    if not os.path.isfile(settings_file):
        print("Yo, where's that settings.yml at?")
        sys.exit(1)

    with open(settings_file, 'r') as f:
        settings = yaml.safe_load(f)
    for key, value in settings.items():
        if isinstance(value, str) and '$(' in value:
            settings[key] = replace_shell_commands(value)
    if 'environment_variables' not in settings:
        settings['environment_variables'] = {}

    settings['environment_variables'].setdefault('BASE_DIRECTORY', settings['base_directory'])
    settings['environment_variables'].setdefault('CONTAINER_NAME', settings['container_name'])
    settings['environment_variables'].setdefault('NETWORK_NAME', settings['network_name'])

    return settings
