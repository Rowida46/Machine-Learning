I. Week Content
------------

- ***A Comprehensive Guide to Convolutional Neural Networks (CNN) architecture***

-  ***Pooling Layer***

II. ****Summary**** 
------------

***A. Defined CNN architecture***

 - Now you know that image is just a matrix of numbers so let's normalize them, `X_norm = X / 255 - .5` 
 
 - In the figure, we have an RGB image which has been separated by its three color planes — Red, Green, and Blue . To applay a convolution kernal it will be a **(W x H x C)** 
   tensor as well and stripthis kernal wooththe whole pixels of the images.
     
     - Note that we cannot use only one filtter as we will lose some depth , we need to trail C kernal with size **(W x H x C)**
 
        ![](https://miro.medium.com/max/500/1*15yDvGKV47a0nkf5qLKOOQ.png)
    
    - Every time performing a matrix multiplication operation between K and the portion P of the image over which the kernel is hovering. 
    
    ![](https://miro.medium.com/max/326/1*NsiYxt8tPDQyjyH3C08PVA@2x.png)
        
 - **Convolution Layer — The Kernel** 
   - If Image Dimensions = 5 (Height) x 5 (Breadth) x 1 (Number of channels, eg. RGB) , The element involved in carrying out the convolution operation in the first part of a 
   Convolutional Layer is called the Kernel/Filter, K, represented in the color yellow. We have selected K as a **3x3x1** matrix.
 
     ![](https://miro.medium.com/max/500/1*GcI7G-JLAQiEoCON7xFbhg.gif)
     
   - If Image Dimensions = 5 (Height) x 5 (Breadth) x 3(Number of channels, eg. RGB) , The filter moves to the right with a certain Stride Value till it parses the complete 
     width. Moving on, it hops down to the beginning (left) of the image with the same Stride Value and repeats the process until the entire image is traversed.
   
   ![](https://miro.medium.com/max/700/1*ciDgQEjViWLnCbmX-EeSrA.gif)
 
Each neuron within a CNN is responsible for a defined region of the input data, and this enables neurons to learn patterns such as lines, edges and small details that make up the image.
This defined region of space that a neuron or unit is exposed to in the input data is called the **Local Receptive Field**.
![]()

 
 
 
****B. Pooling Layer****

 - Similar to the Convolutional Layer, the Pooling layer is responsible for reducing the spatial size of the Convolved Feature .
 - It decrease the computational power required to process the data through dimensionality reduction.
    - It is useful for extracting dominant features which are rotational and positional invariant, thus maintaining the process of effectively training of the model.

   ![](https://miro.medium.com/max/396/1*uoWYsCV5vBU8SHFPAPao-w.gif)
   
   - *Types of Pooling*
   
   ![](https://miro.medium.com/max/500/1*KQIEqhxzICU7thjaQBfPBQ.png)
   
   
 ***Classification — Fully Connected Layer (FC Layer)***
 
   ![](https://miro.medium.com/max/700/1*kToStLowjokojIQ7pY2ynQ.jpeg)
   

III. ****Resources ?****
------------

- [A Comprehensive Guide to Convolutional Neural Networks — the ELI5 way](https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53)

- [A guide to receptive field arithmetic for Convolutional Neural Networks](https://us.hidester.com/proxy.php?u=eJwBdQCK%2F3M6MTA4OiJf9bm6pNWun6SXuM%2BlG%2B%2BClzSlmAM14r6s5dBiCLyIyeanzPdXDZEdhaFQuwngki5vU1cw78mjLEFiJNT67ZHKNxAym21AwlQdTLaTtoIy2j9V4%2FeZa5eQbmJuqNqn%2FFJ%2BIvGT4f3Aecu4%2FMEiOw0IPrc%3D&b=7&f=norefer)

- [Understand Local Receptive Fields In Convolutional Neural Networks](https://towardsdatascience.com/understand-local-receptive-fields-in-convolutional-neural-networks-f26d700be16c)

- [Week 1: Foundations of Convolutional Neural Networks](https://www.analyticsvidhya.com/blog/2018/12/guide-convolutional-neural-network-cnn/)

- [Tensor docs about model.fit parameter](https://keras.rstudio.com/reference/fit.html)
