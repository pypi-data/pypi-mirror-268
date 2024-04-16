# Heare IDs

A Python module for creating, validating, parsing, and manipulating tokens that are base-62 encoded.

## Features

- Generate unique tokens with a prefix, generation character, timestamp, and entropy part
- Validate the structure and character set of tokens
- Parse tokens into their components (prefix, generation, timestamp, entropy)
- Swap the prefix of a token with a new prefix

## Installation

```
pip install heare-ids
```

## Usage

### Generating Tokens

```python
from heare import ids

# Generate a new token with default settings
token = ids.new('my_prefix')

# Generate a token with custom generation, timestamp, and entropy
token = ids.new('my_prefix', generation='A', timestamp=1234567890, entropy=15)
```

### Validating Tokens

```python
is_valid = ids.is_valid(token)
```

### Parsing Tokens

```python
parsed = ids.parse(token)
prefix = parsed.prefix
generation = parsed.generation
timestamp = parsed.timestamp
entropy = parsed.entropy
```

### Swapping Prefixes

```python
new_token = ids.swap_prefix(token, 'new_prefix')
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
