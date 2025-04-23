# pleiades/docker-toolz

This project contains a set of utility scripts to manage Docker containers and services related to the Pleiades server. The tools included allow you to configure Docker Compose, boot containers, and manage environment settings for the services.

## Directory Structure

The project contains the following directory and file structure:

```
.
├── bals                      # Script for a specific utility (e.g., handling Docker Compose operations)
├── getreadyin40sec           # Another script that prepares the environment and container
├── lib                       # Contains various helper modules
│   ├── argument_parser.py    # Handles argument parsing for commands
│   ├── compose_runner.py     # Functions for running Docker Compose commands
│   ├── defaults.py           # Default configurations and settings
│   ├── docker_compose.py     # Docker Compose file generation logic
│   ├── environment.py        # Handles environment variable setup
│   ├── __init__.py           # Marks the directory as a Python package
│   ├── parsers.py            # Parses configuration files
│   └── templates.py          # Templates for Docker Compose and related config
└── takeoff                   # Utility script to boot up containers with specific settings
```

## Installation

To use the scripts in this repository, you need to have Docker and Python installed. This project uses a virtual environment to manage Python dependencies.

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/pleiades.git
   cd pleiades/docker-toolz
   ```

2. Set up a Python virtual environment (if you haven't already):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate    # Windows
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, you can install the necessary packages individually (e.g., `python-dotenv`).

4. Make sure you have Docker and Docker Compose installed on your system.

## Usage

### `bals`

The `bals` script performs Docker Compose operations. You can use it to interact with the Docker Compose setup defined in your project.

```bash
./bals [options]
```

### `getreadyin40sec`

This script prepares the environment for your containers by loading settings and booting up Docker containers.

```bash
./getreadyin40sec [options]
```

### `takeoff`

The `takeoff` script boots up the Docker containers based on environment settings and executes a shell inside the container.

```bash
./takeoff [options]
```

## Configuration

- The `settings.yml` file defines the settings for the Docker Compose setup.
- `.env` contains environment variables like `APP_USER` and `SHELL`, which can be used for configuring the container execution.
- `.gitignore` ensures that sensitive files, such as `.env`, are not committed to version control.

## Contributing

Feel free to fork the repository and contribute by submitting pull requests. Ensure that your code follows the existing coding style and includes tests where applicable.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

