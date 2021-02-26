#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/2/22 13:12
# @file: part3.py
# import asyncio
# import aiohttp
#
# async def do_call(name, session):
#     async with session.get('https://www.google.be') as response:
#         await response.text()
#         return 'ok - {}'.format(name)
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         tasks = [do_call(str(i), session) for i in range(0,4)]
#         results = await asyncio.gather(*tasks)
#         print(results)
#
# asyncio.run(main())

a = [[1,2],[2,3],[3,4]]

for _ in a:
    print('_', _)
    for i in a[a.index(_) + 1:]:
        print('i',i)
