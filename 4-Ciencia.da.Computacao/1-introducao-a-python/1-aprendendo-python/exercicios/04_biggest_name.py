def find_biggest_name(names):
    biggest_name = ""
    for name in names:
        if len(name) > len(biggest_name):
            biggest_name = name
    return biggest_name


# testar: >>> find_biggest_name(
# ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"])
