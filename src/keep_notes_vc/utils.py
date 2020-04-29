# -*- coding: utf-8 -*-

def format_filename(name):
    import string
    valid_chars = "-_.() {}{}".format(string.ascii_letters, string.digits)
    return (
        ''.join(c for c in name if c in valid_chars)
        .replace(' ','_')
    )