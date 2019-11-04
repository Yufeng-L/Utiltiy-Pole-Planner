# EC601 5G Utility Pole Planner 
Hello, this is the readme of 5G Utility Pole Planner.

### Team member: 
- __Yufeng Lin__  yflin@bu.edu
- __Yuan Wei__    yuanwei@bu.edu
- __Junyou Chi__  chi12@bu.edu


## Introduction

This project is going to use Google Street Imagery to model utility poles in a neighborhood and find matches to install certain equipment. Machine learning & Computer Visions will help us analyze the photos of utility poles and finally display results. (Plan for Sprint1, may be subject to change later)

## Product Definition
### __Product Mission__
For Telecom Company to determine where to install the 5G equipments on utility poles.

### __Target User(s)__
Target users are the Telecom Companies.
### __User Stories__
- I, the telecom company, should be able to identify if there is utility pole on screen/image.
- I, the telecom company, should be able to identify if a specific utility pole has enough space to install the 5G equipment.
- I, the telecom company, should be able to see the qualified utility poles on a specific area.

### __MVP(Minimum viable product)__
5G is the fifth generation cellular network technology. In this project, the most important mission is to determine if a specific utility pole has space to install the 5G equipment, and the next step is consider the distribution of installations.

### Example of Image using Google Street View Api
![stex](https://github.com/Yufeng-L/EC601_5G_project/blob/master/img/SampleCo_42.3502517_-71.107573_95.JPG)

### Example of Target Image to Analyze
![ex2](https://github.com/Yufeng-L/EC601_5G_project/blob/master/eximg.jpg)

<br/>

### :warning: Images are grabbed from different websites, only used for educational/learning purpose :warning:

## Product Survey
- Exisiting similar products<br/>
As we google "5G United States", we can find the following information:
![5Ginfo: ](https://github.com/Yufeng-L/EC601_5G_project/blob/master/5G_info.png)

### Patent Analysis
Some of the important patents are shown below:

1. [Method for Measuring Real Size of Object Using Camera of Mobile Terminal - US20120224052A1](http://appft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&p=1&u=/netahtml/PTO/srchnum.html&r=1&f=G&l=50&d=PG01&s1=20120224052.PGNR.)  
(1)recognizing an object image taken using a camera of a mobile terminal  
(2)measuring a size of an object image recognized in step (1)  
(3)measuring a distance between the object and the camera;  
(4)computing a real size of the object using the characteristic of the camera, the size of the object image measured in step     (2), and the distance between the object measured in step (3) and the camera.

2. [Method for recognizing object images and learning method for neural networks  - US6728404B1](http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&p=1&u=/netahtml/PTO/srchnum.html&r=1&f=G&l=50&d=PALL&s1=6728404.PN.)  
(1)A method for recognizing an object image comprises the steps of extracting a candidate for a predetermined object image  from an image.  
(2)making a judgment as to whether the extracted candidate for the predetermined object image is or is not the predetermined object image.  
(3)A learning method for a neural network comprises the steps of extracting a target object image, for which learning operations are to be carried out, from an image, feeding a signal, which represents the extracted target object image, into a neural network, and carrying out the learning operations of the neural network in accordance with the input target object image.
 
## System Design
 __Language:__ <br/>
  Python      <br/>
 __Major Components to use:__ <br/>
 Google Street View API, OPENCV library for image processing for __sprint1__ <br/>
 Tensorflow, LabelImg, YOLO used for Image label and classification for __sprint2__
 
 
## Flowchart
![flowchart](https://github.com/Yufeng-L/EC601_5G_project/blob/sprint2/systemdesign.png)

## Training via Tensorflow
After doing image classification between poles and nopoles, here is the traning result for sprint2. Here is the training result for 15 epochs. (Results still need to be optimized. Validation rate is not high enough)
![tfres](https://github.com/Yufeng-L/EC601_5G_project/blob/master/res.png)

Here is the result when epoch = 30. As we can see, comparing with the result above, the accurary is higher and the loss is lower. The value of epochs is related to the training accuracy. (Para: Batch size = 64, Epochs = 30)
![tfresepo30](https://github.com/Yufeng-L/EC601_5G_project/blob/master/res_epoch30.png)

Here is the result when epoch = 60. (Para: Batch size = 128, Epochs = 60)
![tfresepo60](https://github.com/Yufeng-L/EC601_5G_project/blob/master/res_epoch60.png)


## Training via YOLO


## YOLO 

the latest version, YOLOv3, was applied in our object detection program.


### Procedure

​	Basiclly,The procedure is devided into three part establishing dataset, traning our data and test it.

##### 	Establish Dataset 

- We use ***LabelImg\*.py** to annotate our training data. Anotation will be saved in coordinates as txt. You can also see the details [here](https://github.com/tzutalin/labelImg#macos).

  Type the following command to make sure you meet the requirements.

  ```
  brew install python3
  pip install pipenv
  pipenv --three
  pipenv shell
  pip install py2app
  pip install PyQt5 lxml
  make qt5py3
  rm -rf build dist
  python setup.py py2app -A
  mv "dist/labelImg.app" /Applications
  ```

  ##### Annotation 

  - In data/predefined_classes.txt define the list of classes that will be used for your training. In my case, I just defined **utility poles**.
  - Build and launch using the instructions above.
  - Right below "Save" button in toolbar, click "PascalVOC" button to switch to YOLO format.
  - You may use Open/OpenDIR to process single or multiple images. When finished with single image, click save.
  - A txt file of yolo format will be saved in the same folder as your image with same name. A file named "classes.txt" is saved to that folder too. "classes.txt" defines the list of class names that your yolo label refers to.

  Note:

  - Your label list shall not change in the middle of processing a list of images. When you save a image, classes.txt will also get updated, while previous annotations will not be updated.
  - You shouldn't use "default class" function when saving to YOLO format, it will not be referred.
  - When saving as YOLO format, "difficult" flag is discarded.

（图片 label img）

​		after anotation, you should get bunches of .txt files like this

![image-20191104112732769](https://github.com/Yufeng-L/EC601_5G_project/blob/master/img/image-20191104112732769.png)



Open one .txt file, the output should be:

![image-20191104112910646](https://github.com/Yufeng-L/EC601_5G_project/blob/master/img/image-20191104112910646.png)

Where, 0 is the predefined index for class utility poles, the other for float number is the coordiantes we annotated in picture. Each row represets a rectangular annotation

##### Training & test set file path 



here we use process.py to generate，take the python file to the picture folder and run it. This script file generate 2 .txt file named train.txt and test.txt.

![image-20191104114221285](https://github.com/Yufeng-L/EC601_5G_project/blob/master/img/image-20191104114221285.png)

![image-20191104113942320](https://github.com/Yufeng-L/EC601_5G_project/blob/master/img/image-20191104113942320.png)





##### Training 

Note: we do the trainning in the Windows PC using Nvida GPU for accelartion.

Before we stat we should make 3 config files names voc.data, voc.names, yolov3-voc.cfg.

voc.data:

```
classes= 1
train  = （your path）+pole_train.txt
valid  = （your path）+pole_test.txt
#difficult = data/difficult_2007_test.txt
names = data/voc.names
backup = (path where you want to save)


```



voc.name:

```
utility poles
```

Note the name and number of rows should be same as your predefined_classes.txt in our annotation software

yolov3-voc.cfg:

for each [yolo] and adjacent [convolutional],make following changes to them

```
[convolutional]
size=1
stride=1
pad=1
filters=18 # class=1 filter=18
activation=linear

[yolo]
mask = 6,7,8
anchors = 10,13,  16,30,  33,23,  30,61,  62,45,  59,119,  116,90,  156,198,  373,326
classes=1 #only 1 class: utility poles
num=9
jitter=.3
ignore_thresh = .5
truth_thresh = 1
random=1
```



After we finish this, we can begin our tranning.

Download the darknet using the these comand:

```
git clone https://github.com/pjreddie/darknet.git
cd darknet
make
```

Type the code to see whether you successfually 

```
./darknet
```

you will get:

```
usage: ./darknet <function>
```



Let's start brutally, 

```
darknet.exe detector train .\data\voc.data yolov3-voc.cfg .\weights_pr\darknet53.conv.74 .\results_mine
```

we can have series output in our cmd window:

![image-20191104120811296](/Users/yuanwei/Library/Application Support/typora-user-images/image-20191104120811296.png)



now we can do is to drink a cup of tea/coffee. Enjoy the sunshine and take a nap.

Note: if you use CPU to deal with the traning part,  you can sleep for the whole day.

```
 avg - average loss (error) - the lower, the better
```

ResultL:

![image-20191104121132711](https://github.com/Yufeng-L/EC601_5G_project/blob/master/img/image-20191104113851516.png)
![image-20191104121151847](https://github.com/Yufeng-L/EC601_5G_project/blob/master/img/image-20191104121151847.png)
![image-20191104113851516](https://github.com/Yufeng-L/EC601_5G_project/blob/master/img/image-20191104121132711.png)




 



 
 
 
 
__Reference__: <br/>
https://www.lifewire.com/5g-availability-us-4155914 <br/>
http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&p=1&u=/netahtml/PTO/srchnum.html&r=1&f=G&l=50&d=PALL&s1=6728404.PN.

__Img Reference__ : <br/>
https://blog.plover.com/tech/utility-poles.html <br/>
https://github.com/hardikvasa/google-images-download 
