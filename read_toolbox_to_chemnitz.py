"""A very rough Toolbox→Chemnitz dictionary translator."""

import argparse

parser = argparse.ArgumentParser(description="""Translate a
 toolbox dictionary into a Chemnitz-style dictionary""")
parser.add_argument("outfile", default= open('Abui.txt', mode='w', encoding='utf-8'), nargs="?", type=argparse.FileType("w"))
parser.add_argument("filename", default=open('Abui Dictionary.db', encoding='utf-8'), nargs="?", type=argparse.FileType("r"))
args = parser.parse_args()


def tofile(file, abui, indonesian, last_example_abui, last_example_indonesian):
    """Write lexemes and examples out in Chemnitz-style lines.

    For every pair of translations in the two languages, generate a
    dictionary entry line. Include all examples that match that
    particular translation pair.

    """
    for abui_word.strip("-") in abui.split(", "):
        for indonesian_word.strip("-") in indonesian.split(", "):
            if (abui_word in last_example_abui and
                indonesian_word in last_example_indonesian):
                file.write(abui_word)
                file.write(' | ')
                file.write(last_example_abui)
                file.write(" :: ")
                file.write(indonesian_word)
                file.write(' | ')
                file.write(last_example_indonesian)
                file.write(" \n ")
            else:
                file.write(abui_word)
                file.write(" :: ")
                file.write(indonesian_word)
                file.write("\n")


def line_to_entry(line):
    r"""Clean a .db entry line.

    Strip the line from its header (first four characters, '\aa '),
    any surrounding whitespace, and convert all to lowercase

    """
    return line[4:].strip().lower()


for line in args.filename:
    if line.startswith(r"\lx"):
        # If there was a previous lexeme, it has obviously
        # ended, now that a new one is starting. Output it.
        try:
            tofile(args.outfile, lexeme, definition_indonesian, last_example_abui, last_example_indonesian)
        except NameError:
            pass

    if line.startswith(r"\lx"):
        lexeme = line_to_entry(line)
    elif line.startswith(r"\dn"):
        definition_indonesian = line_to_entry(line)
    elif line.startswith(r"\xn"):
        last_example_indonesian = line_to_entry(line)
    elif line.startswith(r"\xv"):
        last_example_abui = line_to_entry(line)

tofile(args.outfile, lexeme, definition_indonesian, last_example_abui, last_example_indonesian)

