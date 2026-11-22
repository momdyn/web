.. seo::
   :title: Getting Started with MOMDYN – Multibody Dynamics on iPhone & iPad
   :description: A tour of MOMDYN on iPhone and iPad: the Welcome, Diagram and Report screens, plus where to find the tutorials, dialogs and component reference.
   :type: article

Getting Started
===============

Welcome to the help documentation for Mobile Multibody Dynamics (MOMDYN), the first multibody dynamics app for iOS. This page gives an overview of the user interface in the app. Here we
will introduce tutorials that demonstrate the basics of building a dynamics model. This is followed by a discussion of
the screens in the app, and some of the details of the interface. For detail on the physical components, check out the
section on the `Mechanism Module <mechanism.html>`_.

Tutorials
---------

Below are examples of a simple pendulum and mass-spring-damper. These are standard models that are taught in
dynamics and vibration coursework, and are used to teach the fundamentals of kinematic definition with
translational and rotational motion, and equation of motion generation for specified bodies and loads. The tutorials
introduce definition kinematics using the classic interface, followed by mechanical joints.

Start with the `tutorials <tutorials.html>`_.

Welcome Screen
--------------

.. image:: img/welcomescreen.png
   :width: 200
   :align: center
   :alt: The Welcome Screen

The first screen you see, with the three basic options, "Create," "Import," or "Help." Tap on
the first button to bring up the settings dialog, where you will configure a new model. Tap on the second button to
bring up the import dialog, with a list of pre-created examples that are packaged with MOMDYN, as well as any models
you have saved as a user. Lastly, tap on the third button to open a popup with a link to this site, and two tutorials.

Details on the dialogs: `Create / Settings Dialogs <create_dialog.html>`_ and `Import Dialog <import_dialog.html>`_.


Diagram View
------------

.. image:: img/diagramview.png
   :width: 200
   :align: center
   :alt: The Diagram View

The primary screen for interacting with the model. Drag in the center of the screen to rotate the model, drag with two
fingers to pan (translate) the model, and use the button in the lower right to zoom in, or zoom out. The menu button in
the upper left opens the navigation drawer, with options to modify settings or export the model, and
panels for each of the dynamics modeling components. The play button in the lower left is used to derive equations of
motion (EOM), simulate, and start animations. Tap on the slider bar on the bottom to reposition the animation in time.

Details: `On-Screen Controls <on_screen_controls.html>`_, `Menu Dialog <menu_dialog.html>`_ and `Import/Export <save.html>`_.


Report View
-----------

Provides text and mathematical equations important to the dynamicist. At the top of the screen are several tabs which
each direct to a different set of report data. Start with the symbolic variables, including the time-varying
generalized coordinates and speeds, and the constant parameters. Next are the kinematics, including rotating reference
frames, vectors, and points. This is followed by the bodies and loads. Finally, once the model has been defined, you
may derive EOM which are viewed with the second to last button, and with these EOM run a simulation with plotted data
shown with the last button.

.. image:: img/report1.png
   :width: 200
   :alt: The Report View Tab Showing Symbols

.. image:: img/report2.png
   :width: 200
   :alt: The Report View Tab Showing Equations

.. image:: img/report3.png
   :width: 200
   :alt: The Report View Tab Showing Plots
