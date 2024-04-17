def func(f):
    # 我嵌套定义一个函数
    def func2():
        print("f 准备执行！")
        f()
        print("f 结束执行！")

    return func2


@func
def test():
    print("这是原有的函数逻辑")


# 不再需要这样写
# new_f = func(test)
# new_f()

test()
