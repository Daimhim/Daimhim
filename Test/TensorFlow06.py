import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


#  载入数据集
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

# 每个批次大小
batch_size = 100  # 可调试
# 计算一共有多少个批次
n_batch = mnist.train.num_examples // batch_size

# 定义两个placeholder
x = tf.placeholder(tf.float32, [None, 784])
y = tf.placeholder(tf.float32, [None, 10])

# 创建一个简单的神经网络（可优化增加隐藏网络）
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
# 激活函数 计算概论
prediction = tf.nn.softmax(tf.matmul(x, W) + b)

# 二次代价函数
loss = tf.reduce_mean(tf.square(y - prediction))
# 使用梯度下降法(可优化)
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# 初始化变量
init = tf.global_variables_initializer()

# 结果存放在一个布尔类型列表中
# arg_max返回一维张量中最大的值所在的位置
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(prediction, 1))
# 求准确率
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(init)
    for epoch in range(21):  # 所有图片训练次数（可优化更多次数）
        for batch in range(n_batch):  # 所有图片训练一次
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})

        acc = sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels})
        print("Iter " + str(epoch) + ",Testing Accuracy " + str(acc))


"""
API记录
tf.nn.softmax(tf.matmul(x, W) + b)  # 激励函数（归一化指数函数）
tf.argmax(y, 1)  # 获取标签内最大值的位置
tf.equal(int, int)  # 比较大小
tf.cast(correct_prediction, tf.float32)  # 类型转换（布尔值转32位浮点）
mnist.train.next_batch(batch_size)  # 每运行一次调到下一个size
"""