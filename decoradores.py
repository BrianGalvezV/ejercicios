from datetime import datetime

def execution_time(func):
    def envoltura():
        initial_time = datetime.now()
        func()
        final_tim = datetime.now()
        time_elapsed = final_tim - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds())+ " Segundos")
    return envoltura

@execution_time
def random_func():
    for _ in range (1, 100):
        print("hola")


random_func()