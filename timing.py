import time

def calculate_time(func):
    """
    Calculate time to run a function

    A decorator that gets the current time, calls a function, then subtracts the current time with the previous current time to print total time to run function

    Parameters
    ----------
    func : function
        Any function that the decorator can use.

    Returns
    -------
    float
        Time taken for function to run.

    See Also
    --------
    time.time()
        Get current time.

    Examples
    --------
    >>> aFunction()
    Total time  4.005674839019775
    """
    def wrapper():
        current_time = time.time()
        func()
        print("Total time ", time.time() - current_time)

    return wrapper

@calculate_time
def aFunction():
    """
    Call time function to sleep.

    A test function for the decorator to show that the calculate_time function works.

    See Also
    --------
    time.sleep()
        Pause program for a certain number of seconds.
    """
    time.sleep(4)
    return;
