import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 去警告

def tensorflow_demo1():
   """
   tensoflow的基本结构
   """
   # python版本
   a=2
   b=3
   c=a+b
   print('python版本的加法操作：\n',c)

   # tensorflow实现加法操作
   a_t=tf.constant(2) # 定义常量
   b_t=tf.constant(3)
   c_t=a_t+b_t
   print('tensorflow版本的加法操作：\n',c_t)

   # 开启会话
   with tf.Session() as sess:
      c_t_value=sess.run(c_t)
      print('开启会话的结果\n',c_t_value)


if __name__ == '__main__':
   tensorflow_demo1()
'''
python版本的加法操作：
 5
tensorflow版本的加法操作：
 Tensor("add:0", shape=(), dtype=int32)
开启会话的结果
 5
'''
