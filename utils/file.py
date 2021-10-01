from os.path import basename, split


def get_file_name_ext(filepath):
    base_name = basename(filepath)
    head, tail = split(base_name)
    return head, tail
