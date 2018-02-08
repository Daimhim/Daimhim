import tensorflow as tf

# 创建一个常量op
m1 = tf.constant([[3, 3]])
# 创建一个常量op
m2 = tf.constant([[2], [3]])
# 创建一个矩阵乘法op，吧m1、m2传入
product = tf.matmul(m1, m2)
# 尝试输出，得到一下结果
print(product)  # Tensor("MatMul:0", shape=(1, 1), dtype=int32)

# 定义一个会话Session，启动默认图
# 普通用法
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()

# 定义一个会话Session，启动默认图
# 推荐用法
with tf.Session() as sess:
    # 调用Session的run方法来执行矩阵乘法op
    # run(product)触发了图中的三个op
    result = sess.run(product)
    print(result)  # [[15]]


"""
API记录
tf.constant([[2], [3]])  # 创建一个常量OP
sess = tf.Session()  # 初始化一个会话
sess.run(product)  # 运行常量计算
sess.close()  # 关闭会话
tf.matmul(m1, m2)  # 创建一个矩阵乘法op，吧m1、m2传入
"""

