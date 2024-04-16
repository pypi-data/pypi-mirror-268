import re
from pathlib import Path
import pyfiglet

FONT_PATH = Path(__file__).resolve().parent / 'fonts' / 'default.flf'


class CaliberIcon:

    class CustomFigletFont(pyfiglet.FigletFont):
        @classmethod
        def preloadFont(cls, font):
            with open(font, 'rb') as f:
                return f.read().decode('UTF-8', 'replace')

    class CustomFiglet(pyfiglet.Figlet):

        def setFont(self, **kwargs):
            if 'font' in kwargs:
                self.font = kwargs['font']
            self.Font = CaliberIcon.CustomFigletFont(font=self.font)

    WHITE = 0xFFFFFF
    BLACK = 0x000000
    ROW_SIZE = 32
    COL_SIZE = 32
    WHITE_ROW = [WHITE] * ROW_SIZE
    BLACK_ROW = [BLACK] * ROW_SIZE

    @classmethod
    def make_line(cls, txt: str, row_length=ROW_SIZE):
        rows = txt.split('\n')
        pixels = []
        rows.insert(0, rows.pop(-1))

        for row in rows:
            row = re.sub(r"\S", "$", row)
            # row = re.sub(r"\s", " ", row)

            if len(row) < row_length:
                pad = ' ' * int((row_length - len(row)) / 2)
                if len(pad) >= 1:
                    row = pad + row + pad

            if len(row) < row_length:
                row = ' ' * (row_length - len(row)) + row

            row = row[:row_length]

            pixels.append([cls.BLACK if p == '$' else cls.WHITE for p in row])
        return pixels

    @classmethod
    def create_icon_matrix(cls, caliber: str, weight: [int, float], custom_font_path=FONT_PATH):
        caliber = cls.trunc_caliber(caliber)
        custom_figlet = cls.CustomFiglet(font=custom_font_path)

        rnd_weight = round(weight, 1)
        if rnd_weight % 1 == 0:
            rnd_weight = int(rnd_weight)

        weight = str(rnd_weight) + 'grn'

        caliber_txt = custom_figlet.renderText(caliber)
        weight_txt = custom_figlet.renderText(weight)

        cal_height = len(caliber_txt.split('\n'))
        cal_height_pad = (15 - cal_height) // 2

        w_height = len(weight_txt.split('\n'))
        w_height_pad = (15 - w_height) // 2

        cal_pad_pxl = [cls.WHITE_ROW] * cal_height_pad
        w_pad_pxl = [cls.WHITE_ROW] * w_height_pad

        caliber_pxl = cal_pad_pxl + cls.make_line(caliber_txt) + cal_pad_pxl

        weight_pxl = w_pad_pxl + cls.make_line(weight_txt) + w_pad_pxl
        delimiter_pxl = [cls.BLACK_ROW] * 2

        matrix = caliber_pxl + delimiter_pxl + weight_pxl
        matrix.reverse()
        return matrix

    @classmethod
    def matrix_to_icon(cls, matrix: list):
        _matrix = matrix.copy()
        _matrix.reverse()
        output = b''
        for row in _matrix:
            line = b''.join([b'\x00' if p == cls.WHITE else b'\xC0' for p in row])
            output += line * 2
        return output

    @staticmethod
    def concat_icons(icons: [bytes, bytearray]):
        return b''.join(icons)

    @staticmethod
    def trunc_caliber(caliber: str):
        caliber = re.sub(r'\s', '', caliber)
        caliber = ''.join([ch if ch.isupper() or ch.isdigit() or ch in '.,/| ' else "" for ch in caliber])
        return caliber

    @classmethod
    def create_icon(cls, caliber: str, weight: [int, float], font_path=FONT_PATH):
        matrix = cls.create_icon_matrix(caliber, weight, font_path)
        return cls.matrix_to_icon(matrix)
