from PIL import Image, ImageDraw, ImageFont

FONTSIZE = 24
back = Image.new()
font = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONTSIZE)


def image(display, image):

    pass


def text(display, text):
    draw = ImageDraw.Draw(image)
    (font_width, font_height) = font.getsize(text)
    draw.text(
        (display.width // 2 - font_width // 2,
         display.height // 2 - font_height // 2),
        text,
        font=font,
        fill=(255, 255, 0),
    )
