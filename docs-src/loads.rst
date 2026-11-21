Loads
=====

Loads are the forces and moments that are exerted on points and frames in the model, respectively.

.. toctree::
   :maxdepth: 2
   :caption: Load Types

   loads/external_force
   loads/actuated_force
   loads/external_moment
   loads/actuated_moment
   loads/translational_spring
   loads/rotational_spring

.. raw:: html

   <hr>


`External Force <loads/external_force.html>`_

An external force acts on a single point, with vector components x, y, and z defined in the reference frame.

.. raw:: html

   <hr>


`Actuated Force <loads/actuated_force.html>`_

An actuated force acts with equal and opposite magnitude on two points, with vector components x, y, and z defined in the reference frame.

.. raw:: html

   <hr>


`External Moment <loads/external_moment.html>`_

An external moment acts on a single frame, about a vector with components x, y, and z defined in the reference frame.

.. raw:: html

   <hr>


`Actuated Moment <loads/actuated_moment.html>`_

An actuated moment acts with equal and opposite magnitude on two frames, about a vector with components x, y, and z defined in the reference frame.

.. raw:: html

   <hr>


`Translational Spring <loads/translational_spring.html>`_

A translational spring/damper induces an attractive force between two points that is colinear with a vector drawn from the start to end point. The force magnitude is

    F = k (x - e) + c x'

where k is the spring stiffness, x is the distance between the two points, e is an equilibrium length of the spring, c is the damping constant, and x' is the differential speed between the two points.

.. raw:: html

   <hr>


`Rotational Spring <loads/rotational_spring.html>`_

A rotational spring/damper induces an attractive moment between two frames about the rotation axis corresponding to the relative orientation of the frames. The moment magnitude is

    M = k θ + c θ'

where k is the spring stiffness, θ is the angle between the two frames, c is the damping constant, and θ' is the differential angular speed between the two frames.

.. raw:: html

   <hr>
