## Opencv图像处理

#### 1. 二值化图像

​		[参考地址](https://blog.csdn.net/hjxu2016/article/details/77834599)

* **将rgb图像转化为hsv图像**

  `hsv = cv2.cvtColor(rgb_image,cv2.COLOR_RGB2HSV)`

* **利用 inRange 函数设阈值,获得二值化图像**

  `mask = cv2.inRange(hsv,lower,upper)`

​		第一个参数: hsv 为原图

​		第二和第三个参数: lower 和 upper 为阈值,把图像在这个范围内的 hsv 值改为255,否则改为0

​		lower和 upper 都是数组,可以用 numpy.array([x, x, x]) 来定义

***

#### 2. 形态学操作

* **图像的腐蚀与膨胀**

  [参考地址](https://blog.csdn.net/hjxu2016/article/details/77837765)

  图像腐蚀

  `erosion = cv2.erode(image,kernel,iterations = 1)`

  图像膨胀

  `dilation = cv2.dilate(image,kernel,inerations = 1)`

  第一个参数: image 为原图

  第二个参数: kernel 为腐蚀或膨胀操作的内核,默认为3x3

  第三个参数: inerations 为腐蚀或膨胀的次数

  

* **开运算与闭运算**

  [参考地址](https://blog.csdn.net/chen134225/article/details/80874367?utm_medium=distribute.pc_relevant.none-task-blog-baidujs-2)

  开运算																

  `erosion =cv2.erode(image,kernel,iterations = 1)`

  `dilation = cv2.dilate(erosion,kernel,inerations = 1)`

  闭运算

  `dilation = cv2.dilate(image,kernel,inerations = 1)`

  `erosion =cv2.erode(dilation,kernel,iterations = 1)`

  由上可知开运算就是先腐蚀后膨胀,闭运算则相反

  > **开运算的作用是在消除细小噪点的情况下不明显影响目标物体的体积**
  >
  > **闭运算的作用是在填补细小空洞的情况下不明显影响目标物体的体积**