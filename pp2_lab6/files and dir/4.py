def line_text(name):
    num_lines = 0
    with open(name, 'r') as f:
        for line in f:
            num_lines += 1
    return num_lines
print("Number:", line_text('text.txt'))