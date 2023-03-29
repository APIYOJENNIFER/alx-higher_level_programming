#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            try:
                res = (my_list_1[i]/my_list_2[i])
                new_list.append(res)
            except ZeroDivisionError:
                new_list.append(0)
                print("division by 0")
            except TypeError:
                new_list.append(0)
                print("wrong type")
            except IndexError:
                new_list.append(0)
                print("out of range")
    except Exception as ex:
        raise ex
    finally:
        return new_list


if __name__ == "__main__":
    list_division()
