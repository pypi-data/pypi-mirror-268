import os

from archerdfu.bmp import framebuf
from archerdfu.bmp import matrix_to_bmp


def reticle2bmp(img_data, filename: [str, os.PathLike], size=(640, 480), cross=False, grid=False):
    width, height = size
    buf = bytearray(width * height * 3)
    f_buf = framebuf.FrameBuffer(buf, width=width, height=height, buf_format=framebuf.RGB888)
    f_buf.fill(0xFFFFFF)
    if cross:
        f_buf.line(0, 481, 640, 481, color=0x0000FF)
        f_buf.line(0, 240, 640, 240, color=0x0000FF)
        f_buf.line(320, 0, 320, 480, color=0x0000FF)

    for i, el in enumerate(img_data):

        if grid and el.x == 700 and el.q == 0:
            element = 340, 240 + el.y, 640, 240 + el.y
            f_buf.line(*element, color=0x00CF00)
            # print(el)

        element = el.x, el.y, el.x + el.q - 1, el.y
        f_buf.line(*element, color=0x000000)

    # Convert the framebuffer buffer to a matrix representation
    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(f_buf.pixel(x, y))  # Append the pixel color to the row
        matrix.append(row)  # Append the row to the matrix
    matrix.reverse()
    matrix_to_bmp(matrix, filename=filename)


# def bmp2reticle(img):
#     w, h = img.size
#     imgdata = list(img.getdata())
#     els = []
#     offset = 0
#     for y in range(h):
#         rowdata = imgdata[offset:offset + w]
#         bt = b''
#         for item in rowdata:
#             bt += b'\x00' if item == (255, 255, 255) else b'\xFF'
#         matches = re.finditer(rb'\xFF+', bt)
#         if matches:
#             els += [Container(x=m.start(0), y=y, q=len(m.group())) for m in matches]
#         offset += w
#     return els
