Classic
=======

The classic interface implements several fundamental components for defining kinematics, largely based on the physics and classical mechanics modules in SymPy. A few of the objects that are used in MOMDYN are:

* `symbols <https://docs.sympy.org/latest/modules/core.html#module-sympy.core.symbol>`_
* `dynamicsymbols <https://docs.sympy.org/latest/modules/physics/vector/api/functions.html>`_
* `ReferenceFrame <https://docs.sympy.org/latest/modules/physics/vector/api/classes.html>`_
* `Vector <https://docs.sympy.org/latest/modules/vector/api/classes.html#vector>`_
* `Point <https://docs.sympy.org/latest/modules/geometry/points.html>`_
* `Particle <https://docs.sympy.org/latest/modules/physics/mechanics/api/part_bod.html>`_
* `RigidBody <https://docs.sympy.org/latest/modules/physics/mechanics/api/part_bod.html#module-sympy.physics.mechanics.rigidbody>`_
* `inertia <https://docs.sympy.org/latest/modules/physics/mechanics/api/part_bod.html#inertia>`_
* `KanesMethod <https://docs.sympy.org/latest/modules/physics/mechanics/kane.html>`_

MOMDYN provides a front-end interface for interacting with these data types, creating a "Mechanism" object that acts as a container for the various types, and uses them to generate bodies and loads. These are passed to the KanesMethod object to generate equations of motion, simulated using custom numerical algorithms, and reported in text and plot form. The following components are implemented in the classic interface:

.. toctree::
   :maxdepth: 2
   :caption: Classic Types:

   classic/parameter
   classic/generalized_coordinate
   classic/generalized_speed
   classic/frame
   classic/vector
   classic/point

.. raw:: html

   <hr>


`Parameter <classic/parameter.html>`_

Front-end for SymPy `symbols` type

A parameter is a symbolic variable used to represent constants in the model. Typical uses are fixed lengths or angles in vector or frame definitions, mass properties, or spring stiffness and damping.

.. raw:: html

   <hr>


`Generalized Coordinate <classic/generalized_coordinate.html>`_

Front-end for SymPy `dynamicsymbols` type

A generalized coordinate is a symbolic variable representing the mechanism configuration, typically as either a length or angular dimension. It is time-varying, and is alternately termed a degree of freedom. When using the classic interface, the generalized coordinate dialog is used to create the symbolic variable, which is later selected in the frame or vector dialogs as a dimension.

.. raw:: html

   <hr>


`Generalized Speed <classic/generalized_speed.html>`_

Front-end for SymPy `dynamicsymbols` type

A generalized speed is a symbolic variable representing the mechanism motion. It is common to equate a generalized speed to the first derivative of a corresponding generalized speed with respect to time, however, this is not required. In fact, a more compact form of equations of motion are often obtained by using an alternate set of generalized speeds, for example, in free motion of a rigid body it is common to define generalized coordinates as positions relative to the origin in the inertial frame, with generalized speeds being the velocity components in the body-fixed frame.

.. raw:: html

   <hr>


`Frame <classic/frame.html>`_

Front-end for SymPy `ReferenceFrame` type

A reference frame is a set of three orthonormal basis vectors which are rotated relative to the inertial frame, or some intermediate frame.

.. raw:: html

   <hr>


`Vector <classic/vector.html>`_

Front-end for SymPy `Vector` type

Create a vector using an existing reference frame and specified distances.

.. raw:: html

   <hr>


`Point <classic/point.html>`_

Front-end for SymPy `Point` type

A point has a location, velocity, and acceleration relative to the inertial reference frame. Points are used to define interfaces between multiple parts in the mechanism, to position bodies (masses and inertias), or as locations of applied forces.

.. raw:: html

   <hr>
