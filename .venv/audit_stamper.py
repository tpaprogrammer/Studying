from datetime import datetime
import random
import time


def audit_decorator():
    def wrapper(passed_function):
        def internal_wrapper(*args):
            timestamp = datetime.now()
            string_timestamp = timestamp.strftime('%Y%m%d.%H:%M:%S EST')
            print(string_timestamp)
            passed_function(*args)
            print()
        return internal_wrapper
    return wrapper

@audit_decorator()
def do_a_thing():
    print("A thing was did.")


@audit_decorator()
def do_a_different_thing():
    print("A different thing was did.")


counter = 0
lst = [0,1]

for x in range(1,6):
    if counter == 0:
        pass
    else:
        print("Counter is at:", counter)
    selected_function = random.choice(lst)
    if selected_function == 0:
        print("The randomly selected function this run is 'do_a_thing'.")
        do_a_thing()
    elif selected_function == 1:
        print("The randomly selected function this run is 'do_a_different_thing'.")
        do_a_different_thing()
    counter += 1
    if counter == 5:
        print("Counter is at", str(counter) + ", process terminated.")
    else:
        test_time = random.randrange(1, 6)
        print("Now we wait this many random seconds:", test_time)
        print()
        time.sleep(test_time)
