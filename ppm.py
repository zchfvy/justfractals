from tqdm import tqdm

def save_img(name, data_array):
    data = _print_img(data_array)
    with open(name, 'w') as f:
        f.write(data)

def _print_img(data_array):
    w = len(data_array[1])
    h = len(data_array)

    rows = []
    for row in tqdm(data_array):
        row_data = [str(int(pix*255)) for pix in row]
        rows.append(' '.join(row_data))
    data = '\n'.join(rows)

    return f"""P2
    {w} {h}
    255
    {data}
    """
