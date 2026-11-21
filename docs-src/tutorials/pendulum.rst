Simple Pendulum
###############

Introduction
============

This is a tutorial for creating a simple pendulum with a point mass attached to a rigid, mass-less beam, which has a
single rotational degree-of-freedom (DOF), and in a uniform gravitational field. The animation below is generated in
MOMDYN at the completion of the tutorial. You can also watch a video demonstration of this tutorial on
`Youtube <https://youtu.be/JSzmP5InGek>`_.

.. image:: ../img/simplePendulum2p0.gif
   :width: 400
   :alt: Animation of the pendulum in a 2-D diagram view

A depiction of this system is shown below, which shows the inertial reference frame with unit vectors **n**\ :sub:`x` \
and **n**\ :sub:`y`\, single angular degree-of-freedom θ, the rotated reference frame with unit vectors
**e**\ :sub:`x` \ and **e**\ :sub:`y` \, the mass *m*, length *l*, and gravitational vector **g**.

.. image:: ../img/pendulum_diagram.png
   :width: 400
   :alt: Schematic depiction of the pendulum

The model is generated using two variations on the kinematics interface, "Classic," and "Joints." The former is akin to
a pencil-and-paper approach, each symbolic parameter is individually named by the user, and each frame, vector, and
point is created using these parameters. The latter is closer to the approach used in modern mulitibody dynamics
software, where lower-level modeling attributes are consolidated into the joint object, reducing the total number of
steps.

.. _create-new:

Create the New Model
--------------------

.. image:: pendulum/01-1.png
   :width: 108
   :alt: Welcome screen

.. image:: pendulum/01-2.png
   :width: 108
   :alt: Create screen

.. image:: pendulum/01-3.png
   :width: 108
   :alt: Create screen, bottom

To begin, from the welcome screen tap the "Create" button, which will bring up a dialog with the title
"Create - Specify Settings." Many of the settings in this dialog can remain with their defaults. The modified
specifications give a model name and description, and creates gravitational force, time, and tolerance. Enter the
following:

  - *model_name*: Pendulum
  - *model_description*: A simple pendulum with a point mass and single angular degree of freedom
  - *gravity_method*: Uniform
  - *gravity_constant*: 9.8
  - *gravity_direction*: -Y
  - *time_duration*: 5
  - *tol*: 0.00001

Tap the green check in the lower right, which will bring up a blank diagram. Tap the save button, as we will be
returning to this stage later in the tutorial.

.. raw:: html

   <hr>

Classic Interface
=================

.. image:: pendulum/02a-1.png
   :width: 108
   :alt: Diagram view, prior to creating symbols

.. image:: pendulum/02a-2.png
   :width: 108
   :alt: Navigation drawer, highlighting classic menu

Here we will use the classic interface, which allows for more direct control over the fundamental building blocks of
the kinematics. The joints interface is more convenient for many applications, as it consolidates functionality of the
building block components into common mechanical joints, and doesn't require individually defining all of the symbols,
reference frames, vectors, and points in the model. If you are interested in using the joints interface, you may
proceed to the :ref:`joints section <joints>`.

Symbols
-------

Length
++++++

.. image:: pendulum/02a-3.png
   :width: 108
   :alt: Classic menu

.. image:: pendulum/02a-4.png
   :width: 108
   :alt: New parameter

Tap the navigation button (three horizontal bars) in the upper left to open the navigation drawer. We will first create
the pendulum using the classic interface. Open the classic menu, and tap the plus sign under **Parameter**, which
will bring up the new parameter dialog. Create a constant for pendulum length with the following specifications

  - *name*: l
  - *value*: 1
  - *description*: length

then tap **Ok** after entering the values for each parameter to create it.

Angular Degree-of-Freedom
+++++++++++++++++++++++++

.. image:: pendulum/02a-3.png
   :width: 108
   :alt: Classic menu

.. image:: pendulum/03a-2.png
   :width: 108
   :alt: New generalized coordinate

Next create the generalized coordinate, *θ*, corresponding to the angular degree of freedom. With the classic menu
open, tap the plus sign under **Generalized Coordinate**, and enter the following specifications

  - *name*: \theta
  - *initial*: 1
  - *description*: angle

noting that when \theta is entered as the name, it will be replaced by the unicode character θ.

Kinematics
----------

Orientation
+++++++++++

.. image:: pendulum/02a-3.png
   :width: 108
   :alt: Classic menu

.. image:: pendulum/04a-2.png
   :width: 108
   :alt: New frame

.. image:: pendulum/04a-3.png
   :width: 108
   :alt: Created frame in the diagram view

Once again, with the classic menu open, tap the plus sign under **Frame**, and enter the following (noting that
line items that are not listed below can retain their default values)

  - *first_angle*: θ(t)

tap **Ok* to create the frame. This will create the new frame rotated by the angle *θ* measured about
the out of plane axis **k**.

Vector
++++++

.. image:: pendulum/02a-3.png
   :width: 108
   :alt: Classic menu

.. image:: pendulum/05a-2.png
   :width: 108
   :alt: New vector

.. image:: pendulum/05a-3.png
   :width: 108
   :alt: Created vector in the diagram view

Next, tap the plus sign under **vector**, and enter the following

  - *name*: r
  - *ref_frame_key*: E
  - *x*: l

and tap **Ok** to create the vector named **r**, aligned with the **e**\ :sub:`x` \ axis of the rotated
frame, with constant length *l*.

Point
+++++

.. image:: pendulum/02a-3.png
   :width: 108
   :alt: Classic menu

.. image:: pendulum/06a-2.png
   :width: 108
   :alt: New point

.. image:: pendulum/06a-3.png
   :width: 108
   :alt: Created point in the diagram view

Finally, tap the plus sign under **Point**, and enter the following

  - vector_key: r

and tap **Ok** to create the point a at the end of the vector *r*. Minimize the edit menu by tapping
the three horizontal lines, at which point you should see the diagram updated to include the frame, vector, and point.

.. raw:: html

   <hr>

.. _joints:

Joints Interface
================

Angular Degree of Freedom
-------------------------

.. image:: pendulum/02b-1.png
   :width: 108
   :alt: Navigation drawer, highlighting joints menu

.. image:: pendulum/02b-2.png
   :width: 108
   :alt: Joints menu

.. image:: pendulum/02b-3.png
   :width: 108
   :alt: New revolute joint

Tap on the welcome tab on the bottom of the screen, then the import button, and select the saved `Pendulum` file,
which will return the model to its state after :ref:`creating the model <create-new>`. Open the navigation drawer, and
the joints menu, then tap the plus sign under **Revolute.** Add the following specifications, leaving line items that
are unlisted at their default value,

  - *name*: E
  - *motion_axis*: +Z
  - *value*: 1

and then tap **Ok** to create the joint. This will create a new frame rotated about the out-of-plane
**k** axis by an angle θ\ :sub:`E` \, similar to the output of step (5a). Notably, the creation of the generalized
coordinate is combined with the generation of a reference frame in a single joint object.

Rigid, Massless Beam
--------------------

.. image:: pendulum/02b-2.png
   :width: 108
   :alt: Joints menu

.. image:: pendulum/03b-2.png
   :width: 108
   :alt: New rigid translation

.. image:: pendulum/06a-3.png
   :width: 108
   :alt: Created revolute joint and rigid translation in the diagram view

Next, tap the plus sign under **Rigid Translation**, and add the following specifications

  - *ref_frame_key*: E
  - *x*: 1

once again tapping **Ok** to create the joint. This will create a new vector ra aligned with the
**e**\ :sub:`x`\ axis with length 1, and a new point *a*, similar to the output of step (7a). Thus, in this example,
the same kinematics definition requiring 5 steps using the classic interface, is completed using two joints.

.. raw:: html

   <hr>

Bodies
======

Point Mass
----------

.. image:: pendulum/07-1.png
   :width: 108
   :alt: Navigation drawer, highlighting the bodies menu

.. image:: pendulum/07-2.png
   :width: 108
   :alt: Bodies menu

.. image:: pendulum/07-3.png
   :width: 108
   :alt: New particle

.. image:: pendulum/07-4.png
   :width: 108
   :alt: Created particle in the diagram view

Expand the bodies panel. Tap on the plus sign under **particle**, and enter the following.

  - *name*: bob
  - *ref_point_key*: a
  - *mass*: 1

which will create the pendulum bob with mass *1* represented by the symbol *m*\ :sub:`bob`\ attached to the point *a*,
as shown above.

.. raw:: html

   <hr>

Analysis
========

Simulation
----------

To generate equations of motion, tap the right-arrow button in the lower left corner of the diagram. Since this is a
very simple model, the derivation run nearly instantaneously. Once complete, the icon will change to the outline of a
play button. Tap again to run the simulation, once again this will be nearly instantaneous. Tap again to play the
animation, which will show the pendulum swinging from right to left with around a 3 second period, as seen previously
at the top of this page.

Model Export
------------

Open the edit menu by tapping the three horizontal lines in the upper left corner, and then tap on the export button.
Tap each of the three line items, Model, Simulation, and Python, to activate them, and then tap the check button in the
lower right to export the files. The Model file (momdyn_model.py) is the format used to import to the MOMDYN app. The
Simulation file (simulation.csv) are the time-series reflecting the generalized coordinates and speeds that are
animated. The Python file (py_model.py) contains code that can be executed and further manipulated on a desktop Python
environment.

.. image:: pendulum/export-1.png
   :width: 108
   :alt: Press the export button in the menu

.. image:: pendulum/export-2.png
   :width: 108
   :alt: Select to export model, simulation, and python

.. image:: pendulum/export-3.png
   :width: 108
   :alt: Exported Python code, shown in the Pyto app

.. image:: pendulum/export-states.png
   :height: 196
   :alt: Plotted states

Report
------

Tap on the report tab in the lower right to open up the report view showing text, equations and plots. The buttons at
the top specify which section of the report to view. From left to right these are symbols, frames, points, bodies,
loads, equations, and plots. The images below show these sections for the Pendulum model, omitting loads as there are
none (except for gravity).

.. image:: pendulum/report-symbols.png
   :width: 108
   :alt: Symbols in the report view

.. image:: pendulum/report-frames.png
   :width: 108
   :alt: Frames in the report view

.. image:: pendulum/report-points.png
   :width: 108
   :alt: Points in the report view

.. image:: pendulum/report-bodies.png
   :width: 108
   :alt: Bodies in the report view

.. image:: pendulum/report-equations.png
   :width: 108
   :alt: Equations in the report view

.. image:: pendulum/report-plots.png
   :width: 108
   :alt: Plots in the report view
