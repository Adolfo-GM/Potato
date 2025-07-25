import base64
import time

class Potato:
    '''
    # Potato
    The Potato file format created by Adolfo GM
    '''
    def __init__(self, file_name: str):
        if not file_name.endswith(".potato"):
            file_name += ".potato"
        self.file_name = file_name
        try:
            open(self.file_name, "x", encoding="utf-8")
        except FileExistsError:
            pass
        
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
            
        content_preview = content[:10] + "..." if len(content) > 10 else content
        print(f"Baking {potato_name} at column number {location} with content: {content_preview}")
        print(f"{potato_name} is baked and ready to eat!")

        with open(self.file_name, "r+", encoding="utf-8") as f:
            lines = f.readlines()
            while len(lines) <= location:
                lines.append("\n")
            lines[location] = f'<potato name="{potato_name}" column="{location}" potato_type="{potato_type}" timestamp="{time.time()}">{content}</potato>\n'
            f.seek(0)
            f.writelines(lines)
            f.truncate()

    def mash(self, column: int, delete: bool = False):
        """
        Mashes a potato at the specified column.
        > column: The column number of the potato to be mashed. It must be a positive integer.
        > delete: If True, the potato will be returned and deleted. If False, it will be returned.
        Returns the mashed potato (content of the potato at the column) or None if not found.
        """
        if not isinstance(column, int) or column < 0:
            raise ValueError("Column must be a positive integer")

        with open(self.file_name, "r+", encoding="utf-8") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if f'column="{column}"' in line:
                    potato = line
                    if delete:
                        lines[i] = "\n"
                        f.seek(0)
                        f.writelines(lines)
                        f.truncate()
                    return potato
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