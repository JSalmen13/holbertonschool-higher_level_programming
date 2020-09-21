#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        f = fct(*args)
        return (f)
    except Exception as error:
        sys.stderr.write("Exception: {}\n".format(error.args[0]))
        return (None)
