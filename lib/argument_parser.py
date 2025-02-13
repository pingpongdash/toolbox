import argparse
import os

def parse_arguments(defaults):
    parser = argparse.ArgumentParser(description='Generate .env file from settings file.')
    parser.add_argument('--settings', help='Specify the settings file (default: settings.yml)')
    parser.add_argument('--noboot', action='store_true', help='Do not boot the container')
    parser.add_argument('--noconf', action='store_true', help='Do not generate config')
    args = parser.parse_args()

    if args.settings:
        defaults['settings'] = args.settings
    else:
        defaults['settings'] = os.path.join(os.getcwd(), 'settings.yml')

    return args
