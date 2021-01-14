![](https://github.com/pytorch/pytorch/blob/master/docs/source/_static/img/pytorch-logo-dark.png)

----------

**I. Content**

- **What is PyTorch**
- ***Tensor***



[PyTorch](https://us.hidester.com/proxy.php?u=eJwrtjI0s1ISmnSq537GmV4ne9cnTHXz1JWsAXPICVc%3D&b=7) is an open source machine learning library based on the Torch library.
        
   >  It's an improvement overTorch framework, however, the most notable change is the adoption of a **Dynamic Computational Graph**.
        
      ![](https://github.com/pytorch/pytorch/blob/master/docs/source/_static/img/dynamic_graph.gif)
    
Developed by Facebook's AI Research lab *(FAIR)* .PyTorch emphasizes flexibility and allows DL models to be expressed in **idiomatic Python**.


Similarly to NumPy, it also has a C backend, so they are both much faster than native Python, It's a replacement for NumPy to use the **power of GPUs** providing maximum       
flexibility and speed.

PyTorch is a Python package that provides two high-level features:
   
   - Tensor computation (like NumPy) with strong GPU acceleration
   - Deep neural networks built on a tape-based autograd system

    
- [More About PyTorch](https://github.com/pytorch/pytorch#more-about-pytorch)
- [Installation](https://github.com/pytorch/pytorch#installation)
 
 
***Tensor***   
      
![](https://github.com/pytorch/pytorch/blob/master/docs/source/_static/img/tensor_illustration.png)

A `torch.Tensor` is a  specialized data structure that 1D or 2D matrix containing elements of a single data type .


PyTorch provides Tensors that can live either on the CPU or the GPU and accelerates the computation by a huge amount.

      
In PyTorch, we use tensors to encode the inputs and outputs of a model, as well as the model’s parameters.
      
   - There are a few main ways to create a tensor, depending on your use case.

   - To create a tensor From a NumPy array , use `np.array(data)`
   
   - To create a tensor With random or constant values, use `torch.rand(shape)`.
   - To create a tensor From another tensor , `torch.rand_like(shape, datatype)`.

   - In-place operations Operations that have a _ suffix are in-place. For example: `x.copy_(y)`, `x.t_()`, will change x.

A tensor can be created with `requires_grad=True` so that torch.autograd records operations on them for automatic differentiation.





III. **Referances**
------------

- [PyTorch docs Tensor](https://pytorch.org/docs/stable/tensors.html)
- [PyTorch docs about Tensor](https://pytorch.org/docs/stable/tensors.html)

- [Developing deep learning models using  Pytorch](https://www.coursera.org/learn/deep-neural-networks-with-pytorch/home/welcome)

- [PyTorch Autograd](https://towardsdatascience.com/pytorch-autograd-understanding-the-heart-of-pytorchs-magic-2686cd94ec95)

- [Trying to understand what “save_for_backward” is in Pytorch question on stackoverflow](https://stackoverflow.com/questions/64460017/trying-to-understand-what-save-for-backward-is-in-pytorch)

- [PYTORCH: DEFINING NEW AUTOGRAD FUNCTIONS](https://pytorch.org/tutorials/beginner/examples_autograd/two_layer_net_custom_function.html)

- Implementing a Transformer with PyTorch and [PyTorch Lightning](https://www.linkedin.com/company/pytorch-lightning/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_recent_activity_details_shares%3BO3kQZoBQQd6AwlfGTfvmDg%3D%3D)

- Full Stack Deep Learning, Colab: https://lnkd.in/dRZTdBm
