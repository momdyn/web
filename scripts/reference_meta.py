"""Hand-written content for the generated reference pages (read by gen_reference.py).

The docstrings of the Mechanism module give the parameter names, types and descriptions. Everything an engineering student needs
beyond that lives here: a one-sentence definition, units, equations (LaTeX, rendered with KaTeX), sign conventions, related pages
and the SEO description. A value of "TODO" in `units` (or a note starting with "TODO") is shown on the page, flagged for the owner.

Keys are the Mechanism.create_* method names.
"""

NOUN = {"classic": "", "joints": "Joint", "bodies": "Body", "loads": "Load", "sensors": "Sensor"}

UNITS_NOTE = ("Units are shown in SI (m, kg, s, N, rad). MOMDYN does not enforce units, so any consistent set works, "
              "but angles are always in radians.")

# Units that do not depend on the component. Keys ending in _key and other text options show a dash.
GENERIC_UNITS = {
    "first_angle": "rad", "second_angle": "rad", "third_angle": "rad",
    "mass": "kg", "density": "kg/m³", "length": "m", "width": "m", "height": "m", "radius": "m",
    "ixx": "kg·m²", "iyy": "kg·m²", "izz": "kg·m²", "ixy": "kg·m²", "iyz": "kg·m²", "izx": "kg·m²",
    "force": "N", "moment": "N·m",
}
TEXT_PARAMS = {"name", "description", "motion_axis", "is_form", "rotation_sequence", "rotation_pair", "normal_axis", "velocity_in",
               "attach_to", "color", "use_quaternion", "equates_to", "start_point", "end_point", "vector_key", "ref_point_key",
               "ref_frame_key", "point_key", "frame_key", "ref_point_key", "loaded_frame_key", "first_frame_key", "second_frame_key"}


def generic_unit(param):
    """Units that follow from the parameter's name: t* translational, r* rotational."""
    import re
    if param in GENERIC_UNITS:
        return GENERIC_UNITS[param]
    if param in TEXT_PARAMS:
        return "—"
    rules = [(r"^initial_t\d?$", "m"), (r"^equilibrium_t\d?$", "m"), (r"^rate_t\d?$", "m/s"), (r"^kt\d?$", "N/m"), (r"^ct\d?$", "N·s/m"),
             (r"^initial_r\d?$", "rad"), (r"^equilibrium_r\d?$", "rad"), (r"^rate_r\d?$", "rad/s"), (r"^kr\d?$", "N·m/rad"), (r"^cr\d?$", "N·m·s/rad")]
    for pat, unit in rules:
        if re.match(pat, param):
            return unit
    return None


IS_FORM = ("`is_form` is `'degree of freedom'` (the value is a time-varying coordinate that the simulation solves for) or "
           "`'constant'` (the value is fixed).")

M = {}

# ----------------------------------------------------------------------------------------------- classic
M["create_param"] = dict(
    definition="A parameter is a named constant, such as a length, a mass or a spring stiffness, that you define once and reuse in other components.",
    figure=None, figure_alt="A parameter named l with value 1 and description length, listed in the report's symbols tab",
    desc="A MOMDYN parameter is a named constant, such as a length, mass or stiffness, that vectors, frames and other components can reference by name.",
    units={"value": "depends on use"},
    equations=[],
    notes=["A parameter keeps the same value for the whole simulation. For a quantity that changes with time, use a "
           "[generalized coordinate](generalized_coordinate.html).",
           "Names accept LaTeX-style input: `\\theta` becomes θ and `\\omega` becomes ω.",
           "Bodies, joints and spring-dampers create their own parameters (for example the mass of a particle named `bob` is `m_bob`)."],
    related=[("classic/generalized_coordinate", "Generalized Coordinate"), ("classic/vector", "Vector"),
             ("loads/translational_spring", "Translational Spring"), ("bodies/particle", "Particle")])
M["create_coord"] = dict(
    definition="A generalized coordinate is a time-varying symbol that describes one degree of freedom of the mechanism, such as an angle or a displacement.",
    figure=None, figure_alt="A generalized coordinate dialog with name theta, initial value 1 and description angle",
    desc="A MOMDYN generalized coordinate is a time-varying symbol for one degree of freedom, such as an angle or displacement, used by frames and vectors.",
    units={"initial": "m or rad"},
    equations=[("The coordinate is a function of time, and its initial value sets the starting configuration:", r"q = q(t), \qquad q(0) = q_0")],
    notes=["Each generalized coordinate adds one degree of freedom to the equations of motion.",
           "Names accept LaTeX-style input: `\\theta` becomes θ. Select the coordinate by name in frame and vector dialogs, for example `θ(t)`.",
           "The Joints interface creates coordinates for you (the revolute joint `E` creates θ_E)."],
    related=[("classic/generalized_speed", "Generalized Speed"), ("classic/frame", "Frame"), ("classic/vector", "Vector"),
             ("joints/revolute", "Revolute Joint")])
M["create_speed"] = dict(
    definition="A generalized speed is a time-varying symbol that describes the motion of the mechanism; by default it is the time derivative of a generalized coordinate.",
    figure=None, figure_alt="A generalized speed dialog with a name, an equates-to expression and an initial value",
    desc="A MOMDYN generalized speed is a time-varying symbol for mechanism motion, usually the derivative of a coordinate, giving compact equations of motion.",
    units={"initial": "m/s or rad/s"},
    equations=[("By default the speed is the derivative of its coordinate:", r"u_i = \dot{q}_i"),
               ("In general, the coordinate rates follow from the speeds through the kinematic differential equations:", r"\dot{\mathbf{q}} = \mathbf{f}(\mathbf{q}, \mathbf{u})")],
    notes=["Choosing other speeds can give a more compact set of equations. For a free rigid body, a common choice is the velocity components in the body-fixed frame.",
           "`equates_to` names the terms in a point velocity or a frame angular velocity that this speed replaces."],
    related=[("classic/generalized_coordinate", "Generalized Coordinate"), ("joints/free_motion", "Free Motion Joint"),
             ("bodies/particle", "Particle")])
M["create_frame"] = dict(
    definition="A frame is a set of three perpendicular unit vectors that is rotated by up to three Euler angles relative to another frame.",
    figure=None, figure_alt="A rotated reference frame drawn with red, green and blue axes next to the inertial frame",
    desc="A MOMDYN frame is a set of three perpendicular unit vectors rotated by Euler angles from another frame; it defines orientation for vectors and bodies.",
    units={},
    equations=[("A single rotation θ about the z-axis of a frame with unit vectors n gives a new frame with unit vectors e:",
                r"\mathbf{e}_x = \cos\theta\,\mathbf{n}_x + \sin\theta\,\mathbf{n}_y, \qquad \mathbf{e}_y = -\sin\theta\,\mathbf{n}_x + \cos\theta\,\mathbf{n}_y, \qquad \mathbf{e}_z = \mathbf{n}_z")],
    notes=["Angles are in radians and positive by the right-hand rule. Each angle can be a number or the name of a parameter or generalized coordinate.",
           "`rotation_sequence` such as `'ZYX'` means: rotate `first_angle` about the Z-axis of the reference frame, `second_angle` about the new Y-axis, then `third_angle` about the newest X-axis.",
           "`ref_point_key` only sets where the frame is drawn in the diagram. It does not change the physics."],
    related=[("joints/rigid_rotation", "Rigid Rotation"), ("joints/revolute", "Revolute Joint"), ("classic/vector", "Vector"),
             ("classic/generalized_coordinate", "Generalized Coordinate")])
M["create_vector"] = dict(
    definition="A vector is an arrow whose x, y and z components are measured along the axes of a chosen frame.",
    figure=None, figure_alt="A gray line from the origin to a blue point, representing a vector with its start at the origin",
    desc="A MOMDYN vector is an arrow with x, y and z components along a chosen frame; each component can be a parameter or coordinate. Used to locate points.",
    units={"x": "—", "y": "—", "z": "—"},
    equations=[("The vector is the sum of its components along the basis vectors of the reference frame:",
                r"\mathbf{r} = x\,\mathbf{e}_x + y\,\mathbf{e}_y + z\,\mathbf{e}_z")],
    notes=["Each of `x`, `y` and `z` is the name of a parameter or generalized coordinate (or a number). That symbol supplies the length, so its units are lengths.",
           "`ref_point_key` marks where the vector starts in the diagram. To place a point with the vector, create a [point](point.html).",
           "In the pendulum tutorial the vector `r` has `x = l` in the rotated frame `E`."],
    related=[("classic/point", "Point"), ("classic/frame", "Frame"), ("joints/rigid_translation", "Rigid Translation"),
             ("joints/prismatic", "Prismatic Joint")])
M["create_point"] = dict(
    definition="A point is a location in space, defined by a vector from another point; its velocity and acceleration follow from the motion of the mechanism.",
    figure=None, figure_alt="A blue sphere marking a point at the end of a vector in the diagram view",
    desc="A MOMDYN point is a location defined by a vector from a reference point. Bodies, forces, springs and sensors attach to points. The origin is the default.",
    units={},
    equations=[("The new point P is offset from the reference point Q by the vector:", r"\mathbf{r}_{P/O} = \mathbf{r}_{Q/O} + \mathbf{r}")],
    notes=["The default reference point is `origin`, which is fixed in the inertial frame.",
           "Bodies, loads and sensors attach to points, so any location you want to put a mass, force or sensor needs a point."],
    related=[("classic/vector", "Vector"), ("bodies/particle", "Particle"), ("joints/rigid_translation", "Rigid Translation"),
             ("loads/translational_spring", "Translational Spring")])

# ----------------------------------------------------------------------------------------------- joints
M["create_rigid_translation"] = dict(
    definition="A rigid translation adds a new point at a fixed offset from an existing point. It has no degree of freedom.",
    figure="img/rigidtranslation.jpg", figure_alt="A rigid translation: a new point offset from a start point along the axes of a reference frame",
    desc="A MOMDYN rigid translation adds a point at a fixed offset from another point, with components in a reference frame. It adds no degrees of freedom.",
    units={"x": "m", "y": "m", "z": "m"},
    equations=[("The offset from the start point A to the new point B:", r"\mathbf{r}_{B/A} = x\,\mathbf{e}_x + y\,\mathbf{e}_y + z\,\mathbf{e}_z")],
    notes=["It is the Joints-interface equivalent of creating a vector and a point in the Classic interface. In the pendulum tutorial it makes the rod (`x = 1` in frame `E`).",
           "The components `x`, `y` and `z` are measured along the axes of `ref_frame_key`, and the rigid translation creates the offsets as constants."],
    related=[("classic/vector", "Vector"), ("classic/point", "Point"), ("joints/revolute", "Revolute Joint"), ("joints/prismatic", "Prismatic Joint")])
M["create_rigid_rotation"] = dict(
    definition="A rigid rotation adds a new frame at a fixed orientation relative to another frame, using an Euler angle sequence. It has no degree of freedom.",
    figure="img/rigidrotation.jpg", figure_alt="A rigid rotation: a new frame turned by fixed angles relative to a reference frame",
    desc="A MOMDYN rigid rotation adds a frame at a fixed orientation from a reference frame using a three-angle Euler sequence. It adds no degrees of freedom.",
    units={},
    equations=[("For the default `ZYX` sequence, with angles α, β and γ, the components in the reference frame A follow from those in the new frame B:",
                r"{}^{A}C^{B} = R_z(\alpha)\,R_y(\beta)\,R_x(\gamma)")],
    notes=["`R_z`, `R_y` and `R_x` are the elementary rotation matrices about each axis. Angles are in radians and positive by the right-hand rule.",
           "Each rotation is about an axis of the frame produced by the previous rotation (a body-fixed sequence).",
           "`ref_point_key` only sets where the frame is drawn."],
    related=[("classic/frame", "Frame"), ("joints/revolute", "Revolute Joint"), ("joints/spherical", "Spherical Joint"),
             ("sensors/dcm_sensor", "DCM Sensor")])
M["create_prismatic_joint"] = dict(
    definition="A prismatic joint lets a point slide along one axis of a reference frame, like a piston or a linear rail. It adds one translational degree of freedom.",
    figure="img/prismatic.jpg", figure_alt="A prismatic joint: a point that slides along one axis of the reference frame",
    desc="A MOMDYN prismatic joint lets a point slide along one reference-frame axis, adding one translational degree of freedom, with an optional spring-damper.",
    units={"value": "m", "rate": "m/s", "k": "N/m", "c": "N·s/m", "equilibrium": "m"},
    equations=[("Position of the new point B relative to the start point A, along the unit vector a of the motion axis:", r"\mathbf{r}_{B/A} = q\,\hat{\mathbf{a}}"),
               ("Optional spring-damper force along the axis, restoring toward the equilibrium distance q_e:", r"F = -k\,(q - q_e) - c\,\dot{q}")],
    notes=[IS_FORM, "`motion_axis` is `'+X'`, `'-X'`, `'+Y'`, `'-Y'`, `'+Z'` or `'-Z'` in `ref_frame_key`. A minus sign reverses the direction in which positive `q` moves the point.",
           "`value` and `rate` are the initial coordinate q(0) and its initial speed. The spring-damper is off while `k` and `c` keep their default of 0."],
    related=[("loads/translational_spring", "Translational Spring"), ("joints/rigid_translation", "Rigid Translation"),
             ("joints/cylindrical", "Cylindrical Joint"), ("bodies/particle", "Particle")])
M["create_revolute_joint"] = dict(
    definition="A revolute joint is a hinge: it rotates a frame about one axis that is fixed in a reference frame. It adds one rotational degree of freedom.",
    figure="img/revolute.jpg", figure_alt="A revolute joint: a frame rotating about one axis of the reference frame",
    desc="A MOMDYN revolute joint is a hinge that rotates a frame about one reference-frame axis, adding one rotational degree of freedom, plus an optional spring.",
    units={"value": "rad", "rate": "rad/s", "k": "N·m/rad", "c": "N·m·s/rad", "equilibrium": "rad"},
    equations=[("Optional spring-damper torque about the axis, restoring toward the equilibrium angle θ_e:", r"\tau = -k\,(\theta - \theta_e) - c\,\dot{\theta}")],
    notes=[IS_FORM, "`motion_axis` is `'+X'`, `'-X'`, `'+Y'`, `'-Y'`, `'+Z'` or `'-Z'`. Positive θ follows the right-hand rule about the chosen axis, so `'-Z'` reverses the direction.",
           "`ref_point_key` only sets where the joint is drawn. It does not change the physics. In the pendulum tutorial, `value = 1` sets the initial angle θ_E to 1 rad."],
    related=[("loads/rotational_spring", "Rotational Spring"), ("loads/actuated_moment", "Actuated Moment"),
             ("joints/rigid_rotation", "Rigid Rotation"), ("joints/cylindrical", "Cylindrical Joint")])
M["create_universal_joint"] = dict(
    definition="A universal joint orients a frame with two successive rotation angles, giving two rotational degrees of freedom, like a drive-shaft coupling.",
    figure="img/universal.jpg", figure_alt="A universal joint: a frame rotated by two angles about perpendicular axes",
    desc="A MOMDYN universal joint orients a frame with two successive rotations, giving two rotational degrees of freedom, with optional spring-dampers.",
    units={},
    equations=[("For `rotation_pair = 'YX'`, with angles θ₀ and θ₁, the frame orientation is:", r"{}^{A}C^{B} = R_y(\theta_0)\,R_x(\theta_1)"),
               ("Optional spring-damper torque for each angle i = 0, 1:", r"\tau_i = -k_{r,i}\,(\theta_i - \theta_{e,i}) - c_{r,i}\,\dot{\theta}_i")],
    notes=[IS_FORM, "`rotation_pair` is one of `'XY'`, `'YX'`, `'YZ'`, `'ZY'`, `'ZX'` or `'XZ'`. The second rotation is about an axis of the frame produced by the first.",
           "TODO: confirm that `cr0` and `cr1` damp the angular rates of the 0th and 1st angles (the docstring describes them in terms of the created frame's x and y axes)."],
    related=[("joints/revolute", "Revolute Joint"), ("joints/spherical", "Spherical Joint"), ("joints/rigid_rotation", "Rigid Rotation")])
M["create_spherical_joint"] = dict(
    definition="A spherical joint is a ball joint: it lets a frame take any orientation relative to another, with three rotational degrees of freedom.",
    figure="img/spherical.jpg", figure_alt="A spherical joint: a frame that can take any orientation relative to the reference frame",
    desc="A MOMDYN spherical joint lets a frame take any orientation using a quaternion, giving three rotational degrees of freedom with no gimbal lock.",
    units={},
    equations=[("Orientation is tracked with a unit quaternion, which avoids the singularities of Euler angles:", r"q_0^2 + q_1^2 + q_2^2 + q_3^2 = 1")],
    notes=[IS_FORM, "`initial_r0`, `initial_r1` and `initial_r2` give the starting orientation as an equivalent Euler angle sequence (`rotation_sequence`), which MOMDYN converts to the initial quaternion.",
           "The `rate_r*` values are the initial angular velocity components about the axes of the created frame."],
    related=[("joints/universal", "Universal Joint"), ("joints/free_motion", "Free Motion Joint"), ("joints/revolute", "Revolute Joint"),
             ("sensors/rate_gyro", "Rate Gyro")])
M["create_planar_joint"] = dict(
    definition="A planar joint moves a point in a plane and rotates a frame about the plane's normal, giving two translational and one rotational degree of freedom.",
    figure="img/planar.jpg", figure_alt="A planar joint: a point moving in a plane with a frame rotating about the plane's normal",
    desc="A MOMDYN planar joint moves a point in a plane and rotates a frame about the plane normal, giving three degrees of freedom, with optional spring-dampers.",
    units={},
    equations=[("For `normal_axis = 'Z'`, the point moves in the x-y plane of the reference frame and the frame rotates by θ about z:", r"\mathbf{r}_{B/A} = t_0\,\mathbf{e}_x + t_1\,\mathbf{e}_y"),
               ("Optional spring-damper forces and torque:", r"F_i = -k_{t,i}\,(t_i - t_{e,i}) - c_{t,i}\,\dot{t}_i, \qquad \tau = -k_r\,(\theta - \theta_e) - c_r\,\dot{\theta}")],
    notes=[IS_FORM, "`normal_axis` is `'X'`, `'Y'` or `'Z'`. The two translations are in the plane perpendicular to it.",
           "`velocity_in` is `'Reference Frame'` or `'Created Frame'` and sets the frame in which the translational speeds are measured."],
    related=[("joints/free_motion", "Free Motion Joint"), ("joints/revolute", "Revolute Joint"), ("joints/prismatic", "Prismatic Joint"),
             ("bodies/rigid_body_box", "Rigid Body Box")])
M["create_free_motion_joint"] = dict(
    definition="A free motion joint gives a frame all six degrees of freedom: three translations and a free orientation, like a rigid body floating in space.",
    figure="img/freemotion.jpg", figure_alt="A free motion joint: a frame that can translate along all three axes and take any orientation",
    desc="A MOMDYN free motion joint gives a frame six degrees of freedom, three translations plus a quaternion orientation, like a free-floating rigid body.",
    units={},
    equations=[("Position of the new point relative to the start point A:", r"\mathbf{r}_{B/A} = t_0\,\mathbf{e}_x + t_1\,\mathbf{e}_y + t_2\,\mathbf{e}_z"),
               ("Orientation is a unit quaternion:", r"q_0^2 + q_1^2 + q_2^2 + q_3^2 = 1")],
    notes=[IS_FORM, "`initial_r0`, `initial_r1` and `initial_r2` give the starting orientation as an equivalent Euler angle sequence (`rotation_sequence`).",
           "The `rate_t*` values are velocity components, and the `rate_r*` values are angular velocity components, about the axes of the created frame."],
    related=[("joints/spherical", "Spherical Joint"), ("joints/planar", "Planar Joint"), ("bodies/general_rigid_body", "General Rigid Body"),
             ("classic/generalized_speed", "Generalized Speed")])
M["create_cylindrical_joint"] = dict(
    definition="A cylindrical joint slides a point along an axis and rotates a frame about that same axis, giving one translational and one rotational degree of freedom.",
    figure="img/cylindrical.jpg", figure_alt="A cylindrical joint: a point sliding along an axis while a frame rotates about the same axis",
    desc="A MOMDYN cylindrical joint slides a point along an axis and rotates a frame about it, giving one translation and one rotation, plus optional springs.",
    units={},
    equations=[("Position along the unit vector a of the motion axis, with rotation θ about the same axis:", r"\mathbf{r}_{B/A} = t\,\hat{\mathbf{a}}"),
               ("Optional spring-damper force and torque:", r"F = -k_t\,(t - t_e) - c_t\,\dot{t}, \qquad \tau = -k_r\,(\theta - \theta_e) - c_r\,\dot{\theta}")],
    notes=[IS_FORM, "`motion_axis` is `'+X'`, `'-X'`, `'+Y'`, `'-Y'`, `'+Z'` or `'-Z'`. A minus sign reverses the positive direction of both the translation and the rotation."],
    related=[("joints/prismatic", "Prismatic Joint"), ("joints/revolute", "Revolute Joint"), ("loads/translational_spring", "Translational Spring")])

# ----------------------------------------------------------------------------------------------- bodies
M["create_particle"] = dict(
    definition="A particle is a point mass: mass concentrated at one point, with no rotational inertia.",
    figure="img/particle.jpg", figure_alt="A particle: a green and black sphere marking a point mass attached to a point",
    desc="A MOMDYN particle is a point mass fixed to a point, with no inertia tensor. It is the simplest body, used for pendulum bobs and oscillator masses.",
    units={"mass": "kg"},
    equations=[("The inertial force of a particle of mass m with acceleration a, and its weight in uniform gravity g:", r"\mathbf{F}^{*} = -m\,\mathbf{a}, \qquad \mathbf{F}_g = m\,\mathbf{g}")],
    notes=["MOMDYN creates a parameter for the mass, named `m_` plus the particle name (for a particle named `bob`, the symbol is m_bob).",
           "`color` sets the color drawn in the diagram and does not change the physics. Options: Black, Gray, White, Red, Brown, Orange, Yellow, Mint, Green (default), Cyan, Blue, Teal, Pink, Indigo or Purple.",
    related=[("classic/point", "Point"), ("bodies/rigid_body_box", "Rigid Body Box"), ("loads/external_force", "External Force"),
             ("loads/translational_spring", "Translational Spring")])
_ATTACH = ("`attach_to` is `'CG'`, `'fore'` or `'aft'` and selects which place on the body sits at the point `ref_point_key`: its center of gravity, or one end of its length.")
M["create_body_box"] = dict(
    definition="A rigid body box is a rectangular block of uniform density; its mass and inertia follow from its dimensions.",
    figure="img/rigidbodybox.jpg", figure_alt="A rigid body box: a rectangular block of uniform density",
    desc="A MOMDYN rigid body box is a rectangular block of uniform density with length, width and height; mass and inertia about its center are computed.",
    units={"density": "kg/m³"},
    equations=[("Mass of a box with length ℓ (X), width w (Y), height h (Z) and density ρ:", r"m = \rho\,\ell\,w\,h"),
               ("Moments of inertia about the center of gravity:", r"I_{xx} = \tfrac{m}{12}(w^2 + h^2), \quad I_{yy} = \tfrac{m}{12}(\ell^2 + h^2), \quad I_{zz} = \tfrac{m}{12}(\ell^2 + w^2)")],
    notes=[_ATTACH, "The dimensions are measured along the X, Y and Z axes of the body-fixed frame, which is oriented in `ref_frame_key`."],
    related=[("bodies/rigid_body_cylinder", "Rigid Body Cylinder"), ("bodies/rigid_body_cone", "Rigid Body Cone"),
             ("bodies/general_rigid_body", "General Rigid Body"), ("joints/rigid_rotation", "Rigid Rotation")])
M["create_body_cylinder"] = dict(
    definition="A rigid body cylinder is a circular rod of uniform density; its mass and inertia follow from its length and radius.",
    figure="img/rigidbodycylinder.jpg", figure_alt="A rigid body cylinder: a circular rod of uniform density along the X axis",
    desc="A MOMDYN rigid body cylinder is a circular rod of uniform density along the X axis; mass and inertia about its center come from length and radius.",
    units={"density": "kg/m³"},
    equations=[("Mass of a cylinder with length ℓ (X), radius r and density ρ:", r"m = \rho\,\pi r^2 \ell"),
               ("Moments of inertia about the center of gravity:", r"I_{xx} = \tfrac{1}{2} m r^2, \qquad I_{yy} = I_{zz} = \tfrac{m}{12}\left(3 r^2 + \ell^2\right)")],
    notes=[_ATTACH, "The axis of the cylinder is the X axis of the body-fixed frame, which is oriented in `ref_frame_key`."],
    related=[("bodies/rigid_body_box", "Rigid Body Box"), ("bodies/rigid_body_cone", "Rigid Body Cone"),
             ("bodies/general_rigid_body", "General Rigid Body"), ("joints/rigid_rotation", "Rigid Rotation")])
M["create_body_cone"] = dict(
    definition="A rigid body cone is a circular cone of uniform density; its mass and inertia follow from its length and base radius.",
    figure="img/rigidbodycone.jpg", figure_alt="A rigid body cone: a circular cone of uniform density along the X axis",
    desc="A MOMDYN rigid body cone is a circular cone of uniform density along the X axis; mass and inertia about its center come from length and base radius.",
    units={"density": "kg/m³"},
    equations=[("Mass of a cone with length ℓ (X), base radius r and density ρ:", r"m = \tfrac{1}{3}\,\rho\,\pi r^2 \ell"),
               ("Moments of inertia about the center of gravity, which is a distance ℓ/4 from the base:", r"I_{xx} = \tfrac{3}{10} m r^2, \qquad I_{yy} = I_{zz} = \tfrac{3}{80}\,m\left(4 r^2 + \ell^2\right)")],
    notes=[_ATTACH, "The axis of the cone is the X axis of the body-fixed frame, which is oriented in `ref_frame_key`."],
    related=[("bodies/rigid_body_box", "Rigid Body Box"), ("bodies/rigid_body_cylinder", "Rigid Body Cylinder"),
             ("bodies/general_rigid_body", "General Rigid Body"), ("joints/rigid_rotation", "Rigid Rotation")])
M["create_general_rigid_body"] = dict(
    definition="A general rigid body has a given mass and inertia tensor about its center of gravity, for shapes that the box, cylinder and cone cannot describe.",
    figure="img/generalrigidbody.jpg", figure_alt="A general rigid body: a body defined by its mass and inertia tensor about its center of gravity",
    desc="A MOMDYN general rigid body has a specified mass and inertia tensor about its center of gravity, for shapes the box, cylinder and cone cannot describe.",
    units={},
    equations=[("The inertia tensor about the center of gravity, in the axes of the reference frame:", r"\mathbf{I} = \begin{bmatrix} I_{xx} & I_{xy} & I_{zx} \\ I_{xy} & I_{yy} & I_{yz} \\ I_{zx} & I_{yz} & I_{zz} \end{bmatrix}")],
    notes=["The center of gravity is at `ref_point_key`, and the inertia tensor is expressed in the axes of `ref_frame_key`.",
           "TODO: state the sign convention of the products of inertia (`ixy`, `iyz`, `izx`): whether they are the tensor entries as shown above or the integrals of x·y, y·z and z·x over the mass."],
    related=[("bodies/rigid_body_box", "Rigid Body Box"), ("bodies/particle", "Particle"), ("joints/free_motion", "Free Motion Joint"),
             ("classic/frame", "Frame")])

# ----------------------------------------------------------------------------------------------- loads
_DIR = ("The direction is set by the components x, y and z in `ref_frame_key`. TODO: confirm that the components are normalized, "
        "so that only `force` (or `moment`) sets the magnitude.")
M["create_external_force"] = dict(
    definition="An external force pushes on a single point, with a magnitude and a direction given in a reference frame.",
    figure=None, figure_alt="A force arrow acting on a point in the diagram view",
    desc="A MOMDYN external force acts on a single point, with a magnitude and a direction given by x, y and z components in a reference frame.",
    units={"x": "—", "y": "—", "z": "—"},
    equations=[("Force on the point, with magnitude F along the unit vector u that points in the direction (x, y, z):", r"\mathbf{F} = F\,\hat{\mathbf{u}}")],
    notes=[_DIR, "Gravity is not an external force you add: it is set in the model settings and acts on every body."],
    related=[("loads/actuated_force", "Actuated Force"), ("loads/external_moment", "External Moment"), ("bodies/particle", "Particle"),
             ("classic/point", "Point")])
M["create_actuated_force"] = dict(
    definition="An actuated force acts with equal and opposite magnitude on two points, like a linear actuator pushing two parts of a mechanism apart.",
    figure=None, figure_alt="Equal and opposite force arrows on two points, like a linear actuator",
    desc="A MOMDYN actuated force acts with equal and opposite magnitude on two points, like a linear actuator, with its direction set in a reference frame.",
    units={"x": "—", "y": "—", "z": "—"},
    equations=[("Force on the start point and on the end point, with magnitude F along the unit vector u:", r"\mathbf{F}_{\text{start}} = F\,\hat{\mathbf{u}}, \qquad \mathbf{F}_{\text{end}} = -F\,\hat{\mathbf{u}}")],
    notes=[_DIR, "Because the two forces are equal and opposite, an actuated force changes the internal motion of a mechanism but not its net momentum."],
    related=[("loads/external_force", "External Force"), ("loads/translational_spring", "Translational Spring"),
             ("joints/prismatic", "Prismatic Joint"), ("loads/actuated_moment", "Actuated Moment")])
M["create_external_moment"] = dict(
    definition="An external moment twists a single frame, with a magnitude and an axis given in a reference frame.",
    figure=None, figure_alt="A moment arrow acting on a frame in the diagram view",
    desc="A MOMDYN external moment acts on a single frame, with a magnitude and an axis given by x, y and z components in a reference frame.",
    units={"x": "—", "y": "—", "z": "—"},
    equations=[("Moment on the frame, with magnitude M about the unit vector u that points along (x, y, z):", r"\mathbf{M} = M\,\hat{\mathbf{u}}")],
    notes=[_DIR, "A positive moment turns the frame counterclockwise about its axis (right-hand rule)."],
    related=[("loads/actuated_moment", "Actuated Moment"), ("loads/external_force", "External Force"), ("joints/revolute", "Revolute Joint"),
             ("classic/frame", "Frame")])
M["create_actuated_moment"] = dict(
    definition="An actuated moment acts with equal and opposite magnitude on two frames, like a motor turning one link against another.",
    figure=None, figure_alt="Equal and opposite moment arrows on two frames, like a motor between two links",
    desc="A MOMDYN actuated moment acts with equal and opposite magnitude on two frames, like a motor between two links, about an axis set in a reference frame.",
    units={"x": "—", "y": "—", "z": "—"},
    equations=[("Moment on the first frame and on the second frame, with magnitude M about the unit vector u:", r"\mathbf{M}_{1} = M\,\hat{\mathbf{u}}, \qquad \mathbf{M}_{2} = -M\,\hat{\mathbf{u}}")],
    notes=[_DIR, "Use it between the two frames on either side of a revolute joint to model a motor or an actuator."],
    related=[("loads/external_moment", "External Moment"), ("loads/rotational_spring", "Rotational Spring"), ("joints/revolute", "Revolute Joint"),
             ("classic/frame", "Frame")])
M["create_translational_spring_damper"] = dict(
    definition="A translational spring-damper connects two points with a spring that resists stretching and a damper that resists their relative speed.",
    figure=None, figure_alt="A spring drawn between two points in the diagram view",
    desc="A MOMDYN translational spring-damper pulls two points together with a spring force and a damping force along the line between them.",
    units={"k": "N/m", "c": "N·s/m", "equilibrium": "m"},
    equations=[("Magnitude of the attractive force along the line from the start point to the end point:", r"F = k\,(x - e) + c\,\dot{x}"),
               ("Here x is the distance between the two points, e is the equilibrium length and ẋ is the rate at which that distance changes.", r"\dot{x} = \dfrac{d}{dt}\,\lVert \mathbf{r}_{\text{end}} - \mathbf{r}_{\text{start}} \rVert")],
    notes=["A positive F pulls the points together, so the spring is relaxed at the equilibrium length e and pulls the points together when stretched beyond it.",
           "MOMDYN creates parameters for the stiffness, damping and equilibrium, named from the two points (for points O and a: k_O/a, c_O/a and e_O/a)."],
    related=[("loads/rotational_spring", "Rotational Spring"), ("joints/prismatic", "Prismatic Joint"), ("bodies/particle", "Particle"),
             ("loads/actuated_force", "Actuated Force")])
M["create_rotational_spring_damper"] = dict(
    definition="A rotational spring-damper connects two frames with a torsion spring that resists their relative angle and a damper that resists their relative angular speed.",
    figure=None, figure_alt="A torsion spring drawn between two frames in the diagram view",
    desc="A MOMDYN rotational spring-damper applies a moment between two frames from a torsion spring and a damper, about their relative rotation axis.",
    units={"k": "N·m/rad", "c": "N·m·s/rad"},
    equations=[("Magnitude of the attractive moment about the axis of relative rotation:", r"M = k\,\theta + c\,\dot{\theta}"),
               ("Here θ is the angle between the two frames and θ̇ is their relative angular speed.", r"\dot{\theta} = \dfrac{d\theta}{dt}")],
    notes=["There is no separate equilibrium angle: the spring is relaxed when the two frames are aligned (θ = 0).",
           "`ref_point_key` only sets where the spring is drawn. It does not change the physics."],
    related=[("loads/translational_spring", "Translational Spring"), ("joints/revolute", "Revolute Joint"),
             ("loads/actuated_moment", "Actuated Moment"), ("classic/frame", "Frame")])

# ----------------------------------------------------------------------------------------------- sensors
M["create_position_sensor"] = dict(
    definition="A position sensor records where one point is relative to another point, in the axes of a chosen frame.",
    figure=None, figure_alt="A position sensor: the vector from a reference point to a sensed point, with components in a frame",
    desc="A MOMDYN position sensor records the position of a point relative to a reference point, with components in a chosen frame, in the plots and exports.",
    units={},
    equations=[("The sensed quantity is the position vector from the reference point Q to the point P, resolved in the axes of frame F:", r"\{\mathbf{r}_{P/Q}\}_F = \begin{bmatrix} x \\ y \\ z \end{bmatrix}")],
    notes=["The sensor adds three time series (x, y and z) to the simulation output.",
           "A real counterpart is a linear variable differential transformer (LVDT). The simulated sensor has none of its range or contact limits."],
    related=[("sensors/velocity_sensor", "Velocity Sensor"), ("sensors/accelerometer", "Accelerometer"), ("classic/point", "Point"),
             ("classic/frame", "Frame")])
M["create_velocity_sensor"] = dict(
    definition="A velocity sensor records how fast a point is moving, in the axes of a chosen frame.",
    figure=None, figure_alt="A velocity sensor: the velocity vector of a point, with components in a frame",
    desc="A MOMDYN velocity sensor records the velocity of a point with components in a chosen frame, adding three time series to the simulation output.",
    units={},
    equations=[("The sensed quantity is the velocity of the point P, resolved in the axes of frame F:", r"\{\mathbf{v}_P\}_F = \begin{bmatrix} v_x \\ v_y \\ v_z \end{bmatrix}")],
    notes=["TODO: state the frame in which the velocity is differentiated (the inertial frame is assumed here).",
           "A real counterpart is a laser Doppler vibrometer. The simulated sensor has no line-of-sight or isolation limits."],
    related=[("sensors/position_sensor", "Position Sensor"), ("sensors/accelerometer", "Accelerometer"), ("classic/generalized_speed", "Generalized Speed"),
             ("classic/point", "Point")])
M["create_accelerometer"] = dict(
    definition="An accelerometer records the acceleration of a point, in the axes of a chosen frame.",
    figure=None, figure_alt="An accelerometer: the acceleration vector of a point, with components in a frame",
    desc="A MOMDYN accelerometer records the acceleration of a point with components in a chosen frame, adding three time series to the simulation output.",
    units={},
    equations=[("The sensed quantity is the acceleration of the point P, resolved in the axes of frame F:", r"\{\mathbf{a}_P\}_F = \begin{bmatrix} a_x \\ a_y \\ a_z \end{bmatrix}")],
    notes=["TODO: confirm whether gravity is excluded, as it is from the kinematic acceleration, or included as the specific force that a physical accelerometer would feel."],
    related=[("sensors/velocity_sensor", "Velocity Sensor"), ("sensors/position_sensor", "Position Sensor"), ("classic/point", "Point"),
             ("sensors/rate_gyro", "Rate Gyro")])
M["create_dcm_sensor"] = dict(
    definition="A direction cosine matrix (DCM) sensor records the orientation of one frame relative to another as the nine entries of a rotation matrix.",
    figure=None, figure_alt="A DCM sensor: the rotation matrix between a sensed frame and a reference frame",
    desc="A MOMDYN direction cosine matrix sensor records the orientation of a frame relative to a reference frame as nine rotation-matrix entries over time.",
    units={},
    equations=[("The components of a vector in the sensed frame B follow from its components in the reference frame A:", r"\{\mathbf{v}\}_B = {}^{B}C^{A}\,\{\mathbf{v}\}_A")],
    notes=["The sensor adds nine time series, named R00 to R22 for the rows and columns of the matrix.",
           "For an orthogonal matrix the inverse is the transpose, so the matrix from A to B is the transpose of the matrix from B to A."],
    related=[("sensors/rate_gyro", "Rate Gyro"), ("classic/frame", "Frame"), ("joints/rigid_rotation", "Rigid Rotation"),
             ("joints/spherical", "Spherical Joint")])
M["create_rate_gyro"] = dict(
    definition="A rate gyro records how fast a frame is rotating, as an angular velocity in the axes of a chosen frame.",
    figure=None, figure_alt="A rate gyro: the angular velocity vector of a frame, with components in a reference frame",
    desc="A MOMDYN rate gyro records the angular velocity of a frame with components in a chosen reference frame, adding three time series to the simulation.",
    units={},
    equations=[("The sensed quantity is the angular velocity of frame B, resolved in the axes of frame F:", r"\{\boldsymbol{\omega}_B\}_F = \begin{bmatrix} \omega_x \\ \omega_y \\ \omega_z \end{bmatrix}")],
    notes=["TODO: state the frame relative to which the angular velocity is measured (the inertial frame is assumed here).",
           "A rate gyro measures angular rate. To record orientation, use a [DCM sensor](dcm_sensor.html)."],
    related=[("sensors/dcm_sensor", "DCM Sensor"), ("sensors/accelerometer", "Accelerometer"), ("joints/revolute", "Revolute Joint"),
             ("classic/frame", "Frame")])


ORD = {"0": "0th", "1": "1st", "2": "2nd"}


def generic_desc(param):
    """Descriptions for parameters that the docstrings do not document yet, from the naming pattern of the joint parameters."""
    import re
    if param == "is_form":
        return "'degree of freedom' makes the value a time-varying generalized coordinate; 'constant' fixes it at the given value."
    if param == "rotation_sequence":
        return "Euler angle sequence of the rotations, for example 'ZYX' (the default): the first angle is about the first axis, the second about the second, and so on."
    if param == "color":
        return "Color of the body in the diagram view (default Green). It does not affect the physics."
    m = re.match(r"^(kt|ct|kr|cr|equilibrium_t|equilibrium_r)(\d)$", param)
    if m:
        kind, i = m.groups()
        o = ORD[i]
        return {"kt": f"Stiffness in the {o} translational coordinate", "ct": f"Damping in the {o} translational coordinate",
                "equilibrium_t": f"Equilibrium distance in the {o} translational coordinate",
                "kr": f"Stiffness corresponding to the {o} rotation angle", "cr": f"Damping corresponding to the angular rate of the {o} rotation angle",
                "equilibrium_r": f"Equilibrium corresponding to the {o} rotation angle"}[kind]
    return None
