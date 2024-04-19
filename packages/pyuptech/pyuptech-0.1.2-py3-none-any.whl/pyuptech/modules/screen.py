from enum import Enum
from typing import Literal, Self

from .constant import LIB_FILE_PATH
from .loader import load_lib
from .logger import _logger


class FontSize(Enum):
    """
    All supported font size enum
    """

    FONT_4X6 = 0
    FONT_5X8 = 1
    FONT_5X12 = 2
    FONT_6X8 = 3
    FONT_6X10 = 4
    FONT_7X12 = 5
    FONT_8X8 = 6
    FONT_8X12 = 7
    FONT_8X14 = 8
    FONT_10X16 = 9
    FONT_12X16 = 10
    FONT_12X20 = 11
    FONT_16X26 = 12
    FONT_22X36 = 13
    FONT_24X40 = 14


class Color(Enum):
    """
    All supported color display on the led/lcd
    """

    WHITE = 0xFFFF
    BLACK = 0x0000
    BLUE = 0x001F
    BRED = 0xF81F
    GRED = 0xFFE0
    GBLUE = 0x07FF
    RED = 0xF800
    MAGENTA = 0xF81F
    GREEN = 0x07E0
    CYAN = 0x7FFF
    YELLOW = 0xFFE0
    BROWN = 0xBC40
    BRRED = 0xFC07
    GRAY = 0x8430
    DARKBLUE = 0x01CF
    LIGHTBLUE = 0x7D7C
    GRAYBLUE = 0x5458
    LIGHTGREEN = 0x841F
    LGRAY = 0xC618
    LGRAYBLUE = 0xA651
    LBBLUE = 0x2B12


class Screen:
    """
    Screen module

    This class represents an LCD screen and provides methods to manipulate it.
    Each method returns self to enable chainable calls.
    """

    lib = load_lib(LIB_FILE_PATH)

    def __init__(self, screen_dir: Literal[1, 2] = None):
        """
        Initializes the Screen class.

        Parameters:
            screen_dir (Literal[1, 2], optional): The direction to open the screen in. Defaults to None.

        Returns:
            None
        """

        if screen_dir is not None:
            self.open(direction=screen_dir).fill_screen(Color.BLACK).refresh()

    def open(self, direction: Literal[1, 2] = 2) -> Self:
        """
        Open the LCD and set the displaying direction.

        Args:
          direction (Literal[1, 2]): Display direction; 1 for vertical, 2 for horizontal.

        Returns:
          Self for chainable calls.
        """

        _logger.info(f"Open LCD with direction: {direction}")
        self.lib.lcd_open(direction)
        return self

    def refresh(self) -> Self:
        """
        Refresh the screen, printing the display data from the cache onto the screen.

        Returns:
          Self for chainable calls.
        """
        self.lib.LCD_Refresh()
        return self

    def set_font_size(self, font_size: FontSize) -> Self:
        """
        Set the font size.

        Args:
          font_size (FontSize): The desired font size.

        Returns:
          Self for chainable calls.
        """
        self.lib.LCD_SetFont(font_size.value)
        return self

    def set_fore_color(self, color: Color) -> Self:
        """
        Set the foreground color.

        Args:
          color (Color): The desired foreground color.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_SetForecolor(color)
        return self

    def set_back_color(self, color: Color) -> Self:
        """
        Set the background color of the LCD.

        Args:
          color (Color): The desired background color.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_SetBackcolor(color)
        return self

    def set_led_color(self, index: Literal[0, 1], color: Color) -> Self:
        """
        Set the LED color at a specific index.

        Parameters:
            index (Literal[0, 1]): The index of the LED to set the color for.
            color (Color): The color to set for the LED.

        Returns:
            Self: The instance of the class to allow for method chaining.
        """
        self.lib.adc_led_set(index, color.value)
        return self

    def fill_screen(self, color: Color) -> Self:
        """
        Fill the entire screen with the specified color.

        Args:
          color (Color): The color to fill the screen with.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_FillScreen(color.value)
        return self

    def put_string(self, x: int, y: int, display_string: str) -> Self:
        """
        Place a string at specific coordinates on the LCD.

        Args:
          x (int): X coordinate (in pixels).
          y (int): Y coordinate (in pixels).
          display_string (str): The string to display on the LCD.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_PutString(x, y, display_string)
        return self

    def fill_frame(self, x1: int, y1: int, x2: int, y2: int, color: Color) -> Self:
        """
        Fill a rectangular frame with the specified color.

        Args:
          x1 (int): The X coordinate of the top-left corner.
          y1 (int): The Y coordinate of the top-left corner.
          x2 (int): The X coordinate of the bottom-right corner.
          y2 (int): The Y coordinate of the bottom-right corner.
          color (Color): The color to fill the frame with.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_FillFrame(x1, y1, x2, y2, color.value)
        return self

    def fill_round_frame(
        self, x1: int, y1: int, x2: int, y2: int, r: int, color: Color
    ) -> Self:
        """
        Fill a rounded rectangular frame with the specified color.

        Args:
          x1 (int): The X coordinate of the top-left corner.
          y1 (int): The Y coordinate of the top-left corner.
          x2 (int): The X coordinate of the bottom-right corner.
          y2 (int): The Y coordinate of the bottom-right corner.
          r (int): The radius of the corners.
          color (Color): The color to fill the round frame with.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_FillRoundFrame(x1, y1, x2, y2, r, color.value)
        return self

    def fill_circle(self, x0: int, y0: int, r: int, color: Color) -> Self:
        """
        Fill a circle with the specified color.

        Args:
          x0 (int): The X coordinate of the circle center.
          y0 (int): The Y coordinate of the circle center.
          r (int): The radius of the circle.
          color (Color): The color to fill the circle with.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_FillCircle(x0, y0, r, color.value)
        return self

    def draw_mesh(self, x1: int, y1: int, x2: int, y2: int, color: Color) -> Self:
        """
        Draw a mesh pattern within a rectangle with the specified color.

        Args:
          x1 (int): The X coordinate of the top-left corner.
          y1 (int): The Y coordinate of the top-left corner.
          x2 (int): The X coordinate of the bottom-right corner.
          y2 (int): The Y coordinate of the bottom-right corner.
          color (Color): The color of the mesh lines.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_DrawMesh(x1, y1, x2, y2, color.value)
        return self

    def draw_frame(self, x1: int, y1: int, x2: int, y2: int, color: Color) -> Self:
        """
        Draw an empty rectangular frame with the specified color.

        Args:
          x1 (int): The X coordinate of the top-left corner.
          y1 (int): The Y coordinate of the top-left corner.
          x2 (int): The X coordinate of the bottom-right corner.
          y2 (int): The Y coordinate of the bottom-right corner.
          color (Color): The color of the frame lines.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_DrawFrame(x1, y1, x2, y2, color.value)
        return self

    def draw_round_frame(
        self, x1: int, y1: int, x2: int, y2: int, r: int, color: Color
    ) -> Self:
        """
        Draw an empty rounded rectangular frame with the specified color.

        Args:
          x1 (int): The X coordinate of the top-left corner.
          y1 (int): The Y coordinate of the top-left corner.
          x2 (int): The X coordinate of the bottom-right corner.
          y2 (int): The Y coordinate of the bottom-right corner.
          r (int): The radius of the corners.
          color (Color): The color of the frame lines.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_DrawRoundFrame(x1, y1, x2, y2, r, color.value)
        return self

    def draw_pixel(self, x0: int, y0: int, color: Color) -> Self:
        """
        Draw a single pixel at the specified coordinates with the specified color.

        Args:
          x0 (int): The X coordinate of the pixel.
          y0 (int): The Y coordinate of the pixel.
          color (Color): The color of the pixel.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_DrawPixel(x0, y0, color.value)
        return self

    def draw_circle(self, x0: int, y0: int, r: int, color: Color) -> Self:
        """
        Draw an empty circle with the specified color.

        Args:
          x0 (int): The X coordinate of the circle center.
          y0 (int): The Y coordinate of the circle center.
          r (int): The radius of the circle.
          color (Color): The color of the circle lines.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_DrawCircle(x0, y0, r, color.value)
        return self

    def draw_arc(self, x0: int, y0: int, r: int, s: int, color: Color) -> Self:
        """
        Draw an arc with the specified color.

        Args:
          x0 (int): The X coordinate of the circle center.
          y0 (int): The Y coordinate of the circle center.
          r (int): The radius of the arc circle.
          s (int): The starting angle of the arc.
          color (Color): The color of the arc lines.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_DrawArc(x0, y0, r, s, color.value)
        return self

    def draw_line(self, x1: int, y1: int, x2: int, y2: int, color: Color) -> Self:
        """
        Draw a line between two points with the specified color.

        Args:
          x1 (int): The X coordinate of the first point.
          y1 (int): The Y coordinate of the first point.
          x2 (int): The X coordinate of the second point.
          y2 (int): The Y coordinate of the second point.
          color (Color): The color of the line.

        Returns:
          Self for chainable calls.
        """
        self.lib.UG_DrawLine(x1, y1, x2, y2, color.value)
        return self


if __name__ == "__main__":
    pass
