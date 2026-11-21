Mechanism Module
================

The analytical back-end of MOMDYN, referred to here as the "Mechanism module," is implemented using Python, taking
very basic data classes (numeric and string) as user inputs to numerous high-level, object-oriented methods.

.. raw:: html

   <hr>


Classic Interface
-----------------

The classic interface implements several fundamental components for defining kinematics, largely based on the physics
and classical mechanics modules in SymPy. These include constant and time-varying symbols, frames to model orientation,
and vectors and points to model location.

.. toctree::
   :maxdepth: 2

   classic

.. raw:: html

   <hr>


Mechanical Joints
-----------------

Mechanical joints are typical of modern multibody software, and combine attributes of the fundamental objects found in
the classic interface. A good reference to common joint definitions may be found in the documentation for the
open-source Modelica project, in the OpenModelica Mechanics Multibody package. While MOMDYN does not use Modelica
code, I will attempt to use similar terminology and input parameters where applicable.

.. toctree::
   :maxdepth: 2

   joints

.. raw:: html

   <hr>


Bodies
------

Bodies are used to define the mass and inertial properties of the model. The most basic body is a Particle, which is a
mass that is attached to a Point, without an inertia tensor. Basic RigidBody objects are defined, which also have mass
defined at the body's mass-center, and inertia tensors dependent on the body geometry.

.. toctree::
   :maxdepth: 2

   bodies

.. raw:: html

   <hr>


Loads
-----

Loads are the forces and moments that are exerted on points and frames in the model, respectively. These include
external loads, which act on a single point or frame, or external loads that act with equal and opposite amounts on
pairs of points or frames. Additionally, spring behavior can be implemented in translational and rotational forms.


.. toctree::
   :maxdepth: 2

   loads

.. raw:: html

   <hr>


Sensors
--------

Sensors measure translational or rotational motion of points or frames. These generally
parallel a real world sensor used in engineering or physics test laboratories; for example,
linear variable differential transformers can measure the displacement of a point, provided
the motion is predominantly in a single axis and the instrument is in constant contact.
Similarly, laser doppler vibrometers can measure velocity of a point on a surface, provided
the surface is visible to the instrument, and the instrument can be isolated from the
motion of the unit under test. The simulation is not subject to these same real-world
limitations.


.. toctree::
   :maxdepth: 2

   sensors
