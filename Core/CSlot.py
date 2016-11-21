def CSlot(*args, **kwargs):
    """ a decorator for functions connected to a signal """
    __type_args = args

    def slot_wrapper(func):
        def wrapper(*args, **kwargs):
            if len(__type_args) != len(args[2:]):
                raise TypeError("QcSlot has not same number of arguments")
            func(*args[1:])

        return wrapper
    return slot_wrapper
