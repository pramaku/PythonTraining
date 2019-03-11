"""
os modules methods
os.system()      -> to start app
os.popen()       -> to start app, and returns the output of the app.
os.execvp()      -> to submit a new process, overlaying the current process (the code after this call dont execute)
os.fork()        -> to create a new process. (returns '0' on child, '> 0' on parent)
os.wait()        -> waits for the child process to complete, gives error if there is no child.
os._exit(result) -> exits the current process.
"""

"""
    Exception handling....

    try:
    ....
    ....
    ....
    ....
    except <error_type>:
    .....
    except <error_type>:
    .....
    except Exception:
    ....
    else:
    .... <executes when there is no exception>
    finally:
    .... <executes when there is no exception and exception also>
"""

"""
lambda expressions : to represent (math) expressions as objects.
add = lambda a,b : a + b
s = add(2, 3)
print s

def sum(a, b):
    return a + b

l1 = [1, 2, 3]

l2 = [4, 5, 6]

l3 = map(add, l1, l2)

l4 = map(sum, l1, l2)

r  = reduce(add, l3) -> reduces the iterable to single value.


"""

"""
copying of lists

L1 = L # shallow copy
L1 = L[:] # deep copy at first level

import copy
L1 = copy.deepcopy(L) # total levels deep copy
"""

"""
# serialization and de-serialization.

serialization : process of saving the state of objects persistantly.
de-serialization : loading the object state from disk to application (memory)
"""
