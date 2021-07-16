import inspect
from inspect import getmembers, isfunction


def dry_run_function(function_collection_with_values):
    string_storage = str()
    for i in function_collection_with_values:
        try:
            i[0](**i[1])
        except Exception as x:
            string_storage += str(x)
    return string_storage


def create_function_list(module_name):
    return [o for o in getmembers(module_name) if isfunction(o[1])]


# gives argument names as list.
def get_args(function_object):
    fullargspec = inspect.getfullargspec(function_object)
    return fullargspec.args

# create a dictionary that corresponds exactly to the keywords of the functions than do func(**keyword_dict)



