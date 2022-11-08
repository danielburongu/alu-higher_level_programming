#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    output_list = list()
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            result = 0
            print("divided zero")
        except TypeError:
            result = 0
            print("invalid type")
        except IndexError:
            result = 0
            print("index does not exist")
        finally:
            output_list.append(result)
            continue
    return output_list
