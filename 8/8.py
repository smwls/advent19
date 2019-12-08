def parse_image(data, width, height):
    num_layers = len(data)//(width*height)
    layers = []
    for layer in range(num_layers):
        rows = []
        for row in range(height):
            row_list = []
            for col in range(width):
                row_list.append(int(data[width*height*layer + row*width + col]))
            rows.append(row_list)
        layers.append(rows)
    return layers

def count_num(layer, number):
    count = 0
    for row in layer:
        for col in row:
            if col == number:
                count += 1
    return count

def layer_with_least_zeros(layers):
    least = float('inf')
    least_layer = None
    for i in range(len(layers)):
        num_zeros = count_num(layers[i], 0)
        if num_zeros <= least:
            least_layer = layers[i]
            least = num_zeros
    return least_layer

def render_pixel(pixel_layers):
    for layer in pixel_layers:
        if layer in [0, 1]:
            return " " if layer == 0 else "#"
    return " "

def render_image(layers, cols, rows):
    image_string = ""
    for row in range(rows):
        for col in range(cols):
            image_string += str(render_pixel([layer[row][col] for layer in layers]))
        image_string += '\n'
    return image_string

with open('8', 'r') as f:
    input_data = f.read()
    img = parse_image(input_data, 25, 6)
    print(render_image(img, 25, 6))
    least_layer = layer_with_least_zeros(img)
    least_ones = count_num(least_layer, 1)
    least_twos = count_num(least_layer, 2)
    print(least_ones * least_twos)
    