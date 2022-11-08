# 对paddle框架一个简单的应用

## 项目总览

+  [AutoEncoder](https://www.paddlepaddle.org.cn/documentation/docs/zh/practices/time_series/autoencoder.html) : 基于自编码器的异常值检测（本仓库中实现的是一维的）

+  [Boston](https://www.paddlepaddle.org.cn/documentation/docs/zh/tutorial/quick_start/linear_regression/linear_regression.html#id1) : 基于线性回归的波士顿房价预测

+  [ExpandPic](https://www.paddlepaddle.org.cn/documentation/docs/zh/tutorial/cv_case/super_resolution_sub_pixel/super_resolution_sub_pixel.html) : 通过Sub-Pixel实现图像超分辨率

+  [FacialKeypoint](https://www.paddlepaddle.org.cn/documentation/docs/zh/practices/cv/landmark_detection.html) : 人脸关键点检测

+  [HandwriterNumber](https://www.paddlepaddle.org.cn/documentation/docs/zh/tutorial/quick_start/linear_regression/linear_regression.html#id1) : 基于卷积神经网络的手写数字识别

+  [YanzCode](https://www.paddlepaddle.org.cn/documentation/docs/zh/practices/cv/image_ocr.html) : 通过OCR实现验证码识别

+  [Z_TY](../../) : 基于单层线性网络的二分类算法，基于自建的随机数据

## 对二维自测数据的表现

在使用genData2.py创建的数据:使用的公式为$y=2 \cdot x_1+3 \cdot x_2 + 2 + bias$ 其中bias为处于(-2,2)的随机噪声

结果如下图所示,其中红色的为使用原有公式生成的一系列坐标，蓝色为模型预测生成坐标，我们可以看到拟合效果十分不错。
![二维图示](./markdown/image/2d.png
)