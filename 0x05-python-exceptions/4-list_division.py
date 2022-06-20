#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """ Divides element by element 2 lists"""
    r_list = []
    i = 0
    while (i < list_length):
        try:
            r_list.append(my_list_1[i] / my_list_2[i])
            i += 1
        except (ValueError, TypeError):
            print("wrong type")
            r_list.append(0)
            i += 1
        except ZeroDivisionError:
            print("division by 0")
            r_list.append(0)
            i += 1
        except IndexError:
            print("out of range")
            r_list.append(0)
            i += 1
        finally:
            pass
    return (r_list)
