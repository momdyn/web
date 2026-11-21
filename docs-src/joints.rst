Joints
======

Mechanical joints are typical of modern multibody software, and combine attributes of the fundamental objects found in the classic interface. A good reference to common joint definitions may be found in the documentation for the open-source Modelica project, in the OpenModelica Mechanics Multibody package. While MOMDYN does not use Modelica  code, I will attempt to use similar terminology and input parameters where applicable.

.. toctree::
   :maxdepth: 2
   :caption: Joint Types:

   joints/rigid_translation
   joints/rigid_rotation
   joints/prismatic
   joints/revolute
   joints/cylindrical
   joints/universal
   joints/spherical
   joints/planar
   joints/free_motion

.. raw:: html

   <hr>


`Rigid Translation <joints/rigid_translation.html>`_

.. image:: img/rigidtranslation.jpg
   :width: 128
   :alt: Depiction of a rigid translation

A rigid translation creates a point that is translated relative to an existing point with vector components defined in a specified reference frame. The rigid translation is analogous to creating a vector and point using the classic interface.

.. raw:: html

   <hr>


`Rigid Rotation <joints/rigid_rotation.html>`_

.. image:: img/rigidrotation.jpg
   :width: 128
   :alt: Depiction of a rigid rotation

A rigid rotation creates a frame that is oriented relative to an existing frame by a Euler angle sequence.

.. raw:: html

   <hr>


`Prismatic Joint <joints/prismatic.html>`_

.. image:: img/prismatic.jpg
   :width: 128
   :alt: Depiction of a prismatic joint

A prismatic joint creates a point that is translated relative to an existing point with vector components defined in a specified reference frame. The joint is analogous to creating a vector and point using the classic interface. The vector component can be constant valued, or a degree of freedom (DOF) may be generated where the point can translate in the unit vector direction. If the DOF form is chosen, then an optional linear stiffness, damping, and equilibrium distance can be used to include translational spring-damper physics in the joint.

.. raw:: html

   <hr>


`Revolute Joint <joints/revolute.html>`_

.. image:: img/revolute.jpg
   :width: 128
   :alt: Depiction of a revolute joint

A revolute joint creates a frame that is rotated relative to an existing frame about an axis defined in a specified reference frame. The angular component can be constant valued, or a degree of freedom (DOF) may be generated. If the DOF form is chosen, then an optional rotational stiffness, damping, and equilibrium angle can be used to include rotational spring-damper physics in the joint.

.. raw:: html

   <hr>


`Cylindrical Joint <joints/cylindrical.html>`_

.. image:: img/cylindrical.jpg
   :width: 128
   :alt: Depiction of a cylindrical joint

A cylindrical joint creates a point that is translated along an axis defined in the reference frame, and a frame that is rotated relative to an existing frame about the same axis.

.. raw:: html

   <hr>


`Universal Joint <joints/universal.html>`_

.. image:: img/universal.jpg
   :width: 128
   :alt: Depiction of a universal joint

A universal joint creates a frame that is rotated relative to an existing frame using a two angles to define its orientation.

.. raw:: html

   <hr>


`Spherical Joint <joints/spherical.html>`_

.. image:: img/spherical.jpg
   :width: 128
   :alt: Depiction of a spherical joint

A spherical joint creates a frame that is rotated relative to an existing frame using a quaternion to define its orientation. Initial quaternion values are defined using an equivalent Euler angle sequence. The components can be constant valued, or a three degrees of freedom (DOF) form may be generated.

.. raw:: html

   <hr>


`Planar Joint <joints/planar.html>`_

.. image:: img/planar.jpg
   :width: 128
   :alt: Depiction of a planar joint

A planar joint creates a point that is translated by two components coordinates defined in the reference frame, and a frame that is rotated relative to an existing frame about an axis that is normal to the two components. The components can be constant valued, or a three degrees of freedom (DOF) form may be generated. If the DOF form is chosen, then optional stiffness, damping, and equilibrium coefficients can be used to include translational and rotational spring-damper physics in the joint.

.. raw:: html

   <hr>


`Free Motion Joint <joints/free_motion.html>`_

.. image:: img/freemotion.jpg
   :width: 128
   :alt: Depiction of a free motion joint

A free motion joint creates a point that is translated by three components coordinates defined in the reference frame, and a frame that is rotated relative to an existing frame using a quaternion to define its orientation. Initial quaternion values are defined using an equivalent Euler angle sequence. The components can be constant valued, or a six degrees of freedom (DOF) form may be generated. If the DOF form is chosen, then optional stiffness, damping, and equilibrium coefficients can be used to include translational and rotational spring-damper physics in the joint.

.. raw:: html

   <hr>
