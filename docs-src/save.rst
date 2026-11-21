Import/Export
=============

From the navigation drawer, if you tap the the export button, then you will have options to export this file to a location
accessible in the file browser on your device, and can be shared with other users. Additionally, the export menu lets
you create a second Python file that can execute in a standard Python environment, a `.csv` formatted data file
containing time-series data for the simulation results, and `.png` formatted plots.

Each save file begins with the following header::

    # Initiate the mechanism
    from mechanism import Mechanism
    m = Mechanism()

This imports the mechanism class, and initiates an empty Mechanism object. This is followed by generating the settings::

    # Update the settings
    m.update_settings(
        model_name='ThreeLinkPendulum',
        model_description='Triple pendulum defined using three angular degrees of freedom and three point masses',
        time_duration=30,
        simplify_equations=True,
        simulation_rate=30,
        gravity_method='Uniform',
        gravity_constant=9.81,
        gravity_direction='-Y',
    )

Then, individual components are created, for example::

    # Create generalized coordinates
    m.create_coord(
        name='\theta_0',
        initial=-1,
        description='first link angle'
    )

**Create Methods**

Below are the modeling components referenced to the applicable create method. See the
`mechanism module <mechanism.html>`_ documentation for information on the keyword arguments. The arguments shown are
defaults for the respective component.

Classic Interface
-----------------

`Parameters <classic/parameter.html>`_::

    m.create_param(
        name=None,
        value=0,
        description=None
    )

`Generalized Coordinates <classic/generalized_coordinate.html>`_::

    m.create_coord(
        name=None,
        initial=0,
        description=None
    )

`Generalized Speeds <classic/generalized_speed.html>`_::

    m.create_speed(
        name=None,
        equates_to=None,
        initial=0,
        description=None
    )

`Reference Frames <classic/frame.html>`_::

    m.create_frame(
        ref_point_key='origin',
        ref_frame_key='inertial',
        rotation_sequence='ZYX',
        first_angle=0,
        second_angle=0,
        third_angle=0
    )

`Vectors <classic/vector.html>`_::

    m.create_vector(
        name=None,
        start_point='origin',
        ref_frame_key='inertial',
        x=0,
        y=0,
        z=0
    )

`Points <classic/point.html>`_::

    m.create_point(
        name=None,
        ref_point_key='origin',
        vector_key=None
    )

Joints
------

`Rigid Translation <joints/rigid_translation.html>`_::

    m.create_rigid_translation(
        name=None,
        ref_point_key='origin',
        ref_frame_key='inertial',
        x=0,
        y=0,
        z=0
    )

`Rigid Rotation <joints/rigid_rotation.html>`_::

    m.create_rigid_rotation(
        name=None,
        ref_point_key='origin',
        ref_frame_key='inertial',
        first_angle=0,
        second_angle=0,
        third_angle=0,
        rotation_sequence='ZYX'
    ):

`Prismatic Joint <joints/prismatic.html>`_::

    m.create_prismatic_joint(
        name=None,
        ref_point_key='origin',
        ref_frame_key='inertial',
        motion_axis='+X',
        value=0,
        rate=0,
        k=0,
        c=0,
        equilibrium=0
    )

`Revolute Joint <joints/revolute.html>`_::

    m.create_revolute_joint(
        name=None,
        ref_point_key='origin',
        ref_frame_key='inertial',
        motion_axis='+Z',
        value=0,
        rate=0,
        k=0,
        c=0,
        equilibrium=0
    )

`Cylindrical Joint <joints/cylindrical.html>`_::

    m.create_cylindrical_joint(
        name=None,
        ref_point_key='origin',
        ref_frame_key='inertial',
        motion_axis='+X',
        initial_t=0,
        initial_r=0,
        rate_t=0,
        rate_r=0,
        kt=0,
        kr=0,
        ct=0,
        cr=0,
        equilibrium_t=0,
        equilibrium_r=0
    ):

`Universal Joint <joints/universal.html>`_::

    m.create_universal_joint(
        name=None,
        ref_point_key='origin',
        ref_frame_key='inertial',
        rotation_pair='YX',
        initial_r0=0,
        initial_r1=0,
        rate_r0=0,
        rate_r1=0,
        kr0=0,
        kr1=0,
        cr0=0,
        cr1=0,
        equilibrium_r0=0,
        equilibrium_r1=0
    ):

`Spherical Joint <joints/spherical.html>`_::

    m.create_spherical_joint(
        name=None,
        ref_point_key='origin',
        ref_frame_key='inertial',
        rotation_sequence='ZYX',
        initial_r0=0,
        initial_r1=0,
        initial_r2=0,
        rate_r0=0,
        rate_r1=0,
        rate_r2=0,
        kr0=0,
        kr1=0,
        kr2=0,
        cr0=0,
        cr1=0,
        cr2=0,
        equilibrium_r0=0,
        equilibrium_r1=0,
        equilibrium_r2=0
    ):

`Planar Joint <joints/planar.html>`_::

    m.create_planar_joint(
        name=None,
        ref_point_key='origin',
        ref_frame_key='inertial',
        normal_axis='Z',
        velocity_in='Reference Frame',
        initial_t0=0,
        initial_t1=0,
        initial_r=0,
        rate_t0=0,
        rate_t1=0,
        rate_r=0,
        kt0=0,
        kt1=0,
        kr=0,
        ct0=0,
        ct1=0,
        cr=0,
        equilibrium_t0=0,
        equilibrium_t1=0,
        equilibrium_r=0
    ):

`Free Motion Joint <joints/free_motion.html>`_::

    m.create_free_motion_joint(
        name=None,
        ref_point_key='origin',
        ref_frame_key='inertial',
        rotation_sequence='ZYX',
        initial_t0=0,
        initial_t1=0,
        initial_t2=0,
        initial_r0=0,
        initial_r1=0,
        initial_r2=0,
        rate_t0=0,
        rate_t1=0,
        rate_t2=0,
        rate_r0=0,
        rate_r1=0,
        rate_r2=0,
        kt0=0,
        kt1=0,
        kt2=0,
        kr0=0,
        kr1=0,
        kr2=0,
        ct0=0,
        ct1=0,
        ct2=0,
        cr0=0,
        cr1=0,
        cr2=0,
        equilibrium_t0=0,
        equilibrium_t1=0,
        equilibrium_t2=0,
        equilibrium_r0=0,
        equilibrium_r1=0,
        equilibrium_r2=0
    ):

Bodies
------

`Particle <bodies/particle.html>`_::

    m.create_particle(
        name=None,
        ref_point_key='origin',
        mass=0
    )

`General Rigid Body <bodies/general_rigid_body.html>`_::

    m.create_general_rigid_body(
        name=None,
        ref_point_key='origin',
        ref_frame_key='inertial',
        mass=0,
        ixx=0,
        iyy=0,
        izz=0,
        ixy=0,
        iyz=0,
        izx=0
    ):

`Rigid Body Box <bodies/rigid_body_box.html>`_::

    m.create_body_box(
        name=None,
        ref_point_key='origin',
        ref_frame_key='inertial',
        density=0,
        length=0,
        width=0,
        height=0,
        attach_to='CG'
    )

`Rigid Body Cylinder <bodies/rigid_body_cylinder.html>`_::

    m.create_body_cylinder(
        name=None,
        ref_point_key='origin',
        ref_frame_key='inertial',
        density=0,
        length=0,
        radius=0,
        attach_to='CG'
    ):

`Rigid Body Cone <bodies/rigid_body_cone.html>`_::

    m.create_body_cone(
        name=None,
        ref_point_key='origin',
        ref_frame_key='inertial',
        density=0,
        length=0,
        radius=0,
        attach_to='CG'
    ):

Loads
-----

`External Force <loads/external_force.html>`_::

    m.create_external_force(
        name=None,
        ref_frame_key='inertial',
        ref_point_key='origin',
        force=0,
        x=0,
        y=0,
        z=0
    ):

`Actuated Force <loads/actuated_force.html>`_::

    m.create_actuated_force(
        name=None,
        ref_frame_key='inertial',
        start_point='origin',
        end_point='origin',
        force=0,
        x=0,
        y=0,
        z=0
    ):

`External Moment <loads/external_moment.html>`_::

    m.create_external_moment(
        name=None,
        ref_frame_key='inertial',
        loaded_frame_key='inertial',
        moment=0,
        x=0,
        y=0,
        z=0
    ):

`Actuated Moment <loads/actuated_moment.html>`_::

    m.create_actuated_moment(
        name=None,
        ref_frame_key='inertial',
        first_frame_key='inertial',
        second_frame_key='inertial',
        moment=0,
        x=0,
        y=0,
        z=0
    ):

`Translational Spring-Damper <loads/translational_spring.html>`_::

    m.create_translational_spring_damper(
        start_point='origin',
        end_point='origin',
        k=0,
        c=0,
        equilibrium=0
    )

`Rotational Spring-Damper <loads/rotational_spring.html>`_::

    m.create_rotational_spring_damper(
        ref_point_key='origin',
        first_frame_key='inertial',
        second_frame_key='inertial',
        k=0,
        c=0
    )
