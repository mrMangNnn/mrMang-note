## Opencv

#### 1.基本操作

​		`cap = cv.VideoCapture(0)  ##打开摄像头`

​		`cv2.imshow('name',image)  ##将image显示在名为name的窗口上,利用循环可输出视频`

​		`cv.waitKey(0)  ##等待用户按任意键继续,不会打断图片显示，显示视频时需设置大于0的参数`

​		`niubi = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)  ##将rgb图像转化为灰度图`

#### 2. 二值化图像

* **将rgb图像转化为hsv图像**

  `niubi = cv2.cvtColor(rgb_image,cv2.COLOR_RGB2HSV)`

* **利用 inRange 函数设阈值,获得二值化图像**

  [参考地址](https://blog.csdn.net/hjxu2016/article/details/77834599)
  
  `mask = cv2.inRange(niubi,lower,upper)`
  
  第一个参数: niubi 为 hsv 图像
  
  第二和第三个参数: lower , upper 为阈值,把图像在这个范围内的 hsv 值改为255,否则改为0
  
  lower和 upper 都是数组,可以用 numpy.array([x, x, x]) 来定义

***

#### 3. 形态学操作

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

***

#### 4.滑动条操作

 * **创建滑动条**

   创建窗口

   `cv.namedWindow('niubi')`

   设置滑动条参数

   `cv.createTrackbar('name','niubi',initial_value,max_value,Callable)`

   第一个参数: name 为该滑动条的名字

   第二个参数: niubi 为该滑动条所处窗口的名字

   第三个参数: initial_value 为滑动条上的初始值

   第四个参数: max_value 为滑动条的最大值

   第五个参数: Callable 为回调函数,创建一个pass函数即可

   > `def Callable():`
   >
   > ​	`pass`

 * **调用滑动条**

   读取滑动条数据

   `current_value = cv.getTrackbarPos('name','niubi')`

   第一个参数: name 为要读取的滑动条的名字

   第二个参数: niubi 为要读取的滑动条所处窗口的名字

***

#### 5.边缘操作

* **边缘检测**

  [参考链接](https://blog.csdn.net/saltriver/article/details/80545571)

  高斯降噪

  `xiuer = cv2.GaussianBlur(image,(5,5),0)`

  需要注意的是第二个参数 (x , y) 必须为奇数

  Canny检测

  `canny = cv2.Canny(xiuer,low,high)`

  第一个参数: xiuer 为经过降噪的图

  第二和第三个参数: low , high 为检测的低阈值和高阈值

 * **寻找轮廓findContours**

   [参考链接](https://blog.csdn.net/dcrmg/article/details/51987348)

   `findContours(image,contours,hierarchy,mode,method,Point_offset)`

   第一个参数: image 原图,常用经过Canny,拉普拉斯等边缘检测算子处理过的二值图像,可以是灰度图

   第二和第三个参数: contours, hierarchy 可忽略,详情见链接 

   第四个参数: mode 定义轮廓的检索方式

   第五个参数: method 定义轮廓的近似方法

   第六个参数: Point 在每一个检测出的轮廓点上加上该偏移量,一般直接忽略
   
   opencv2.x中返回值为 contours, hierarchy,第一个返回值为轮廓的点集,第二个返回值为各个轮廓的编号

* **轮廓特征**

  [参考链接](https://www.jianshu.com/p/6a71aceb8da6)

  计算轮廓面积

  `area = contourArea(contour,bool oriented = False)`

  第一个参数: contour 为目标轮廓

  第二个参数一般直接用默认的False

  计算轮廓周长

  `perimeter = cv2.arcLength(contour,True)`

  第一个参数: contour 为目标轮廓

  第二个参数: True 表示轮廓是否闭合,不闭合则用False

  图像矩

  `niubi = cv2.moments(contour)`

  > **利用niubi可以计算出轮廓质心的坐标**
  >
  > **`cx=int(M['m10']/M['m00'])`**
  >
  > **`cy=int(M['m01']/M['m00'])`**

  