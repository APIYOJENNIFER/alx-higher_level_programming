#!/usr/bin/python3
def safe_print_division(a, b):
    res = 0
    try:
        res = (a/b)
    except Exception:
        res = None
        return res
    finally:
        print("Inside result: {}".format(res))
        return res


if __name__ == "__main__":
    safe_print_division
