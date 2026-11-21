Create / Settings Dialogs
=========================

When you tap the create button on the welcome screen, or if the settings button in the edit menu, a dialog will appear
showing several options. These will correspond to the configuration for either the newly created or currently open
model, respectively.

.. image:: img/create_dialog.png
   :width: 200
   :alt: Dialog for creating a new model

.. image:: img/settings_dialog.png
   :width: 200
   :alt: Dialog for updating settings


Create
------

From the welcome screen, tap the "Create" button. This will open a settings dialog with blank or default settings.
After entering values for your intended model, tap the check mark in the lower right, this will send you to the diagram
view with an empty model, only the inertial frame and the origin point.

Settings
--------

From the diagram view, tap the edit button in the upper left. The menu drawer will scroll from the left of the
screen, tap the settings button at the top to open the settings dialog, with values from your current working
model. After editing settings, press the check mark in the lower right to return to the diagram view.

Below are the settings available in the dialog, their form, and default values.

**Keyword Arguments**

**model_name: string, 'New Model'**

Name of the model, used for saving

**model_description: string, ''**

Description of the model, for display purposes

**gravity_method: None or string, None**

Current string option is 'Uniform', where gravitational force on each body is m * g * Vector

**gravity_constant: numeric,**

Value for the gravitational acceleration 'g'

**gravity_direction: None or string, None**

Direction for the gravity vector, options are ('+X', '-X', '+Y', '-Y', '+Z', '-Z') in the inertial frame

**time_duration: numeric, 1**

Duration of the simulation, in seconds

**simulation_rate: numeric, 100**

Output interval for the simulation, in Hz. The simulation itself is a continuous time approximation, not fixed time interval.

**simplify_equations: boolean, False**

Option for whether or not to simplify the displayed equations of motion. Makes for a prettier output, and may speed up the simulation step, but often requires a significant computational time up front.

**integration_method: string, 'RKF45'**

Algorithm used for integrating the equations of motion during the simulation step.

**tol: numeric, 1e-3**

Tolerance for adaptive step size solvers.

**approximate_size: numeric, 1**

Used to set size of fonts, line widths, etc.

**playback_speed: numeric, 1**

Speed of the animation, 1 is real time, <1 is slower, >1 is faster.