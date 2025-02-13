required_keys = ['base_directory', 'container_name', 'network_name']

defaults = {
    'settings': 'settings.yml',
    'dot_env': '.env',
    'output_dir': '.compose',
    'output_file': 'docker-compose.yml',
    'dockerfile_path': 'Dockerfile',
    'image_save_dir': '.',
    'dns': ['8.8.8.8', '8.8.4.4'],
}
