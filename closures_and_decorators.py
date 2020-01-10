# a language is said to have first class functions:
# functions treated as object and can be assigned, passed, returned
# Decorators use Closures in an easy way so that the closured function can be executed
from functools import wraps # see at last for why it is needed
def log_you(log_me):
    print('in log_you')
    @wraps(log_me)
    def inner_func_log(*args, **kwargs):
        print("{} ran with arguments: {}".format(log_me.__name__, args))
        return log_me(*args, **kwargs)
    return inner_func_log

def exec_time(incoming_function):
    import time
    @wraps(incoming_function)
    def inner_func_exec(*args, **kwargs):
        start_time = time.time()
        incoming_function(*args, **kwargs)
        time_taken = time.time()-start_time
        print(time_taken)
        print('time taken for {} is {} with argument {}'.
              format(incoming_function.__name__, time_taken, args))
    return inner_func_exec

import time
@exec_time
def function1():
    time.sleep(1)
    print('function1')


@exec_time
@log_you
def function2(param1):
    time.sleep(1)
    print('function2', param1)

######### below code only for closures ###########
#f1 = exec_time(function2) #no need to pass arguments in function2. Just pass in f1
#f1('Hello')
#f1('Hi')
##################################################

######### below code for decorators calling ##########
#function1()
function2('hellos')
######################################################

# Why do we need @wraps?
#function2 call actually happens as f2 = exec_time(log_you(function2)) where log_you function will return
# inner_func_log which will be passed to exec_time for execution. So, this inner_func_log will be printed
# instead of function2

