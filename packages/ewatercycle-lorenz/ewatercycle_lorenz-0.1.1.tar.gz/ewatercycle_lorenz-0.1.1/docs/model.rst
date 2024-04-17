.. eWaterCycle-HBV documentation master file, created by
   sphinx-quickstart on Thu Mar  7 10:34:21 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Model
===========================================

Text from `eWaterCycle/streamingDataAssimilation <https://github.com/eWaterCycle/streamingDataAssimilation>`__


Chaotic model divergence: an ensemble of Lorenz 96 models using basic model interface (BMI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Lorenz 96 model is a model often used to demonstrate chaotic
behavior and it is the de-facto standard benchmark model used in the
field of data assimilation to test data assimilation methods. In this
notebook I present how to easily interact with an implementation of the
Lorenz 96 model through the Basic Model Interface (BMI). I show to run a
complete ensemble of model-instances that illustrates the chaotic nature
of the model.

the Lorenz 96 model
^^^^^^^^^^^^^^^^^^^

The Lorenz 96 model is a dynamical sytem for :math:`i=1,...,N` defined
by:

:math:`\frac{dx_{i}}{dt}=\left(x_{i+1} - x_{i-2}\right)x_{i-1} - x_{i} + F`


where i is cyclical, ie. :math:`x_{0}=x_{N}` and
:math:`x_{-1} = x_{N-1}`. :math:`F` is an external force acting on the
system. A value of :math:`F=8` is known to create chaotic bahavior and
is often used. The dimension :math:`N` can be freely chosen and is
typical :math:`40`, but for testing very high dimension systems, higher
values can be used. The Lorenz 96 model is a typical chaotic model
where, although, the model is deterministic, slight variations in the
input state will over time result in complete different states.

Numerical implementation of the Lorenz 96 model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A fourth order Runga Kutta scheme is used to implement the Lorenz 96
model. Writing the entire state-vector as :math:`\vec{x}` and using
:math:`f\left(\vec{x}\right)` as the right hand side of the model, ie:

:math:`f\left(x_{i}\right) = \left(x_{i+1} - x_{i-2}\right)x_{i-1} - x_{i} + F`

:math:`f\left(\vec{x}\right) = \left\{f\left(x_{1}\right),...,f\left(x_{N}\right)\right\}` 

the implementation is given by:

:math:`\vec{k}_{1}=f\left(\vec{x}\left(t\right)\right)`

:math:`\vec{k}_{2}=f\left(\vec{x}\left(t\right) + \frac{1}{2}\vec{k}_{1}\Delta t\right)`


:math:`\vec{k}_{3}=f\left(\vec{x}\left(t\right) + \frac{1}{2}\vec{k}_{2}\Delta t\right)`

:math:`\vec{k}_{4}=f\left(\vec{x}\left(t\right) + \vec{k}_{3}\Delta t\right)`

and finally 

:math:`\vec{x}\left(t + \Delta t\right) = \vec{x}\left(t\right) + \frac{1}{6}\left(\vec{k}_{1} + 2\vec{k}_{2} + 2 \vec{k}_{3} + \vec{k}_{4}\right)`


