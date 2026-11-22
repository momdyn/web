.. seo::
   :title: Mechanism Module Reference – Multibody Dynamics Components | MOMDYN
   :description: Reference for the MOMDYN Mechanism module: Classic types, joints, bodies, loads and sensors, with every parameter, equation and sign convention.
   :type: techarticle

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

Features
--------

Numeric and string input definition
+++++++++++++++++++++++++++++++++++

The mobile implementation requires simplification of the user input commensurate with the limited interaction
capability provided by a mobile device compared to a desktop workstation. Many high-level methods available in open
source software have been re-structured in MOMDYN such that their inputs can be defined using only numeric and string
variables.

New/edit/delete methods
+++++++++++++++++++++++

Each object implemented in the Mechanism module has a "new," "edit," and "delete" method.

Embedded documentation
++++++++++++++++++++++

Each object implemented in the Mechanism module has documentation that can be accessed from the front-end interface.

Equation of motion generation
+++++++++++++++++++++++++++++

Once the kinematic and dynamic relations are defined in the Mechanism module, equations relating the generalized
coordinates to generalized speeds, equilibrium conditions, mass and forcing matrix are automatically derived. These can
be displayed in the front-end, or exported to human-readable source code or typeset reports.

Simulation
++++++++++

Commonly used open-source numerical integration algorithms necessary for simulation of dynamic systems have been
implemented in architectures that cannot be compiled on mobile device. MOMDYN includes a custom simulation routine that
can be built on all devices.

Automated code generation
+++++++++++++++++++++++++

Complex dynamics models created in MOMDYN require interactivity with desktop workstations or high performance computing
systems to execute fast and/or high volume analysis. The Mechanism module provides an interface to automatically
generate human-readable source code in Python formats that can be transferred to these systems.
