Bodies
======

Bodies are used to define the mass and inertial properties of the model. The most basic body is a Particle, which is a mass that is attached to a Point, without an inertia tensor. Basic RigidBody objects are defined, which also have mass defined at the body's mass-center, and inertia tensors dependent on the body geometry.

.. toctree::
   :maxdepth: 2
   :caption: Body Types:

   bodies/particle
   bodies/general_rigid_body
   bodies/rigid_body_box
   bodies/rigid_body_cone
   bodies/rigid_body_cylinder

.. raw:: html

   <hr>


`Particle <bodies/particle.html>`_

.. image:: img/particle.jpg
   :width: 128
   :alt: Depiction of a particle

A particle is a mass that is fixed to a point, with no inertia tensor.

.. raw:: html

   <hr>


`General Rigid Body <bodies/general_rigid_body.html>`_

.. image:: img/generalrigidbody.jpg
   :width: 128
   :alt: Depiction of a general rigid body

A general rigid body has its center of gravity (CG) located at a user-specified point and orientation defined in a specified frame, a fixed mass, and specified inertia tensor.

.. raw:: html

   <hr>


`Rigid Body Box <bodies/rigid_body_box.html>`_

.. image:: img/rigidbodybox.jpg
   :width: 128
   :alt: Depiction of a rigid body box

A rigid body box is a rectangular prism of uniform density. The box has length defined in the X-axis, width defined in the Y-axis, and height defined in the Z-axis, where (X, Y, Z) are the basis vectors of the body fixed frame.

.. raw:: html

   <hr>


`Rigid Body Cylinder <bodies/rigid_body_cylinder.html>`_

.. image:: img/rigidbodycylinder.jpg
   :width: 128
   :alt: Depiction of a rigid body cylinder

A rigid body cylinder is a circular rod of uniform density. The cylinder has length defined in the X-axis, and radius for the Y- anc Z-axes, where (X, Y, Z) are the basis vectors of the body fixed frame.

.. raw:: html

   <hr>


`Rigid Body Cone <bodies/rigid_body_cone.html>`_

.. image:: img/rigidbodycone.jpg
   :width: 128
   :alt: Depiction of a rigid body cone

A rigid body cone is a circular cone of uniform density. The cone has length defined in the X-axis, and radius for the Y- anc Z-axes, where (X, Y, Z) are the basis vectors of the body fixed frame.

.. raw:: html

   <hr>
