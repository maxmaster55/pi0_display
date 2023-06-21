from PIL import Image, ImageDraw, ImageFont


DEF_FONT_SIZE = 22


class Screen:
    default_font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", DEF_FONT_SIZE)

    def __init__(self, display):
        self.display = display

    def show_text(self, text, font_size=DEF_FONT_SIZE, loc=(0, 0)):
        back = Image.new("RGB", (self.display.height, self.display.width))
        draw = ImageDraw.Draw(back)
        font = self.default_font.font_variant(size=font_size)

        draw.text(
            loc,
            text,
            font=font,
            fill=(255, 255, 255),
        )

        self.display.image(back)

    def show_text_centered(self, text, font_size=DEF_FONT_SIZE):
        # inverted dimentions because we are rotating the screen
        font = self.default_font.font_variant(size=font_size)
        (font_width, font_height) = font.getsize(text)
        center = (self.display.height // 2 - font_width // 2,
                  self.display.width // 2 - font_height // 2)

        self.show_text(text, font_size, center)


class Picker:
    def __init__(self, options, indicator=">"):
        self.options = options
        self.indicator = indicator
        self.length = len(options)
        self.current = 0  # index of the current option

    def next(self):
        if self.current < self.length - 1:
            self.current += 1
        else:
            self.current = 0

    def prev(self):
        if self.current > 0:
            self.current -= 1
        else:
            self.current = self.length - 1

    def get_current(self):
        return self.options[self.current]

    def show_all(self, screen, font_size=DEF_FONT_SIZE):
        ret_str = ""
        for i, option in enumerate(self.options):
            if i == self.current:
                ret_str += f"{self.indicator}:{option}\n"
            else:
                ret_str += f"  :{option}\n"

        screen.show_text(ret_str, font_size=18)
