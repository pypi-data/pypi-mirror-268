import unittest

from archerdfu.bmp import ArcherFonts


class TestGuiFont(unittest.TestCase):

    def test_bin2bmp(self):
        ArcherFonts.bin2bmp('../assets/fonts.bin', '../assets/fonts_bin2bmp.bmp', ArcherFonts.ASCII_SIZE)

    def test_bmp2bin(self):
        ArcherFonts.bmp2bin('../assets/fonts_bin2bmp.bmp', '../assets/fonts_bmp2bin.bin')

        with open('../assets/fonts_bmp2bin.bin', 'rb') as fp0:
            data0 = fp0.read()

        with open('../assets/fonts.bin', 'rb') as fp1:
            data1 = fp1.read()

        self.assertEqual(data0, data1)
