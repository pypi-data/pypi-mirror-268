from typing import overload
import typing

import System
import System.Collections
import System.ComponentModel
import System.Drawing
import System.Globalization
import System.Numerics

System_Drawing_SizeF = typing.Any
System_Drawing_Size = typing.Any
System_Drawing_Point = typing.Any
System_Drawing_PointF = typing.Any
System_Drawing_RectangleF = typing.Any
System_Drawing_Color = typing.Any
System_Drawing_Rectangle = typing.Any


class PointF(System.IEquatable[System_Drawing_PointF]):
    """Represents an ordered pair of x and y coordinates that define a point in a two-dimensional plane."""

    EMPTY: System.Drawing.PointF
    """Creates a new instance of the System.Drawing.PointF class with member data left uninitialized."""

    @property
    def is_empty(self) -> bool:
        """Gets a value indicating whether this System.Drawing.PointF is empty."""
        ...

    @property
    def x(self) -> float:
        """Gets the x-coordinate of this System.Drawing.PointF."""
        ...

    @property
    def y(self) -> float:
        """Gets the y-coordinate of this System.Drawing.PointF."""
        ...

    @overload
    def __init__(self, x: float, y: float) -> None:
        """Initializes a new instance of the System.Drawing.PointF class with the specified coordinates."""
        ...

    @overload
    def __init__(self, vector: System.Numerics.Vector2) -> None:
        """
        Initializes a new instance of the System.Drawing.PointF struct from the specified
        System.Numerics.Vector2.
        """
        ...

    @staticmethod
    @overload
    def add(pt: System.Drawing.PointF, sz: System.Drawing.Size) -> System.Drawing.PointF:
        """Translates a System.Drawing.PointF by a given System.Drawing.Size ."""
        ...

    @staticmethod
    @overload
    def add(pt: System.Drawing.PointF, sz: System.Drawing.SizeF) -> System.Drawing.PointF:
        """Translates a System.Drawing.PointF by a given System.Drawing.SizeF ."""
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Drawing.PointF) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    @overload
    def subtract(pt: System.Drawing.PointF, sz: System.Drawing.Size) -> System.Drawing.PointF:
        """Translates a System.Drawing.PointF by the negative of a given System.Drawing.Size ."""
        ...

    @staticmethod
    @overload
    def subtract(pt: System.Drawing.PointF, sz: System.Drawing.SizeF) -> System.Drawing.PointF:
        """Translates a System.Drawing.PointF by the negative of a given System.Drawing.SizeF ."""
        ...

    def to_string(self) -> str:
        ...

    def to_vector2(self) -> System.Numerics.Vector2:
        """Creates a new System.Numerics.Vector2 from this System.Drawing.PointF."""
        ...


class Point(System.IEquatable[System_Drawing_Point]):
    """Represents an ordered pair of x and y coordinates that define a point in a two-dimensional plane."""

    EMPTY: System.Drawing.Point
    """Creates a new instance of the System.Drawing.Point class with member data left uninitialized."""

    @property
    def is_empty(self) -> bool:
        """Gets a value indicating whether this System.Drawing.Point is empty."""
        ...

    @property
    def x(self) -> int:
        """Gets the x-coordinate of this System.Drawing.Point."""
        ...

    @property
    def y(self) -> int:
        """Gets the y-coordinate of this System.Drawing.Point."""
        ...

    @overload
    def __init__(self, x: int, y: int) -> None:
        """Initializes a new instance of the System.Drawing.Point class with the specified coordinates."""
        ...

    @overload
    def __init__(self, sz: System.Drawing.Size) -> None:
        """Initializes a new instance of the System.Drawing.Point class from a System.Drawing.Size ."""
        ...

    @overload
    def __init__(self, dw: int) -> None:
        """Initializes a new instance of the Point class using coordinates specified by an integer value."""
        ...

    @staticmethod
    def add(pt: System.Drawing.Point, sz: System.Drawing.Size) -> System.Drawing.Point:
        """Translates a System.Drawing.Point by a given System.Drawing.Size ."""
        ...

    @staticmethod
    def ceiling(value: System.Drawing.PointF) -> System.Drawing.Point:
        """Converts a PointF to a Point by performing a ceiling operation on all the coordinates."""
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Specifies whether this System.Drawing.Point contains the same coordinates as the specified
        object.
        """
        ...

    @overload
    def equals(self, other: System.Drawing.Point) -> bool:
        ...

    def get_hash_code(self) -> int:
        """Returns a hash code."""
        ...

    @overload
    def offset(self, dx: int, dy: int) -> None:
        """Translates this System.Drawing.Point by the specified amount."""
        ...

    @overload
    def offset(self, p: System.Drawing.Point) -> None:
        """Translates this System.Drawing.Point by the specified amount."""
        ...

    @staticmethod
    def round(value: System.Drawing.PointF) -> System.Drawing.Point:
        """Converts a PointF to a Point by performing a round operation on all the coordinates."""
        ...

    @staticmethod
    def subtract(pt: System.Drawing.Point, sz: System.Drawing.Size) -> System.Drawing.Point:
        """Translates a System.Drawing.Point by the negative of a given System.Drawing.Size ."""
        ...

    def to_string(self) -> str:
        """Converts this System.Drawing.Point to a human readable string."""
        ...

    @staticmethod
    def truncate(value: System.Drawing.PointF) -> System.Drawing.Point:
        """Converts a PointF to a Point by performing a truncate operation on all the coordinates."""
        ...


class Size(System.IEquatable[System_Drawing_Size]):
    """Represents the size of a rectangular region with an ordered pair of width and height."""

    EMPTY: System.Drawing.Size
    """Initializes a new instance of the System.Drawing.Size class."""

    @property
    def is_empty(self) -> bool:
        """Tests whether this System.Drawing.Size has zero width and height."""
        ...

    @property
    def width(self) -> int:
        """Represents the horizontal component of this System.Drawing.Size."""
        ...

    @property
    def height(self) -> int:
        """Represents the vertical component of this System.Drawing.Size."""
        ...

    @overload
    def __init__(self, pt: System.Drawing.Point) -> None:
        """
        Initializes a new instance of the System.Drawing.Size class from the specified
        System.Drawing.Point.
        """
        ...

    @overload
    def __init__(self, width: int, height: int) -> None:
        """Initializes a new instance of the System.Drawing.Size class from the specified dimensions."""
        ...

    @staticmethod
    def add(sz1: System.Drawing.Size, sz2: System.Drawing.Size) -> System.Drawing.Size:
        """Performs vector addition of two System.Drawing.Size objects."""
        ...

    @staticmethod
    def ceiling(value: System.Drawing.SizeF) -> System.Drawing.Size:
        """Converts a SizeF to a Size by performing a ceiling operation on all the coordinates."""
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Tests to see whether the specified object is a System.Drawing.Size  with the same dimensions
        as this System.Drawing.Size.
        """
        ...

    @overload
    def equals(self, other: System.Drawing.Size) -> bool:
        ...

    def get_hash_code(self) -> int:
        """Returns a hash code."""
        ...

    @staticmethod
    def round(value: System.Drawing.SizeF) -> System.Drawing.Size:
        """Converts a SizeF to a Size by performing a round operation on all the coordinates."""
        ...

    @staticmethod
    def subtract(sz1: System.Drawing.Size, sz2: System.Drawing.Size) -> System.Drawing.Size:
        """Contracts a System.Drawing.Size by another System.Drawing.Size ."""
        ...

    def to_string(self) -> str:
        """Creates a human-readable string that represents this System.Drawing.Size."""
        ...

    @staticmethod
    def truncate(value: System.Drawing.SizeF) -> System.Drawing.Size:
        """Converts a SizeF to a Size by performing a truncate operation on all the coordinates."""
        ...


class SizeF(System.IEquatable[System_Drawing_SizeF]):
    """Represents the size of a rectangular region with an ordered pair of width and height."""

    EMPTY: System.Drawing.SizeF
    """Initializes a new instance of the System.Drawing.SizeF class."""

    @property
    def is_empty(self) -> bool:
        """Tests whether this System.Drawing.SizeF has zero width and height."""
        ...

    @property
    def width(self) -> float:
        """Represents the horizontal component of this System.Drawing.SizeF."""
        ...

    @property
    def height(self) -> float:
        """Represents the vertical component of this System.Drawing.SizeF."""
        ...

    @overload
    def __init__(self, size: System.Drawing.SizeF) -> None:
        """
        Initializes a new instance of the System.Drawing.SizeF class from the specified
        existing System.Drawing.SizeF.
        """
        ...

    @overload
    def __init__(self, pt: System.Drawing.PointF) -> None:
        """
        Initializes a new instance of the System.Drawing.SizeF class from the specified
        System.Drawing.PointF.
        """
        ...

    @overload
    def __init__(self, vector: System.Numerics.Vector2) -> None:
        """
        Initializes a new instance of the System.Drawing.SizeF struct from the specified
        System.Numerics.Vector2.
        """
        ...

    @overload
    def __init__(self, width: float, height: float) -> None:
        """Initializes a new instance of the System.Drawing.SizeF class from the specified dimensions."""
        ...

    @staticmethod
    def add(sz1: System.Drawing.SizeF, sz2: System.Drawing.SizeF) -> System.Drawing.SizeF:
        """Performs vector addition of two System.Drawing.SizeF objects."""
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Tests to see whether the specified object is a System.Drawing.SizeF  with the same dimensions
        as this System.Drawing.SizeF.
        """
        ...

    @overload
    def equals(self, other: System.Drawing.SizeF) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def subtract(sz1: System.Drawing.SizeF, sz2: System.Drawing.SizeF) -> System.Drawing.SizeF:
        """Contracts a System.Drawing.SizeF by another System.Drawing.SizeF."""
        ...

    def to_point_f(self) -> System.Drawing.PointF:
        ...

    def to_size(self) -> System.Drawing.Size:
        ...

    def to_string(self) -> str:
        """Creates a human-readable string that represents this System.Drawing.SizeF."""
        ...

    def to_vector2(self) -> System.Numerics.Vector2:
        """Creates a new System.Numerics.Vector2 from this System.Drawing.SizeF."""
        ...


class KnownColor(System.Enum):
    """This class has no documentation."""

    ACTIVE_BORDER = 1

    ACTIVE_CAPTION = 1

    ACTIVE_CAPTION_TEXT = 2

    APP_WORKSPACE = 3

    CONTROL = 4

    CONTROL_DARK = 5

    CONTROL_DARK_DARK = 6

    CONTROL_LIGHT = 7

    CONTROL_LIGHT_LIGHT = 8

    CONTROL_TEXT = 9

    DESKTOP = 10

    GRAY_TEXT = 11

    HIGHLIGHT = 12

    HIGHLIGHT_TEXT = 13

    HOT_TRACK = 14

    INACTIVE_BORDER = 15

    INACTIVE_CAPTION = 16

    INACTIVE_CAPTION_TEXT = 17

    INFO = 18

    INFO_TEXT = 19

    MENU = 20

    MENU_TEXT = 21

    SCROLL_BAR = 22

    WINDOW = 23

    WINDOW_FRAME = 24

    WINDOW_TEXT = 25

    TRANSPARENT = 26

    ALICE_BLUE = 27

    ANTIQUE_WHITE = 28

    AQUA = 29

    AQUAMARINE = 30

    AZURE = 31

    BEIGE = 32

    BISQUE = 33

    BLACK = 34

    BLANCHED_ALMOND = 35

    BLUE = 36

    BLUE_VIOLET = 37

    BROWN = 38

    BURLY_WOOD = 39

    CADET_BLUE = 40

    CHARTREUSE = 41

    CHOCOLATE = 42

    CORAL = 43

    CORNFLOWER_BLUE = 44

    CORNSILK = 45

    CRIMSON = 46

    CYAN = 47

    DARK_BLUE = 48

    DARK_CYAN = 49

    DARK_GOLDENROD = 50

    DARK_GRAY = 51

    DARK_GREEN = 52

    DARK_KHAKI = 53

    DARK_MAGENTA = 54

    DARK_OLIVE_GREEN = 55

    DARK_ORANGE = 56

    DARK_ORCHID = 57

    DARK_RED = 58

    DARK_SALMON = 59

    DARK_SEA_GREEN = 60

    DARK_SLATE_BLUE = 61

    DARK_SLATE_GRAY = 62

    DARK_TURQUOISE = 63

    DARK_VIOLET = 64

    DEEP_PINK = 65

    DEEP_SKY_BLUE = 66

    DIM_GRAY = 67

    DODGER_BLUE = 68

    FIREBRICK = 69

    FLORAL_WHITE = 70

    FOREST_GREEN = 71

    FUCHSIA = 72

    GAINSBORO = 73

    GHOST_WHITE = 74

    GOLD = 75

    GOLDENROD = 76

    GRAY = 77

    GREEN = 78

    GREEN_YELLOW = 79

    HONEYDEW = 80

    HOT_PINK = 81

    INDIAN_RED = 82

    INDIGO = 83

    IVORY = 84

    KHAKI = 85

    LAVENDER = 86

    LAVENDER_BLUSH = 87

    LAWN_GREEN = 88

    LEMON_CHIFFON = 89

    LIGHT_BLUE = 90

    LIGHT_CORAL = 91

    LIGHT_CYAN = 92

    LIGHT_GOLDENROD_YELLOW = 93

    LIGHT_GRAY = 94

    LIGHT_GREEN = 95

    LIGHT_PINK = 96

    LIGHT_SALMON = 97

    LIGHT_SEA_GREEN = 98

    LIGHT_SKY_BLUE = 99

    LIGHT_SLATE_GRAY = 100

    LIGHT_STEEL_BLUE = 101

    LIGHT_YELLOW = 102

    LIME = 103

    LIME_GREEN = 104

    LINEN = 105

    MAGENTA = 106

    MAROON = 107

    MEDIUM_AQUAMARINE = 108

    MEDIUM_BLUE = 109

    MEDIUM_ORCHID = 110

    MEDIUM_PURPLE = 111

    MEDIUM_SEA_GREEN = 112

    MEDIUM_SLATE_BLUE = 113

    MEDIUM_SPRING_GREEN = 114

    MEDIUM_TURQUOISE = 115

    MEDIUM_VIOLET_RED = 116

    MIDNIGHT_BLUE = 117

    MINT_CREAM = 118

    MISTY_ROSE = 119

    MOCCASIN = 120

    NAVAJO_WHITE = 121

    NAVY = 122

    OLD_LACE = 123

    OLIVE = 124

    OLIVE_DRAB = 125

    ORANGE = 126

    ORANGE_RED = 127

    ORCHID = 128

    PALE_GOLDENROD = 129

    PALE_GREEN = 130

    PALE_TURQUOISE = 131

    PALE_VIOLET_RED = 132

    PAPAYA_WHIP = 133

    PEACH_PUFF = 134

    PERU = 135

    PINK = 136

    PLUM = 137

    POWDER_BLUE = 138

    PURPLE = 139

    RED = 140

    ROSY_BROWN = 141

    ROYAL_BLUE = 142

    SADDLE_BROWN = 143

    SALMON = 144

    SANDY_BROWN = 145

    SEA_GREEN = 146

    SEA_SHELL = 147

    SIENNA = 148

    SILVER = 149

    SKY_BLUE = 150

    SLATE_BLUE = 151

    SLATE_GRAY = 152

    SNOW = 153

    SPRING_GREEN = 154

    STEEL_BLUE = 155

    TAN = 156

    TEAL = 157

    THISTLE = 158

    TOMATO = 159

    TURQUOISE = 160

    VIOLET = 161

    WHEAT = 162

    WHITE = 163

    WHITE_SMOKE = 164

    YELLOW = 165

    YELLOW_GREEN = 166

    BUTTON_FACE = 167

    BUTTON_HIGHLIGHT = 168

    BUTTON_SHADOW = 169

    GRADIENT_ACTIVE_CAPTION = 170

    GRADIENT_INACTIVE_CAPTION = 171

    MENU_BAR = 172

    MENU_HIGHLIGHT = 173

    REBECCA_PURPLE = 174


class Color(System.IEquatable[System_Drawing_Color]):
    """This class has no documentation."""

    EMPTY: System.Drawing.Color

    transparent: System.Drawing.Color

    alice_blue: System.Drawing.Color

    antique_white: System.Drawing.Color

    aqua: System.Drawing.Color

    aquamarine: System.Drawing.Color

    azure: System.Drawing.Color

    beige: System.Drawing.Color

    bisque: System.Drawing.Color

    black: System.Drawing.Color

    blanched_almond: System.Drawing.Color

    blue: System.Drawing.Color

    blue_violet: System.Drawing.Color

    brown: System.Drawing.Color

    burly_wood: System.Drawing.Color

    cadet_blue: System.Drawing.Color

    chartreuse: System.Drawing.Color

    chocolate: System.Drawing.Color

    coral: System.Drawing.Color

    cornflower_blue: System.Drawing.Color

    cornsilk: System.Drawing.Color

    crimson: System.Drawing.Color

    cyan: System.Drawing.Color

    dark_blue: System.Drawing.Color

    dark_cyan: System.Drawing.Color

    dark_goldenrod: System.Drawing.Color

    dark_gray: System.Drawing.Color

    dark_green: System.Drawing.Color

    dark_khaki: System.Drawing.Color

    dark_magenta: System.Drawing.Color

    dark_olive_green: System.Drawing.Color

    dark_orange: System.Drawing.Color

    dark_orchid: System.Drawing.Color

    dark_red: System.Drawing.Color

    dark_salmon: System.Drawing.Color

    dark_sea_green: System.Drawing.Color

    dark_slate_blue: System.Drawing.Color

    dark_slate_gray: System.Drawing.Color

    dark_turquoise: System.Drawing.Color

    dark_violet: System.Drawing.Color

    deep_pink: System.Drawing.Color

    deep_sky_blue: System.Drawing.Color

    dim_gray: System.Drawing.Color

    dodger_blue: System.Drawing.Color

    firebrick: System.Drawing.Color

    floral_white: System.Drawing.Color

    forest_green: System.Drawing.Color

    fuchsia: System.Drawing.Color

    gainsboro: System.Drawing.Color

    ghost_white: System.Drawing.Color

    gold: System.Drawing.Color

    goldenrod: System.Drawing.Color

    gray: System.Drawing.Color

    green: System.Drawing.Color

    green_yellow: System.Drawing.Color

    honeydew: System.Drawing.Color

    hot_pink: System.Drawing.Color

    indian_red: System.Drawing.Color

    indigo: System.Drawing.Color

    ivory: System.Drawing.Color

    khaki: System.Drawing.Color

    lavender: System.Drawing.Color

    lavender_blush: System.Drawing.Color

    lawn_green: System.Drawing.Color

    lemon_chiffon: System.Drawing.Color

    light_blue: System.Drawing.Color

    light_coral: System.Drawing.Color

    light_cyan: System.Drawing.Color

    light_goldenrod_yellow: System.Drawing.Color

    light_green: System.Drawing.Color

    light_gray: System.Drawing.Color

    light_pink: System.Drawing.Color

    light_salmon: System.Drawing.Color

    light_sea_green: System.Drawing.Color

    light_sky_blue: System.Drawing.Color

    light_slate_gray: System.Drawing.Color

    light_steel_blue: System.Drawing.Color

    light_yellow: System.Drawing.Color

    lime: System.Drawing.Color

    lime_green: System.Drawing.Color

    linen: System.Drawing.Color

    magenta: System.Drawing.Color

    maroon: System.Drawing.Color

    medium_aquamarine: System.Drawing.Color

    medium_blue: System.Drawing.Color

    medium_orchid: System.Drawing.Color

    medium_purple: System.Drawing.Color

    medium_sea_green: System.Drawing.Color

    medium_slate_blue: System.Drawing.Color

    medium_spring_green: System.Drawing.Color

    medium_turquoise: System.Drawing.Color

    medium_violet_red: System.Drawing.Color

    midnight_blue: System.Drawing.Color

    mint_cream: System.Drawing.Color

    misty_rose: System.Drawing.Color

    moccasin: System.Drawing.Color

    navajo_white: System.Drawing.Color

    navy: System.Drawing.Color

    old_lace: System.Drawing.Color

    olive: System.Drawing.Color

    olive_drab: System.Drawing.Color

    orange: System.Drawing.Color

    orange_red: System.Drawing.Color

    orchid: System.Drawing.Color

    pale_goldenrod: System.Drawing.Color

    pale_green: System.Drawing.Color

    pale_turquoise: System.Drawing.Color

    pale_violet_red: System.Drawing.Color

    papaya_whip: System.Drawing.Color

    peach_puff: System.Drawing.Color

    peru: System.Drawing.Color

    pink: System.Drawing.Color

    plum: System.Drawing.Color

    powder_blue: System.Drawing.Color

    purple: System.Drawing.Color

    rebecca_purple: System.Drawing.Color
    """Gets a system-defined color that has an ARGB value of #663399."""

    red: System.Drawing.Color

    rosy_brown: System.Drawing.Color

    royal_blue: System.Drawing.Color

    saddle_brown: System.Drawing.Color

    salmon: System.Drawing.Color

    sandy_brown: System.Drawing.Color

    sea_green: System.Drawing.Color

    sea_shell: System.Drawing.Color

    sienna: System.Drawing.Color

    silver: System.Drawing.Color

    sky_blue: System.Drawing.Color

    slate_blue: System.Drawing.Color

    slate_gray: System.Drawing.Color

    snow: System.Drawing.Color

    spring_green: System.Drawing.Color

    steel_blue: System.Drawing.Color

    tan: System.Drawing.Color

    teal: System.Drawing.Color

    thistle: System.Drawing.Color

    tomato: System.Drawing.Color

    turquoise: System.Drawing.Color

    violet: System.Drawing.Color

    wheat: System.Drawing.Color

    white: System.Drawing.Color

    white_smoke: System.Drawing.Color

    yellow: System.Drawing.Color

    yellow_green: System.Drawing.Color

    @property
    def r(self) -> int:
        ...

    @property
    def g(self) -> int:
        ...

    @property
    def b(self) -> int:
        ...

    @property
    def a(self) -> int:
        ...

    @property
    def is_known_color(self) -> bool:
        ...

    @property
    def is_empty(self) -> bool:
        ...

    @property
    def is_named_color(self) -> bool:
        ...

    @property
    def is_system_color(self) -> bool:
        ...

    @property
    def name(self) -> str:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Drawing.Color) -> bool:
        ...

    @staticmethod
    @overload
    def from_argb(argb: int) -> System.Drawing.Color:
        ...

    @staticmethod
    @overload
    def from_argb(alpha: int, red: int, green: int, blue: int) -> System.Drawing.Color:
        ...

    @staticmethod
    @overload
    def from_argb(alpha: int, base_color: System.Drawing.Color) -> System.Drawing.Color:
        ...

    @staticmethod
    @overload
    def from_argb(red: int, green: int, blue: int) -> System.Drawing.Color:
        ...

    @staticmethod
    def from_known_color(color: System.Drawing.KnownColor) -> System.Drawing.Color:
        ...

    @staticmethod
    def from_name(name: str) -> System.Drawing.Color:
        ...

    def get_brightness(self) -> float:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_hue(self) -> float:
        ...

    def get_saturation(self) -> float:
        ...

    def to_argb(self) -> int:
        ...

    def to_known_color(self) -> int:
        """:returns: This method returns the int value of a member of the System.Drawing.KnownColor enum."""
        ...

    def to_string(self) -> str:
        ...


class ColorTranslator(System.Object):
    """Translates colors to and from GDI+ Color objects."""

    @staticmethod
    def from_html(html_color: str) -> System.Drawing.Color:
        """Translates an Html color representation to a GDI+ Color."""
        ...

    @staticmethod
    def from_ole(ole_color: int) -> System.Drawing.Color:
        """Translates an Ole color value to a GDI+ Color."""
        ...

    @staticmethod
    def from_win32(win32color: int) -> System.Drawing.Color:
        """Translates an Win32 color value to a GDI+ Color."""
        ...

    @staticmethod
    def to_html(c: System.Drawing.Color) -> str:
        """Translates the specified Color to an Html string color representation."""
        ...

    @staticmethod
    def to_ole(c: System.Drawing.Color) -> int:
        """Translates the specified Color to an Ole color."""
        ...

    @staticmethod
    def to_win32(c: System.Drawing.Color) -> int:
        """Translates the specified Color to a Win32 color."""
        ...


class RectangleF(System.IEquatable[System_Drawing_RectangleF]):
    """Stores the location and size of a rectangular region."""

    EMPTY: System.Drawing.RectangleF
    """Initializes a new instance of the System.Drawing.RectangleF class."""

    @property
    def location(self) -> System.Drawing.PointF:
        """
        Gets or sets the coordinates of the upper-left corner of the rectangular region represented by this
        System.Drawing.RectangleF.
        """
        ...

    @property
    def size(self) -> System.Drawing.SizeF:
        """Gets or sets the size of this System.Drawing.RectangleF."""
        ...

    @property
    def x(self) -> float:
        """
        Gets or sets the x-coordinate of the upper-left corner of the rectangular region defined by this
        System.Drawing.RectangleF.
        """
        ...

    @property
    def y(self) -> float:
        """
        Gets or sets the y-coordinate of the upper-left corner of the rectangular region defined by this
        System.Drawing.RectangleF.
        """
        ...

    @property
    def width(self) -> float:
        """Gets or sets the width of the rectangular region defined by this System.Drawing.RectangleF."""
        ...

    @property
    def height(self) -> float:
        """Gets or sets the height of the rectangular region defined by this System.Drawing.RectangleF."""
        ...

    @property
    def left(self) -> float:
        """
        Gets the x-coordinate of the upper-left corner of the rectangular region defined by this
        System.Drawing.RectangleF .
        """
        ...

    @property
    def top(self) -> float:
        """
        Gets the y-coordinate of the upper-left corner of the rectangular region defined by this
        System.Drawing.RectangleF.
        """
        ...

    @property
    def right(self) -> float:
        """
        Gets the x-coordinate of the lower-right corner of the rectangular region defined by this
        System.Drawing.RectangleF.
        """
        ...

    @property
    def bottom(self) -> float:
        """
        Gets the y-coordinate of the lower-right corner of the rectangular region defined by this
        System.Drawing.RectangleF.
        """
        ...

    @property
    def is_empty(self) -> bool:
        """Tests whether this System.Drawing.RectangleF has a System.Drawing.RectangleF.Width or a System.Drawing.RectangleF.Height of 0."""
        ...

    @overload
    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        """
        Initializes a new instance of the System.Drawing.RectangleF class with the specified location
        and size.
        """
        ...

    @overload
    def __init__(self, location: System.Drawing.PointF, size: System.Drawing.SizeF) -> None:
        """
        Initializes a new instance of the System.Drawing.RectangleF class with the specified location
        and size.
        """
        ...

    @overload
    def __init__(self, vector: System.Numerics.Vector4) -> None:
        """
        Initializes a new instance of the System.Drawing.RectangleF struct from the specified
        System.Numerics.Vector4.
        """
        ...

    @overload
    def contains(self, x: float, y: float) -> bool:
        """
        Determines if the specified point is contained within the rectangular region defined by this
        System.Drawing.Rectangle .
        """
        ...

    @overload
    def contains(self, pt: System.Drawing.PointF) -> bool:
        """
        Determines if the specified point is contained within the rectangular region defined by this
        System.Drawing.Rectangle .
        """
        ...

    @overload
    def contains(self, rect: System.Drawing.RectangleF) -> bool:
        """
        Determines if the rectangular region represented by  is entirely contained within
        the rectangular region represented by this System.Drawing.Rectangle .
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Tests whether  is a System.Drawing.RectangleF with the same location and
        size of this System.Drawing.RectangleF.
        """
        ...

    @overload
    def equals(self, other: System.Drawing.RectangleF) -> bool:
        ...

    @staticmethod
    def from_ltrb(left: float, top: float, right: float, bottom: float) -> System.Drawing.RectangleF:
        """Creates a new System.Drawing.RectangleF with the specified location and size."""
        ...

    def get_hash_code(self) -> int:
        """Gets the hash code for this System.Drawing.RectangleF."""
        ...

    @overload
    def inflate(self, x: float, y: float) -> None:
        """Inflates this System.Drawing.Rectangle by the specified amount."""
        ...

    @overload
    def inflate(self, size: System.Drawing.SizeF) -> None:
        """Inflates this System.Drawing.Rectangle by the specified amount."""
        ...

    @staticmethod
    @overload
    def inflate(rect: System.Drawing.RectangleF, x: float, y: float) -> System.Drawing.RectangleF:
        """Creates a System.Drawing.Rectangle that is inflated by the specified amount."""
        ...

    @overload
    def intersect(self, rect: System.Drawing.RectangleF) -> None:
        """Creates a Rectangle that represents the intersection between this Rectangle and rect."""
        ...

    @staticmethod
    @overload
    def intersect(a: System.Drawing.RectangleF, b: System.Drawing.RectangleF) -> System.Drawing.RectangleF:
        """
        Creates a rectangle that represents the intersection between a and b. If there is no intersection, an
        empty rectangle is returned.
        """
        ...

    def intersects_with(self, rect: System.Drawing.RectangleF) -> bool:
        """Determines if this rectangle intersects with rect."""
        ...

    @overload
    def offset(self, pos: System.Drawing.PointF) -> None:
        """Adjusts the location of this rectangle by the specified amount."""
        ...

    @overload
    def offset(self, x: float, y: float) -> None:
        """Adjusts the location of this rectangle by the specified amount."""
        ...

    def to_string(self) -> str:
        """
        Converts the System.Drawing.RectangleF.Location and System.Drawing.RectangleF.Size
        of this System.Drawing.RectangleF to a human-readable string.
        """
        ...

    def to_vector4(self) -> System.Numerics.Vector4:
        """Creates a new System.Numerics.Vector4 from this System.Drawing.RectangleF."""
        ...

    @staticmethod
    def union(a: System.Drawing.RectangleF, b: System.Drawing.RectangleF) -> System.Drawing.RectangleF:
        """Creates a rectangle that represents the union between a and b."""
        ...


class SystemColors(System.Object):
    """This class has no documentation."""

    active_border: System.Drawing.Color

    active_caption: System.Drawing.Color

    active_caption_text: System.Drawing.Color

    app_workspace: System.Drawing.Color

    button_face: System.Drawing.Color

    button_highlight: System.Drawing.Color

    button_shadow: System.Drawing.Color

    control: System.Drawing.Color

    control_dark: System.Drawing.Color

    control_dark_dark: System.Drawing.Color

    control_light: System.Drawing.Color

    control_light_light: System.Drawing.Color

    control_text: System.Drawing.Color

    desktop: System.Drawing.Color

    gradient_active_caption: System.Drawing.Color

    gradient_inactive_caption: System.Drawing.Color

    gray_text: System.Drawing.Color

    highlight: System.Drawing.Color

    highlight_text: System.Drawing.Color

    hot_track: System.Drawing.Color

    inactive_border: System.Drawing.Color

    inactive_caption: System.Drawing.Color

    inactive_caption_text: System.Drawing.Color

    info: System.Drawing.Color

    info_text: System.Drawing.Color

    menu: System.Drawing.Color

    menu_bar: System.Drawing.Color

    menu_highlight: System.Drawing.Color

    menu_text: System.Drawing.Color

    scroll_bar: System.Drawing.Color

    window: System.Drawing.Color

    window_frame: System.Drawing.Color

    window_text: System.Drawing.Color


class Rectangle(System.IEquatable[System_Drawing_Rectangle]):
    """Stores the location and size of a rectangular region."""

    EMPTY: System.Drawing.Rectangle

    @property
    def location(self) -> System.Drawing.Point:
        """
        Gets or sets the coordinates of the upper-left corner of the rectangular region represented by this
        System.Drawing.Rectangle.
        """
        ...

    @property
    def size(self) -> System.Drawing.Size:
        """Gets or sets the size of this System.Drawing.Rectangle."""
        ...

    @property
    def x(self) -> int:
        """
        Gets or sets the x-coordinate of the upper-left corner of the rectangular region defined by this
        System.Drawing.Rectangle.
        """
        ...

    @property
    def y(self) -> int:
        """
        Gets or sets the y-coordinate of the upper-left corner of the rectangular region defined by this
        System.Drawing.Rectangle.
        """
        ...

    @property
    def width(self) -> int:
        """Gets or sets the width of the rectangular region defined by this System.Drawing.Rectangle."""
        ...

    @property
    def height(self) -> int:
        """Gets or sets the width of the rectangular region defined by this System.Drawing.Rectangle."""
        ...

    @property
    def left(self) -> int:
        """
        Gets the x-coordinate of the upper-left corner of the rectangular region defined by this
        System.Drawing.Rectangle .
        """
        ...

    @property
    def top(self) -> int:
        """
        Gets the y-coordinate of the upper-left corner of the rectangular region defined by this
        System.Drawing.Rectangle.
        """
        ...

    @property
    def right(self) -> int:
        """
        Gets the x-coordinate of the lower-right corner of the rectangular region defined by this
        System.Drawing.Rectangle.
        """
        ...

    @property
    def bottom(self) -> int:
        """
        Gets the y-coordinate of the lower-right corner of the rectangular region defined by this
        System.Drawing.Rectangle.
        """
        ...

    @property
    def is_empty(self) -> bool:
        """
        Tests whether this System.Drawing.Rectangle has a System.Drawing.Rectangle.Width
        or a System.Drawing.Rectangle.Height of 0.
        """
        ...

    @overload
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        """
        Initializes a new instance of the System.Drawing.Rectangle class with the specified location
        and size.
        """
        ...

    @overload
    def __init__(self, location: System.Drawing.Point, size: System.Drawing.Size) -> None:
        """Initializes a new instance of the Rectangle class with the specified location and size."""
        ...

    @staticmethod
    def ceiling(value: System.Drawing.RectangleF) -> System.Drawing.Rectangle:
        """Converts a RectangleF to a Rectangle by performing a ceiling operation on all the coordinates."""
        ...

    @overload
    def contains(self, x: int, y: int) -> bool:
        """
        Determines if the specified point is contained within the rectangular region defined by this
        System.Drawing.Rectangle .
        """
        ...

    @overload
    def contains(self, pt: System.Drawing.Point) -> bool:
        """
        Determines if the specified point is contained within the rectangular region defined by this
        System.Drawing.Rectangle .
        """
        ...

    @overload
    def contains(self, rect: System.Drawing.Rectangle) -> bool:
        """
        Determines if the rectangular region represented by  is entirely contained within the
        rectangular region represented by this System.Drawing.Rectangle .
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Tests whether  is a System.Drawing.Rectangle with the same location
        and size of this Rectangle.
        """
        ...

    @overload
    def equals(self, other: System.Drawing.Rectangle) -> bool:
        ...

    @staticmethod
    def from_ltrb(left: int, top: int, right: int, bottom: int) -> System.Drawing.Rectangle:
        """Creates a new System.Drawing.Rectangle with the specified location and size."""
        ...

    def get_hash_code(self) -> int:
        ...

    @overload
    def inflate(self, width: int, height: int) -> None:
        """Inflates this System.Drawing.Rectangle by the specified amount."""
        ...

    @overload
    def inflate(self, size: System.Drawing.Size) -> None:
        """Inflates this System.Drawing.Rectangle by the specified amount."""
        ...

    @staticmethod
    @overload
    def inflate(rect: System.Drawing.Rectangle, x: int, y: int) -> System.Drawing.Rectangle:
        """Creates a System.Drawing.Rectangle that is inflated by the specified amount."""
        ...

    @overload
    def intersect(self, rect: System.Drawing.Rectangle) -> None:
        """Creates a Rectangle that represents the intersection between this Rectangle and rect."""
        ...

    @staticmethod
    @overload
    def intersect(a: System.Drawing.Rectangle, b: System.Drawing.Rectangle) -> System.Drawing.Rectangle:
        """
        Creates a rectangle that represents the intersection between a and b. If there is no intersection, an
        empty rectangle is returned.
        """
        ...

    def intersects_with(self, rect: System.Drawing.Rectangle) -> bool:
        """Determines if this rectangle intersects with rect."""
        ...

    @overload
    def offset(self, pos: System.Drawing.Point) -> None:
        """Adjusts the location of this rectangle by the specified amount."""
        ...

    @overload
    def offset(self, x: int, y: int) -> None:
        """Adjusts the location of this rectangle by the specified amount."""
        ...

    @staticmethod
    def round(value: System.Drawing.RectangleF) -> System.Drawing.Rectangle:
        """Converts a RectangleF to a Rectangle by performing a round operation on all the coordinates."""
        ...

    def to_string(self) -> str:
        """Converts the attributes of this System.Drawing.Rectangle to a human readable string."""
        ...

    @staticmethod
    def truncate(value: System.Drawing.RectangleF) -> System.Drawing.Rectangle:
        """Converts a RectangleF to a Rectangle by performing a truncate operation on all the coordinates."""
        ...

    @staticmethod
    def union(a: System.Drawing.Rectangle, b: System.Drawing.Rectangle) -> System.Drawing.Rectangle:
        """Creates a rectangle that represents the union between a and b."""
        ...


class SizeFConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...

    def create_instance(self, context: System.ComponentModel.ITypeDescriptorContext, property_values: System.Collections.IDictionary) -> System.Object:
        ...

    def get_create_instance_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    def get_properties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def get_properties_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...


class PointConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...

    def create_instance(self, context: System.ComponentModel.ITypeDescriptorContext, property_values: System.Collections.IDictionary) -> System.Object:
        ...

    def get_create_instance_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    def get_properties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def get_properties_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...


class ColorConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...

    def get_standard_values(self, context: System.ComponentModel.ITypeDescriptorContext) -> System.ComponentModel.TypeConverter.StandardValuesCollection:
        ...

    def get_standard_values_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...


class RectangleConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...

    def create_instance(self, context: System.ComponentModel.ITypeDescriptorContext, property_values: System.Collections.IDictionary) -> System.Object:
        ...

    def get_create_instance_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    def get_properties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def get_properties_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...


class SizeConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        ...

    def create_instance(self, context: System.ComponentModel.ITypeDescriptorContext, property_values: System.Collections.IDictionary) -> System.Object:
        ...

    def get_create_instance_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    def get_properties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def get_properties_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...


