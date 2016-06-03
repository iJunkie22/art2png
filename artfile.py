from __future__ import print_function
from collections import namedtuple
import plistlib
import struct

ColorTuple = namedtuple('ColorTupleType', ['r', 'g', 'b'], verbose=True)
ColorTuple2 = namedtuple('ColorTupleType', ['r', 'g', 'b', 'a'], verbose=True)
ColorTuple.__str__ = lambda self: ','.join([str(x) for x in self])
ColorTuple2.__str__ = lambda self: ','.join([str(x) for x in self])

#__oldnew = ColorTuple.__new__
#ColorTuple._make = classmethod(lambda cls, iterable, new=tuple.__new__, len=len: print(cls))


class ArtFile(object):
    def __init__(self):
        self._old_keys = None
        self._old_keys = list(self.__dict__.keys())
        self.activeLayer = 1
        self.color = str(ColorTuple(255, 255, 255))
        self.color2 = str(ColorTuple(0, 0, 0))
        self.currentTool = {}
        self.eyedropperMode = 0
        self.gridSpacing = 10
        self.gridSubdivisions = 5
        self.guidelinesH = {}
        self.guidelinesV = {}
        self.height = 1
        self.layers = {}
        self.masks = {}
        self.nLayers = 0
        self.nMasks = 0
        self.name = "UntitledArtFile"
        self.orientation = 1
        self.shape = 0
        self.showGrid = False
        self.showGuidelines = True
        self.snapToGrid = False
        self.snapToGuidelines = True
        self.swatches = {}
        self.symmetry = 0
        self.width = 1
        self.new_keys = [k for k in self.__dict__.keys() if k not in self._old_keys]
        self.new_keys_rules = {k: type(self.__dict__[k]) for k in self.new_keys}

    def weak_unpack(self, d1):
        self.__dict__.update(d1)

    def strict_unpack(self, d2):
        for k, v in d2.items():
            assert k in self.new_keys
            assert type(v) == self.new_keys_rules[k] or \
                ((self.new_keys_rules[k] == dict) and (v.__class__.__name__ == plistlib._InternalDict.__name__))
            self.__dict__[k] = v

    def get_dict(self):
        return {k: self.__dict__[k] for k in self.new_keys}

    @classmethod
    def weak_from_dict(cls, d3):
        af1 = cls()
        af1.weak_unpack(d3)
        return af1

    @classmethod
    def strict_from_dict(cls, d4):
        af2 = cls()
        af2.strict_unpack(d4)
        return af2

    def get_swatches(self):
        return {k: ColorTuple(self.swatches[k].split(',')) for k in self.swatches.keys()}

    def add_layer(self, new_layer):
        assert isinstance(ArtLayer, new_layer)
        self.nLayers += 1
        self.layers["layer" + str(self.nLayers)] = new_layer.get_dict()

    def get_layers(self, strict=True):
        for lk in sorted(self.layers.keys()):
            if strict:
                yield ArtLayer.strict_from_dict(self.layers[lk])
            else:
                yield ArtLayer.weak_from_dict(self.layers[lk])


class ArtLayer(object):
    def __init__(self):
        self._old_keys = None
        self._old_keys = list(self.__dict__.keys())
        self.blending = 0
        self.contentX0 = 0
        self.contentX1 = 0
        self.contentY0 = 0
        self.contentY1 = 0
        self.idNumber = -1
        self.linked = False
        self.maskId = -1
        self.maskVisible = False
        self.name = "UntitledLayer"
        self.opacity = 1.0
        self.preserveTransparency = False
        self.textAlignment = 0
        self.textAutoSetName = True
        self.textColorB = 0
        self.textColorG = 0
        self.textColorR = 0
        self.textInterfaceOrientation = 0
        self.textPositionX = 0.0
        self.textPositionY = 0.0
        self.textShadow = False
        self.textFont = "Helvetica"
        self.textShadowColorB = 0
        self.textShadowColorG = 0
        self.textShadowColorR = 0
        self.textShadowOffsetX = 0
        self.textShadowOffsetY = 0
        self.textShadowOpacity = 0.0
        self.textSize = 0.0
        self.textTransformAngle = 0.0
        self.textTransformPanX = 0.0
        self.textTransformPanY = 0.0
        self.textTransformZoom = 0.0
        self.textText = ""
        self.type = 0
        self.visible = True
        self.new_keys = [k for k in self.__dict__.keys() if k not in self._old_keys]
        self.new_keys_rules = {k: type(self.__dict__[k]) for k in self.new_keys}

    def weak_unpack(self, d1):
        self.__dict__.update(d1)

    def strict_unpack(self, d2):
        for k, v in d2.items():
            assert k in self.new_keys
            assert type(v) == self.new_keys_rules[k]
            self.__dict__[k] = v

    def get_dict(self):
        return {k: self.__dict__[k] for k in self.new_keys}

    @classmethod
    def weak_from_dict(cls, d3):
        al1 = cls()
        al1.weak_unpack(d3)
        return al1

    @classmethod
    def strict_from_dict(cls, d4):
        al2 = cls()
        al2.strict_unpack(d4)
        return al2


class ArtTool(object):
    def __init__(self):
        self._old_keys = None
        self._old_keys = list(self.__dict__.keys())
        self._angle0 = 0.0
        self._blurMode = 0
        self._blurSharpenMode = 0
        self._brushName = "UntitledBrush"
        self._colorize = False
        self._dodgeBurnColor = False
        self._dodgeBurnMode = 1
        self._fadeout = 0.0
        self._fadeoutScale = 0.0
        self._flipMode = 0
        self._forceEraser = False
        self._gradientMode = 0
        self._gradientOffset = 0.0
        self._gradientRepeat = 0
        self._gradientShape = 0
        self._gradientSmooth = True
        self._hardEdge = False
        self._incremental = True
        self._jitterAngle = 0.0
        self._jitterFlipMode = 0
        self._jitterHue = 0.0
        self._jitterLightness = 0.0
        self._jitterOpacity = 0.0
        self._jitterSaturation = 0.0
        self._jitterScatter = 0.0
        self._jitterSize = 0.0
        self._jitterSpacing = 0.0
        self._jitterSqueeze = 0.0
        self._livePreview = False
        self._name = "UntitledTool"
        self._opacity = 1.0
        self._opacityStart = 1.0
        self._opacityStop = 1.0
        self._sampleMode = 0
        self._scale = 0.25
        self._scaleStart = 0.25
        self._scaleStop = 0.25
        self._scaleFromCenter = False
        self._selectMode = 0
        self._selectRatioX = -1.0
        self._selectRatioY = -1.0
        self._selectShape = 0
        self._smartMode = 1
        self._spacing = 0.09
        self._speedOpacity = 0.0
        self._speedSize = 0.0
        self._squeeze = 0.0
        self._textAlignment = 0
        self._textFont = "Helvetica"
        self._textShadow = False
        self._textShadowOffsetX = 0
        self._textShadowOffsetY = 1
        self._threshold = 15.0
        self._toolType = 0
        self._wetness = 0.0
        self.new_keys = [k for k in self.__dict__.keys() if k not in self._old_keys]
        self.new_keys_rules = {k: type(self.__dict__[k]) for k in self.new_keys}

    def weak_unpack(self, d1):
        self.__dict__.update(d1)

    def strict_unpack(self, d2):
        for k, v in d2.items():
            assert k in self.new_keys
            assert type(v) == self.new_keys_rules[k]
            self.__dict__[k] = v

    def get_dict(self):
        return {k: self.__dict__[k] for k in self.new_keys}

    @classmethod
    def weak_from_dict(cls, d3):
        at1 = cls()
        at1.weak_unpack(d3)
        return at1

    @classmethod
    def strict_from_dict(cls, d4):
        at2 = cls()
        at2.strict_unpack(d4)
        return at2


class Curses:
    _layer_h = struct.Struct('<ii')
    _pixl_rgba = struct.Struct('<4B')
    _file_h = struct.Struct('<8Bi')

    @classmethod
    def unpack_layer_header(cls, fd_in):
        validator, layer_len = cls._layer_h.unpack(fd_in.read(8))
        assert validator == 3
        return layer_len

    @classmethod
    def unpack_pixel(cls, fd_in):
        pix_tup = cls._pixl_rgba.unpack(fd_in.read(4))
        return ColorTuple2(*pix_tup)

    @classmethod
    def unpack_file_header(cls, fd_in):
        v1, v2, v3, v4, v5, v6, v7, v8, header_len = cls._file_h.unpack(fd_in.read(12))
        assert [x == 0 for x in (v1, v2, v3, v6, v7, v8)]
        assert v4 == 64
        assert v5 == 1
        return header_len

    @classmethod
    def unpack_header_and_plist(cls, fd_in):
        pl_len = cls.unpack_file_header(fd_in)
        pl_str = struct.unpack('{}s'.format(pl_len), fd_in.read(pl_len))[0]
        return pl_str

