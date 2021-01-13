I. Week Content
------------

- **What is TensorFlow**


II. ****Summary**** 
------------

***A. What is TensorFlow***

 - **TensorFlow** is a deep learning framework , TensorFlow is essentially two things. 
  
   - First it is a tool to describe computational graphs. The foundation of computation in TensorFlow is the *graph object*.
   
   - TensorFlow is also a run time for execution of these graphs. You can execute them on CPU, GPU, or even custom hardware, like Tensor Processing Unit.

 - *Why this name ?*
  
   - Inputs and Outputs to any operation are nothing more than  a collection of tensors, which are multi-dimensional arrays. 
   
 - *how our input might look like?*
  
    - The first one is a **placeholder**. A placeholder is just a place for a tensor, which will be fed during graph execution. For example, it can be input features. You already 
      know the size of your features and the type of your features, but you might not have them right now when you define your graph.
 
   - Another kind of input is a **variable**. This is a tensor with some value that is stored and updated during our graph execution. For example, it could be a weights matrix in 
     our MLP, And you can define a variable easily, just fitting the shape and type of that arrival.
     
   - The third type of input which is a **constant**. This is a tensor with constant value that cannot be changed. And you can define it easily as well, using Numpy or any other 
     inputs. 
      

III. ****Resources ?****
------------

- [TensorFlow tutorials](https://www.tensorflow.org/tutorials)

- [TensorFlow doc about tensorflow.keras.layers.Dense Parameters](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense)

- [TensorFlow doc about train.GradientDescentOptimizer](https://www.tensorflow.org/api_docs/python/tf/compat/v1/train/GradientDescentOptimizer)
