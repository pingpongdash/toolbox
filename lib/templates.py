docker_compose_version = '3.8'
docker_compose = {
    'version': docker_compose_version,
    'services': {},
    'networks': {
        'default': {
            'external': True ,
        },
    },
}
