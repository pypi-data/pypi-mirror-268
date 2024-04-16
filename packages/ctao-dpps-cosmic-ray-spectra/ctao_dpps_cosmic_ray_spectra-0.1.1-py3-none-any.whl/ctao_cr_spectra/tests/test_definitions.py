import pytest

from ctao_cr_spectra.definitions import (
    CRAB_HEGRA,
    CRAB_MAGIC_JHEAP2015,
    IRFDOC_ELECTRON_SPECTRUM,
    IRFDOC_PROTON_SPECTRUM,
    PDG_ALL_PARTICLE,
    DAMPE_P_He_SPECTRUM,
)


@pytest.mark.parametrize(
    ("spectrum", "expected_repr"),
    [
        (CRAB_HEGRA, "PowerLaw(2.83e-11 1 / (TeV s cm2) * (E / 1.0 TeV)**-2.62)"),
        (
            CRAB_MAGIC_JHEAP2015,
            "LogParabola(3.23e-11 1 / (TeV s cm2) * (E / 1.0 TeV)**(-2.47 + -0.24 * "
            "log10(E / 1.0 TeV))",
        ),
        (PDG_ALL_PARTICLE, "PowerLaw(18000.0 1 / (GeV s sr m2) * (E / 1.0 GeV)**-2.7)"),
        (
            IRFDOC_PROTON_SPECTRUM,
            "PowerLaw(9.8e-06 1 / (TeV s sr cm2) * (E / 1.0 TeV)**-2.62)",
        ),
        (
            IRFDOC_ELECTRON_SPECTRUM,
            "PowerLawWithExponentialGaussian(2.385e-09 1 / (TeV s sr cm2) * (E / 1.0 TeV)**-3.43 *"
            " (1 + 1.95 * (exp(Gauss(log10(E / 1.0 TeV), -0.101, 0.741)) - 1))",
        ),
    ],
)
def test_spectrum_repr(spectrum, expected_repr):
    actual_repr = repr(spectrum)
    assert actual_repr == expected_repr


def test_dampe_p_he_spectrum():
    from astropy import units as u

    calculated_flux = DAMPE_P_He_SPECTRUM(1 * u.TeV)
    assert pytest.approx(calculated_flux.value, 0.1) == 0.00015
    assert calculated_flux.unit == 1 / (u.GeV * u.s * u.sr * u.m**2)
