import yaml
import json
from lib.defaults import defaults, required_keys

def generate_compose(settings):
    docker_compose = {
        'services': {},
        'networks': {}
    }

    # Define the container configuration from settings.yml
    container_name = settings['container_name']
    docker_compose['services'][container_name] = {
        'hostname': container_name,
        'container_name': container_name,
        'image': container_name,
        'tty': True,
        'build': {
            'context': '.',
        },
        'dns': settings.get('dns', '8.8.8.8')  # Set DNS if available
    }

    # Handle network settings based on 'network_type'
    network_name = settings['network_name']
    if 'network_type' in settings and settings['network_type'] == 'overlay':
        docker_compose['networks'][network_name] = {
            'external': True,
            'driver': 'overlay'
        }
        docker_compose['services'][container_name]['networks'] = [network_name]
    else:
        docker_compose['networks'][network_name] = {
            'driver': 'bridge',
            'name': network_name ,
        }
        docker_compose['services'][container_name]['networks'] = [network_name]

    # Add environment variables from the settings
    docker_compose['services'][container_name]['environment'] = {
        key: '${'+key+'}'
        for key, value in settings.get('environment_variables', {}).items()
    }
    docker_compose['services'][settings['container_name']]['build']['args'] = {
        key: '${'+key+'}'
        for key, value in settings.get('environment_variables', {}).items()
    }

    # Add volume bindings from the settings without evaluating shell commands or replacing variables
    docker_compose['services'][container_name]['volumes'] = [
        {
            'source': volume['source'],
            'target': volume['target'],
            'type': volume.get('type', 'bind')
        }
        for volume in settings.get('shared_directories', [])
    ]

    # Add service options like restart policy and ports
    service_options = settings.get('service_options', {})
    docker_compose['services'][container_name].update(service_options)

    # Write the generated Docker Compose file
    # print(json.dumps(docker_compose, indent=4, ensure_ascii=False))
    write_docker_compose_yaml(docker_compose, defaults)

def write_docker_compose_yaml(docker_compose, defaults):
    output_file = defaults.get('output_file', 'docker-compose.yml')
    with open(output_file, 'w') as file:
        yaml.dump(docker_compose, file, sort_keys=False)
