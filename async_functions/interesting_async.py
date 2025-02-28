import asyncio
import time

# The event loop is the core of asyncio. It is responsible for:
# Managing and executing asynchronous functions (coroutines).
# Scheduling and switching between different tasks when they hit an await (yielding control).
# Handling I/O-bound operations efficiently without blocking execution.
# An async function can only run inside an event loop, so if event loop is not available, you can run async function.

# asyncio.run(main()):
# start an event loop, run the async function, at last, close the event loop

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()
# another way to run an async function, use the event loop directly. make sure to close it after running the function.

# if the event loop already exist, such as fastapi, jupyter notebook, databricks notebook etc.
# you don't need to call asyncio.run(main())
# you can run an async function directly using await: await async_func()

# t1 = asyncio.create_task(task1()):
# t2 = asyncio.create_task(task2()):
# asyncio.create_task does not create event loop.
# It takes a coroutine and wraps it into an asyncio.Task.
# Imagine it like a list, you can add multiple coroutines to it, one by one
# The tasks are scheduled to run in the background inside the existing event loop.
# It does not block execution—other code continues running immediately.
# t1 is an instance of asyncio.Task, which is a subclass of asyncio.Future. it can be awaited.
# When event loop starts execute the tasks, the order matters: first come, first start,
# but you don't have to wait the first to finish to start the second one.
# the "await" switches it to start another one
# Use asyncio.create_task() when you want to schedule background tasks but don’t need to await them immediately.

# results = await asyncio.gather(task1(), task2())
# like create_task, it does not create event loop, but use event loop
# "gather" can add/schedule multiple tasks at once
# it returns results of the tasks in a list
# Use asyncio.gather() when you need to start multiple tasks at once and wait for all to complete.


# how does the event loop execute the async function/coroutine?
# every time you call "await something", the execution will pause and give control back to event loop
# event loop will then starts the available async functions/coroutines in the task list(),
# when meet next "await", it starts another async/coroutine, and so on and so forth


# -----case 1--------------------------------------------------------------------------------------------
# in this block when you run asyncio.run(main()), the event loop will be created,
# when it execute to the first await: t1_result = await t1
# it pause and yield back control to the event loop,
# the event loop then check the tasks in the list (we have two added by create_task())
# it will start the one that added first, it is task1
# inside task1, when the code execute to await asyncio.sleep(2), it pauses and yields back control to event loop again
# this time event loop will start the existing task 2.
# when it encounters await asyncio.sleep(1), it pauses and yields back control to event loop again
# but this time the event loop has no other tasks to starts
# the control will be return to whatever awaits that finishes first
# since it only sleep 1 second in task 2, when the sleep ends, the control gives back to task 2
# (task 1 is still sleeping)
# task 2 get controls and proceed to next line of code, it will print "004 Task 2 asynchronous sleep finished"
# and collect the result.
# now task 2 is done and but task 1 is still sleeping.
# after 1 more second, the task 1 sleep ends, then proceed to print and return.
# task 1 is done, the control gives back to "t1_result = await t1"
# t1_result is assigned to the result of task 1
# the code move on until it meets "t2_result = await t2"
# it will pause and yield back control to event loop, but now no other tasks to start
# and since t2 already finished, t2_result = await t2 will gain control back immediately
# the results of t2 will be assigned to t_2 result.
# the code moves on

async def task1():
    print("002 Task 1 asynchronous sleep (2s) started")
    await asyncio.sleep(2)  # Task 1 "takes a break"
    print("005 Task 1 asynchronous sleep (2s) finished")
    return "Task 1 returned"

async def task2():
    print("003 Task 2 asynchronous sleep started")
    await asyncio.sleep(1)  # Task 2 "takes a break"
    print("004 Task 2 asynchronous sleep finished")
    return "Task 2 returned"

async def main():
    t1 = asyncio.create_task(task1())  # Task 1 is scheduled
    t2 = asyncio.create_task(task2())  # Task 2 is scheduled
    print("001 awaiting task 1 starts")
    t1_result = await t1  # The event loop ensures t1 finishes
    print(t1_result)
    print("006 awaiting task 1 ends")
    print("007 awaiting task 2 starts")
    t2_result = await t2  # The event loop ensures t2 finishes
    print(t2_result)
    print("008 awaiting task 2 ends")

asyncio.run(main())

# ---case 2-------------------------------------------------------------------------------------------------------------
# Here the order of crating tasks changed: task2 is added first
# remember for create_task, the order matters, the first added will be started first
# when the code runs to t1_result = await t1
# the await will give control back to event loop,
# the event loop will start task2 first and then task1 in the background
# even if the code here is waiting for t1.

async def main():
    t2 = asyncio.create_task(task2())  # Task 2 is scheduled
    t1 = asyncio.create_task(task1())  # Task 1 is scheduled
    print("001 awaiting task 1 starts")
    t1_result = await t1  # The event loop ensures t1 finishes
    print(t1_result)
    print("006 awaiting task 1 ends")
    print("007 awaiting task 2 starts")
    t2_result = await t2  # The event loop ensures t2 finishes
    print(t2_result)
    print("008 awaiting task 2 ends")

asyncio.run(main())

# -----case 3-----------------------------------------------------------------------------------------------------------
# here the after the asyncio.sleep(1), another 2 seconds of sync sleep is added.
# since this is the syn code, it does not yield back control
# during the syn sleep here,
# even if the task1 has finished sleep, it will not print
# task1 has to wai task2 to complete the sync code

# so be careful when you write async function. If it has a sync func that takes longer (compute intensive)
# it will block other async tasks

async def task2():
    print("003 Task 2 asynchronous sleep (1s) started")
    await asyncio.sleep(1)  # Task 2 "takes a break"
    print("004 Task 2 asynchronous sleep (1s) finished")
    print("004-1 Task 2 needs to sleep 1 more second (sync)")
    time.sleep(1)
    print("004-2 Task 2 wakes up from 1 second sleep (sync) ")
    print("004-3 Task 1 asynchronous sleep (2s) is done")
    print("004-4 However, Task 2  want to sleep another second")
    print("004-5 Task 1 has to wait, sorry ...")
    time.sleep(1)
    print("004-6 Task 2 wakes up now")
    print("004-7 Now let us go back to Task 1 and print it is finished ...")
    return "Task 2 returned"


async def main():
    t1 = asyncio.create_task(task1())  # Task 1 is scheduled
    t2 = asyncio.create_task(task2())  # Task 2 is scheduled
    print("001 awaiting task 1 starts")
    t1_result = await t1  # The event loop ensures t1 finishes
    print(t1_result)
    print("006 awaiting task 1 ends")
    print("007 awaiting task 2 starts")
    t2_result = await t2  # The event loop ensures t2 finishes
    print(t2_result)
    print("008 awaiting task 2 ends")

asyncio.run(main())

# -----case 4-----------------------------------------------------------------------------------------------------------
# in this case when you run await task2(), it will start task2 immediately.
# when encounter the await asyncio.sleep(1), the it starts task1
# Confusing? why in case 2, it is different?

async def task1():
    print("002 Task 1 asynchronous sleep (2s) started")
    await asyncio.sleep(2)  # Task 1 "takes a break"
    print("005 Task 1 asynchronous sleep (2s) finished")
    return "Task 1 returned"

async def task2():
    print("003 Task 2 asynchronous sleep started")
    await asyncio.sleep(1)  # Task 2 "takes a break"
    print("004 Task 2 asynchronous sleep finished")
    return "Task 2 returned"

async def main():
    t1 = asyncio.create_task(task1())  # Task 1 is scheduled
    print("001 start awaiting task 2")
    await task2()
    print("task2 is done")
    await t1

asyncio.run(main())

# -----case 5----------------------------------------------------------------------------------------------------------