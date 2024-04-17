"""A module containing the helical push spring class"""
from math import pi, sqrt
from sympy import Symbol, symbols

from me_toolbox.fatigue import FailureCriteria
from me_toolbox.springs import Spring
from me_toolbox.tools import percent_to_decimal


class HelicalCompressionSpring(Spring):
    """A helical push spring object"""

    def __init__(self, max_force, wire_diameter, spring_diameter, ultimate_tensile_strength,
                 shear_yield_percent, shear_modulus, elastic_modulus, end_type,
                 spring_rate=None, active_coils=None, free_length=None,
                 set_removed=False, shot_peened=False,
                 density=None, working_frequency=None, anchors=None,
                 zeta=0.15):
        """Instantiate helical push spring object with the given parameters

        :param float or Symbol max_force: The maximum load on the spring [N]
        :param float or Symbol wire_diameter: Spring wire diameter [mm]
        :param float or Symbol spring_diameter: Spring diameter measured from [mm]
            the center point of the wire diameter
        :param float ultimate_tensile_strength: Ultimate tensile strength of the material [MPa]
        :param float shear_yield_percent: Yield percent used to estimate shear_yield_stress
        :param float shear_modulus: Shear modulus [MPa]
        :param float or None elastic_modulus: Elastic modulus (used for buckling calculations) [MPa]
        :param str end_type: What kind of ending the spring has (effects length and number of coils)
            ,the options are: 'plain', 'plain and ground', 'squared or closed', 'squared and ground'
        :param float or None spring_rate: Spring rate (k) [N/mm]
        :param float or None active_coils: Number of active coils (Na)
        :param float or None free_length: Spring length when no force is applied (L0)
        :param bool set_removed: If True adds to STATIC strength
            (must NOT use for fatigue application)
        :param bool shot_peened: If True adds to fatigue strength
        :param float or None density: Material density (used for finding natural frequency) [kg/m^3]
        :param float or None working_frequency: the spring working frequency [Hz]
        :param str or None anchors: How the spring is anchored (for buckling test),
            The options are: 'fixed-fixed', 'fixed-hinged', 'hinged-hinged', 'clamped-free'

            (used for buckling calculations)
        :param float zeta: Overrun safety factor

        :returns: HelicalCompressionSpring object
        """

        super().__init__(max_force, wire_diameter, spring_diameter, ultimate_tensile_strength,
                         shear_modulus, elastic_modulus, shot_peened, density, working_frequency)

        if set_removed:
            print("Note: set should ONLY be removed for static loading"
                  "and NOT for periodical loading")

        self.set_removed = set_removed
        self.shot_peened = shot_peened
        self.shear_yield_percent = shear_yield_percent
        self.zeta = zeta  # overrun safety factor

        self.end_type = end_type.lower()
        end_types = ('plain', 'plain and ground', 'squared or closed', 'squared and ground')
        if self.end_type not in end_types:
            raise ValueError(f"{end_type} not one of this: {end_types}")

        if (active_coils is None) and (spring_rate is None):
            raise ValueError("active_coils and the spring_rate can't both be None,"
                             "Tip: Find the spring rate")
        elif active_coils is None:
            self.spring_rate = spring_rate
        elif spring_rate is None:
            self.active_coils = active_coils
        else:
            raise ValueError("Both active coils and spring rate were"
                             "given but only one is expected")

        self.free_length = free_length
        self.anchors = anchors

        self.check_design()

    def check_design(self):
        """Check if the spring index,active_coils,zeta and free_length
        are in acceptable range for good design

        :returns: True if all the checks are good
        :rtype: bool
        """
        good_design = True
        C = self.spring_index  # pylint: disable=invalid-name
        if isinstance(C, float) and not 4 <= C <= 12 and self.set_removed:
            print("Note: C - spring index should be in range of [4,12],"
                  "lower C causes surface cracks,\n"
                  "higher C causes the spring to tangle and requires separate packing")
            good_design = False
        elif isinstance(C, float) and not 3 <= C <= 12:
            print("Note: C - spring index should be in range of [3,12],"
                  "lower C causes surface cracks,\n"
                  "higher C causes the spring to tangle and requires separate packing")
            good_design = False

        active_coils = self.active_coils
        if isinstance(active_coils, float) and not 3 <= active_coils <= 15:
            print(f"Note: active_coils={active_coils:.2f} is not in range [3,15],"
                  f"this can cause non linear behavior")
            good_design = False

        if not self._free_length_input_flag:
            print(f"Note: the free length was not given so Fsolid={self.Fsolid:.2f} "
                  f"was estimated using zeta={self.zeta}")

        zeta = self.zeta
        if zeta < 0.15:
            print(f"Note: zeta={zeta:.2f} is smaller then 0.15,"
                  f"the spring could reach its solid length")
            good_design = False
        if (self.free_length is not None) and (self.anchors is not None) \
                and (self.elastic_modulus is not None):
            buckling, safe_length = self.buckling(self.anchors, verbose=False)
            if buckling:
                print(f"Note: buckling is accruing, max free length"
                      f"(free_length)= {safe_length:.2f}, "
                      f"free_length= {self.free_length:.2f}")
                good_design = False

        if (self.density is not None) and (self.working_frequency is not None):
            natural_freq = self.natural_frequency
            if natural_freq <= 20 * self.working_frequency:
                print(
                    f"Note: the natural frequency={natural_freq:.2f} is less than 20*working"
                    f"frequency={20 * self.working_frequency:.2f} which is not good")
                good_design = False

        return good_design

    @property
    def shear_yield_strength(self):
        """ Ssy - yield strength for shear
        (shear_yield_stress = % * ultimate_tensile_strength))

        :returns: yield strength for shear stress
        :rtype: float
        """
        try:
            return percent_to_decimal(self.shear_yield_percent) * self.ultimate_tensile_strength
        except TypeError:
            return self.shear_yield_percent * self.ultimate_tensile_strength

    @property
    def wire_diameter(self):
        """Getter for the wire diameter attribute

        :returns: The spring's wire diameter
        :rtype: float or Symbol
        """
        return self._wire_diameter

    @wire_diameter.setter
    def wire_diameter(self, diameter):
        """Sets the wire diameter and updates relevant attributes

        :param float diameter: Spring's wire diameter
        """
        self._wire_diameter = diameter
        # updating active_coils and free length with the new diameter
        self.active_coils = None
        self.free_length = None

    @property
    def spring_diameter(self):
        """Getter for the spring diameter attribute

        :returns: The spring diameter
        :rtype: float or Symbol
        """
        return self._spring_diameter

    @spring_diameter.setter
    def spring_diameter(self, diameter):
        """Sets the spring diameter and updates relevant attributes

        :param float diameter: Spring's diameter
        """
        self._spring_diameter = diameter
        # updating active_coils and free length with the new diameter
        self.active_coils = None
        self.free_length = None

    @property
    def active_coils(self):
        """getter for the :attr:`active_coils` attribute

        :returns: The spring active coils
        :rtype: float
        """
        return self._active_coils

    @active_coils.setter
    def active_coils(self, active_coils):
        """getter for the :attr:`active_coils` attribute
        the method checks if active_coils was given and if not
        it calculates it form the other known parameters and then
        update the :attr:`spring_rate` attribute to match

        :param float or None active_coils: Spring active coils
        """
        if active_coils is not None:
            # active_coils was given
            self._active_coils = active_coils
            # recalculate spring rate and free_length according to the new active_coils
            self.spring_rate = None
            self.free_length = None
        else:
            # active_coils was not given so calculate it
            self._active_coils = self.calc_active_coils()

    def calc_active_coils(self):
        """Calculate active_coils which is the number of active coils (using Castigliano's theorem)

        :returns: number of active coils
        :rtype: float
        """
        return ((self.shear_modulus * self.wire_diameter) /
                (8 * self.spring_index ** 3 * self.spring_rate)) * (
                       (2 * self.spring_index ** 2) / (1 + 2 * self.spring_index ** 2))

    @property
    def spring_rate(self):
        """getter for the :attr:`spring_rate` attribute

        :returns: The spring rate
        :rtype: float
        """
        return self._spring_rate

    @spring_rate.setter
    def spring_rate(self, spring_rate):
        """getter for the :attr:`spring_rate` attribute
        the method checks if the spring rate was given and if not
        it calculates it form the other known parameters and then
        update the :attr:`active_coils` attribute to match

        :param float or None spring_rate: K - The spring rate
        """
        if spring_rate is not None:
            # spring_rate was given
            self._spring_rate = spring_rate
            # recalculate active_coils and the free length according to the new spring_rate
            self.active_coils = None
            self.free_length = None
        else:
            # spring_rate was not given so calculate it
            self._spring_rate = self.calc_spring_rate()

    @property
    def factor_Ks(self):  # pylint: disable=invalid-name
        """factor_Ks - Static shear stress concentration factor

        :returns: Static shear stress concentration factor
        :rtype: float
        """
        return (2 * self.spring_index + 1) / (2 * self.spring_index)

    @property
    def factor_Kw(self):  # pylint: disable=invalid-name
        """K_W - Wahl shear stress concentration factor

        :returns: Wahl shear stress concentration factor
        :rtype: float
        """
        return (4 * self.spring_index - 1) / (4 * self.spring_index - 4) + \
               (0.615 / self.spring_index)

    @property
    def factor_KB(self):  # pylint: disable=invalid-name
        """K_B - Bergstrasser shear stress concentration factor (very close to factor_Kw)

        NOT IMPLEMENTED!!!

        :returns: Bergstrasser shear stress concentration factor
        :rtype: float
        """
        return (4 * self.spring_index + 2) / (4 * self.spring_index - 3)

    @property
    def max_shear_stress(self):
        """ Return's the shear stress

        :returns: Shear stress
        :rtype: float
        """
        k_factor = self.factor_Ks if self.set_removed else self.factor_Kw
        return self.calc_max_shear_stress(self.max_force, k_factor)

    @property
    def max_deflection(self):
        """Returns the spring max_deflection, It's change in length

        :returns: Spring max_deflection
        :rtype: float or Symbol
        """
        return self.calc_deflection(self.max_force)

    def calc_deflection(self, force):
        """Calculate the spring deflection (change in length) due to specific max_force

        :param float or Symbol force: Spring working max_force

        :returns: Spring deflection
        :rtype: float or Symbol
        """
        C = self.spring_index
        d = self.wire_diameter
        G = self.shear_modulus
        Na = self.active_coils
        return ((8 * force * C ** 3 * Na) / (G * d)) * ((1 + 2 * C ** 2) / (2 * C ** 2))

    @property
    def end_coils(self):
        """Ne - the end coils of the spring

        :returns: Number of the spring end coils
        :rtype: float or Symbol
        """
        options = {'plain': 0,
                   'plain and ground': 1,
                   'squared or closed': 2,
                   'squared and ground': 2}
        return options.get(self.end_type)

    @property
    def total_coils(self):
        """Nt - the total coils of the spring

        :returns: Number of the spring total coils
        :rtype: float or Symbol
        """
        return self.end_coils + self.active_coils

    @property
    def solid_length(self):
        """Ls - the solid length of the spring
        (if the spring is fully compressed so the coils are touching each other)

        :returns: Spring solid length (when all the coils are touching)
        :rtype: float or Symbol
        """
        diameter = self.wire_diameter
        total_coils = self.total_coils
        options = {'plain': diameter * (total_coils + 1),
                   'plain and ground': diameter * total_coils,
                   'squared or closed': diameter * (total_coils + 1),
                   'squared and ground': diameter * total_coils}
        return options.get(self.end_type)

    @property
    def Fsolid(self):  # pylint: disable=invalid-name
        """calculate the max_force necessary to bring the spring to solid length
        it is good practice for the max_force that compresses the spring to
        solid state to be greater than the maximum max_force anticipated, so we
        use this calculation: Fs=(1+zeta)Fmax in case the free length is unknown

        Note: zeta is the overrun safety factor, it's customary that zeta=0.15 so Fs=1.15Fmax

        :returns: The max_force it takes to get the spring to solid length
        :rtype: float
        """
        if self._free_length_input_flag:
            # if free_length is given
            return self.spring_rate * (self.free_length - self.solid_length)
        else:
            # if free_length is unknown make an estimation
            return (1 + self.zeta) * self.max_force

    @property
    def free_length(self):
        """ getter for the :attr:`free_length` attribute

        :returns: free length of the springs
        :rtype: float
        """
        return self._free_length

    @free_length.setter
    def free_length(self, free_length):
        """free_length setter methods
        if free length is specified assign it and set the
        _free_length_input_flag for the :attr:`Fsolid` method
        if free length is not specified calculate it using :meth:`calc_free_length()`
        :param float or None free_length: The free length of the spring
        """
        self._free_length_input_flag = False if free_length is None else True
        self._free_length = self.calc_free_length() if free_length is None else free_length

    def calc_free_length(self):
        """Calculates the free length of the spring"""
        return (self.Fsolid / self.spring_rate) + self.solid_length

    def static_safety_factor(self, solid=False):
        """ Returns the static safety factor according to the object attributes

        :returns: static factor of safety
        :type: float or Symbol
        """
        k_factor = self.factor_Ks if self.set_removed else self.factor_Kw
        shear_stress = self.calc_max_shear_stress(self.Fsolid,
                                                  k_factor) if solid else self.max_shear_stress
        return self.shear_yield_strength / shear_stress

    def min_wire_diameter(self, safety_factor, spring_diameter=None, spring_index=None,
                          solid=False):
        """The minimal wire diameter for given
        safety factor in order to avoid failure,
        according to the spring parameters.
        if solid is True the calculation uses :attr:`Fsolid`
        instead of :attr:`max_force`

        Note: In order for the calculation to succeed the spring
            diameter or the spring index should be known

        :param float safety_factor: Static safety factor
        :param float spring_diameter: The spring diameter
        :param float spring_index: The spring index
        :param bool solid: If true calculate to according to the solid max_force

        :returns: The minimal wire diameter
        :rtype: float or Symbol
        """
        if spring_index is not None:
            factor_ks = (2 * spring_index + 1) / (2 * spring_index)
            factor_kw = (4 * spring_index - 1) / (4 * spring_index - 4) + (0.615 / spring_index)
            factor_k = factor_ks if self.set_removed else factor_kw
            force = self.Fsolid if solid else self.max_force
            return ((8 * factor_k * force * spring_index * safety_factor) / (
                    self.shear_yield_percent * self.Ap * pi)) ** (1 / (2 - self.m))

        elif spring_index is None and spring_diameter is not None:

            factor_k, temp_k = 1.1, 0
            diam = 0
            while abs(factor_k - temp_k) > 1e-4:
                # waiting for k to converge
                diam = ((8 * self.max_force * spring_diameter * safety_factor * factor_k) / (
                        pi * self.shear_yield_percent * self.Ap)) ** (1 / (3 - self.m))
                temp_k = factor_k
                factor_ks = (2 * spring_diameter + diam) / (2 * spring_diameter)
                factor_kb = (4 * spring_diameter + 2 * diam) / (4 * spring_diameter - 3 * diam)
                factor_k = factor_ks if self.set_removed else factor_kb
            return diam
        else:
            print("Need to know spring index or spring diameter to calculate wire diameter")

    def min_spring_diameter(self, safety_factor, wire_diameter, solid=False):
        """return the minimum spring diameter to avoid static failure
        according to the specified safety factor, if the solid flag is True :attr:'Fsolid'
        is used instead of :attr:`max_force`

        :param float safety_factor: static safety factor
        :param float wire_diameter: Spring's wire diameter
        :param bool solid: If true calculate to according to the solid max_force

        :returns: The minimal spring diameter
        :rtype: float or Symbol
        """
        force = self.Fsolid if solid else self.max_force
        d = wire_diameter
        if self.set_removed:
            Ssy = self.shear_yield_strength
            return 0.5 * ((Ssy / safety_factor) * ((pi * d ** 3) / (4 * force)) - d)
        else:
            # derived using the KB factor (because it was easier)
            Sut = self.ultimate_tensile_strength
            alpha = (Sut * pi * d ** 3) / (8 * self.max_force * safety_factor)
            return 0.25 * ((2 * alpha - d) + sqrt((d - 2 * alpha) ** 2 - 24 * alpha * d))

    def buckling(self, anchors, verbose=True):
        """ Checks if the spring will buckle and find the
        maximum free length to avoid buckling
        :param str or None anchors: How the spring is anchored
            (The options are: 'fixed-fixed', 'fixed-hinged', 'hinged-hinged', 'clamped-free')
        :param bool verbose: Print buckling test result
        :returns: True if buckling occurring and The maximum safe length (free_length)
            to avoid buckling
        :rtype: tuple(bool, float)
        """
        # alpha values from table 10-2
        options = {'fixed-fixed': 0.5, 'fixed-hinged': 0.707, 'hinged-hinged': 1, 'clamped-free': 2}

        try:
            D = self.spring_diameter
            E = self.elastic_modulus
            G = self.shear_modulus
            alpha = options[anchors.lower()]
            max_safe_length = (pi * D / alpha) * sqrt((2 * (E - G)) / (2 * G + E))
        except ValueError as err:
            print(f"{err}, make sure E and G have the same units (Mpa)")
        except KeyError as key:
            print(f"Ends: {key} is unknown ")
        except AttributeError:
            print("Anchors not specified")
        else:
            if verbose:
                if self.free_length >= max_safe_length:
                    print(f"Buckling is accruing, the max safe length = {max_safe_length:.2f}, ",
                          f"but the free_length = {self.free_length:.2f}")

                else:
                    print(f"Buckling is NOT accruing, the max safe length = {max_safe_length:.2f}, ",
                          f"and the free_length = {self.free_length:.2f}")

            return self.free_length >= max_safe_length, max_safe_length

    def fatigue_analysis(self, max_force, min_force, reliability,
                         criterion='modified goodman', verbose=False, metric=True):
        """ Returns safety factors for fatigue and
        for first cycle according to Langer

        :param float max_force: Maximal max_force acting on the spring
        :param float min_force: Minimal max_force acting on the spring
        :param float reliability: in percentage
        :param str criterion: fatigue criterion
        :param bool verbose: print more details
        :param bool metric: Metric or imperial

        :returns: static and dynamic safety factor
        :rtype: tuple[float, float]
        """
        # calculating mean and alternating forces
        alternating_force = abs(max_force - min_force) / 2
        mean_force = (max_force + min_force) / 2

        # calculating mean and alternating stresses
        k_factor = self.factor_Ks if self.set_removed else self.factor_Kw
        alt_shear_stress = self.calc_max_shear_stress(alternating_force, k_factor)
        mean_shear_stress = self.calc_max_shear_stress(mean_force, k_factor)

        Sse = self.shear_endurance_limit(reliability, metric)
        Ssu = self.shear_ultimate_strength
        Ssy = self.shear_yield_strength
        nf, nl = FailureCriteria.get_safety_factors(Ssy, Ssu, Sse, alt_shear_stress,
                                                    mean_shear_stress, criterion)
        if verbose:
            print(f"Alternating force = {alternating_force:.2f}, Mean force = {mean_force:.2f}\n"
                  f"Alternating shear stress = {alt_shear_stress:.2f}, "
                  f"Mean shear stress = {mean_shear_stress:.2f}\n"
                  f"Sse = {Sse:.2f}")
        return nf, nl

    def calc_spring_index(self, solid_safety_factor):
        """Calculate Spring index for certain safety factor if only wire diameter was given
        but the spring diameter was not (from Shigley's)

        :param float solid_safety_factor: Spring's safety factor for solid length

        :returns: Spring's index number
        """
        alpha = self.shear_yield_strength / solid_safety_factor
        beta = (8 * self.Fsolid) / (pi * self.wire_diameter ** 2)
        if self.set_removed:
            # for factor_Ks
            return (alpha / beta) + 0.5
        else:
            # for factor_Kw
            try:
                return (alpha - 0.365 * beta) / (2 * beta) + (
                    (0.966 * sqrt(0.268 * alpha ** 2 - alpha * beta + 0.53 * beta ** 2))) / beta
            except TypeError as type_error:
                raise ValueError("In this method diameter can't be symbolic") from type_error
            # for Kb NOT IMPLEMENTED!!!
            # return ((2 * alpha - beta) / (4 * beta)) + sympy.sqrt(
            #     ((2 * alpha - beta) / (4 * beta)) ** 2 - ((3 * alpha) / (4 * beta)))