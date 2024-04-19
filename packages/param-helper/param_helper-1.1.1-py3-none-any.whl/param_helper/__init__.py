import inspect

def param(**kwargs):
    caller_frame = inspect.currentframe().f_back
    caller_name = caller_frame.f_code.co_name

    args, _, _, values = inspect.getargvalues(caller_frame)

    # Is the analysis a class function or an ordinary function?
    if self := values.get('self'):
        class_ = self.__class__
        func = getattr(class_, caller_name, None)
        caller_signatures = inspect.signature(func)
    else:
        func = caller_frame.f_locals.get(caller_name, None)
        if not func:
            func = caller_frame.f_globals.get(caller_name, None)
        caller_signatures = inspect.signature(caller_frame.f_globals[caller_name])

    caller_signatures = caller_signatures.parameters

    previous_function_args = {}
    for arg in args:
        if arg == 'self':
            continue
        signature = caller_signatures[arg]
        annotation = signature.annotation
        value = values[arg]
        if value == None:
            continue
        if annotation == inspect._empty:
            default = signature.default
            if default != inspect._empty:
                default = type(default)
                if default != type(None):
                    previous_function_args[arg] = default(value)
                else:
                    previous_function_args[arg] = value
            else:
                previous_function_args[arg] = value
        else:
            previous_function_args[arg] = annotation(value)

    previous_function_args.update(kwargs)
    return previous_function_args
