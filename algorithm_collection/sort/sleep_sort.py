from asyncio import run, sleep, wait


res = []


def sleep_sort(arr):
    global res
    res = []
    run(wait(list(map(f, map(int, arr)))))

    return res


async def f(n):
    await sleep(n)
    res.append(n)
