#######################################
# IMPORTS
#######################################

import time
import sys
import inspect

from PyNucleus.functions import PrintSuccess

#######################################
# DECORATORS
#######################################

def Timer(func):
    """
    ## Decorator to check how long it takes to run a function.

    ### >> Example of usage:
    ```
    from PyNucleus.decorators import Timer
    import time

    @Timer
    def example_func(x, y):
        time.sleep(1)
        return x ** y

    print(exaple_func(2, 3))
    ```
    """
    def wrapper(*args, **kwargs):
        t1 = time.time()
        out = func(*args, **kwargs)
        t2 = time.time() - t1
        PrintSuccess(f"Function '{func.__name__}' ran in {t2} seconds.")
        return out
    
    return wrapper

def Info(func):
    """
    ## Decorator to display information about the given function.

    ### >> Example of usage:
    ```
    from PyNucleus.decorators import Info

    @Info
    def example_func(x, y):
        return x * y

    print(exaple_func(2, 3))
    ```
    """
    def wrapper(*args, **kwargs):
        params = []
        for param_name, param in inspect.signature(func).parameters.items():
            params.append({param_name, param})
        print(
f"""Function info:
* name:      {func.__name__}
* signature: {inspect.signature(func)}
* size:      {sys.getsizeof(func)} bytes
* parameters: {params or "None"}""")
    
        return func(*args, **kwargs)
    
    return wrapper