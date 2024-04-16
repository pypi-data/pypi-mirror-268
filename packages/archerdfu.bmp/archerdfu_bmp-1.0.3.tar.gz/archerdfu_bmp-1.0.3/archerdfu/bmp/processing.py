import os

from construct import Padding, Const, Int32ul, Int16ul, GreedyRange, Bytes, Struct, this, If, Array, IfThenElse, Int8ul

BIT24 = 24
BIT32 = 32

DIB_HEADER = Struct(
    "header_size" / Int32ul,
    "image_width" / Int32ul,
    "image_height" / Int32ul,
    "color_planes" / Int16ul,
    "bits_per_pixel" / Int16ul,
    "compression" / Int32ul,
    "image_size" / Int32ul,
    "horizontal_resolution" / Int32ul,
    "vertical_resolution" / Int32ul,
    "colors_in_palette" / Int32ul,
    "important_colors" / Int32ul
)

BMP_HEADER = Struct(
    "header" / Struct(
        "signature" / Const(b"BM"),
        "file_size" / Int32ul,
        "reserved1" / Padding(2),
        "reserved2" / Padding(2),
        "pixel_data_offset" / Int32ul,
    ),
    "dib_header" / DIB_HEADER
)

# BMP = Struct(
#     *BMP_HEADER.subcons,
#     'pixel_data' / GreedyRange(Bytes(this.dib_header.bits_per_pixel // 8))
#     # 'pixel_data' / Array(
#     #     lambda ctx: ctx.dib_header.image_size // (ctx.dib_header.bits_per_pixel // 8),
#     #     Bit[this.dib_header.bits_per_pixel // 8])
# )


# Define a color palette entry structure
ColorPaletteEntry = Struct(
    "blue" / Int8ul,
    "green" / Int8ul,
    "red" / Int8ul,
    "reserved" / Int8ul
)

BMP = Struct(
    *BMP_HEADER.subcons,
    "color_palette" / If(this.dib_header.bits_per_pixel == 8,
                         Array(lambda ctx: ctx.header.dib_header.colors_in_palette, ColorPaletteEntry)),
    "pixel_data" / IfThenElse(this.dib_header.bits_per_pixel == 8,
                              GreedyRange(Int8ul),
                              GreedyRange(Bytes(this.dib_header.bits_per_pixel // 8)))
)

# # Sample color palette and pixel data
# color_palette = [
#     {"blue": 0, "green": 0, "red": 0, "reserved": 0},  # Black
#     {"blue": 255, "green": 255, "red": 255, "reserved": 0},  # White
#     {"blue": 0, "green": 0, "red": 255, "reserved": 0},  # Red
#     # Add more colors as needed
# ]
#
# # Sample pixel data (indices into the color palette)
# pixel_data = [0, 1, 2, 1, 0]  # Black, White, Red, White, Black
# # Build the BMP data structure
# bmp_data = BMP.build({
#     "header": {
#         "signature": b"BM",
#         "file_size": 0,  # Set to actual size
#         "pixel_data_offset": 0x36,  # Assuming no additional metadata before pixel data
#         "dib_header": {
#             "header_size": 40,
#             "image_width": 2,  # Width of the image in pixels
#             "image_height": 1,  # Height of the image in pixels
#             "color_planes": 1,
#             "bits_per_pixel": 8,  # 8-bit image
#             "compression": 0,
#             "image_size": 0,  # Can be set to 0 for uncompressed images
#             "horizontal_resolution": 0,
#             "vertical_resolution": 0,
#             "colors_in_palette": len(color_palette),
#             "important_colors": 0
#         }
#     },
#     "color_palette": color_palette,
#     "pixel_data": pixel_data
# })


def _create_bmp_headers(matrix, bits=24) -> (dict, dict):
    height = len(matrix)
    width = len(matrix[0])

    # Calculate file size
    pixel_data_size = height * width * (bits // 8)
    file_size = 54 + pixel_data_size

    # Create header data
    header_data = {
        "signature": b"BM",
        "file_size": file_size,
        "pixel_data_offset": 54,
    }

    # Create DIB header data
    dib_header_data = {
        "header_size": 40,
        "image_width": width,
        "image_height": height,
        "color_planes": 1,
        "bits_per_pixel": bits,
        "compression": 0,
        "image_size": pixel_data_size,
        "horizontal_resolution": 0,
        "vertical_resolution": 0,
        "colors_in_palette": 0,
        "important_colors": 0,
    }

    return header_data, dib_header_data


def matrix_to_bmp(matrix: list[list[int]], filename: [str, os.PathLike], bits: int = 24) -> None:
    header_data, dib_header_data = _create_bmp_headers(matrix, bits)

    def extract_rgb(pixel: int):
        red = pixel >> 16 & 0xFF
        green = pixel >> 8 & 0xFF
        blue = pixel & 0xFF
        return bytes((blue, green, red))

    def extract_rgba(pixel: int):
        alpha = pixel >> 24 & 0xFF
        red = pixel >> 16 & 0xFF
        green = pixel >> 8 & 0xFF
        blue = pixel & 0xFF
        return bytes((blue, green, red, alpha))

    if bits == 24:
        extract = extract_rgb
    elif bits == 32:
        extract = extract_rgba
    else:
        raise ValueError("Bits have to be 24 or 32")

    # Convert the matrix of pixels to bytes
    pixel_data = []
    for row in matrix:
        for pixel in row:
            # Append the pixel components as bytes (BGR order)
            pixel_data.append(extract(pixel))

    # Create the BMP data
    bmp_data = {
        "header": header_data,
        "dib_header": dib_header_data,
        "color_palette": None,
        "pixel_data": pixel_data,
    }

    # Save the BMP data to a file
    with open(filename, "wb") as f:
        f.write(BMP.build(bmp_data))


def bmp_to_matrix(filename: [str, os.PathLike]) -> list[list[int]]:
    with open(filename, "rb") as f:
        bmp_data = f.read()
    data = BMP.parse(bmp_data)
    bits_per_pixel = data.dib_header.bits_per_pixel

    matrix = []
    row = []
    img_width = data.dib_header.image_width

    def extract_rgb(pixel_bytes: bytes):
        # Extract RGB components
        blue, green, red = pixel_bytes
        return (red << 16) | (green << 8) | blue

    def extract_rgba(pixel_bytes: bytes):
        # Extract RGBA components
        blue, green, red, alpha = pixel_bytes
        return (alpha << 24) | (red << 16) | (green << 8) | blue

    if bits_per_pixel == 24:
        extract = extract_rgb
    elif bits_per_pixel == 32:
        extract = extract_rgba
    else:
        raise ValueError("Unsupported bitmap format")

    for pixel_bytes in data.pixel_data:
        row.append(extract(pixel_bytes))

        if len(row) == img_width:
            matrix.append(row)
            row = []
    return matrix
