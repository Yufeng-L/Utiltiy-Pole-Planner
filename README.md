# EC601 5G Utility Pole Planner 
Hello, this is the readme of 5G Utility Pole Planner.

### Team member: 
- __Yufeng Lin__  yflin@bu.edu
- __Yuan Wei__    yuanwei@bu.edu
- __Junyou Chi__  chi12@bu.edu


## Introduction

This project is going use Google Street Imagery to model every utiltiy pole in a neighborhood and find a match to install certain equipment. Machine learning & Computer Visions will help us analyze the photos of utility poles and finally display results on web application.

## Product Definition
### __Product Mission__
For Telecom Company to determine where to install the 5G equipments on utility poles.

### __Target User(s)__
Target users are the Telecom Companies.
### __User Stories__
- I, the user, should be able to indentify if a specific utility pole has enough space to install the 5G equipment.
- I, the user, should be able to see the qualified utility poles on a specific area.

### __MVP(Minimum viable product)__
5G is the fifth generation cellular network technology. In this project, the most important mission is to determine if a specific utility pole has space to install the 5G equipment, and the next step is consider the distribution of installations.


## Product Survey
- Exisiting similar products &nbsp;
As we google "5G United States", we can find the following information:
![5Ginfo: ](https://github.com/Yufeng-L/EC601_5G_project/blob/5G_sprint1/5G_info.png)

### Patent Analysis
Some of the important patents are shows below:

1. [Method for Measuring Real Size of Object Using Camera of Mobile Terminal - US20120224052A1](http://appft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&p=1&u=/netahtml/PTO/srchnum.html&r=1&f=G&l=50&d=PG01&s1=20120224052.PGNR.)  
(1)recognizing an object image taken using a camera of a mobile terminal  
(2)measuring a size of an object image recognized in step (1)  
(3)measuring a distance between the object and the camera;  
(4)computing a real size of the object using the characteristic of the camera, the size of the object image measured in step     (2), and the distance between the object measured in step (3) and the camera.

2. [Method for recognizing object images and learning method for neural networks  - US6728404B1](http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&p=1&u=/netahtml/PTO/srchnum.html&r=1&f=G&l=50&d=PALL&s1=6728404.PN.)  
(1)A method for recognizing an object image comprises the steps of extracting a candidate for a predetermined object image  from an image.  
(2)making a judgment as to whether the extracted candidate for the predetermined object image is or is not the predetermined object image.  
(3)A learning method for a neural network comprises the steps of extracting a target object image, for which learning operations are to be carried out, from an image, feeding a signal, which represents the extracted target object image, into a neural network, and carrying out the learning operations of the neural network in accordance with the input target object image.
 

__Reference__: https://www.lifewire.com/5g-availability-us-4155914



Mobile communications has brought about profound changes in people's lives. In order to cope with a burst of traffic growth in 2020, the industry is witnessing the arrival of massive device connections, and emerging new services and scenarios, and celebrating the fifth generation of mobile communications.
http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO1&Sect2=HITOFF&p=1&u=/netahtml/PTO/srchnum.html&r=1&f=G&l=50&d=PALL&s1=6728404.PN.
