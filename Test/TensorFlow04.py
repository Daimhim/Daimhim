import tensorflow as tf
import numpy as np

# 使用numpy生成100个随机点
x_data = np.random.rand(100)
# y_data = 真实值
y_data = x_data * 0.1 + 0.2

# 构造一个线性模型
b = tf.Variable(0.)
k = tf.Variable(0.)
# y = 预测值（上下公式保持一致）
y = k * x_data + b

# 二次代价函数（样本值减去预测值->求平方->平均值）
# 影响loss值的变量是：k，b
loss = tf.reduce_mean(tf.square(y_data - y))
# 定义一个梯度下降法来进行训练的优化器（学习率，值越大越不精确，但不能<=0）
optimizer = tf.train.GradientDescentOptimizer(0.1)
# 最小化代价函数
train = optimizer.minimize(loss)

# 初始化变量
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for step in range(200):
        # 执行顺序：梯度下降法》最小化代价函数》二次代价函数
        sess.run(train)
        if step % 20 == 0:  # 间隔20打印一次
            print(step, sess.run([k, b]))
            # 0[0.027093565, 0.05022619]
            # 20[0.104833506, 0.19686383]
            # 40[0.104043014, 0.19781029]
            # 60[0.103237, 0.19824797]
            # 80[0.10259131, 0.19859748]
            # 100[0.102074385, 0.19887725]
            # 120[0.10166061, 0.19910121]
            # 140[0.10132934, 0.19928049]
            # 160[0.101064175, 0.19942401]
            # 180[0.1008519, 0.19953892]#
            # 预测值慢慢的接近真实值

"""
API记录
tf.square(y_data - y)  # 求平方  
tf.reduce_mean()  # 求平均值
loss = tf.reduce_mean(tf.square(y_data - y))  # 二次代价函数
optimizer = tf.train.GradientDescentOptimizer(0.3)  # 梯度下降法
train = optimizer.minimize(loss)  # 最小化代价函数
"""