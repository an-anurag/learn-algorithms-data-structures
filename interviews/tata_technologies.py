

"""
[[1,2,3],[4,5,6]]
"""

# flatten list with comprehension

source = [[1,2,3],[4,5,6]]

flatten = [i for item in source for i in item]
print(flatten)

result_list = []

for item in source:

    for i in item:
        result_list.append(i)

# flattern dict with recursion

d = {'k':1, 'j':2, 'y': {'p': 3, 'r': {'t':10}}}

# output 

flattern_dict = {}


def flatten_function(mydict):
    for key, val in mydict.items():
        if isinstance(val, dict):
            flatten_function(val)
        else:
            flattern_dict[key] = val

flatten_function(d)

print(flattern_dict)

## decorators which takes the parameter

# app.route('/app/customers')


def my_decorator(args):

    def _outer_wrapper(func):

        def _wrapper(args1):

            result = func()
            modified = f"{args} {result}"

            return modified
        
        return _wrapper
    
    return _outer_wrapper


@my_decorator('hi')
def greet():
    return "Anurag"

print(greet())


# implement inheritance

class Controller:

    def __init__(self) -> None:
        pass

    def mymethod(self):
        print("from the controller method")



controller = Controller()
controller.mymethod()


class Entity(Controller):

    def another_method(self):
        super().mymethod()


ent = Entity()
ent.mymethod()



