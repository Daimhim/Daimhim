import tensorflow as tf

x = tf.Variable([1, 2])
a = tf.constant([3, 3])
# 增加一个减法OP
sub = tf.subtract(x, a)
# 增加一个加法OP
add = tf.add(x, sub)
# 在变量使用前，需要初始化（计算），该方法是全局初始化
init = tf.global_variables_initializer()
# 视图输出
with tf.Session() as sess:
    sess.run(init)
    print(sess.run(sub))  # [-2 -1]
    print(sess.run(add))  # [-1  1]

# name指定赋值到哪个参数（python基础）
# 创建一个变量初始化为0
state = tf.Variable(0, name='counter')
# 创建一个OP，作用是使state+1
new_value = tf.add(state, 1)
# 赋值OP（tensorflow中变量不能直接=，需要掉用赋值函数）
# 第二个参数 赋值给第一个参数
update = tf.assign(state, new_value)
# 变量初始化（全局）
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(state))
    for _ in range(5):
        sess.run(update)
        print(sess.run(state))  # 0 1 2 3 4 5

"""
API记录
tf.Variable([1, 2])  # 定义一个变量
tf.constant([3, 3])  # 定义一个常量
tf.subtract(x, a)   # 一个减法OP
tf.add(x, sub)  # 一个加法OP
tf.global_variables_initializer()  # 变量初始化（全局），变量需要初始化，常量不用
tf.assign(state, new_value)  # 赋值OP（tensorflow中变量不能直接=，需要掉用赋值函数） 第二个参数 赋值给第一个参数
"""