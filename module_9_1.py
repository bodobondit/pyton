def apply_all_func(int_list, *functions):
        my_dict = {}
        for function in functions:
            my_dict[function.__name__] = function(int_list)
        return my_dict

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))


