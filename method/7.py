#!/usr/bin/env python3
# encoding: utf-8
# @author: longtao.wu
# @contact: eustancewu@gmail.com
# @time: 2021/2/26 14:33
# @file: 7.py


# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i * i
#
#         fs.append(f)
#     return fs
#
# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs
#
# f1, f2, f3 = count()
#
# print(f1())


# def createCounter():
#     x = 0
#
#     def p():
#         def counter():
#             nonlocal x
#             x += 1
#             return x
#
#         return counter
#
#     return p()

# def createCounter():
#     x = 0
#
#     def counter():
#         nonlocal x
#         x += 1
#         return x
#
#     return counter
#
#
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')



# def z():
#     for _ in range(10):
#         if _ < 12:
#             continue
#         else:
#             break
#     else:
#         print('yes')
#
# z()


#---CASE 1
fs = map(lambda i:(lambda j: i*j),range(6))
print([f(2) for f in fs])
# for _ in fs:
#     print(_)

#---CASE 2
fs = [lambda j:i*j for i in range(6)]

print([f(2) for f in fs])

#---CASE 3
fs = []
for i in range(6):
    fs.append(lambda j:i*j)
    if i==3:
        break
print([f(2) for f in fs])

#---CASE 4
fs = [(lambda i:lambda j:i*j)(i) for i in range(6)]
print([f(2) for f in fs])



i = 1
def f(j):
    return i*j
print(f(2)) # ---> 2

i = 2
print(f(2)) # ---> 4

def g():
    i = 3
    def f(j):
        return i*j
    return f
f = g()
print(f(2)) # ---> 6

i = 100
print(f(2)) # ---> 6
