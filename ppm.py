
def save_img(name, data_array):
    data = _print_img(data_array)
    with open(name, 'w') as f:
        f.write(data)

def _print_img(data_array):
    w = len(data_array[1])
    h = len(data_array)
    rv = ""
    rv += "P2\n"
    rv += str(w) + " " + str(h) + "\n"
    rv += "255\n"
    for row in data_array:
        for pix in row:
            rv += str(int(pix*255)) + " "
        rv += "\n"

    return rv


