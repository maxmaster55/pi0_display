from PIL import Image, ImageDraw, ImageFont


class Screen:
    DEF_FONT_SIZE = 24
    default_font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", DEF_FONT_SIZE)

    def __init__(self, display):
        self.display = display

    def show_text(self, text, font=default_font, loc=(0, 0)):
        back = Image.new("RGB", (self.display.height, self.display.width))
        draw = ImageDraw.Draw(back)
        # inverted dimentions because we are rotating the screen
        draw.text(
            loc,
            text,
            font=font,
            fill=(255, 255, 255),
        )

        self.display.image(back)

    def show_text_centered(self, text, fontsize=22):
        # inverted dimentions because we are rotating the screen
        text = str(text)
        font = self.default_font.font_variant(size=fontsize)
        (font_width, font_height) = font.getsize(text)
        center = (self.display.height // 2 - font_width // 2,
                  self.display.width // 2 - font_height // 2)

        self.show_text(text, font, center)
