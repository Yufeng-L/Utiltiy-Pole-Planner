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
<br/>
 
 
 
 
__Reference__: https://www.lifewire.com/5g-availability-us-4155914 <br/>
https://github.com/hardikvasa/google-images-download
http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&p=1&u=/netahtml/PTO/srchnum.html&r=1&f=G&l=50&d=PALL&s1=6728404.PN.

__Img Reference__ :https://blog.plover.com/tech/utility-poles.html
