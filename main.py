import math
from PIL import Image

# Specify the input and output filenames
INPUT_FILENAME = "picture.png"
OUTPUT_FILENAME = "output.svg"

# Define the size of each hexagon
HEXAGON_SIZE = 10

# Load the input picture
input_image = Image.open(INPUT_FILENAME)

# Calculate the number of hexagons in each row and column
width, height = input_image.size
num_hexagons_x = math.ceil(width / HEXAGON_SIZE)
num_hexagons_y = math.ceil(height / (HEXAGON_SIZE * math.sqrt(3)))

# Create an SVG string
svg_content = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">'

# Iterate through the hexagons
for i in range(num_hexagons_y):
    for j in range(num_hexagons_x):
        # Calculate the center coordinates of the hexagon
        center_x = (j + 0.5) * HEXAGON_SIZE
        center_y = (i + 0.5) * HEXAGON_SIZE * math.sqrt(3)

        # Calculate the average color of the hexagon
        total_r, total_g, total_b = 0, 0, 0
        num_pixels = 0

        # Iterate through the pixels within the hexagon
        for y in range(int(center_y - HEXAGON_SIZE / 2), int(center_y + HEXAGON_SIZE / 2)):
            for x in range(int(center_x - HEXAGON_SIZE / 2), int(center_x + HEXAGON_SIZE / 2)):
                if 0 <= x < width and 0 <= y < height:
                    r, g, b = input_image.getpixel((x, y))
                    total_r += r
                    total_g += g
                    total_b += b
                    num_pixels += 1

        # Calculate the average color
        avg_r = int(total_r / num_pixels)
        avg_g = int(total_g / num_pixels)
        avg_b = int(total_b / num_pixels)

        # Convert the RGB values to a hexadecimal color string
        color = f"#{avg_r:02x}{avg_g:02x}{avg_b:02x}"

        # Create the SVG hexagon element with the average color
        svg_content += f'<polygon points="{center_x - HEXAGON_SIZE / 2},{center_y} ' \
                       f'{center_x - HEXAGON_SIZE / 4},{center_y + HEXAGON_SIZE * math.sqrt(3) / 4} ' \
                       f'{center_x + HEXAGON_SIZE / 4},{center_y + HEXAGON_SIZE * math.sqrt(3) / 4} ' \
                       f'{center_x + HEXAGON_SIZE / 2},{center_y} ' \
                       f'{center_x + HEXAGON_SIZE / 4},{center_y - HEXAGON_SIZE * math.sqrt(3) / 4} ' \
                       f'{center_x - HEXAGON_SIZE / 4},{center_y - HEXAGON_SIZE * math.sqrt(3) / 4}" ' \
                       f'fill="{color}" />'

# Close the SVG string
svg_content += '</svg>'

# Write the resulting output picture as an SVG file
with open(OUTPUT_FILENAME, 'w') as f:
    f.write(svg_content)
