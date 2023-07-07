
def has_method(instance, method_name):
    return callable(getattr(instance, method_name, None))