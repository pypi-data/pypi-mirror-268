.. eWaterCycle-Lorenz documentation master file, created by
   sphinx-quickstart on Thu Mar  7 10:34:21 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to eWaterCycle-Lorenz's documentation!
===========================================


This package is based on the `Leaky
bucket <https://github.com/eWaterCycle/ewatercycle-leakybucket/tree/main>`__
& is a wrapper for the `lorenz-bmi <https://github.com/Daafip/lorenz-bmi>`__
model designed for the `eWaterCycle <https://ewatercycle.nl/>`_ platform. 

The Lorenz-96 model as defined by Edward Lorenz (in 1996) is known for its chaotic behavior and thus often used in data assimilation.

This is the main reason for implementation on a hydrology platform: to test data assimilation techniques.

Installation
------------

Install this package alongside your eWaterCycle installation

.. code:: console

   pip install ewatercycle-lorenz

Then HBV becomes available as one of the eWaterCycle models

.. code:: python

   from ewatercycle.models import Lorenz

Implementing your own model
---------------------------

For more information on how this plugin works, and on how to implement
your own model see the `plugin
guide <https://github.com/eWaterCycle/ewatercycle-leakybucket/blob/main/plugin_guide.md>`__

Changelog
---------

Changelog can be found `here <https://github.com/Daafip/ewatercycle-lorenz/blob/main/CHANGELOG.md>`__

License
-------

This is a ``ewatercycle-plugin`` & thus this is distributed under the
same terms as the template: the
`Apache-2.0 <https://spdx.org/licenses/Apache-2.0.html>`__ license.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   model
   example_model_run_lorenz
   

