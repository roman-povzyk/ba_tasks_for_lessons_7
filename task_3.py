def make_operation(math, *args):

    list_args = []
    answer = {}
    for i in args:
        list_args.append(str(i))
        args_str = math.join(list_args)
        exec("result="+args_str, answer)
    return print(answer["result"])


make_operation("*", 2, 4, 3)