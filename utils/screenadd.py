from PIL import Image, ImageDraw, ImageFont


SCREEN_W = 135
SCREEN_H = 240

FONTSIZE = 24
font = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONTSIZE)


def fix_screen_rotation(display):
    h = display.hight
    display.hight = display.width
    display.width = h
    return display


def image(display, image):
    pass


def text(display, text):
    back = Image.new("RGB", (SCREEN_W, SCREEN_H))
    draw = ImageDraw.Draw(back)
    (font_width, font_height) = font.getsize(text)
    draw.text(
        (display.width // 2 - font_width // 2,
         display.height // 2 - font_height // 2),
        text,
        font=font,
        fill=(255, 255, 0),
    )
    display.image(back)
