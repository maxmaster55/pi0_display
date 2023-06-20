from PIL import Image, ImageDraw, ImageFont

FONTSIZE = 24
font = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONTSIZE)


def show_image(display, image):
    pass



def show_text(display, text, loc=(0,0)):
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


def show_text_centered(display, text):
    # inverted dimentions because we are rotating the screen
    (font_width, font_height) = font.getsize(text)

    center = (display.height // 2 - font_width // 2,
              display.width // 2 - font_height // 2)

    show_text(display, text, center)

