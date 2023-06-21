from PIL import Image, ImageDraw, ImageFont

DEF_FONT_SIZE = 24
default_font = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", DEF_FONT_SIZE)

def show_image(display, image):
    pass

def show_text(display, text, font, loc=(0,0)):

    back = Image.new("RGB", (display.height, display.width))
    draw = ImageDraw.Draw(back)
    (font_width, font_height) = font.getsize(text)
    
    # inverted dimentions because we are rotating the screen
    draw.text(
        loc,
        text,
        font=font,
        fill=(255, 255, 255),
    )
    
    display.image(back)

def show_text_centered(display, text, fontsize = 22):
    # inverted dimentions because we are rotating the screen
    text = str(text)
    font = default_font.font_variant(size=fontsize)
    (font_width, font_height) = font.getsize(text)
    center = (display.height // 2 - font_width // 2,
              display.width // 2 - font_height // 2)

    show_text(display, text, font, center)

