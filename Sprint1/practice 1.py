from PIL import Image

def compress():
    image = Image.open(f"r34.jpg")
    compressed_file = []
    data = image.load()
    height = image.height
    width = image.width
    compressed_file.append(width)
    compressed_file.append(height)
    for y in range(0, height):
        for x in range(0, width):
            pixel = data[x,y]
            red, green, blue = pixel
            packed_int = 0

            packed_int += red << 16
            packed_int += green << 8
            packed_int += blue << 0

            compressed_file.append(packed_int)

    return compressed_file

def generate_compressed_image(compressed_file):
    width = compressed_file.pop(0)

    height = compressed_file.pop(0)


    blank_image = Image.new("RGB", (width, height))
    blank_image_data = blank_image.load()
    compressed_iter = iter(compressed_file)
    for y in range(0, height):
        for x in range(0, width):
            # packed_int = compressed_file.pop(0)
            packed_int = next(compressed_iter)
            new_blue = packed_int & 255  # binary 11111111
            packed_int >>= 8
            new_green = packed_int & 255
            packed_int >>= 8
            new_red = packed_int & 255
            blank_image_data[x,y] = (new_red, new_green, new_blue)
        # print(y)

    return blank_image

def binary():
    image = Image.open(f"r34.jpg")
    data = image.load()
    pixel = data[0,0]
    red, green, blue = pixel # 88, 83, 25
    print(red, green, blue)
    print(bin(red))
    new_red = red << 16
    print(bin(new_red))
    print(bin(green))
    new_green = green << 8
    print(bin(new_green))
    print(bin(blue))
    new_blue = blue << 0
    print(bin(new_blue))
    print(bin(new_red)[2:] + '\n' + " "*8 + bin(new_green)[2:])
    print(bin(new_red + new_green)[2:])
    print(" " * 18 + bin(new_blue)[2:])
    print(bin(new_red + new_green + new_blue)[2:])
    print(bin(new_red + new_green + new_blue)[2:], '=', (new_red + new_green + new_blue), 'Number in English')

def flip_vert():
    image = Image.open(f"r34.jpg")
    data = image.load()
    width = image.width
    height = image.height
    blank_image = Image.new("RGB", (width, height))
    blank_image_data = blank_image.load()

    for y in range(height):
        for x in range(width):
            pixel = data[x,y]
            blank_image_data[x, (height - y) - 1] = pixel

    return blank_image

def flip_horiz():
    image = Image.open(f"r34.jpg")
    data = image.load()
    width = image.width
    height = image.height
    blank_image = Image.new("RGB", (width, height))
    blank_image_data = blank_image.load()

    for y in range(height):
        for x in range(width):
            pixel = data[x,y]
            blank_image_data[(width - x - 1), y] = pixel

    return blank_image


def changing_color():
    image = Image.open("r34.jpg")
    data = image.load()
    blank_image = Image.new("RGB", (image.width, image.height))
    blank_image_data = blank_image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x,y]
            red, green, blue = pixel
            blue += 100
            if blue > 255:
                blue = 255
            blank_image_data[x,y] = (red, green, blue)


    return blank_image


def greyscale():
    image = Image.open("r34.jpg")
    data = image.load()
    blank_image = Image.new("RGB", (image.width, image.height))
    blank_image_data = blank_image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = data[x,y]
            red, green, blue = pixel
            red_factor = .21
            green_factor = .71
            blue_factor = .08
            k = int(red * red_factor + green * green_factor + blue * blue_factor)
            blank_image_data[x,y] = (k,k,k)

    return blank_image


def rotate90(compressed_file):
    image = Image.open("r34.jpg")
    data = image.load()
    print(image.width, image.height)
    blank_image = Image.new("RGB", (image.height, image.width))
    blank_image_data = blank_image.load()
    dataset = [[]]
    compressed_iter = iter(compressed_file)
    for y in image.height:
        for x in image.width:
            value = next(compressed_iter)
            dataset[y][x] = value





def main():
    image = Image.open("r34.jpg")
    data = image.load()

    print(image.width, image.height)


    compressed_file = compress()
    #print(compressed_file)
    image_from_compressed = generate_compressed_image(compressed_file)
    image_from_compressed.save("image_from_compressed.jpg")
    # print(800*533)
    binary()

    vertical_flip_pic = flip_vert()
    vertical_flip_pic.save("verticalflip.png")

    horizontal_flip_pic = flip_horiz()
    horizontal_flip_pic.save("horizontalflip.png")

    color_changed_image = changing_color()
    color_changed_image.save("colorchangedimage.png")

    grey_image = greyscale()
    grey_image.save("greyimage.png")

    rotate90()

main()