def file_read_from_line(fname, nlines):
    from itertools import islice
    lines = []
    with open(fname, encoding="utf-8") as f:
        for line in islice(f, nlines):
            lines.append(line.strip())  # strip() remove espaços em branco, como \n
    return lines


lines_read = file_read_from_line('../../Arquivos/texto.txt', 1)
for line in lines_read:
    print(line)
