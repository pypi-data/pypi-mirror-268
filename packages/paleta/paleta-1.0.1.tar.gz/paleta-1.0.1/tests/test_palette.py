import pytest

from paleta.color import Color, color_average
from paleta.palette import Palette, ConversionPalette, maximize_by_average, minimize_by_average


@pytest.fixture
def palette_object():
    return Palette(
        Color.from_hex("#531380"),
        Color.from_hex("#d7820e"),
        Color.from_hex("#60d048"),
        Color.from_hex("#f8c630"),
    )


def test_const_palette():
    assert Palette() == Palette()
    assert Palette(Color.from_hex("fff")) == Palette(Color.from_hex("fff"))
    assert Palette(Color.from_hex("fff"), Color.from_hex("000")) == Palette(Color.from_hex("000"), Color.from_hex("fff"))

    with pytest.raises(ValueError):
        Palette(0)
        Palette(0x1)
        Palette((0, 1, 2, 3, 4, 5, 6, 7, 8))
        Palette(0, 1, 2, 3, 45)
        Palette(Palette(Color.from_hex("fff")))

    assert Palette() == Palette()


def test_palette_color_set(palette_object):
    assert len(palette_object.color_set) == len(palette_object.colors)
    assert type(palette_object.color_set) == set

    assert (83, 19, 128, 255) in palette_object.color_set
    assert (215, 130, 14, 255) in palette_object.color_set
    assert (96, 208, 72, 255) in palette_object.color_set
    assert (248, 198, 48, 255) in palette_object.color_set


def test_palette_colors(palette_object):
    assert len(palette_object.color_set) == len(palette_object.color_set)
    assert type(palette_object.color_set) == set


def test_palette_add(palette_object):
    nc = Color.from_hex("fff")
    palette_object.add(nc)
    assert nc in palette_object
    assert nc in palette_object.colors
    assert nc.rgba in palette_object.color_set

    nc = (0, 0, 0, 255)
    palette_object.add(nc)
    assert nc in palette_object
    assert nc in palette_object.color_set

    nc = 1
    with pytest.raises(ValueError):
        palette_object.add(nc)


def test_palette_remove(palette_object):
    nc = Color.from_hex("531380")
    palette_object.remove(nc)
    assert nc not in palette_object
    assert nc not in palette_object.colors
    assert nc.rgba not in palette_object.color_set

    with pytest.raises(KeyError):
        nc = (83, 19, 128, 255)
        palette_object.remove(nc)
        assert nc not in palette_object
        assert nc not in palette_object.color_set

    nc = (215, 130, 14, 255)
    palette_object.remove(nc)
    assert nc not in palette_object
    assert nc not in palette_object.color_set

    nc = 1
    with pytest.raises(ValueError):
        palette_object.add(nc)


def test_palette_clear(palette_object):
    palette_object.clear()

    assert len(palette_object) == 0
    assert len(palette_object.colors) == 0
    assert len(palette_object.color_set) == 0


def test_palette_iter(palette_object):
    for idx, palette in enumerate(palette_object):
        assert isinstance(palette, Color)

    assert idx == len(palette_object) - 1


def test_palette_dlen(palette_object):
    assert len(palette_object) == len(palette_object.colors)
    assert len(palette_object) == len(palette_object.color_set)


def test_palette_deq(palette_object):
    assert palette_object == palette_object
    assert palette_object != Palette()
    assert palette_object == palette_object.colors
    assert 0 != palette_object
    assert 0x1212 != palette_object
    assert [(255, 255, 255, 0), ] != palette_object
    assert ((255, 255, 255, 0),) != palette_object


def test_palette_dor(palette_object):
    assert palette_object | palette_object == palette_object
    assert palette_object | Palette(Color.from_hex("fff")) != palette_object

    with pytest.raises(TypeError):
        assert palette_object | None
        assert palette_object | 121
        assert palette_object | 0x131


def test_palette_dadd(palette_object):
    assert palette_object + palette_object == palette_object
    assert palette_object + Palette(Color.from_hex("fff")) != palette_object

    palette_object += Palette(Color.from_hex("000"))
    assert palette_object + Palette(Color.from_hex("000")) == palette_object

    with pytest.raises(TypeError):
        assert palette_object + None
        assert palette_object + 100
        assert palette_object + 0x24


def test_palette_dand(palette_object):
    np = Palette(Color.from_hex("FFF"))
    op = Palette()

    assert palette_object & palette_object == palette_object
    assert palette_object.colors & palette_object.colors == palette_object.colors
    assert palette_object & np == np & palette_object
    assert palette_object.colors & op.colors == op.colors  # Intersect with Empty Set

    with pytest.raises(TypeError):
        assert palette_object & None
        assert palette_object & set()
        assert palette_object & Color()


def test_palette_dsub(palette_object):
    mp = Palette(Color.from_hex("531380"))
    np = Palette(Color.from_hex("FFF"))
    op = Palette()

    assert palette_object - palette_object == op
    assert palette_object.colors - palette_object.colors == op.colors
    assert palette_object - mp == Palette(
        Color.from_hex("#d7820e"),
        Color.from_hex("#60d048"),
        Color.from_hex("#f8c630"),
    )
    assert palette_object - np == palette_object  # No Intersection
    assert palette_object - np != np - palette_object  # Not Commutative (ofc)
    assert palette_object.colors - op.colors == palette_object.colors  # Difference with Empty Set

    with pytest.raises(TypeError):
        assert palette_object - None
        assert palette_object - Color


def test_palette_dcontains(palette_object):
    assert Color.from_hex("f8c630") in palette_object
    assert Color.from_hex("fff") not in palette_object

    assert (96, 208, 72, 255) in palette_object
    assert (96, 208, 72, 0) not in palette_object

    assert 0 not in palette_object
    assert None not in palette_object
    assert 0x1 not in palette_object
    assert 10000000000 not in palette_object

    with pytest.raises(TypeError):
        assert palette_object not in palette_object


def test_palette_union(palette_object):
    mp = Palette(Color.from_hex("531380"))
    np = Palette(Color.from_hex("FFF"))

    assert palette_object.union(palette_object) == palette_object
    assert palette_object.union(Palette()) == palette_object
    assert palette_object.union(mp) == palette_object
    assert palette_object.union(np) == np.union(palette_object)


def test_palette_difference(palette_object):
    mp = Palette(Color.from_hex("531380"))
    np = Palette(Color.from_hex("FFF"))

    assert palette_object.difference(palette_object) == Palette()
    assert palette_object.difference(Palette()) == palette_object
    assert palette_object.difference(mp) == Palette(
        Color.from_hex("#d7820e"),
        Color.from_hex("#60d048"),
        Color.from_hex("#f8c630"),
    )
    assert palette_object.difference(np) == palette_object
    assert palette_object.difference(np) != np.difference(palette_object)


def test_palette_intersection(palette_object):
    mp = Palette(Color.from_hex("531380"))
    np = Palette(Color.from_hex("FFF"))

    assert palette_object.intersection(palette_object) == palette_object
    assert palette_object.intersection(Palette()) == Palette()
    assert palette_object.intersection(mp) == mp.intersection(palette_object)
    assert palette_object.intersection(np) == Palette()


def test_palette_to_list(palette_object):
    ptl = {Color.from_hex("#531380"),
           Color.from_hex("#d7820e"),
           Color.from_hex("#60d048"),
           Color.from_hex("#f8c630")}

    assert palette_object.to_list() == list(ptl)
    assert len(palette_object.to_list()) > 0


def test_palette_to_dict(palette_object):
    ptl = {Color.from_hex("#531380"),
           Color.from_hex("#d7820e"),
           Color.from_hex("#60d048"),
           Color.from_hex("#f8c630")}

    assert palette_object.to_dict() == {x.hex: x.rgba for x in ptl}
    assert "#d7820e" in palette_object.to_dict().keys()
