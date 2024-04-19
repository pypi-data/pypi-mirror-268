- [Flake8 Small Entities Plugin](#flake8-small-entities-plugin)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Configuration](#configuration)
    - [Command-Line Options](#command-line-options)
    - [Config File Example](#config-file-example)
  - [Rules Enforced](#rules-enforced)
  - [Motivation](#motivation)
  - [Contributing](#contributing)
  - [License](#license)


# Flake8 Small Entities Plugin

`flake8-small-entities` is a Flake8 plugin that encourages developers to write smaller, more manageable entities by enforcing the Object Calisthenics rule "Keep Entities Small." The plugin analyzes Python code to ensure functions, classes, and modules do not exceed predefined line limits.

## Installation

To install `flake8-small-entities`, use pip:

```bash
pip install flake8-small-entities
```

## Usage

Once installed, the plugin will be automatically activated alongside Flake8. To analyze your project, simply run:

```bash
flake8 your_project_directory
```

Violations of the line limits for functions, classes, and modules will be flagged accordingly.

## Configuration

The plugin allows customization of the maximum number of lines allowed for each entity type. You can specify these settings in your Flake8 configuration file or directly via command-line options.

### Command-Line Options

- `--max-fn-lines`: Maximum number of lines in a function (default is 15)
- `--max-class-lines`: Maximum number of lines in a class (default is 50)
- `--max-module-lines`: Maximum number of lines in a module (default is 200)

### Config File Example

You can also set these options in a `.flake8` configuration file in your project root:

```ini
[flake8]
max-fn-lines = 20
max-class-lines = 60
max-module-lines = 300
```

## Rules Enforced

- **FSE100**: Function has too many lines
- **FSE101**: Class has too many lines
- **FSE102**: Module has too many lines

Each rule will indicate where the entity exceeds the specified line count, helping developers to refactor code into smaller, more focused components.

## Motivation

Adhering to the "Keep Entities Small" rule improves code readability, maintainability, and facilitates easier debugging and testing. Large entities often perform too many functions, making them difficult to understand and change.

## Contributing

Contributions are welcome! If you have suggestions for improvements or encounter any issues, please open an issue or submit a pull request on our GitHub repository.

## License

This plugin is distributed under the MIT License. The full license text is available in the `LICENSE` file included with the source code.
