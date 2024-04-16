import unittest

from archerdfu.bmp import *


class TestCaliberIcons(unittest.TestCase):

    def test_create_bmp(self):
        c = CaliberIcon()
        matrix = c.create_icon_matrix("308WIN", 10)
        matrix_to_bmp(matrix, "../assets/icon.bmp", 24)
        self.assertEqual(len(matrix) * len(matrix[0]), 1024)

    def test_load_bmp2matrix(self):
        c = CaliberIcon()
        matrix = bmp_to_matrix("../assets/icon.bmp")
        binicon = c.matrix_to_icon(matrix)
        with open("../assets/icon.bin", 'wb') as fp:
            fp.write(binicon)

        self.assertEqual(len(binicon), 2048)

        with open('../assets/icon.bin', 'rb') as fp0:
            with open('../assets/icon1.bin', 'rb') as fp1:
                self.assertEqual(fp0.read(), fp1.read())

    def test_concat_icons(self):
        c = CaliberIcon()
        icons = (
            c.create_icon("308WIN", 175),
            c.create_icon("338LM", 300),
        )
        binicons = c.concat_icons(icons)
        with open("../assets/icons.bin", 'wb') as fp:
            fp.write(binicons)

        self.assertEqual(len(binicons), 4096)

    def test_create_icon(self):
        matrix = CaliberIcon.create_icon_matrix('338LM', 300)
        matrix_to_bmp(matrix, "../assets/338LM-300gr.bmp")

    def test_other_size_conversion(self):
        matrix = bmp_to_matrix("../assets/640x480.bmp")
        self.assertEqual(len(matrix[0]), 640)
        self.assertEqual(len(matrix), 480)

        matrix_to_bmp(matrix, "../assets/640x480_24.bmp", 24)
        matrix_to_bmp(matrix, "../assets/640x480_32.bmp", 32)

    def test_icon_load(self):
        matrix = bmp_to_matrix("../assets/16.bmp")
        matrix_to_bmp(matrix, "../assets/icons.bmp", 24)
        self.assertEqual(len(matrix[0]), 16)
        self.assertEqual(len(matrix) % 16, 0)
