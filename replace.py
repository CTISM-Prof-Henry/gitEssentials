import os


def main():
    filepath = os.path.join('_build', 'latex', 'main.tex')

    with open(filepath, mode='r', encoding='utf-8') as some_file:
        text = ''.join(some_file.readlines())

    text = text.replace(
        '\\sphinxmaketitle',
        '\\sphinxmaketitle\n'
        '% adiciona folha em branco para folha de rosto\n'
        '\\blankpage\n'
        '\\blankpage\n'
        '\\blankpage\n'
        '\\blankpage\n'
        '% adiciona folha em branco para folha de rosto\n'
    )

    os.remove(filepath)

    with open(filepath, mode='w', encoding='utf-8') as some_file:
        some_file.write(text)


if __name__ == '__main__':
    main()
