from .get_utms import ALL_UTMS
import pytest

TESTS = (
    [(name, "standard") for name in ALL_UTMS.keys()]
    + [(name, "double") for name in ALL_UTMS.keys()]
    + [(name, "eights") for name in ALL_UTMS]
)


@pytest.mark.parametrize("name,precision", TESTS)
def test_fqir_runtime(name, precision):
    ALL_UTMS[name].test_fqir_runtime(bw_conf=precision)


@pytest.mark.parametrize("name", list(ALL_UTMS.keys()))
def test_fqir_runtime_with_round(name):
    import fmot

    fmot.CONFIG.quant_round = True
    ALL_UTMS[name].allow_fqir_offby = 9
    ALL_UTMS[name].test_fqir_runtime(bw_conf="double")
    fmot.CONFIG.quant_round = False
