.. seo::
   :title: Mass-Spring-Damper Tutorial – Equation of Motion | MOMDYN
   :description: Build a mass-spring-damper in MOMDYN on iPhone or iPad, the basic model of linear vibration, then derive its equation of motion and export Python.
   :type: howto

Mass-Spring-Damper
##################

Introduction
============

This tutorial builds a mass-spring-damper in a uniform gravitational field, the fundamental problem of linear vibration. By the end you will have derived its equation of motion, simulated it and exported it as Python.

.. video:: oscillator/oscillator.mp4
   :width: 400
   :alt: Animation of the finished mass bouncing on its spring in the 2-D diagram view

.. admonition:: Two ways to build the same model

   MOMDYN has two kinematics interfaces, and they build exactly the same oscillator. You only need one of them.
   `Path A: Classic <#path-a-classic-interface>`__ is like a pencil-and-paper derivation: you create a coordinate, a vector, a point and a spring one at a time.
   `Path B: Joints <#path-b-joints-interface>`__ replaces those four steps with one prismatic joint.
   Both paths start at `Step 1 <#step-1-create-the-new-model>`__ and continue at `Step 6 <#step-6-add-the-point-mass>`__.

Set up the model
================

Step 1: Create the new model
----------------------------

.. image:: oscillator/01-1.png
   :width: 108
   :alt: The Welcome screen with the Create, Import and Help buttons

.. image:: oscillator/01-2.png
   :width: 108
   :alt: The top of the Create settings dialog with the model name and description fields

.. image:: oscillator/01-3.png
   :width: 108
   :alt: The bottom of the Create settings dialog with the gravity, time and tolerance fields

From the Welcome screen, tap **Create**. A dialog titled "Create - Specify Settings" opens (see the `settings reference <../create_dialog.html>`__). Most settings can keep their defaults. Enter the following:

  - *model_name*: Oscillator
  - *model_description*: Simple mass-spring-damper as is common in linear vibration analysis
  - *gravity_method*: Uniform
  - *gravity_constant*: 9.8
  - *gravity_direction*: -Y
  - *time_duration*: 5
  - *tol*: 0.00001

Tap the green check in the lower right to create the model. Then save it (menu drawer, then Export, with **Save File** on), because the Joints path returns to this point.

Path A: Classic interface
=========================

The Classic interface gives direct control over the building blocks of the kinematics. Here you define a generalized coordinate for the displacement, attach it to a vector, create a point at the end of that vector, and connect the origin and that point with a spring. If you prefer fewer steps, jump to `Path B: Joints <#path-b-joints-interface>`__.

Step 2: Create the displacement coordinate
------------------------------------------

.. image:: oscillator/02a-1.png
   :width: 108
   :alt: The navigation drawer with the Classic menu highlighted

.. image:: oscillator/02a-2.png
   :width: 108
   :alt: The Classic menu with a plus button under Generalized Coordinate

.. image:: oscillator/02a-3.png
   :width: 108
   :alt: The New Generalized Coordinate dialog filled in with name h, initial value 1 and description displacement

Open the navigation drawer, then the **Classic** menu. Tap the plus sign under **Generalized Coordinate** and enter

  - *name*: h
  - *initial*: 1
  - *description*: displacement

and tap **Ok**. This creates the displacement :math:`h(t)`, the model's one translational DOF. The spring's stiffness, damping and equilibrium constants are created automatically with the spring in Step 5. See `Generalized Coordinate <../classic/generalized_coordinate.html>`__.

Step 3: Create the vector
-------------------------

.. image:: oscillator/02a-1.png
   :width: 108
   :alt: The navigation drawer with the Classic menu highlighted

.. image:: oscillator/06a-2.png
   :width: 108
   :alt: The New Vector dialog with name h and y set to h(t)

.. image:: oscillator/06a-3.png
   :width: 108
   :alt: The new vector drawn as a gray line along the vertical axis of the diagram

With the Classic panel open, tap the plus sign under **Vector** and enter

  - *name*: h
  - *y*: h(t)

and tap **Ok**. This creates the vector :math:`\mathbf{h}` along the :math:`\mathbf{j}` (y) axis of the inertial frame, with a length equal to the coordinate :math:`h`. Return to the diagram to see it as a gray line. See `Vector <../classic/vector.html>`__.

Step 4: Create the point
------------------------

.. image:: oscillator/07a-1.png
   :width: 108
   :alt: The Classic menu with a plus button under Point

.. image:: oscillator/07a-2.png
   :width: 108
   :alt: The New Point dialog with vector_key set to h

.. image:: oscillator/07a-3.png
   :width: 108
   :alt: The new point drawn as a blue sphere at the end of the vector

Tap the plus sign under **Point** and enter

  - *vector_key*: h

and tap **Ok** to create point *a* at the end of the vector :math:`\mathbf{h}`. In the diagram, the point is a blue sphere. See `Point <../classic/point.html>`__.

Step 5: Add the translational spring
------------------------------------

.. image:: oscillator/08a-1.png
   :width: 108
   :alt: The navigation drawer with the Loads menu highlighted

.. image:: oscillator/08a-2.png
   :width: 108
   :alt: The Loads menu with a plus button under Translational Spring

.. image:: oscillator/08a-3.png
   :width: 108
   :alt: The New Translational Spring dialog with end_point a, k 50, c 1 and equilibrium 1

.. image:: oscillator/08a-4.png
   :width: 108
   :alt: The spring drawn between the origin and the point in the diagram view

The only load in this model is a spring-damper between the origin and the point. Open the navigation drawer, then the **Loads** menu, and tap the plus sign under **Translational Spring**. Enter

  - *end_point*: a
  - *k*: 50
  - *c*: 1
  - *equilibrium*: 1

and tap **Ok**. MOMDYN also creates the parameters :math:`k_{O/a}`, :math:`c_{O/a}` and :math:`e_{O/a}` for the stiffness, damping and equilibrium length. The spring appears between the two points. See `Translational Spring <../loads/translational_spring.html>`__. Continue at `Step 6 <#step-6-add-the-point-mass>`__.

Path B: Joints interface
========================

The Joints interface consolidates the building blocks into common mechanical joints. Here the displacement coordinate, the vector, the point and the spring all live in one prismatic joint.

Step 2 (Joints path): Add a prismatic joint
-------------------------------------------

.. image:: oscillator/02b-1.png
   :width: 108
   :alt: The navigation drawer with the Joints menu highlighted

.. image:: oscillator/02b-2.png
   :width: 108
   :alt: The Joints menu with a plus button under Prismatic

.. image:: oscillator/02b-3.png
   :width: 108
   :alt: The New Prismatic joint dialog with y 1, value 1, k 50, c 1 and equilibrium 1

Tap the **Welcome** tab at the bottom of the screen, then **Import**, and choose the saved *Oscillator* model. This returns the model to its state after `Step 1 <#step-1-create-the-new-model>`__. Open the navigation drawer, open the **Joints** menu and tap the plus sign under **Prismatic**. Enter (items not listed keep their defaults)

  - *y*: 1
  - *value*: 1
  - *k*: 50
  - *c*: 1
  - *equilibrium*: 1

and tap **Ok**. The diagram shows the same point and spring as the Classic path. See `Prismatic Joint <../joints/prismatic.html>`__.

Add the mass
============

Step 6: Add the point mass
--------------------------

.. image:: oscillator/10-1.png
   :width: 108
   :alt: The navigation drawer with the Bodies menu highlighted

.. image:: oscillator/10-2.png
   :width: 108
   :alt: The Bodies menu with a plus button under Particle

.. image:: oscillator/10-3.png
   :width: 108
   :alt: The New Particle dialog with name bob, ref_point_key a and mass 1

.. image:: oscillator/10-4.png
   :width: 108
   :alt: The particle drawn as a green and black sphere at the end of the spring

A single particle (a point mass) is attached to the created point. Its inertial force is proportional to its mass times its acceleration. Open the navigation drawer and the **Bodies** menu, tap the plus sign under **Particle**, and enter

  - *name*: bob
  - *ref_point_key*: a
  - *mass*: 1

This creates the bob with mass 1 at point *a*, and the parameter :math:`m_{bob}`. See `Particle <../bodies/particle.html>`__.

Simulate and analyze
====================

Step 7: Derive the equations and simulate
-----------------------------------------

On the Diagram tab, tap the right-arrow button in the lower left to derive the equations of motion. This model is small, so the derivation runs nearly instantly, and the icon changes to the outline of a play button. Tap again to run the simulation, and once more to play the animation. The mass bounces with a period of about 0.9 seconds, as in the animation at the top of this page. The on-screen controls are described in `On-Screen Controls <../on_screen_controls.html>`__.

Step 8: Export the model
------------------------

.. image:: oscillator/export-1.png
   :width: 108
   :alt: The Export button in the menu drawer

.. image:: oscillator/export-2.png
   :width: 108
   :alt: The Export screen with switches for the model file, the Python file and the simulation data

.. image:: oscillator/export-3.png
   :width: 108
   :alt: The exported Python code opened in the Pyto app

.. image:: oscillator/export-states.png
   :height: 196
   :alt: A plot of the oscillator's displacement and speed against time

Open the menu drawer and tap **Export**. Switch on the items you want, then export:

  - **Save File** (``model.py``): the model, in the format MOMDYN imports.
  - **Python File** (``python_model.py``): code you can run and extend on a desktop Python environment.
  - **Tabular Data** (``simulation.csv``): the time series of the generalized coordinates and speeds that drive the animation.
  - **Plot Images** (``plots.pdf``): plots of the simulation results.

See `Import/Export <../save.html>`__ for the file formats.

Step 9: Read the report
-----------------------

Tap the **Report** tab to see the model as text, equations and plots. The buttons at the top choose the section: symbols, frames, points, bodies, loads, equations and plots. The images show these sections for the oscillator (there are no frames other than the inertial frame).

.. image:: oscillator/report-symbols.png
   :width: 108
   :alt: The Symbols section of the report, listing the displacement, the mass, the stiffness, the damping and the equilibrium length

.. image:: oscillator/report-points.png
   :width: 108
   :alt: The Points section of the report, listing the origin and point a

.. image:: oscillator/report-bodies.png
   :width: 108
   :alt: The Bodies section of the report, listing the particle bob

.. image:: oscillator/report-loads.png
   :width: 108
   :alt: The Loads section of the report, listing the translational spring between the origin and point a

.. image:: oscillator/report-equations.png
   :width: 108
   :alt: The Equations section of the report, showing the mass matrix and the forcing vector

.. image:: oscillator/report-plots.png
   :width: 108
   :alt: The Plots section of the report, showing the displacement and speed over time

What you built
==============

The model has one coordinate :math:`h`, one particle of mass :math:`m`, gravity :math:`g` in the :math:`-y` direction, and one spring-damper with stiffness :math:`k`, damping :math:`c` and equilibrium length :math:`e`. Its equation of motion is

.. math::

   m\,\ddot{h} + c\,\dot{h} + k\,(h - e) + m\,g = 0

With :math:`m = 1`, :math:`k = 50`, :math:`c = 1`, :math:`e = 1` and :math:`g = 9.8`, the natural frequency is :math:`\omega_n = \sqrt{k/m} \approx 7.07` rad/s, and the damped period is :math:`2\pi / \sqrt{k/m - (c/2m)^2} \approx 0.89` s. The mass starts at the spring's equilibrium length, so gravity pulls it down and it oscillates around the static equilibrium :math:`h = e - m g / k \approx 0.80` m.

Exported Python
===============

The Python File export contains the equations of motion and a short simulation script. This is an excerpt:

.. TODO (owner): replace the placeholder below with a short excerpt of python_model.py exported from this oscillator.

.. pycode::
   :caption: python_model.py (placeholder excerpt)

   # TODO (owner): paste a short excerpt of the exported oscillator code here
   # (the equations of motion and the simulation call).

Next steps
==========

Reference pages for the components used here: `Generalized Coordinate <../classic/generalized_coordinate.html>`__, `Vector <../classic/vector.html>`__, `Point <../classic/point.html>`__, `Translational Spring <../loads/translational_spring.html>`__, `Prismatic Joint <../joints/prismatic.html>`__ and `Particle <../bodies/particle.html>`__.

.. appcta::
   :next: /docs/tutorials/pendulum/ | Simple Pendulum
