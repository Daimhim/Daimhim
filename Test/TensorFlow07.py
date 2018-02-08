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
keep_prob = tf.placeholder(tf.float32)
lr = tf.Variable(0.001, dtype=tf.float32)

# 创建一个简单的神经网络（可优化增加隐藏网络）
W1 = tf.Variable(tf.truncated_normal([784, 500], stddev=0.1))
b1 = tf.Variable(tf.zeros([500]) + 0.1)
L1 = tf.nn.tanh(tf.matmul(x, W1) + b1)
L1_drop = tf.nn.dropout(L1, keep_prob)
# 增加一个隐藏层
W2 = tf.Variable(tf.truncated_normal([500, 300], stddev=0.1))
b2 = tf.Variable(tf.zeros([300]) + 0.1)
L2 = tf.nn.tanh(tf.matmul(L1_drop, W2) + b2)
L2_drop = tf.nn.dropout(L2, keep_prob)

W3 = tf.Variable(tf.truncated_normal([300, 10], stddev=0.1))
b3 = tf.Variable(tf.zeros([10]) + 0.1)

# 激活函数 计算概论
prediction = tf.nn.softmax(tf.matmul(L2_drop, W3) + b3)

#  二次代价函数 改为交叉熵代价函数
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=prediction))
# 使用梯度下降法(可优化)
train_step = tf.train.AdadeltaOptimizer(lr).minimize(loss)

# 初始化变量
init = tf.global_variables_initializer()

# 结果存放在一个布尔类型列表中
# arg_max返回一维张量中最大的值所在的位置
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(prediction, 1))
# 求准确率
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(init)
    for epoch in range(50):  # 所有图片训练次数（可优化更多次数）
        # 初始化 学习率较大比较更快学习 学习次数越多 学习率越小  精度越高（此写法会让学习率不断降低）
        sess.run(tf.assign(lr, 0.001 * (0.95 ** epoch)))
        for batch in range(n_batch):  # 所有图片训练一次
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys, keep_prob: 1.0})

        learning_rate = sess.run(lr)
        acc = sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels, keep_prob: 1.0})
        print("Iter " + str(epoch) + ", Testing Accuracy " + str(acc) + ", Learning Rate= " + str(learning_rate))

"""
API记录
tf.nn.softmax(tf.matmul(x, W) + b)  # 激励函数（归一化指数函数）
tf.argmax(y, 1)  # 获取标签内最大值的位置
tf.equal(int, int)  # 比较大小
tf.cast(correct_prediction, tf.float32)  # 类型转换（布尔值转32位浮点）
mnist.train.next_batch(batch_size)  # 每运行一次调到下一个size
"""
