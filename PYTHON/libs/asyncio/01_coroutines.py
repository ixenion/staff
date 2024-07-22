import asyncio


##############
# COROUTINES #
##############

# returns cotoutine object
# to execute coroutine you need 'await' it.
async def main():
    print('tim')
    await foo('text')
    print('finished')

async def foo(text):
    print(text)
    # await keyword required to run coroutine
    await asyncio.sleep(1)

# start main function
# 'main' is coroutine (entry point to the programm)

# asyncio.run(main())



#########
# TASKS #
#########

# line
# await foo('text')
# blocking our code, so
# to make it non-blocking
# create task instead

async def main2():
    print('tim')
    # start 'foo' ASAP and to allow other code to run
    # while this task not running itself
    task = asyncio.create_task(foo('text'))
    print('finished')

# asyncio.run(main())

# output
# tim
# finished
# text
# BUT why 'text' after 'finished'?
# because 'main' function still running



async def main3():
    print('tim')
    # start 'foo' ASAP and to allow other code to run
    # while this task not running itself
    task = asyncio.create_task(foo('text'))
    # wait 'task' to finish
    await task
    print('finished')

# asyncio.run(main())

# output
# tim
# text
# 'sleep 1'
# finished






async def main4():
    print('tim')
    task = asyncio.create_task(foo2('text'))
    await asyncio.sleep(0.5)
    print('finished')

async def foo2(text):
    print(text)
    # await keyword required to run coroutine
    await asyncio.sleep(10)

asyncio.run(main4())

# output
# tim
# text
# 'sleep 0.5'
# finished
