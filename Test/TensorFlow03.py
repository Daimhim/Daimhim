import tensorflow as tf

# Fetch 多个参数会话
input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)

add = tf.add(input2, input3)
mu1 = tf.multiply(input1, add)

with tf.Session() as sess:
    result = sess.run([mu1, add])
    print(result)  # [21.0, 7.0]

# Feed  动态参数会话
# 创建占位符（32位）
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1, input2)

with tf.Session() as sess:
    # feed的数据以字典的形式传入
    print(sess.run(output, feed_dict={input1: [7.0], input2: [2.0]}))  # [14.]


"""
API记录
result = sess.run([mu1, add])  # Fetch传入形式
tf.placeholder(tf.float32)  # 创建占位符（32位）
sess.run(output, feed_dict={input1: [7.0], input2: [2.0]})  # feed的数据以字典的形式传入
"""