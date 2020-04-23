def show_parameters(basic, keyword_arg, optional_param=3):
    print(f"{basic} {keyword_arg} {optional_param}")


def return_statment():
    return "Done"


show_parameters("Some value", keyword_arg="more text")
show_parameters("Some value", optional_param=5, keyword_arg="more text")


def send_many_args(*multi_args):
    for arg in multi_args:
        print(arg)


send_many_args("This ", "is ", "a ", "message")


def define_many_args(**defined_multi_args):
    print(defined_multi_args)
    print(defined_multi_args["name"])


define_many_args(id=1, name="Mike")

'''
Navigate in the file
begin of line           = Home
end of line             = End
being file              = Home + Alt
end file                = End + Alt
move code               = Highlight line + Alt + arrow up/down
comment/uncomment block = ctrl + /
'''
