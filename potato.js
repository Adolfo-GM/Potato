class Potato {
  /**
   * # Potato
   * The Potato file format created by Adolfo GM (JS version)
   */
  constructor(fileName) {
    if (!fileName.endsWith(".potato")) {
      fileName += ".potato";
    }
    this.fileName = fileName;
    this.lines = []; 
  }

  bake(location, content, potatoName = "potato", potatoType = "text") {
    if (typeof location !== "number" || location < 0) {
      throw new Error("Location must be a positive integer");
    }

    const contentPreview = content.length > 10 ? content.slice(0, 10) + "..." : content;
    console.log(`Baking ${potatoName} at column number ${location} with content: ${contentPreview}`);
    console.log(`${potatoName} is baked and ready to eat!`);

    while (this.lines.length <= location) {
      this.lines.push("\n");
    }

    const potatoTag = `<potato name="${potatoName}" column="${location}" potato_type="${potatoType}" timestamp="${Date.now()}">${content}</potato>\n`;
    this.lines[location] = potatoTag;
  }

  mash(column, deletePotato = false) {
    if (typeof column !== "number" || column < 0) {
      throw new Error("Column must be a positive integer");
    }

    const line = this.lines[column];
    if (line && line.includes(`column="${column}"`)) {
      if (deletePotato) {
        this.lines[column] = "\n";
      }
      return line;
    } else {
      console.log("No potato found at this column.");
      return null;
    }
  }

  async bakeImage(location, imageFile, potatoName = "potato") {
    if (typeof location !== "number" || location < 0) {
      throw new Error("Location must be a positive integer");
    }

    try {
      const base64 = await this._encodeImageToBase64(imageFile);
      this.bake(location, base64, potatoName, "image");
    } catch (err) {
      throw new Error("Failed to read image file: " + err.message);
    }
  }

  _encodeImageToBase64(file) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => resolve(reader.result.split(',')[1]); 
      reader.onerror = () => reject(reader.error);
      reader.readAsDataURL(file);
    });
  }

  download() {
    const blob = new Blob([this.lines.join("")], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = this.fileName;
    a.click();
    URL.revokeObjectURL(url);
  }
}
