import time
import threading
import asyncio
from multiprocessing import Process


# _________________________________________________________________________
# One task and one thread. No speed increase
# def greeting_with_sleep(string):
#     s = time.perf_counter()
#     print(string)
#     time.sleep(2)
#     print("says hello!")
#     elapsed = time.perf_counter() - s
#     print("Sequential Programming Elapsed Time: " + str(elapsed) + " seconds")
#
#
# t = threading.Thread(target=greeting_with_sleep, args=('Codecademy',))
# t.start()

# _________________________________________________________________________
# Multiple threads
# def greeting_with_sleep(string):
#     print(string)
#     time.sleep(2)
#     print("says hello!")
#
#
# def main_threading():
#     s = time.perf_counter()
#     greetings = ['Codecademy', 'Chelsea', 'Hisham', 'Ashley']
#     # your code goes here
#     for i in range(len(greetings)):
#         # create thread
#         t = threading.Thread(target=greeting_with_sleep, args=(greetings[i],))
#
#         # start thread
#         t.start()
#
#     elapsed = time.perf_counter() - s
#     print("Threading Elapsed Time: " + str(elapsed) + " seconds")
#
#
# main_threading()

# _________________________________________________________________________
# Joining a thread
# def greeting_with_sleep(string):
#     print(string)
#     time.sleep(2)
#     print(string + " says hello!")
#
#
# def main_threading():
#     s = time.perf_counter()
#     threads = []
#     greetings = ['Codecademy', 'Chelsea', 'Hisham', 'Ashley']
#     for i in range(len(greetings)):
#         t = threading.Thread(target=greeting_with_sleep, args=(greetings[i],))
#         t.start()
#         # add append code here
#         threads.append(t)
#
#     # add join code here
#     for t in threads:
#         t.join()
#
#     elapsed = time.perf_counter() - s
#     print("Threading Elapsed Time: " + str(elapsed) + " seconds")
#
#
# main_threading()

# _________________________________________________________________________
# Asyncio Module

# async def greeting_with_sleep_async(string):
#     s = time.perf_counter()
#     print(string)
#     await asyncio.sleep(2)
#     print("says hello!")
#     elapsed = time.perf_counter() - s
#     print("Asyncio Elapsed Time: " + str(elapsed) + " seconds")
#
# # asyncio run syntax pre Python 3.7
# # loop = asyncio.get_event_loop()
# # loop.run_until_complete(greeting_with_sleep_async('Codecademy'))
#
# # asyncio run syntax Python 3.7 and greater
# asyncio.run(greeting_with_sleep_async('Codecademy'))

# _________________________________________________________________________
# Multiple Asynchronous Tasks

# async def greeting_with_sleep_async(string):
#     print(string)
#     await asyncio.sleep(2)
#     print(string + " says hello!")
#
#
# async def main_async():
#     s = time.perf_counter()
#     greetings = [greeting_with_sleep_async('Codecademy'), greeting_with_sleep_async('Chelsea'),
#                  greeting_with_sleep_async('Hisham'), greeting_with_sleep_async('Ashley')]
#     # your code goes here
#     await asyncio.gather(*greetings)
#
#     elapsed = time.perf_counter() - s
#     print("Asyncio Elapsed Time: " + str(elapsed) + " seconds")
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main_async())

# _________________________________________________________________________
# The Multiprocessing Module

# def greeting_with_sleep(string):
#     print(string)
#     time.sleep(2)
#     print("says hello!")
#
#
# def main_multiprocessing():
#     s = time.perf_counter()
#     processes = []
#     greetings = ['Codecademy', 'Chelsea', 'Hisham', 'Ashley']
#     # add your code here
#     for i in range(len(greetings)):
#         p = multiprocessing.Process(target=greeting_with_sleep, args=(greetings[i],))
#         processes.append(p)
#         p.start()
#
#     for p in processes:
#         p.join()
#
#     elapsed = time.perf_counter() - s
#     print("Multiprocessing Elapsed Time: " + str(elapsed) + " seconds")
#
#
# main_multiprocessing()

# _________________________________________________________________________
# Concurrent Programming Project

def cal_average(num):  # Average function used for sequential programming, threading, and multiprocessing
    sum_num = 0
    for t in num:
        sum_num = sum_num + t
    avg = sum_num / len(num)
    time.sleep(1)
    return avg


def main_sequential(list1, list2, list3):  # Main wrapper for sequential example
    s = time.perf_counter()
    # your code goes here
    cal_average(list1)
    cal_average(list2)
    cal_average(list3)

    elapsed = time.perf_counter() - s
    print("Sequential Programming Elapsed Time: " + str(elapsed) + " seconds")


async def cal_average_async(
        num):  # Average function used for asynchronous programming only ( needs await asyncio.sleep() )
    sum_num = 0
    for t in num:
        sum_num = sum_num + t
    avg = sum_num / len(num)
    await asyncio.sleep(1)
    return avg


async def main_async(list1, list2, list3):  # Main wrapper for asynchronous example
    s = time.perf_counter()
    # your code goes here
    tasks = [cal_average_async(list1), cal_average_async(list2), cal_average_async(list3)]
    await asyncio.gather(*tasks)

    elapsed = time.perf_counter() - s
    print("Asynchronous Programming Elapsed Time: " + str(elapsed) + " seconds")


def main_threading(list1, list2, list3):  # Main wrapper for threading example
    s = time.perf_counter()
    # your code goes here
    lists = [list1, list2, list3]
    threads = []
    for i in range(len(lists)):
        x = threading.Thread(target=cal_average, args=(lists[i],))
        threads.append(x)
        x.start()

    for x in threads:
        x.join()

    elapsed = time.perf_counter() - s
    print("Threading Elapsed Time: " + str(elapsed) + " seconds")


def main_multiprocessing(list1, list2, list3):  # Main wrapper for multiprocessing example
    s = time.perf_counter()
    # your code goes here
    processes = []
    lists = [list1, list2, list3]
    for i in range(len(lists)):
        p = Process(target=cal_average, args=(lists[i],))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    elapsed = time.perf_counter() - s
    print("Multiprocessing Elapsed Time: " + str(elapsed) + " seconds")


if __name__ == '__main__':  # Need to use this if-statement so multiprocessing doesn't cause an infinite loop
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Three lists we are trying to calculate average on
    l2 = [2, 4, 6, 8, 10]
    l3 = [1, 3, 5, 7, 9, 11]
    main_sequential(l1, l2, l3)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_async(l1, l2, l3))
    main_threading(l1, l2, l3)
    main_multiprocessing(l1, l2, l3)
