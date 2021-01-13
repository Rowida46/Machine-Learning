I. Content
------------

- **What is PyTorch**
- ***Tensor***




II. ****Summary**** 
------------

1. ***What is PyTorch***

  - [PyTorch](https://us.hidester.com/proxy.php?u=eJwrtjI0s1ISmnSq537GmV4ne9cnTHXz1JWsAXPICVc%3D&b=7) is an open source machine learning library based on the Torch library.
  
  - Used for applications such as computer vision and natural language processing.
  
  - Similarly to NumPy, it also has a C (the programming language) backend, so they are both much faster than native Python libraries
  
  - Developed by Facebook's AI Research lab *(FAIR)*. It is free and open-source software released under the Modified BSD license.PyTorch emphasizes flexibility and allows deep 
      learning models to be expressed in **idiomatic Python**.

      
  - PyTorch supports **dynamic computation graphs** that allow you to change how the network behaves on the fly, unlike static graphs that are used in frameworks such as Tensorflow.
  
  ![](https://us.hidester.com/proxy.php?u=eJwBQQC%2B%2F3M6NTc6IhKSyozCeMqNHjFIrgR5lCbJX1GN4b6rAljy%2BPo8AwwFNDk9PAC9A7SmK2wa1QXWO4BZ%2FO71aCHv%2FiI7fnocgg%3D%3D&b=7)
  
  - In Tensorflow, you first have to define the entire computation graph of the model and then run your ML model. But in PyTorch, you can define/manipulate your graph on-the-go.

      
2. ****Tensor***   

  - A torch.Tensor is a multi-dimensional matrix containing elements of a single data type.
  
  - There are a few main ways to create a tensor, depending on your use case.

      - To create a tensor with pre-existing data, use torch.tensor().

      - To create a tensor with specific size, use torch.* tensor creation ops (see Creation Ops).

      - To create a tensor with the same size (and similar types) as another tensor, use torch.*_like tensor creation ops (see Creation Ops).

      - To create a tensor with similar type but different size as another tensor, use tensor.new_* creation ops.
  
  - A tensor can be created with `requires_grad=True` so that torch.autograd records operations on them for automatic differentiation.





III. **Referances**
------------

- [PyTorch docs Tensor](https://pytorch.org/docs/stable/tensors.html)
- [PyTorch docs about Tensor](https://pytorch.org/docs/stable/tensors.html)

- [Developing deep learning models using  Pytorch](https://www.coursera.org/learn/deep-neural-networks-with-pytorch/home/welcome)

- [PyTorch Autograd](https://towardsdatascience.com/pytorch-autograd-understanding-the-heart-of-pytorchs-magic-2686cd94ec95)

- [Trying to understand what “save_for_backward” is in Pytorch question on stackoverflow](https://stackoverflow.com/questions/64460017/trying-to-understand-what-save-for-backward-is-in-pytorch)

- [PYTORCH: DEFINING NEW AUTOGRAD FUNCTIONS](https://pytorch.org/tutorials/beginner/examples_autograd/two_layer_net_custom_function.html)
