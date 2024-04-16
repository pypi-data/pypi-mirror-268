import pytest

from paleta.color import Color, color_average


@pytest.fixture
def color_object():
    return Color(42.2, 8.4, 5.5, 255.0)


def test_const_color():
    assert Color(127, 127, 127) == Color(127, 127, 127)
    assert Color(127, 127, 127) != Color(127, 127, 127, 0)
    assert Color(127, 127, 127, 0) == (127, 127, 127, 0)
    assert Color(256, 256, 256, 0) == (255, 255, 255, 0)
    assert Color(-12, -12, -12, 0) == (0, 0, 0, 0)


def test_r(color_object):
    assert color_object.r == 42.2

    color_object.r += 92.2
    assert color_object.r == 42.2 + 92.2

    color_object.r -= 255.0
    assert color_object.r == 0

    color_object.r = 270.0
    assert color_object.r == 255.0

    assert type(color_object.r) == float


def test_g(color_object):
    assert color_object.g == 8.4

    color_object.g += 81.2
    assert color_object.g == 8.4 + 81.2

    color_object.g -= 255.0
    assert color_object.g == 0

    color_object.g = 290.0
    assert color_object.g == 255.0

    assert type(color_object.g) == float


def test_b(color_object):
    assert color_object.b == 5.5

    color_object.b += 81.2
    assert color_object.b == 5.5 + 81.2

    color_object.b -= 255.0
    assert color_object.b == 0

    color_object.b = 280.0
    assert color_object.b == 255.0

    assert type(color_object.b) == float


def test_alpha(color_object):
    assert color_object.alpha == 255.0

    color_object.alpha += 81.2
    assert color_object.alpha == 255.0

    color_object.alpha -= 256.0
    assert color_object.alpha == 0

    color_object.alpha = 264.0
    assert color_object.alpha == 255.0

    assert type(color_object.alpha) == float


def test_rgb(color_object):
    assert color_object.rgb == (color_object.r, color_object.g, color_object.b)
    assert type(color_object.rgb) == tuple
    assert len(color_object.rgb) == 3


def test_rgba(color_object):
    assert color_object.rgba == (color_object.r, color_object.g, color_object.b, color_object.alpha)
    assert type(color_object.rgba) == tuple
    assert len(color_object.rgba) == 4


def test_irgb(color_object):
    assert color_object.irgb == (int(color_object.r), int(color_object.g), int(color_object.b))
    assert type(color_object.irgb) == tuple
    assert len(color_object.irgb) == 3


def test_irgba(color_object):
    assert color_object.irgba == (
        int(color_object.r), int(color_object.g), int(color_object.b), int(color_object.alpha))
    assert type(color_object.irgba) == tuple
    assert len(color_object.irgba) == 4


def test_bgr(color_object):
    assert color_object.bgr == (color_object.b, color_object.g, color_object.r)
    assert type(color_object.bgr) == tuple
    assert len(color_object.bgr) == 3


def test_bgra(color_object):
    assert color_object.bgra == (color_object.b, color_object.g, color_object.r, color_object.alpha)
    assert type(color_object.bgra) == tuple
    assert len(color_object.bgra) == 4


def test_hex(color_object):
    assert type(color_object.hex) == str
    assert len(color_object.hex) == 7
    assert color_object.hex == "#2a0805"


def test_dstr(color_object):
    assert str(color_object) == str(color_object.rgba)


def test_dadd(color_object):
    assert min(color_object.r + color_object.r, 255) == (color_object + color_object).r
    assert min(color_object.g + color_object.g, 255) == (color_object + color_object).g
    assert min(color_object.b + color_object.b, 255) == (color_object + color_object).b
    assert min(color_object.alpha + color_object.alpha, 255) == (color_object + color_object).alpha

    val = 10
    assert min(color_object.r + val, 255) == (color_object + val).r
    assert min(color_object.g + val, 255) == (color_object + val).g
    assert min(color_object.b + val, 255) == (color_object + val).b
    assert min(color_object.alpha + val, 255) == (color_object + val).alpha

    val = (20, 30, 40, 50)
    assert min(color_object.r + val[0], 255) == (color_object + val).r
    assert min(color_object.g + val[1], 255) == (color_object + val).g
    assert min(color_object.b + val[2], 255) == (color_object + val).b
    assert min(color_object.alpha + val[3], 255) == (color_object + val).alpha


def test_dsub(color_object):
    assert max(color_object.r - color_object.r, 0) == (color_object - color_object).r
    assert max(color_object.g - color_object.g, 0) == (color_object - color_object).g
    assert max(color_object.b - color_object.b, 0) == (color_object - color_object).b
    assert max(color_object.alpha - color_object.alpha, 0) == (color_object - color_object).alpha

    val = 10
    assert max(color_object.r - val, 0) == (color_object - val).r
    assert max(color_object.g - val, 0) == (color_object - val).g
    assert max(color_object.b - val, 0) == (color_object - val).b
    assert max(color_object.alpha - val, 0) == (color_object - val).alpha

    val = (20, 30, 40, 50)
    assert max(color_object.r - val[0], 0) == (color_object - val).r
    assert max(color_object.g - val[1], 0) == (color_object - val).g
    assert max(color_object.b - val[2], 0) == (color_object - val).b
    assert max(color_object.alpha - val[3], 0) == (color_object - val).alpha


def test_deq(color_object):
    assert color_object == color_object
    assert color_object == color_object.rgba


def test_dlt(color_object):
    assert color_object < (color_object + 10)
    assert color_object < (color_object + 10).rgba


def test_dle(color_object):
    assert color_object <= color_object
    assert color_object <= color_object.rgba
    assert color_object <= (color_object + 10)
    assert color_object <= (color_object + 10).rgba


def test_dgt(color_object):
    assert color_object > (color_object - 10)
    assert color_object > (color_object - 10).rgba


def test_dge(color_object):
    assert color_object >= color_object
    assert color_object >= color_object.rgba
    assert color_object >= (color_object - 10)
    assert color_object >= (color_object - 10).rgba


def test_dhash(color_object):
    assert color_object.__hash__() == color_object.__hash__()
    assert color_object.__hash__() == hash((color_object.rgba, color_object.hex))


def test_get_normalize(color_object):
    norm = 10
    r, g, b, a = color_object.get_normalize(normalizer=norm)
    assert color_object.r / norm == r
    assert color_object.g / norm == g
    assert color_object.b / norm == b
    assert color_object.alpha / norm == a


def test_get_inverse(color_object):
    r, g, b = color_object.get_inverse()
    assert 255 - color_object.r == r
    assert 255 - color_object.g == g
    assert 255 - color_object.b == b

    r, g, b, a = color_object.get_inverse(with_alpha=True)
    assert 255 - color_object.r == r
    assert 255 - color_object.g == g
    assert 255 - color_object.b == b
    assert 255 - color_object.alpha == a


def test_clsm_from_hex(color_object):
    nc = Color.from_hex(color_object.hex)
    assert nc.rgba == color_object.irgba

    nc = Color.from_hex("fff")
    assert (255, 255, 255, 255) == nc.rgba

    nc = Color.from_hex("#1d1d1d")
    assert (29, 29, 29, 255) == nc.rgba


def test_to_lightness(color_object):
    assert type(color_object.to_lightness()) == float
    assert color_object.to_lightness() == 0.2126 * color_object.r + 0.7152 * color_object.g + 0.0722 * color_object.b


def test_copy(color_object):
    cp = color_object.copy()
    assert color_object == cp
    assert color_object.rgba == cp.rgba

    cp.r = 20
    assert color_object != cp
    assert color_object.rgba != cp.rgba


def test_copy_inverse(color_object):
    cp = color_object.copy_inverse(with_alpha=True)
    assert color_object.get_inverse(with_alpha=True) == cp.rgba

    cp.r = 20
    assert color_object != cp
    assert color_object.get_inverse(with_alpha=True) != cp.rgba


def test_color_average(color_object):
    cavg = color_average(color_object, color_object)
    assert cavg == color_object

    cavg = color_average(Color.from_hex("fff"), Color.from_hex("000"))
    assert cavg.irgba == Color.from_hex("7f7f7f").rgba

    cavg = color_average(Color.from_hex("fff"), Color.from_hex("000"), with_alpha=True)
    assert cavg.irgba == Color.from_hex("7f7f7f").rgba
