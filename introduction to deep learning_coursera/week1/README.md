I. Week Content
------------

- **Linear Regression**
- **linear classification model**
- **Stochastic gradient descent**

II. ****Summary**** 
------------

***A. Linear Regression***

   - *Linear model for regression example*
    
      `Y = Β0 + Β1X1 + Β2X2 +…..ΒpXp `
    
  - *Linear model for regression :: Vector notation*
  
       - Denote by y  the N times 1 vector of outputs .
       - Denote by X  the N times K matrix of inputs .

         ![](https://statlect.com/images/linear-regression__49.png)
         
  
  - *Loss function*
       - *OLS estimation*
       
         ![](https://statlect.com/images/linear-regression__75.png)
         
      - we can find the “w” vector by equating the slope of the below function to 0 and solve for **w**.
      
         ![](https://miro.medium.com/max/340/1*NpPOUymPCqDa-cdsir4MQg.png)


***B. linear classification model***

   - **Softmax Classifiers**
   
      The *Softmax classifier* is a generalization of the binary form of Logistic Regression. Just like in hinge loss or squared hinge loss, our mapping function f is defined such that it takes an input set of data x and maps them to the output class labels via a simple linear  dot product of the data x and weight matrix W: ![](https://www.pyimagesearch.com/wp-content/latex/3d3/3d3352f33b7787da7b49e1e2d69fc843-ffffff-000000-0.png) 
      
      However, unlike hinge loss, we interpret these scores as unnormalized log probabilities for each class label — this amounts to swapping out our hinge loss function with cross-entropy loss: ![](https://www.pyimagesearch.com/wp-content/latex/6da/6da93cbf6f8b8a53798305f37b536950-ffffff-000000-0.png)


![](https://gombru.github.io/assets/cross_entropy_loss/softmax_CE_pipeline.png)


***C. Stochastic gradient descent***

   if we have a million of gradient examples, then we have to sum over 1 million of gradients to calculate the gradient for one step of our algorithm. That's a lot. For 
    example, to make 1,000 gradient steps, we have to calculate a billion of gradients. So this makes gradient descent infeasible for large scale problems.To overcome this 
    problem we can use **stochastic gradient descent**.
   
   


III. ****Resources ?****
------------

- [Understanding Categorical Cross-Entropy Loss, Binary Cross-Entropy Loss, Softmax Loss, Logistic Loss](https://gombru.github.io/2018/05/23/cross_entropy_loss/#:~:text=%20Losses%20%201%20Cross-Entropy%20loss.%20The%20Cross-Entropy,Sigmoid%20activation%20plus%20a%20Cross-Entropy%20loss.%20More%20)

- [Main assumptions and notation about Linear Regression models ](https://statlect.com/fundamentals-of-statistics/linear-regression)

- [Regression — explained in simple terms!!](https://towardsdatascience.com/regression-explained-in-simple-terms-dccbcad96f61)

- [Stochastic Gradient Descent tutorial](https://towardsdatascience.com/stochastic-gradient-descent-clearly-explained-53d239905d31)

- [Softmax Classifiers Explained](https://www.pyimagesearch.com/2016/09/12/softmax-classifiers-explained/)

- [Cross-Entropy Loss Function](https://towardsdatascience.com/cross-entropy-loss-function-f38c4ec8643e)
