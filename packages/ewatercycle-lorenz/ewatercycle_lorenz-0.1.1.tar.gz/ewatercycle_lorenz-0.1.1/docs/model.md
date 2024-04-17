### Chaotic model divergence: an ensemble of Lorenz 96 models using basic model interface (BMI)
The Lorenz 96 model is a model often used to demonstrate chaotic behavior and it is the de-facto standard benchmark model used in the field of data assimilation to test data assimilation methods. In this notebook I present how to easily interact with an implementation of the Lorenz 96 model through the Basic Model Interface (BMI). I show to run a complete ensemble of model-instances that illustrates the chaotic nature of the model.

#### the Lorenz 96 model
The Lorenz 96 model is a dynamical sytem for $i=1,...,N$ defined by
\begin{equation}
\frac{dx_{i}}{dt}=\left(x_{i+1} - x_{i-2}\right)x_{i-1} - x_{i} + F
\end{equation}
where i is cyclical, ie. $x_{0}=x_{N}$ and $x_{-1} = x_{N-1}$. $F$ is an external force acting on the system. A value of $F=8$ is known to create chaotic bahavior and is often used. The dimension $N$ can be freely chosen and is typical $40$, but for testing very high dimension systems, higher values can be used. The Lorenz 96 model is a typical chaotic model where, although, the model is deterministic, slight variations in the input state will over time result in complete different states.

#### Numerical implementation of the Lorenz 96 model
A fourth order Runga Kutta scheme is used to implement the Lorenz 96 model. Writing the entire state-vector as $\vec{x}$ and using $f\left(\vec{x}\right)$ as the right hand side of the model, ie:
\begin{eqnarray}
f\left(x_{i}\right) = \left(x_{i+1} - x_{i-2}\right)x_{i-1} - x_{i} + F
\\
f\left(\vec{x}\right) = \left\{f\left(x_{1}\right),...,f\left(x_{N}\right)\right\}
\end{eqnarray}
the implementation is given by:
\begin{eqnarray}
\vec{k}_{1}=f\left(\vec{x}\left(t\right)\right)
\\
\vec{k}_{2}=f\left(\vec{x}\left(t\right) + \frac{1}{2}\vec{k}_{1}\Delta t\right)
\\
\vec{k}_{3}=f\left(\vec{x}\left(t\right) + \frac{1}{2}\vec{k}_{2}\Delta t\right)
\\
\vec{k}_{4}=f\left(\vec{x}\left(t\right) + \vec{k}_{3}\Delta t\right)
\end{eqnarray}
and finally
\begin{equation}
\vec{x}\left(t + \Delta t\right) = \vec{x}\left(t\right) + \frac{1}{6}\left(\vec{k}_{1} + 2\vec{k}_{2} + 2 \vec{k}_{3} + \vec{k}_{4}\right)
\end{equation}

#### The Basic Model Interface (BMI)
The basic model interface allows communicating with models in a generic fashion. It requires a few standard methods to be available such as 'initialize()' and 'update()'. Methods that are not relevant for the model need still be implemented, but can simply raise a one line exception. See [ref] for more information. Implementing the BMI allows easy interaction with the model. The cells below initiate one instance of the model. For reasons that will become clear we will call this instance "truthModel".

BMI models are typically initialized with a settings-file. This is overkill here, but for completeness, we generate the settings-file first and than pass it to the model.