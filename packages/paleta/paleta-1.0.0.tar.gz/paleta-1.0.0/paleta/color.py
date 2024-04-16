from __future__ import annotations

import copy


class Color:
    """
    Color Vector (R, G, B, A=255)

    - R : Red Value     (0 - 255)
    - G : Green Value   (0 - 255)
    - B : Blue Value    (0 - 255)
    - A : Alpha Value   (0 - 255)
    """

    def __init__(self, r, g, b, alpha=255.0):
        self._r = max(min(r, 255.0), 0)
        self._g = max(min(g, 255.0), 0)
        self._b = max(min(b, 255.0), 0)
        self._alpha = max(min(alpha, 255.0), 0)

    @property
    def r(self):
        """
        R : Red Value   (0 - 255)

        :return: float
        """
        return self._r

    @r.setter
    def r(self, value):
        self._r = max(min(value, 255.0), 0)

    @property
    def g(self):
        """
        G : Green Value (0 - 255)

        :return: float
        """
        return self._g

    @g.setter
    def g(self, value):
        self._g = max(min(value, 255.0), 0)

    @property
    def b(self):
        """
        B : Blue value  (0 - 255)

        :return: float
        """
        return self._b

    @b.setter
    def b(self, value):
        self._b = max(min(value, 255.0), 0)

    @property
    def alpha(self):
        """
        A : Alpha Value (0 - 255)

        :return: float
        """
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        self._alpha = max(min(value, 255.0), 0)

    @property
    def rgb(self):
        """
        RGB Tuple (Red, Green, Blue)

        :return: tuple(float, float, float)
        """
        return self.r, self.g, self.b

    @property
    def rgba(self):
        """
        RGBA Tuple (Red, Green, Blue, Alpha)

        :return: tuple(float, float, float, float)
        """
        return self.r, self.g, self.b, self.alpha

    @property
    def irgb(self):
        """
        RGB Tuple (Red, Green, Blue)

        :return: tuple(int, int, int)
        """
        return int(self.r), int(self.g), int(self.b)

    @property
    def irgba(self):
        """
        RGBA Tuple (Red, Green, Blue, Alpha)

        :return: tuple(int, int, int, int)
        """
        return int(self.r), int(self.g), int(self.b), int(self.alpha)

    @property
    def bgr(self):
        """
        BGR Tuple (Blue, Green, Red)

        :return: tuple(float, float, float)
        """
        return self.b, self.g, self.r

    @property
    def bgra(self):
        """
        BGRA Tuple (Blue, Green, Red, Alpha)

        :return: tuple(float, float, float, float)
        """
        return self.b, self.g, self.r, self.alpha

    @property
    def hex(self):
        """
        Hexadecimal Code for Color

        :return: str
        """
        return '#{:02x}{:02x}{:02x}'.format(int(self.r), int(self.g), int(self.b))

    def __str__(self):
        return str(self.rgba)

    def __add__(self, other):

        if isinstance(other, Color):
            return Color(self.r + other.r, self.g + other.g, self.b + other.b, self.alpha + other.alpha)

        if isinstance(other, int) or isinstance(other, float):
            return Color(self.r + other, self.g + other, self.b + other, self.alpha + other)

        if isinstance(other, tuple) or isinstance(other, list):
            return Color(*((c1 + c2) for c1, c2 in zip(self.rgba, other)))

        raise TypeError(f'Unsupported operation with class "{type(other)}"')

    def __sub__(self, other):

        if isinstance(other, Color):
            return Color(self.r - other.r, self.g - other.g, self.b - other.b, self.alpha - other.alpha)

        if isinstance(other, int) or isinstance(other, float):
            return Color(self.r - other, self.g - other, self.b - other, self.alpha - other)

        if isinstance(other, tuple) or isinstance(other, list):
            return Color(*((c1 - c2) for c1, c2 in zip(self.rgba, other)))

        raise TypeError(f'Unsupported operation with class "{type(other)}"')

    def __eq__(self, other):

        if isinstance(other, Color):
            return self.rgba == other.rgba

        if isinstance(other, tuple) or isinstance(other, list):
            return self.rgba == Color(*other).rgba

        raise TypeError(f'Unsupported operation with class "{type(other)}"')

    def __lt__(self, other):

        if isinstance(other, Color):
            return sum(self.rgba) < sum(other.rgba)

        if isinstance(other, tuple) or isinstance(other, list):
            return sum(self.rgba) < sum(Color(*other).rgba)

        raise TypeError(f'Unsupported operation with class "{type(other)}"')

    def __le__(self, other):

        if isinstance(other, Color):
            return sum(self.rgba) <= sum(other.rgba)

        if isinstance(other, tuple) or isinstance(other, list):
            return sum(self.rgba) <= sum(Color(*other).rgba)

        raise TypeError(f'Unsupported operation with class "{type(other)}"')

    def __gt__(self, other):

        if isinstance(other, Color):
            return sum(self.rgba) > sum(other.rgba)

        if isinstance(other, tuple) or isinstance(other, list):
            return sum(self.rgba) > sum(Color(*other).rgba)

        raise TypeError(f'Unsupported operation with class "{type(other)}"')

    def __ge__(self, other):

        if isinstance(other, Color):
            return sum(self.rgba) >= sum(other.rgba)

        if isinstance(other, tuple) or isinstance(other, list):
            return sum(self.rgba) >= sum(Color(*other).rgba)

        raise TypeError(f'Unsupported operation with class "{type(other)}"')

    def __hash__(self):
        return hash((self.rgba, self.hex))

    def get_normalize(self, normalizer=255):
        """
        Get Normalized Value by Normalizer Factors

        :param normalizer: RGB Normalizer (float)
        :return: tuple(float, float, float, float)
        """
        return self.r / normalizer, self.g / normalizer, self.b / normalizer, self.alpha / normalizer

    def get_inverse(self, with_alpha=False):
        """
        Get Inverse of Color

        :param with_alpha: Get Inverse of Alpha (bool)
        :return: tuple(float, float, float, *float)
        """
        if with_alpha:
            return 255 - self.r, 255 - self.g, 255 - self.b, 255 - self.alpha
        return 255 - self.r, 255 - self.g, 255 - self.b

    @classmethod
    def from_hex(cls, code):
        """
        Instantiate Class from Hexadecimal Code

        :param code: Hexadecimal Code (str)
        :return: cls
        """
        code = code.lstrip('#')

        # Convert hex to RGB
        if len(code) == 3:
            r = int(code[0] * 2, 16)
            g = int(code[1] * 2, 16)
            b = int(code[2] * 2, 16)
        else:
            r = int(code[0:2], 16)
            g = int(code[2:4], 16)
            b = int(code[4:6], 16)

        return cls(r, g, b)

    @classmethod
    def from_hsl(cls, h, s, l):
        """
        Instantiate Class from HSL Value

        :param h: Hue           (float)
        :param s: Saturation    (float)
        :param l: Lightness     (float)
        :return: cls
        """
        c = (1 - abs(2 * l - 1)) * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = l - c / 2

        if 0 <= h < 60:
            r, g, b = c, x, 0
        elif 60 <= h < 120:
            r, g, b = x, c, 0
        elif 120 <= h < 180:
            r, g, b = 0, c, x
        elif 180 <= h < 240:
            r, g, b = 0, x, c
        elif 240 <= h < 300:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x

        return cls(int((r + m) * 255), int((g + m) * 255), int((b + m) * 255))

    @classmethod
    def from_hsv(cls, h, s, v):
        """
        Instantiate Class from HSV

        :param h: Hue           (float)
        :param s: Saturation    (float)
        :param v: Value         (float)
        :return: cls
        """
        h /= 360.0

        chroma = v * s
        h_prime = h * 6.0

        x = chroma * (1 - abs(h_prime % 2 - 1))

        r, g, b = 0, 0, 0

        if 0 <= h_prime < 1:
            r, g, b = chroma, x, 0
        elif 1 <= h_prime < 2:
            r, g, b = x, chroma, 0
        elif 2 <= h_prime < 3:
            r, g, b = 0, chroma, x
        elif 3 <= h_prime < 4:
            r, g, b = 0, x, chroma
        elif 4 <= h_prime < 5:
            r, g, b = x, 0, chroma
        elif 5 <= h_prime < 6:
            r, g, b = chroma, 0, x

        m = v - chroma

        r += m
        g += m
        b += m

        return cls(round(r * 255), round(g * 255), round(b * 255))

    def to_lightness(self):
        """
        Return Color Lightness Value

        :return: float
        """
        return 0.2126 * self.r + 0.7152 * self.g + 0.0722 * self.b

    def to_hue(self):
        """
        Get Color Hue Value

        :return: float
        """
        min_val = min(self.r, self.g, self.b)
        max_val = max(self.r, self.g, self.b)
        delta = max_val - min_val
        if delta == 0:
            return 0
        elif max_val == self.r:
            return 60 * ((self.g - self.b) / delta % 6)
        elif max_val == self.b:
            return 60 * ((self.b - self.r) / delta + 2)
        else:
            return 60 * ((self.r - self.g) / delta + 4)

    def to_hsl(self, dec=2):
        """
        Get Color HSL Value

        :param dec: Decimal Point (float)
        :return: tuple(float, float, float)
        """
        r_n, g_n, b_n, _ = self.get_normalize()
        max_val = max(r_n, g_n, b_n)
        min_val = min(r_n, g_n, b_n)
        l = (max_val + min_val) / 2.0

        if max_val == min_val:
            h = s = 0
        else:
            d = max_val - min_val
            s = d / (2 - max_val - min_val) if l > 0.5 else d / (max_val + min_val)
            if max_val == r_n:
                h = (g_n - b_n) / d + (6 if g_n < b_n else 0)
            elif max_val == g_n:
                h = (b_n - r_n) / d + 2
            else:
                h = (r_n - g_n) / d + 4
            h *= 60

        return round(h, dec), round(s, dec), round(l, dec)

    def to_hsv(self, dec=2):
        """
        Get Color HSV Value

        :param dec: Decimal Point (float)
        :return: tuple(float, float, float)
        """
        r_n, g_n, b_n, _ = self.get_normalize()
        max_val = max(r_n, g_n, b_n)
        min_val = min(r_n, g_n, b_n)
        delta = max_val - min_val

        # Calculate Hue
        h = 0
        if delta == 0:
            h = 0
        elif max_val == r_n:
            h = 60 * (((g_n - b_n) / delta) % 6)
        elif max_val == g_n:
            h = 60 * (((b_n - r_n) / delta) + 2)
        elif max_val == b_n:
            h = 60 * (((r_n - g_n) / delta) + 4)

        # Calculate Saturation
        if max_val == 0:
            s = 0
        else:
            s = delta / max_val

        # Calculate Value
        v = max_val

        return round(h, dec), round(s, dec), round(v, dec)

    def to_cmyk(self, dec=2):
        """
        Get Color CMYK Value

        :param dec: Decimal Point (float)
        :return: tuple(float, float, float, float)
        """
        r_n, g_n, b_n, _ = self.get_normalize()
        c, m, y = 1 - r_n, 1 - g_n, 1 - b_n
        k = min(c, m, y)

        if k == 1:
            return 0, 0, 0, 1
        else:
            c = (c - k) / (1 - k)
            m = (m - k) / (1 - k)
            y = (y - k) / (1 - k)
            return round(c, dec), round(m, dec), round(y, dec), round(k, dec)

    def copy(self):
        """
        Copy Vector Object

        :return: cls
        """
        return copy.copy(self)

    def copy_inverse(self, with_alpha=False):
        """
        Copy Inverse of Vector Object

        :return: cls
        """
        return Color(*self.get_inverse(with_alpha=with_alpha))


def color_average(*colors: Color, with_alpha=False) -> Color:
    if with_alpha:
        Color(*(
            sum(color.r for color in colors) / len(colors),
            sum(color.g for color in colors) / len(colors),
            sum(color.b for color in colors) / len(colors),
            sum(color.alpha for color in colors) / len(colors))
        )

    return Color(*(
        sum(color.r for color in colors) / len(colors),
        sum(color.g for color in colors) / len(colors),
        sum(color.b for color in colors) / len(colors)
    ))

