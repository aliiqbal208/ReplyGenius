from PIL import Image, ImageDraw, ImageFont

def create_icon(size):
    # Create a new image with a transparent background
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Modern gradient-like background (LinkedIn blue with a twist)
    # Using a vibrant gradient effect
    draw.rounded_rectangle([(0, 0), (size, size)], radius=size//5, fill='#0A66C2')
    
    # Add a subtle accent circle in top-right for "genius" spark effect
    accent_size = size // 3
    accent_pos = size - accent_size - size//10
    draw.ellipse([(accent_pos, size//10), 
                  (accent_pos + accent_size, size//10 + accent_size)], 
                 fill='#00A0DC', outline=None)
    
    # Draw a chat bubble with sparkle effect for "Reply"
    bubble_padding = size // 6
    bubble_width = size - (2 * bubble_padding)
    bubble_height = bubble_width * 0.6
    
    # Main chat bubble
    bubble_y = size // 2 - bubble_height // 2
    draw.rounded_rectangle(
        [(bubble_padding, bubble_y), 
         (bubble_padding + bubble_width, bubble_y + bubble_height)], 
        radius=size//10, 
        fill='white'
    )
    
    # Add chat bubble tail
    tail_points = [
        (bubble_padding + bubble_width//4, bubble_y + bubble_height),
        (bubble_padding + bubble_width//4 - size//12, bubble_y + bubble_height + size//10),
        (bubble_padding + bubble_width//4 + size//12, bubble_y + bubble_height)
    ]
    draw.polygon(tail_points, fill='white')
    
    # Add 3 dots inside bubble (representing AI writing)
    dot_y = bubble_y + bubble_height // 2
    dot_spacing = bubble_width // 5
    dot_radius = size // 20
    start_x = bubble_padding + bubble_width // 3
    
    for i in range(3):
        dot_x = start_x + (i * dot_spacing)
        draw.ellipse(
            [(dot_x - dot_radius, dot_y - dot_radius),
             (dot_x + dot_radius, dot_y + dot_radius)],
            fill='#0A66C2'
        )
    
    # Add sparkle/star effect in top-right corner (genius indicator)
    star_x = size - size//4
    star_y = size//5
    star_size = size // 15
    # Small star sparkle
    draw.polygon([
        (star_x, star_y - star_size),
        (star_x + star_size//3, star_y),
        (star_x, star_y + star_size),
        (star_x - star_size//3, star_y)
    ], fill='#FFD700')
    
    return image

# Generate icons in different sizes
sizes = [16, 48, 128]
for size in sizes:
    icon = create_icon(size)
    icon.save(f'icons/icon{size}.png')
    print(f'Generated icon{size}.png')

print('\n✅ ReplyGenius icons generated successfully!')
 