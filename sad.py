import time
from smiley import Smiley
from blinkable import Blinkable


class Sad(Smiley, Blinkable):
    def __init__(self):
        super().__init__(complexion=self.BLUE)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Method that draws the mouth on the standard faceless smiley.
        """
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Method that draws the eyes (open or closed) on the standard smiley.
        :param wide_open: True if eyes opened, False otherwise
        """
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.complexion()

    def blink(self, delay=0.01):
        """
        Task 5b: Create blink() method in the Sad class with the same prototype.
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
