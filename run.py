from PIL import Image, ImageDraw

def create_image(width, height, bbox_width, bbox_height, x_min, y_min):
    img = Image.new('RGB', (width, height), color=(255, 123, 234))
    draw = ImageDraw.Draw(img)
    
    # Draw the bounding box
    bbox_color = (100, 100, 123)  # Change this value for a different color
    draw.rectangle([x_min, y_min, x_min+bbox_width, y_min+bbox_height], fill=bbox_color)
    
    # Save the image
    img.save('output_image.png')

# Example usage
width = 3024
height = 4032
bbox_width = 1577
bbox_height = 3077
x_min = 723
y_min = 477
create_image(width, height, bbox_width, bbox_height, x_min, y_min)
