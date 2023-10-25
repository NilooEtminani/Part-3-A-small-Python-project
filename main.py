from PIL import Image
import svgwrite
# Specify the input and output filenames
INPUT_FILENAME = "picture.png"
OUTPUT_FILENAME = "output.svg"
# Load the input picture
input_image = Image.open(INPUT_FILENAME)
# Create an SVG object
svg = svgwrite.Drawing(OUTPUT_FILENAME)
# Convert the input image to SVG by iterating over each pixel
width, height = input_image.size
for y in range(height):
    for x in range(width):
        r, g, b = input_image.getpixel((x, y))
        # Convert the RGB values to a hexadecimal color string
        color = f"#{r:02x}{g:02x}{b:02x}"
        # Draw a rectangle with the pixel color
        svg.add(svg.rect(insert=(x, y), size=(1.5, 1.5), fill=color))
# Save the output as an SVG file
with open(OUTPUT_FILENAME, 'w') as f:
    f.write(svg.tostring())