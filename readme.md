# .potato
<img src="potaton.png" height="150px">

## What is .potato?

`.potato` is a simple, text-based file format created by Adolfo GM for storing various types of data, including text and base64 encoded images, in individual "potatoes" identified by a column number. Each potato is stored on a line within the file, enclosed in `<potato>` tags with attributes for name, column number, data type, and a timestamp.

## Basic Usage

To start using the `.potato` format, you'll need the `Potato` class. Here's a quick example of how to create a `.potato` file and bake a potato into it:

```python
from potato import Potato

# Create a new .potato file (or open an existing one)
pt = Potato("my_data.potato")

# Bake a text potato at column 0
pt.bake(0, "This is some important text!", "ImportantNote")

# Acess the potato
print(pt.mash(0))  # Output: This is some important text!

```

to get the potato module download the `potato.py` file from the repository and place it in your project directory. You can then import the `potato` class and use it to create, read, and manipulate `.potato` files!

