
# JsonCanvas Python Implementation

This project provides a Python implementation of the [JsonCanvas format](https://github.com/obsidianmd/jsoncanvas/blob/main/spec/1.0.md), designed to facilitate the creation, manipulation, and visualization of a structured canvas using objects and relations. It leverages Python's `pydantic` library to ensure data validation and management, supporting a range of node and edge types for comprehensive canvas construction.

## Features

- Robust model definitions for canvas elements (Nodes and Edges) with comprehensive validation and default settings via `pydantic`.
- Dynamic addition and manipulation of various node types including Text, File, Link, Group, and Edge elements.
- Enhanced canvas operations allowing easy addition of nodes and edges with automated type handling.
- Serialize canvas structures to standard Python dictionaries for easy integration with other systems.

## Installation

```bash
pip install openjsoncanvas
```

## Usage

### Creating a Canvas

Instantiate and manipulate a canvas with various nodes and edges:

```python
from openjsoncanvas import Canvas

canvas = Canvas()

canvas.create_text_node(id='1', x=0, y=0, width=100, height=100, text='Hello, World!')
canvas.create_file_node(id='2', x=100, y=100, width=100, height=100, file='example.md')
canvas.create_link_node(id='3', x=200, y=200, width=100, height=100, url='https://example.com')
canvas.create_group_node(id='4', x=300, y=300, width=100, height=100)
canvas.create_edge(id='5', fromNode='1', toNode='2', fromEnd='arrow', toEnd='arrow', color='red', label='Edge')

# you can save and load the canvas to/from a file
canvas.to_file('my_canvas.canvas')
canvas = Canvas.from_file('my_canvas.canvas')
```
