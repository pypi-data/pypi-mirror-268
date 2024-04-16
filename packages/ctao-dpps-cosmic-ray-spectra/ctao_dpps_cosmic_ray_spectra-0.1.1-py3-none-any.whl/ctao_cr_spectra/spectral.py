"""Functions and classes for calculating spectral weights."""
from copy import copy

import astropy.units as u
import numpy as np
from astropy.table import QTable
from scipy.interpolate import interp1d

#: Unit of a point source flux
#:
#: Number of particles per Energy, time and area
POINT_SOURCE_FLUX_UNIT = (1 / u.TeV / u.s / u.m**2).unit

#: Unit of a diffuse flux
#:
#: Number of particles per Energy, time, area and solid_angle
DIFFUSE_FLUX_UNIT = POINT_SOURCE_FLUX_UNIT / u.sr


__all__ = [
    "POINT_SOURCE_FLUX_UNIT",
    "DIFFUSE_FLUX_UNIT",
    "calculate_event_weights",
    "PowerLaw",
    "LogParabola",
    "PowerLawWithExponentialGaussian",
    "TableInterpolationSpectrum",
]


@u.quantity_input(angle=u.deg)
def cone_solid_angle(angle):
    """
    Calculate the solid angle of a view cone.

    Parameters
    ----------
    angle: astropy.units.Quantity or astropy.coordinates.Angle
        Opening angle of the view cone.

    Returns
    -------
    solid_angle: astropy.units.Quantity
        Solid angle of a view cone with opening angle ``angle``.

    """
    solid_angle = 2 * np.pi * (1 - np.cos(angle)) * u.sr
    return solid_angle


@u.quantity_input(true_energy=u.TeV)
def calculate_event_weights(true_energy, target_spectrum, simulated_spectrum):
    r"""

    Calculate event weights.

    Events with a certain ``simulated_spectrum`` are reweighted to ``target_spectrum``.

    .. math::
        w_i = \frac{\Phi_\text{Target}(E_i)}{\Phi_\text{Simulation}(E_i)}

    Parameters
    ----------
    true_energy: astropy.units.Quantity[energy]
        True energy of the event
    target_spectrum: callable
        The target spectrum. Must be callable with signature (energy) -> flux
    simulated_spectrum: callable
        The simulated spectrum. Must be a callable with signature (energy) -> flux

    Returns
    -------
    weights: numpy.ndarray
        Weights for each event
    """
    return (target_spectrum(true_energy) / simulated_spectrum(true_energy)).to_value(
        u.one,
    )


class PowerLaw:
    r"""

    A power law with normalization, reference energy and index.

    Index includes the sign:

    .. math::

        \Phi(E, \Phi_0, \gamma, E_\text{ref}) =
        \Phi_0 \left(\frac{E}{E_\text{ref}}\right)^{\gamma}

    Attributes
    ----------
    normalization: astropy.units.Quantity[flux]
        :math:`\Phi_0`,
    index: float
        :math:`\gamma`
    e_ref: astropy.units.Quantity[energy]
        :math:`E_\text{ref}`
    """

    @u.quantity_input(e_ref=u.TeV)
    def __init__(self, normalization, index, e_ref=1 * u.TeV):
        """Create a new PowerLaw spectrum."""
        if index > 0:
            raise ValueError(f"Index must be < 0, got {index}")

        self.normalization = normalization
        self.index = index
        self.e_ref = e_ref

    @u.quantity_input(energy=u.TeV)
    def __call__(self, energy):
        """
        Evaluate the flux at a given energy.

        Parameters
        ----------
        energy : astropy.units.Quantity
            The energy at which to evaluate the flux. Should be in units of energy.

        Returns
        -------
        astropy.units.Quantity
            The flux at the given energy.
        """
        e = (energy / self.e_ref).to_value(u.one)
        return self.normalization * e**self.index

    def __repr__(self):
        """
        Return a string representation of the instance.

        Returns
        -------
        str
            A string representation of the instance.
        """
        return f"{self.__class__.__name__}({self.normalization} * (E / {self.e_ref})**{self.index})"

    @property
    def is_diffuse(self):
        """Returns True if the normalization has units of diffuse flux rather than point-like flux."""
        return self.normalization.unit.is_equivalent(DIFFUSE_FLUX_UNIT)

    @u.quantity_input(inner=u.deg, outer=u.deg)
    def integrate_cone(self, inner, outer):
        """
        Integrate this powerlaw over solid angle in the given cone.

        Parameters
        ----------
        inner : astropy.units.Quantity[angle]
            inner opening angle of cone
        outer : astropy.units.Quantity[angle]
            outer opening angle of cone

        Returns
        -------
        integrated : PowerLaw
            A new powerlaw instance with new normalization with the integration
            result.

        Raises
        ------
        ValueError:
            if the normalization unit does not allow a cone integration.
            if the inner radius is larger than outer radius.

        """
        if inner > outer:
            msg = f"Outer angle {outer} has to be larger than inner angle {inner}."
            raise ValueError(msg)
        if not self.is_diffuse:
            msg = "Can only integrate a diffuse flux over solid angle."
            raise ValueError(msg)
        solid_angle = cone_solid_angle(outer) - cone_solid_angle(inner)

        return PowerLaw(
            normalization=self.normalization * solid_angle,
            index=self.index,
            e_ref=self.e_ref,
        )

    @u.quantity_input(obstime=u.s)
    def integrate_time(self, obs_time):
        """

        Integrate this powerlaw over the given observation time.

        Parameters
        ----------
        obs_time: astropy.units.Quantity[time]
            Observation time to integrate the flux.

        Returns
        -------
        integrated : PowerLaw
            A new time integrated powerlaw instance.
        """
        return PowerLaw(
            normalization=self.normalization * obs_time,
            index=self.index,
            e_ref=self.e_ref,
        )

    @u.quantity_input(area=u.cm**2)
    def integrate_area(self, area):
        """

        Integrate this powerlaw over the given observatory area.

        Parameters
        ----------
        area: astropy.units.Quantity[area]
            Observation time to integrate the flux.

        Returns
        -------
        integrated : PowerLaw
            A new area integrated powerlaw instance.
        """
        return PowerLaw(
            normalization=(self.normalization * area),
            index=self.index,
            e_ref=self.e_ref,
        )

    @u.quantity_input(energy_min=u.TeV, energy_max=u.TeV)
    def integrate_energy(self, energy_min, energy_max):
        """

        Integrate this powerlaw over the given energy range.

        Parameters
        ----------
        energy_min: astropy.units.Quantity[energy]
            Minimum energy in the integration.
        energy_max: astropy.units.Quantity[energy]
            Maximum energy in the integration.

        Returns
        -------
        integrated : PowerLaw
            A new area integrated powerlaw instance.
        """
        nominator = energy_max ** (self.index + 1) - energy_min ** (self.index + 1)
        denominator = (self.index + 1) * self.e_ref**self.index

        return nominator / denominator * self.normalization

    @u.quantity_input(
        inner=u.deg,
        outer=u.deg,
        area=u.cm**2,
        energy_min=u.TeV,
        energy_max=u.TeV,
    )
    def compute_events_rate(
        self,
        inner,
        outer,
        area,
        energy_min,
        energy_max,
    ):
        """
        Integrate all the quantities from the spectrum (except time).

        Derive the events rate expected for an integration in a region of space (inner, outer),
        over the area of the observatory (area) and over an energy range (energy).

        Parameters
        ----------
        inner : astropy.units.Quantity[angle]
            inner opening angle of cone
        outer : astropy.units.Quantity[angle]
            outer opening angle of cone
        area: astropy.units.Quantity[area]
            Observation time to integrate the flux.
        energy_min: astropy.units.Quantity[energy]
            Minimum energy in the integration.
        energy_max: astropy.units.Quantity[energy]
            Maximum energy in the integration.

        Returns
        -------
        float:
            events rate integrated from the spectral distribution.
        """
        if self.is_diffuse:
            new_spectrum = self.integrate_cone(
                inner,
                outer,
            )
        else:
            new_spectrum = copy(self)
        spectrum_area = new_spectrum.integrate_area(area)
        return spectrum_area.integrate_energy(energy_min, energy_max).decompose(
            bases=[u.cm, u.TeV, u.s, u.sr],
        )

    @u.quantity_input(
        inner=u.deg,
        outer=u.deg,
        obstime=u.s,
        area=u.cm**2,
        energy_min=u.TeV,
        energy_max=u.TeV,
    )
    def compute_number_events(
        self,
        inner,
        outer,
        obs_time,
        area,
        energy_min,
        energy_max,
    ):
        """

        Integrate all the quantities from the spectrum and derive the total number of events.

        Parameters
        ----------
        inner : astropy.units.Quantity[angle]
            inner opening angle of cone
        outer : astropy.units.Quantity[angle]
            outer opening angle of cone
        obs_time: astropy.units.Quantity[time]
            Observation time to integrate the flux.
        area: astropy.units.Quantity[area]
            Observation time to integrate the flux.
        energy_min: astropy.units.Quantity[energy]
            Minimum energy in the integration.
        energy_max: astropy.units.Quantity[energy]
            Maximum energy in the integration.

        Returns
        -------
        float:
            number of events integrated from the spectral distribution.
        """
        spectrum_cone = self.compute_events_rate(
            inner,
            outer,
            area,
            energy_min,
            energy_max,
        )
        n_events = (spectrum_cone * obs_time).to_value(u.one)
        return n_events


class LogParabola:
    r"""

    A log parabola flux parameterization.

    .. math::

        \Phi(E, \Phi_0, \alpha, \beta, E_\text{ref}) =
        \Phi_0 \left(
            \frac{E}{E_\text{ref}}
        \right)^{\alpha + \beta \cdot \log_{10}(E / E_\text{ref})}

    Attributes
    ----------
    normalization: astropy.units.Quantity[flux]
        :math:`\Phi_0`,
    a: float
        :math:`\alpha`
    b: float
        :math:`\beta`
    e_ref: astropy.units.Quantity[energy]
        :math:`E_\text{ref}`
    """

    @u.quantity_input(
        normalization=[DIFFUSE_FLUX_UNIT, POINT_SOURCE_FLUX_UNIT],
        e_ref=u.TeV,
    )
    def __init__(self, normalization, a, b, e_ref=1 * u.TeV):
        """
        Initialize the instance.

        Parameters
        ----------
        normalization : astropy.units.Quantity
            The normalization factor for the flux, either in diffuse or point source units.
        a : float
            Parameter 'a' for the instance.
        b : float
            Parameter 'b' for the instance.
        e_ref : astropy.units.Quantity, optional
            Reference energy for normalization. Defaults to 1 TeV.
        """
        self.normalization = normalization
        self.a = a
        self.b = b
        self.e_ref = e_ref

    @u.quantity_input(energy=u.TeV)
    def __call__(self, energy):
        """
        Evaluate the flux at a given energy.

        Parameters
        ----------
        energy : astropy.units.Quantity
            The energy at which to evaluate the flux. Should be in units of energy.

        Returns
        -------
        astropy.units.Quantity
            The flux at the given energy.
        """
        e = (energy / self.e_ref).to_value(u.one)
        return self.normalization * e ** (self.a + self.b * np.log10(e))

    def __repr__(self):
        """
        Return a string representation of the instance.

        Returns
        -------
        str
            A string representation of the instance.
        """
        return f"{self.__class__.__name__}({self.normalization} * (E / {self.e_ref})**({self.a} + {self.b} * log10(E / {self.e_ref}))"


class PowerLawWithExponentialGaussian(PowerLaw):
    r"""
    A power law with an additional Gaussian bump.

    Beware that the Gaussian is not normalized!

    .. math::

        \Phi(E, \Phi_0, \gamma, f, \mu, \sigma, E_\text{ref}) =
        \Phi_0 \left(
            \frac{E}{E_\text{ref}}
        \right)^{\gamma}
        \cdot \left(
            1 + f \cdot
            \left(
                \exp\left(
                    \operatorname{Gauss}(\log_{10}(E / E_\text{ref}), \mu, \sigma)
                \right) - 1
            \right)
        \right)

    Where :math:`\operatorname{Gauss}` is the unnormalized Gaussian distribution:

    .. math::
        \operatorname{Gauss}(x, \mu, \sigma) = \exp\left(
            -\frac{1}{2} \left(\frac{x - \mu}{\sigma}\right)^2
        \right)

    Attributes
    ----------
    normalization: astropy.units.Quantity[flux]
        :math:`\Phi_0`,
    a: float
        :math:`\alpha`
    b: float
        :math:`\beta`
    e_ref: astropy.units.Quantity[energy]
        :math:`E_\text{ref}`
    """

    @u.quantity_input(
        normalization=[DIFFUSE_FLUX_UNIT, POINT_SOURCE_FLUX_UNIT],
        e_ref=u.TeV,
    )
    def __init__(self, normalization, index, e_ref, f, mu, sigma):
        """Create a new PowerLawWithExponentialGaussian spectrum."""
        super().__init__(normalization=normalization, index=index, e_ref=e_ref)
        self.f = f
        self.mu = mu
        self.sigma = sigma

    @u.quantity_input(energy=u.TeV)
    def __call__(self, energy):
        """
        Evaluate the flux at a given energy.

        Parameters
        ----------
        energy : astropy.units.Quantity
            The energy at which to evaluate the flux. Should be in units of energy.

        Returns
        -------
        astropy.units.Quantity
            The flux at the given energy.
        """
        power = super().__call__(energy)
        log10_e = np.log10(energy / self.e_ref)
        # ROOT's TMath::Gauss does not add the normalization
        # this is missing from the IRFDocs
        # the code used for the plot can be found here:
        # https://gitlab.cta-observatory.org/cta-consortium/aswg/irfs-macros/cosmic-rays-spectra/-/blob/master/electron_spectrum.C#L508
        gauss = np.exp(-0.5 * ((log10_e - self.mu) / self.sigma) ** 2)
        return power * (1 + self.f * (np.exp(gauss) - 1))

    def __repr__(self):
        """
        Return a string representation of the instance.

        Returns
        -------
        str
            A string representation of the instance.
        """
        s = super().__repr__()
        gauss = f"Gauss(log10(E / {self.e_ref}), {self.mu}, {self.sigma})"
        return s[:-1] + f" * (1 + {self.f} * (exp({gauss}) - 1))"


class TableInterpolationSpectrum:
    """
    Spectrum interpolating tabulated values.

    By default, flux is interpolated linearly in log-log space.
    """

    def __init__(
        self,
        energy,
        flux,
        log_energy=True,
        log_flux=True,
        reference_energy=1 * u.TeV,
    ):
        self.energy = energy
        self.flux = flux
        self.flux_unit = flux.unit
        self.log_energy = log_energy
        self.log_flux = log_flux
        self.reference_energy = reference_energy

        x = (energy / reference_energy).to_value(u.one)
        y = flux.to_value(self.flux_unit)

        if log_energy:
            x = np.log10(x)

        if log_flux:
            y = np.log10(y)

        self.interp = interp1d(x, y, bounds_error=False, fill_value="extrapolate")

    def __call__(self, energy):
        """
        Evaluate the flux at a given energy.

        Parameters
        ----------
        energy : astropy.units.Quantity
            The energy at which to evaluate the flux.

        Returns
        -------
        astropy.units.Quantity
            The flux at the given energy.
        """
        x = (energy / self.reference_energy).to_value(u.one)

        if self.log_energy:
            x = np.log10(x)

        y = self.interp(x)

        if self.log_flux:
            y = 10**y

        return u.Quantity(y, self.flux_unit, copy=False)

    @classmethod
    def from_table(
        cls,
        table: QTable,
        log_energy=True,
        log_flux=True,
        reference_energy=1 * u.TeV,
    ):
        """
        Create a TableInterpolationSpectrum instance from table.

        Parameters
        ----------
        cls : class
            The class itself (implicit).
        table : astropy.table.QTable
            Table containing energy and flux data.
        log_energy : bool, optional
            Whether to log-transform the energy values. Defaults to True.
        log_flux : bool, optional
            Whether to log-transform the flux values. Defaults to True.
        reference_energy : astropy.units.Quantity, optional
            The reference energy for normalization. Defaults to 1 TeV.

        Returns
        -------
        instance
            An instance of the class populated with data from the table.
        """
        return cls(
            table["energy"],
            table["flux"],
            log_energy=log_energy,
            log_flux=log_flux,
            reference_energy=reference_energy,
        )

    @classmethod
    def from_file(
        cls,
        path,
        log_energy=True,
        log_flux=True,
        reference_energy=1 * u.TeV,
    ):
        """
        Create a TableInterpolationSpectrum instance from file.

        Parameters
        ----------
        cls : class
            The class itself (implicit).
        path : str
            The path to the data file.
        log_energy : bool, optional
            Whether to log-transform the energy values. Defaults to True.
        log_flux : bool, optional
            Whether to log-transform the flux values. Defaults to True.
        reference_energy : astropy.units.Quantity, optional
            The reference energy for normalization. Defaults to 1 TeV.

        Returns
        -------
        instance
            An instance of the class populated with data from the file.
        """
        return cls.from_table(
            QTable.read(path),
            log_energy=log_energy,
            log_flux=log_flux,
            reference_energy=reference_energy,
        )
