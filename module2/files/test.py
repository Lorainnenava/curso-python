# Lee el archivo y lo devuelve
def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            data = file.read()

            print(data)

        return data
    except:
        raise NotImplementedError()


# Lee las multiples lineas del archivo y lo devuelve en una lista
def read_file_into_list(file_name):
    try:
        with open(file_name) as file:
            data = file.readlines()

        return data
    except:
        raise NotImplementedError()


#  Obtiene la primera linea del file_contents y lo almacena en un nuevo archivo
def write_first_line_to_file(file_contents, output_filename):
    try:
        first_line = file_contents.split('\n')[0]

        print(first_line, "first_line")

        with open(output_filename, "w") as file:
            file.write(first_line)

    except:
        raise NotImplementedError()

# Lee el archivo y devuelve las lineas que sean pares


def read_even_numbered_lines(file_name):
    try:
        even_lines = []

        with open(file_name, "r") as file:
            for index, line in enumerate(file, start=1):
                if index % 2 == 0:
                    even_lines.append(line)

        return even_lines
    except:
        raise NotImplementedError()

# Lee la lista y la devuelve en reversa


def read_file_in_reverse(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()

        reversed_lines = lines[::-1]

        print(reversed_lines)

        return reversed_lines
    except:
        raise NotImplementedError()


'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''


def main():
    file_contents = read_file("sample.txt")
    print(read_file_into_list("sample.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sample.txt"))
    print(read_file_in_reverse("sample.txt"))


if __name__ == "__main__":
    main()
