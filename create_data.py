import subprocess
from random import randint, choice

alphabets = 'abcdefghijklmnopqrstuvwxyz'
operations = '+-*/'

def create_power():
    num_vars = randint(1, 10)
    chars_selected = []

    for _ in range(num_vars):
        chars_selected.append(choice(alphabets))

    ret_str = ""
    for i, selected_char in enumerate(chars_selected):
        power = randint(-100, 100)
        ret_str = ret_str + selected_char + "^ {" + "{}".format(power) + "} "
        if i < len(chars_selected) -1 :
            ret_str = ret_str + str(choice(operations)) + " "

    ret_str = ret_str + "= {}^".format(choice(alphabets)) + "{" + "{}".format(randint(-100, 100)) + "}"
    return ret_str


def create_random_equation():
    rand_eqn = create_power()
    write_tex_file(rand_eqn)
    print(rand_eqn)

def write_tex_file(string_to_write):
    file_path = "sometexfile.tex"
    write_string = "\\documentclass{article}\n\\begin{document}\n\(" + string_to_write +"\)\n\\end{document}\n"

    with open(file_path, "w") as f:
        f.write(write_string)

    x = subprocess.call("pdflatex {}".format(file_path), shell=True)


if __name__ == "__main__":
    create_random_equation()


