from multiprocessing import Pool, cpu_count
import time

def is_prime(number):
    if number == 2 or number == 3:
        return number
    if number % 2 == 0 or number < 2:
        return
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return
    return number

def main(threads):
    numbers = range(100000000)
    pool = Pool(processes=threads)
    start = time.time()
    pool.map(is_prime, numbers)
    return time.time() - start


if __name__ == '__main__':
    num_threads = input("Threads to stress\n-->".format(cpu_count()))
    if 0:
        print("Single core test START")
        single_core = main(1)
        print("Single core:", int(round(1000 / single_core, 3) * 1000), "pts")
        print("Waiting for slight cool down")
        time.sleep(10)
    print("Running with {} threads\nPrimeBench test START".format(num_threads))
    multi_core = main(int(num_threads))
    print("Multi core:", int(round(1000 / multi_core, 3) * 1000), "pts")
