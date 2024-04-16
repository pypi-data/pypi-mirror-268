import os

from archerdfu.bmp.processing import matrix_to_bmp, bmp_to_matrix


__all__ = ('ArcherFonts', )


def split_list(input_list, chunk_size):
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]


class ArcherFonts:
    PICTOGRAM_SIZE = 32
    ASCII_SIZE = 16

    @staticmethod
    def bin2bmp(input_: [str, os.PathLike], output_: [str, os.PathLike], font_size: int = ASCII_SIZE) -> None:
        mapping = {
            0x00: 0xFFFFFF,
            0xC0: 0x000000,
            0x01: 0xFF0000,
            0xC1: 0x0000FF,
        }

        with open(input_, 'rb') as fp:
            in_buf = fp.read()

        matrix = []
        icons_buf = split_list(in_buf, font_size ** 2 * 2)

        for icon_buf in icons_buf:
            icon_rows_buf = split_list(icon_buf, font_size)[::2]  # removes each unpair row
            _matrix = [
                [mapping[i] for i in row_buf]
                for row_buf in icon_rows_buf
            ]
            matrix.extend(_matrix)

        # matrix.reverse()  # TODO: fix it in processor
        matrix_to_bmp(matrix, output_, 24)

    @staticmethod
    def bmp2bin(input_: [str, os.PathLike], output_: [str, os.PathLike]) -> None:
        mapping = {
            0xFFFFFF: 0x00,
            0x000000: 0xC0,
            0xFF0000: 0x01,
            0x0000FF: 0xC1,
        }

        matrix = bmp_to_matrix(input_)
        # matrix.reverse()  # TODO: fix it in processor
        buffer = b''
        for row in matrix:
            row_buf = bytearray([mapping[i] for i in row])
            buffer += row_buf
            if row_buf[0] in (0x01, 0xC1):
                row_buf[0] -= 0x01
            buffer += row_buf
        with open(output_, 'wb') as fp:
            fp.write(buffer)
