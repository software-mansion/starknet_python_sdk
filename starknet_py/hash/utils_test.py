# pylint: disable=line-too-long
# fmt: off
import pytest

from starknet_py.hash.utils import compute_hash_on_elements, pedersen_hash


@pytest.mark.parametrize(
    "data, calculated_hash",
    (
        ([1, 2, 3, 4, 5], 3442134774288875752012730520904650962184640568595562887119811371865001706826),
        ([28, 15, 39, 74], 1457535610401978056129941705021139155249904351968558303142914517100335003071),
    ),
)
def test_compute_hash_on_elements(data, calculated_hash):
    assert compute_hash_on_elements(data) == calculated_hash


@pytest.mark.parametrize(
    "x, y, hash_",
    [
        (0, 13289654017234601382751, 1606983897751845338544875557254529092665736388485573456407652201602816719974),
        (32108945712395, 0, 2286557865806578472402728224133061485859287443532833874408098272076626850762),
        (0, 0, 2089986280348253421170679821480865132823066470938446095505822317253594081284),
        (1, 1, 1321142004022994845681377299801403567378503530250467610343381590909832171180),
        (132490123765801925, 19324857132905126, 351268190682426987433778012669634681582518614860795408913953487271166523161),
        (
            1321142004022994845681377299801403567378503530250467610343381590909832171180,
            351268190682426987433778012669634681582518614860795408913953487271166523161,
            167060788452737184339236199176292038116565645273096529093530464707363566091
         ),
    ],
)
def test_pedersen_hash(first, second, hash_):
    assert pedersen_hash(first, second) == hash_
