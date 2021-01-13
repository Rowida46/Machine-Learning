I. Week Content
------------

- **What is Recurrent Neural Networks (RNNs)**
- **Backpropagation through time**


II. ****Summary**** 
------------

***A. What is Recurrent Neural Networks (RNNs)***

  **Recurrent Neural Networks (RNNs)** is useful for such kind of scenarios where the order of the word needs to be considered. We can think of RNNs as a mechanism to hold memory 
  — where the memory is contained within the hidden layer.
 
***RNN Architecture*** 

![](https://www.bing.com/images/blob?bcid=RPWLgr8oajUCeA)
  - The network on the right is unrolled diagram of the network on the left where , 
      -  Wxh: is weights for the connection of the input layer to the hidden layer.
      -  W: is weights for the connection of the hidden layer to the hidden layer.
      -  Why: are the weights for the connection of the hidden-layer-to-output-layer layer.
      -  a: is the activation of the layer.

      The recurrent neural network scans through the data from left to right.
      In RNN making a prediction at time t, it uses not only input “xt” at time t but also information from previous input at time t-1 through activation parameter “a” and   
      weights “W” which passes from previously hidden layer to current hidden layer.


***B. Backpropagation through time***

   The error is back propagated from the last time step to the first time step. The error at each time step is calculated and this allows us to update the weights. The below   
   diagram is a visualization of the backpropagation through time. 
   
   ![](https://www.bing.com/images/blob?bcid=RPrRRS4NeDUCXw)
   




III. ****Resources ?****
------------

- [Introduction to the Architecture of Recurrent Neural Networks (RNNs)](https://medium.com/towards-artificial-intelligence/introduction-to-the-architecture-of-recurrent-neural-networks-rnns-a277007984b7)
- [A Simple overview of Multilayer Perceptron(MLP)](https://www.analyticsvidhya.com/blog/2020/12/mlp-multilayer-perceptron-simple-overview/)
