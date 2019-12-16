def print_res(res):
    print(",".join([str(x) for x in res]))

def read_input_as_list(file_name):
    return [line.rstrip() for line in open(file_name, "r")]