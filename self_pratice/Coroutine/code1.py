'''

协程又称微线程
子程序，或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。
所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。（栈先进后出）

协程是单线程执行：效果类似多线程，但是比多线程减少了切换线程的开销。
提升效率可以是多进程加协程
'''

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(n):
    n.send(None)
    c = 0
    while c < 5:
        c = c + 1
        print("这是c %s" % c)
        r = n.send(c)
        print("这是r %r" % r)
    n.close()


c = consumer()
produce(c)
