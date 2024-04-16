#!/usr/bin/env python3

import sys
import fileinput
from warnings import warn


def main(argv):
    state = 0
    for line in fileinput.input():
        line = line.strip()
        if not line or line.startswith("#"):
            if state == 1:
                state = 2
                print("}\n")
            print(line)
            continue
        if state == 0:
            print("\nglyphname2unicode = {")
            state = 1
        (name, x) = line.split(";")
        codes = x.split(" ")
        print(" {!r}: u'{}',".format(name, "".join("\\u%s" % code for code in codes)))


if __name__ == "__main__":
    warn(
        "The file conf_glpyhlist.py will be removed in 2023. Its functionality"
        "is moved to pdfminer/glyphlist.py. Feel free to create a GitHub issue "
        "if you disagree.",
        DeprecationWarning,
    )
    sys.exit(main(sys.argv))  # type: ignore[no-untyped-call]
