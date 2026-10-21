---
title: "Accelerating Machine Learning with MLOps and FuseML: Part One"
date: 2021-07-25T20:50:38
slug: "accelerating-machine-learning-with-mlops-and-fuseml-part-one"
author: "Stefan Nica"
image: "images/mlops-fuseml-featured.png"
products: ["Other"]
tags: ["ai"]
content_type: "explainer"
draft: true
migration:
  wp_id: 87657
  original_url: "https://www.suse.com/c/rancher_blog/accelerating-machine-learning-with-mlops-and-fuseml-part-one/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "FuseML project discontinued, 2021 MLOps tooling"
  redirect_target: "rancher.com/blog (hub)"
---

Building successful machine learning (ML) production systems requires a specialized re-interpretation of the traditional DevOps culture and methodologies. MLOps, short for machine learning operations, is a relatively new engineering discipline and a set of practices meant to improve the collaboration and communication between the various roles and teams that together manage the end-to-end lifecycle of machine learning projects.

Helping enterprises adapt and succeed with open source is one of SUSE’s key strengths. At SUSE, we have the experience to understand the difficulties posed by adopting disruptive technologies and accelerating digital transformation. Machine learning and MLOps are no different.

The SUSE AI/ML team has recently launched [FuseML](https://fuseml.github.io/), an open source orchestration framework for MLOps. FuseML brings a novel holistic interpretation of MLOps advocated practices to help organizations reshape the lifecycle of their Machine Learning projects. It facilitates frictionless interaction between all roles involved in machine learning development while avoiding massive operational changes and vendor lock-in.

This is the first in a series of articles that provides a gradual introduction to machine learning, MLOps and the FuseML project. We start here by rediscovering some basic facts about machine learning and why it is a fundamentally atypical technology. In the next articles, we will look at some of the key MLOps findings and recommendations and how we interpret and incorporate them into the FuseML project principles.

## MLOps Overview

Old habits that need changing can be difficult to unlearn, even more difficult than re-learning everything. It’s true for people, and it’s even truer for teams and organizations where the combined inertia that makes important changes difficult to implement is several orders of magnitude greater.

With the AI hype on the rise, organizations have been investing more and more in machine learning to make better and faster business decisions or automate key aspects of their operations and production processes. But if history taught us anything about adopting disruptive software technologies like virtualization, containerization and cloud computing, it’s that getting results doesn’t happen overnight. It often requires significant operational and cultural changes. With machine learning, this challenge is very pronounced, with more than 80 percent of AI projects failing to deliver business outcomes, as reported by Gartner in 2019 and repeatedly confirmed by business analysts and industry leaders throughout 2020 and 2021.

Naturally, following this realization about the challenges of using machine learning in production, a lot of effort went into investigating the “whys” and “whats” about this state of affairs. Today, the main causes of this phenomenon are better understood. A brand new engineering discipline - MLOps - was created to tackle the specific problems that machine learning systems encounter in production.

The recommendations and best practices assembled under the MLOps label are rooted in the recognition that machine learning systems have specialized requirements that demand changes in the development and operational project lifecycle and organizational culture. MLOps doesn’t propose to reinvent how we do DevOps with software projects. It’s still DevOps but pragmatically applied to machine learning.

MLOps ideas can be traced back to the defining characteristics of machine learning. The remainder of this article is focused on revisiting what differentiates machine learning from conventional programming. We’ll use the fundamental insights in this exercise as stepping stones when we dive deeper into MLOps in the next chapter of this series.

## Machine Learning Characteristics

Solving a problem with traditional programming requires a human agent to formulate a solution, usually in the form of one or more algorithms, and then translate it into a set of explicit instructions that the computer can execute efficiently and reliably. Generally speaking, conventional programs, when correctly developed, are expected to give accurate results and to have highly predictable and easily reproducible behaviors. When a program produces an erroneous result, we treat that as a defect that needs to be reproduced and fixed. As a best practice, we also process conventional software through as much testing as possible before deploying it in production, where the business cost incurred for a defect could be substantial. We rely on the results of proactive testing to give us some guarantees about how the program will behave in the future, another characteristic derived from the predictability aspect of conventional software. As a result, once released, a software product is expected to take significantly less effort to maintain compared to development.

Some of these statements are highly generic. One might say they could even be used to describe products in general, software or otherwise. They all have in common that they no longer hold as entirely valid when applied to machine learning.

Machine learning algorithms are distinguished by their ability to learn from experience (i.e., from patterns in input data) to behave in a desired way, rather than being programmed to do so through explicit instructions. Human interaction is only required during the so-called training phase when the ML algorithm is carefully calibrated and data is fed into it, resulting in a trained program, also called an ML model. With proper automation in place, it may even seem that human interaction could be eliminated. Still, as we’ll see later in this post, it’s just that the human responsibilities shift from programming to other activities, such as data collection and processing and ML algorithm selection, tuning and monitoring.

Machine learning can be used to solve a specific class of problems:

- the problem is extremely difficult to solve mathematically or programmatically, or it has only solutions that are too computationally expensive to be practical
- a fair amount of data exists (or can be generated) containing a pattern that an ML algorithm can learn

Let’s look at two examples, similar but situated at opposite ends of the spectrum as far as utility is concerned.

### Sum of Two Numbers

A very simple example, albeit with no practical application whatsoever, is training an ML model to calculate the sum of two real numbers. Doing this with conventional programming is trivial and always yields very accurate results.

Training and using an ML model for the same task could be summarized by the following phases:

#### Data Preparation

First, we need to prepare the input data that will be used to train the ML model. Generally speaking, training data is structured as a set of entries. Each entry associates a concrete set of values used as input for the target problem with the correct answer (sometimes known as a target or label in ML terms). In our example, each entry maps a pair of real input values (X, Y) to the desired result (X+Y) that we expect the model to learn to compute. For this purpose, we can generate the training data entirely using conventional programming. Still, it’s often the case with machine learning that training data is not readily available and expensive to acquire and prepare. The code used to generate the input dataset could look like this:

```
import numpy as np 
train_data = np.array([[1.0,1.0]])
train_targets = np.array([2.0])
for i in range(3,10000,2):
  train_data = np.append(train_data,[[i,i]],axis=0)
  train_targets = np.append(train_targets,[i+i])
```

Deciding what kind of data is needed, how much of it and how it needs to be structured and labeled to yield acceptable results during ML training is the realm of data science. The data collection and preparation phase is critical to ensuring the success of ML projects. It takes experimentation and experience to find out which approach yields the best result, and data scientists often need to iterate several times through this phase and improve the quality of their training data to raise the accuracy of ML models.

#### Model Training

Next, we need to define the ML algorithm and train it (also known as fitting) on the input data. For our goal, we can use an Artificial Neural Network (ANN) suitable for this type of problem (regression). The code for it could look like this:

```
import tensorflow as tf
from tensorflow import keras
import numpy as np

model = keras.Sequential([
  keras.layers.Flatten(input_shape=(2,)),
  keras.layers.Dense(20, activation=tf.nn.relu),
  keras.layers.Dense(20, activation=tf.nn.relu),
  keras.layers.Dense(1)
])

model.compile(optimizer='adam', 
  loss='mse',
  metrics=['mae'])

model.fit(train_data, train_targets, epochs=10, batch_size=1)
```

Similar to data preparation, deciding which ML algorithm to use and what values should be configured for its parameters for best results (e.g., the neural network architecture, optimizer, loss, epochs) requires specific ML knowledge and iterative experimentation. However, by now, ML is mature enough to make finding an algorithm that fits the problem not difficult, especially given that there are countless open source libraries, examples, ready-to-use ML models and documented use-case patterns and recipes available for all major classes of problems that can be solved with ML, that one can start from. Moreover, many of the decisions and activities required to develop a high-performing ML model (e.g., hyper-parameter tuning, neural architecture search) can already be fully automated or accelerated through partial automation through a special category of tools called AutoML.

#### Model Prediction

We now have a trained ML model that we can use to calculate the sum of any two numbers (i.e. make predictions):

```
def sum(x, y):
  s = model.predict([[x, y]])[0][0]
  print("%f + %f = %f" % (x, y, s))
```

The first thing to note is that the summation results produced by the trained model are not at all accurate. It’s fair to say that the ML model is not behaving like it’s calculating the result, but more like it’s giving a ballpark estimation of what the result might be, as shown in this set of examples:

```
# sum(2000, 3000)
2000.000000 + 3000.000000 = 4857.666992
# sum(4, 5)
4.000000 + 5.000000 = 9.347977
```

Another notable characteristic is, as we move further away from the pattern of values on which the model was trained, the model’s predictions get worse. In other words, the model is better at estimating summation results for input values that are more similar to the examples on which it was trained:

```
# sum(10, 10000)
10.000000 + 10000.000000 = 8958.944336
# sum(1000000, 4)
1000000.000000 + 4.000000 = 1318969.375000
# sum(4, 1000000)
4.000000 + 1000000.000000 = 895098.750000
# sum(0.1, 0.1)
0.100000 + 0.100000 = 0.724608
# sum(0.01, 0.01)
0.010000 + 0.010000 = 0.549576
```

This phenomenon is well known to ML engineers. If not properly understood and addressed, it can lead to ML specific problems that take various forms and names:

- *bias*: using incomplete, faulty or prejudicial data to train ML models that end up producing biased results
- *training-serving skew*: training an ML model on a dataset that is not representative of the real-world conditions in which the ML model will be used
- *data drift, concept drift or model decay*: the degradation, in time, of the model quality, as the real-world data used for predictions changes to the point where the initial assumptions on which the ML model was trained are no longer valid

In our case, it’s easy to see that the model is performing poorly due to a skew situation: we inadvertently trained the model on pairs of equal numbers, which is not representative of the real-world conditions in which we want to use it. Our model also completely missed the point that addition is commutative, but that’s not surprising, given that we didn’t use training data representative of this property either.

When developing ML models to solve complex, real-world problems, detecting and fixing this type of problem is rarely that simple. Machine learning is as much an art as it is a science and engineering endeavor.

In training ML models, there is usually also a validation step involved, where the labeled input data is split, and part of it is used to test the trained model and calculate its accuracy. This step is intentionally omitted here for the sake of simplicity. The full exercise of implementing this example, with complete code and detailed explanations, is covered in [this article](https://www.pluralsight.com/guides/deep-learning-model-add).

### The Three-Body Problem

At the other end of the spectrum is a physics (classical mechanics) problem that has inspired one of the greatest mathematicians of all times, Isaac Newton, to invent an entirely new branch of math and nowadays a source of constant frustration among high school students: Calculus.

Finding the solution to the set of equations that describe the motion of two celestial bodies (e.g., the Earth and the Moon) given their initial positions and velocities is already a complicated problem. Extending the problem to include a third body (e.g., the Sun) complicates things to the point where a solution cannot be found, and the entire system starts behaving chaotically. With no mathematical solution in sight, Newton himself felt that supernatural powers had to be at play to account for the apparent stability of our solar system.

This problem and its generalized form, the many-body problem, are so famous because solving them is a fundamental part of space travel, space exploration, cosmology and astrophysics. Partial solutions can be calculated using analytical and numerical methods, but it requires immense computational power.

All life forms on this planet are constantly used to dealing with gravity. We are well equipped to learn from experience, and we’re able to make pretty accurate predictions regarding its effects on our bodies and the objects we interact with. It is not entirely surprising that Machine Learning can estimate the motion of objects under the effect of gravity.

Using Machine Learning, researchers at the University of Edinburgh have been able to train an ML model capable of solving the three-body problem 100 million times faster than traditional means. The full story covering this achievement is available [here](https://www.technologyreview.com/2019/10/26/132171/a-neural-net-solves-the-three-body-problem-100-million-times-faster/), and the original scientific paper can be read [here](https://arxiv.org/pdf/1910.07291.pdf).

Solving the three-body problem with ML is similar to our earlier trivial example of adding two numbers together. The training and validation datasets are also generated through simulation, and an ANN is also involved here, albeit one with a more complex structure. The main differences are the complexity of the problem and ML’s immediate practical application to this use case. However, the observations previously stated about general ML characteristics apply equally to both cases, regardless of complexity and utility.

## Conclusion

We haven’t even begun to look at MLOps in detail. Still, we can already identify and summarize key takeaways representative of ML in general just by comparing classical programming to Machine Learning:

1. Not all problems are good candidates for machine learning
2. The process of developing ML models is iterative, exploratory and experimental
3. Developing a machine learning system requires dealing with new categories of artifacts with specialized behaviors that don’t fit the patterns of conventional software
4. It’s usually not possible to produce fully accurate results with ML models
5. Developing and working with machine learning based systems requires a specialized set of skills, in addition to those needed for traditional software engineering
6. Running ML systems in the real world is far less predictable than what we’re used to with regular software
7. Finally, developing ML systems would be next to impossible without specialized tools

Machine Learning characteristics summarized here are reflected in the MLOps discipline and distilled in the principles on which we based the FuseML orchestration framework project. The next article will give a detailed account of MLOps recommendations and how an MLOps orchestration framework like FuseML can make developing and operating ML systems an automated and frictionless experience.
