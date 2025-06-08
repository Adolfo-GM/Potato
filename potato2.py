import base64
import time
import os
import tempfile

class Potato:
    '''
    # Potato
    The Potato file format created by Adolfo GM (version 2.0)
    '''
    def __init__(self, file_name: str):
        if not file_name.endswith(".potato"):
            file_name += ".potato"
        self.file_name = file_name
        try:
            open(self.file_name, "x", encoding="utf-8")
        except FileExistsError:
            pass

    def _generate_potato_line(self, location: int, content: str, potato_name: str, potato_type: str):
        return f'<potato name="{potato_name}" column="{location}" potato_type="{potato_type}" timestamp="{time.time()}">{content}</potato>\n'

    def bake(self, location: int, content: str, potato_name: str = "potato", potato_type: str = "text"):
        """
        # Bake
        Bakes a potato at the specified location with the given content and name.
        > location: The location where the potato is baked. It must be a positive integer.
        > content: The content to be baked into the potato.
        > potato_name: The name of the potato. Default is "potato". 
        """
        if not isinstance(location, int) or location < 0:
            raise ValueError("Location must be a positive integer")
        new_line = self._generate_potato_line(location, content, potato_name, potato_type)
        found = False
        idx = -1
        with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as tmpfile, open(self.file_name, "r", encoding="utf-8") as original:
            for idx, line in enumerate(original):
                if idx == location:
                    tmpfile.write(new_line)
                    found = True
                else:
                    tmpfile.write(line)
            if not found:
                for _ in range(idx + 1, location):
                    tmpfile.write("\n")
                tmpfile.write(new_line)
        os.replace(tmpfile.name, self.file_name)
        content_preview = content[:10] + "..." if len(content) > 10 else content
        print(f"Baking {potato_name} at column number {location} with content: {content_preview}")
        print(f"{potato_name} is baked and ready to eat!")

    def mash(self, column: int, delete: bool = False):
        """
        Mashes a potato at the specified column.
        > column: The column number of the potato to be mashed. It must be a positive integer.
        > delete: If True, the potato will be returned and deleted. If False, it will be returned.
        Returns the mashed potato (content of the potato at the column) or None if not found.
        """
        if not isinstance(column, int) or column < 0:
            raise ValueError("Column must be a positive integer")
        mashed = None
        with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as tmpfile, open(self.file_name, "r", encoding="utf-8") as original:
            for idx, line in enumerate(original):
                if idx == column and f'column="{column}"' in line:
                    mashed = line
                    if delete:
                        tmpfile.write("\n")
                    else:
                        tmpfile.write(line)
                else:
                    tmpfile.write(line)
        os.replace(tmpfile.name, self.file_name)
        if mashed:
            return mashed
        print("No potato found at this column.")
        return None

    def bake_image(self, location: int, image_path: str, potato_name: str = "potato"):
        """
        # Bake Image
        Bakes an image at the specified location with the given name.
        > location: The location where the potato is baked. It must be a positive integer.
        > image_path: The path to the image file to be baked into the potato.
        > potato_name: The name of the potato. Default is "potato". 
        """
        if not isinstance(location, int) or location < 0:
            raise ValueError("Location must be a positive integer")
        try:
            with open(image_path, "rb") as img_file:
                encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
                self.bake(location, encoded_string, potato_name, potato_type="image")
        except FileNotFoundError:
            raise FileNotFoundError(f"Image file not found: {image_path}")

if __name__ == "__main__":
    potato = Potato("demo")
    potato.bake(0, "This is a test potato", "TestPotato")
    potato.bake(1, "Another test potato", "AnotherPotato")
    potato.bake(2, "This is a test potato", "TestPotato")
    potato.bake(3, "Another test potato", "AnotherPotato")
    potato.bake(4, "This is a test potato", "TestPotato")
    potato.bake(5, "Another test potato", "AnotherPotato")
    potato.bake(6, "This is a test potato", "TestPotato")
    potato.bake(7, "Another test potato", "AnotherPotato")
    potato.bake(8, "This is a test potato", "TestPotato")
    potato.bake_image(9, "potaton.png", "TestImagePotato")
