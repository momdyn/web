.. seo::
   :title: Simple Pendulum Tutorial – Derive Equations of Motion | MOMDYN
   :description: Build a simple pendulum in MOMDYN on iPhone or iPad, derive its equation of motion, simulate it and export Python, using the Classic or Joints interface.
   :type: howto

Simple Pendulum
###############

Introduction
============

This tutorial builds a simple pendulum: a point mass on a rigid, massless rod, with one rotational degree of freedom (DOF), in a uniform gravitational field. By the end you will have derived its equation of motion, simulated it and exported it as Python.

.. video:: ../img/simplePendulum2p0.mp4
   :width: 400
   :alt: Animation of the finished pendulum swinging in the 2-D diagram view

The figure below shows the system: the inertial frame with unit vectors :math:`\mathbf{n}_x` and :math:`\mathbf{n}_y`, the angle :math:`\theta`, the rotated frame with unit vectors :math:`\mathbf{e}_x` and :math:`\mathbf{e}_y`, the mass :math:`m`, the rod length :math:`l`, and the gravity vector :math:`\mathbf{g}`.

.. image:: ../img/pendulum_diagram.png
   :width: 400
   :alt: Schematic of the pendulum: a mass m on a rod of length l, at angle theta from the horizontal x axis, with gravity g pointing down

.. admonition:: Two ways to build the same model

   MOMDYN has two kinematics interfaces, and they build exactly the same pendulum. You only need one of them.
   `Path A: Classic <#path-a-classic-interface>`__ is like a pencil-and-paper derivation: you name each parameter, then create the frame, vector and point from them.
   `Path B: Joints <#path-b-joints-interface>`__ is closer to other multibody software: a revolute joint and a rigid translation replace those five steps with two.
   Both paths start at `Step 1 <#step-1-create-the-new-model>`__ and continue at `Step 7 <#step-7-add-the-point-mass>`__.

Set up the model
================

Step 1: Create the new model
----------------------------

.. image:: pendulum/01-1.png
   :width: 108
   :alt: The Welcome screen with the Create, Import and Help buttons

.. image:: pendulum/01-2.png
   :width: 108
   :alt: The top of the Create settings dialog with the model name and description fields

.. image:: pendulum/01-3.png
   :width: 108
   :alt: The bottom of the Create settings dialog with the gravity, time and tolerance fields

From the Welcome screen, tap **Create**. A dialog titled "Create - Specify Settings" opens (see the `settings reference <../create_dialog.html>`__). Most settings can keep their defaults. Enter the following:

  - *model_name*: Pendulum
  - *model_description*: A simple pendulum with a point mass and single angular degree of freedom
  - *gravity_method*: Uniform
  - *gravity_constant*: 9.8
  - *gravity_direction*: -Y
  - *time_duration*: 5
  - *tol*: 0.00001

Tap the green check in the lower right. A blank diagram opens. Save the model now (menu drawer, then Export, with **Save File** on), because the Joints path returns to this point.

Path A: Classic interface
=========================

.. image:: pendulum/02a-1.png
   :width: 108
   :alt: The empty diagram view before any symbols are created

.. image:: pendulum/02a-2.png
   :width: 108
   :alt: The navigation drawer with the Classic menu highlighted

The Classic interface gives direct control over the building blocks of the kinematics. If you prefer fewer steps, jump to `Path B: Joints <#path-b-joints-interface>`__.

Step 2: Create the length parameter
-----------------------------------

.. image:: pendulum/02a-3.png
   :width: 108
   :alt: The Classic menu with a plus button under Parameter

.. image:: pendulum/02a-4.png
   :width: 108
   :alt: The New Parameter dialog filled in with name l, value 1 and description length

Tap the menu button (three horizontal bars) in the upper left to open the navigation drawer, open the **Classic** menu and tap the plus sign under **Parameter**. Enter

  - *name*: l
  - *value*: 1
  - *description*: length

and tap **Ok**. This creates the rod length :math:`l` as a constant. See `Parameter <../classic/parameter.html>`__.

Step 3: Create the angle coordinate
-----------------------------------

.. image:: pendulum/02a-3.png
   :width: 108
   :alt: The Classic menu with a plus button under Generalized Coordinate

.. image:: pendulum/03a-2.png
   :width: 108
   :alt: The New Generalized Coordinate dialog filled in with name theta, initial value 1 and description angle

With the Classic menu open, tap the plus sign under **Generalized Coordinate** and enter

  - *name*: \\theta
  - *initial*: 1
  - *description*: angle

Entering ``\theta`` creates the symbol :math:`\theta`. The initial value of 1 radian is the starting angle. See `Generalized Coordinate <../classic/generalized_coordinate.html>`__.

Step 4: Create the rotated frame
--------------------------------

.. image:: pendulum/02a-3.png
   :width: 108
   :alt: The Classic menu with a plus button under Frame

.. image:: pendulum/04a-2.png
   :width: 108
   :alt: The New Frame dialog with first_angle set to theta(t)

.. image:: pendulum/04a-3.png
   :width: 108
   :alt: The new rotated frame drawn at the origin of the diagram view

Tap the plus sign under **Frame** and enter (items not listed keep their defaults)

  - *first_angle*: θ(t)

and tap **Ok** to create the frame. It is rotated by the angle :math:`\theta` about the out-of-plane axis :math:`\mathbf{k}`. See `Frame <../classic/frame.html>`__.

Step 5: Create the rod vector
-----------------------------

.. image:: pendulum/05a-2.png
   :width: 108
   :alt: The New Vector dialog with name r, ref_frame_key E and x set to l

.. image:: pendulum/05a-3.png
   :width: 108
   :alt: The new vector drawn as a gray line along the x axis of the rotated frame

Tap the plus sign under **Vector** and enter

  - *name*: r
  - *ref_frame_key*: E
  - *x*: l

and tap **Ok**. This creates the vector :math:`\mathbf{r}`, along the :math:`\mathbf{e}_x` axis of the rotated frame, with the constant length :math:`l`. See `Vector <../classic/vector.html>`__.

Step 6: Create the point
------------------------

.. image:: pendulum/06a-2.png
   :width: 108
   :alt: The New Point dialog with vector_key set to r

.. image:: pendulum/06a-3.png
   :width: 108
   :alt: The diagram showing the rotated frame, the rod vector and the new point at its end

Tap the plus sign under **Point** and enter

  - *vector_key*: r

and tap **Ok** to create point *a* at the end of the vector :math:`\mathbf{r}`. Close the edit menu with the three bars: the diagram now shows the frame, the vector and the point. See `Point <../classic/point.html>`__. Continue at `Step 7 <#step-7-add-the-point-mass>`__.

Path B: Joints interface
========================

The Joints interface consolidates the building blocks into common mechanical joints, so you do not have to create each symbol, frame, vector and point yourself.

Step 2 (Joints path): Add a revolute joint
------------------------------------------

.. image:: pendulum/02b-1.png
   :width: 108
   :alt: The navigation drawer with the Joints menu highlighted

.. image:: pendulum/02b-2.png
   :width: 108
   :alt: The Joints menu with a plus button under Revolute

.. image:: pendulum/02b-3.png
   :width: 108
   :alt: The New Revolute joint dialog with name E, motion_axis +Z and value 1

Tap the **Welcome** tab at the bottom of the screen, then **Import**, and choose the saved *Pendulum* model. This returns the model to its state after `Step 1 <#step-1-create-the-new-model>`__. Open the navigation drawer, open the **Joints** menu and tap the plus sign under **Revolute**. Enter (items not listed keep their defaults)

  - *name*: E
  - *motion_axis*: +Z
  - *value*: 1

and tap **Ok**. This creates a frame rotated about the out-of-plane :math:`\mathbf{k}` axis by the angle :math:`\theta_E`, the same result as Steps 3 and 4 above. The joint creates the generalized coordinate and the frame in a single object. See `Revolute Joint <../joints/revolute.html>`__.

Step 3 (Joints path): Add a rigid translation
---------------------------------------------

.. image:: pendulum/02b-2.png
   :width: 108
   :alt: The Joints menu with a plus button under Rigid Translation

.. image:: pendulum/03b-2.png
   :width: 108
   :alt: The New Rigid Translation dialog with ref_frame_key E and x set to 1

.. image:: pendulum/03b-3.png
   :width: 108
   :alt: The diagram showing the revolute joint frame, a rod along its x axis and a point at the end of the rod

.. TODO (owner): 03b-3 is an older screenshot, ported from the old docs for the end of the Joints path. Reshoot it in the current iOS app.

Tap the plus sign under **Rigid Translation** and enter

  - *ref_frame_key*: E
  - *x*: 1

and tap **Ok**. This creates a vector along the :math:`\mathbf{e}_x` axis of length 1 and a new point *a*, the same result as Steps 5 and 6 above. The kinematics that took five steps in the Classic interface took two joints here. See `Rigid Translation <../joints/rigid_translation.html>`__.

Add the mass
============

Step 7: Add the point mass
--------------------------

.. image:: pendulum/07-1.png
   :width: 108
   :alt: The navigation drawer with the Bodies menu highlighted

.. image:: pendulum/07-2.png
   :width: 108
   :alt: The Bodies menu with a plus button under Particle

.. image:: pendulum/07-3.png
   :width: 108
   :alt: The New Particle dialog with name bob, ref_point_key a and mass 1

.. image:: pendulum/07-4.png
   :width: 108
   :alt: The particle drawn as a sphere at the end of the pendulum rod

Open the **Bodies** panel and tap the plus sign under **Particle**. Enter

  - *name*: bob
  - *ref_point_key*: a
  - *mass*: 1

This creates the pendulum bob with mass 1, represented by the symbol :math:`m_{bob}`, attached to point *a*. See `Particle <../bodies/particle.html>`__.

Simulate and analyze
====================

Step 8: Derive the equations and simulate
-----------------------------------------

On the Diagram tab, tap the right-arrow button in the lower left to derive the equations of motion. This model is small, so the derivation runs nearly instantly, and the icon changes to the outline of a play button. Tap again to run the simulation, which is also nearly instant, and tap once more to play the animation. The pendulum starts 1 radian above the horizontal and swings down through the vertical, with a period of about 3.4 seconds, as in the animation at the top of this page. The on-screen controls are described in `On-Screen Controls <../on_screen_controls.html>`__.

Step 9: Export the model
------------------------

.. image:: pendulum/export-1.png
   :width: 108
   :alt: The Export button in the menu drawer

.. image:: pendulum/export-2.png
   :width: 108
   :alt: The Export screen with switches for the model file, the Python file and the simulation data

.. image:: pendulum/export-3.png
   :width: 108
   :alt: The exported Python code opened in the Pyto app

.. image:: pendulum/export-states.png
   :height: 196
   :alt: A plot of the pendulum's angle and angular rate against time

Open the menu drawer and tap **Export**. Switch on the items you want, then export:

  - **Save File** (``model.py``): the model, in the format MOMDYN imports.
  - **Python File** (``python_model.py``): code you can run and extend on a desktop Python environment.
  - **Tabular Data** (``simulation.csv``): the time series of the generalized coordinates and speeds that drive the animation.
  - **Plot Images** (``plots.pdf``): plots of the simulation results.

See `Import/Export <../save.html>`__ for the file formats.

Step 10: Read the report
------------------------

Tap the **Report** tab to see the model as text, equations and plots. The buttons at the top choose the section: symbols, frames, points, bodies, loads, equations and plots. The images show these sections for the pendulum (there are no loads other than gravity).

.. image:: pendulum/report-symbols.png
   :width: 108
   :alt: The Symbols section of the report, listing the length, the angle and the mass

.. image:: pendulum/report-frames.png
   :width: 108
   :alt: The Frames section of the report, listing the inertial frame and the rotated frame E

.. image:: pendulum/report-points.png
   :width: 108
   :alt: The Points section of the report, listing the origin and point a

.. image:: pendulum/report-bodies.png
   :width: 108
   :alt: The Bodies section of the report, listing the particle bob

.. image:: pendulum/report-equations.png
   :width: 108
   :alt: The Equations section of the report, showing the mass matrix and the forcing vector

.. image:: pendulum/report-plots.png
   :width: 108
   :alt: The Plots section of the report, showing the angle and angular rate over time

What you built
==============

The Equations section of the report shows a mass matrix and a forcing vector. For this model, with the rod length :math:`l` (the offset :math:`x_A` in the Joints path), they are

.. math::

   M = m_{bob}\,l^2, \qquad F = -m_{bob}\,g\,l\cos\theta

so the equation of motion is

.. math::

   m\,l^2\,\ddot{\theta} + m\,g\,l\cos\theta = 0 \quad\Longleftrightarrow\quad \ddot{\theta} = -\frac{g}{l}\cos\theta

Here :math:`\theta` is measured from the horizontal :math:`\mathbf{n}_x` axis, because the rod lies along :math:`\mathbf{e}_x`. The pendulum hangs at rest at :math:`\theta = -\pi/2`. If you measure the angle from the hanging position instead, with :math:`\varphi = \theta + \pi/2`, this becomes the familiar :math:`\ddot{\varphi} + (g/l)\sin\varphi = 0`. For small swings its period is :math:`2\pi\sqrt{l/g}`, about 2.0 s for :math:`l = 1` m and :math:`g = 9.8` m/s². This pendulum starts :math:`1 + \pi/2 \approx 2.57` rad from hanging, a swing of about 147 degrees, which is why its period is longer, about 3.4 s.

Exported Python
===============

The Python File export contains the equations of motion and a short simulation script. This is an excerpt:

.. TODO (owner): replace the placeholder below with a short excerpt of python_model.py exported from this pendulum.

.. pycode::
   :caption: python_model.py (placeholder excerpt)

   # TODO (owner): paste a short excerpt of the exported pendulum code here
   # (the equations of motion and the simulation call).

Next steps
==========

Reference pages for the components used here: `Parameter <../classic/parameter.html>`__, `Generalized Coordinate <../classic/generalized_coordinate.html>`__, `Frame <../classic/frame.html>`__, `Vector <../classic/vector.html>`__, `Point <../classic/point.html>`__, `Revolute Joint <../joints/revolute.html>`__, `Rigid Translation <../joints/rigid_translation.html>`__ and `Particle <../bodies/particle.html>`__.

.. appcta::
   :next: /docs/tutorials/oscillator/ | Mass-Spring-Damper
