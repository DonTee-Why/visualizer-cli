
# Visualizer-CLI

Visualizer-CLI is a terminal program written in Python that enables you to visualize data. The data is gotten from an API endpoint in key-value pairs (i.e dates for keys, and number of users for values). Data is then presented using a graph drawn in the terminal.

## Features

- Pass data boundaries in as flags in the terminal
- Represents data in a graph
- Draw graph directly in the terminal

## Installation

This project requires [Python](https://www.python.org/downloads/) v3.8+ to run.

1. Clone the project from the repository and then cd into the root directory.

```sh

git clone https://github.com/DonTee-Why/visualizer-cli.git
cd visualize-cli

```

2. To avoid alterating global packages, I suggest using a virtual environment. Create a virtual environment

```sh
python -m venv env
```

And then activate it.

On linux:

```sh
source ./env/bin/activate
```

On windows:

```sh
env\Scripts\activate.bat
```

3. Install the dependencies in the virtual environment.

```sh
cd visualizer-cli
pip install -r requirements.txt
```

4. Run the project

```sh
python -m visualize -s <START DATE> -e <END DATE>
```

## Testing

The project includes unit tests written with `unittest`.

- To run all the tests:

```sh
python -m unittest
```

- To run individual test suites:

```sh
python -m unittest tests.<TEST SUITE>
```

## License

MIT License
