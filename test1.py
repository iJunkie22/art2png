from __future__ import print_function
from PIL import Image, ImageDraw
import struct
import plistlib
import artfile
import os.path
import os


def run_test(art_file, verbose=False):
    saf = os.path.abspath(art_file)
    af_bd = str(saf).rpartition('/')[0]
    af_bn = str(saf).rpartition('/')[2].rpartition('.')[0]
    test_d = os.path.join(af_bd, af_bn)
    if not os.path.isdir(test_d):
        os.mkdir(test_d)
    pl_f = os.path.join(test_d, af_bn) + '.plist'

    fd1 = open(saf, mode='rb')

    try:
        #mn = fd1.read(8)
        pl_str = artfile.Curses.unpack_header_and_plist(fd1)
        # h = struct.unpack('xxxxxxxxi', fd1.read(12))[0]
        # pl_str = struct.unpack('{}s'.format(h), fd1.read(h))[0]
        pl_dict = plistlib.readPlistFromString(pl_str)
        af1 = artfile.ArtFile.strict_from_dict(pl_dict)
        # fd1.read(4)
        for li, layer in enumerate(af1.get_layers(), start=1):
            layer = artfile.ArtLayer.strict_from_dict(af1.layers["layer" + str(li)])

            lw = (layer.contentX1 - layer.contentX0) + 1
            lh = (layer.contentY1 - layer.contentY0) + 1

            lim = Image.new(mode='RGBA', size=(af1.width, af1.height), color=None)
            ldr = ImageDraw.Draw(lim, mode='RGBA')
            layer_len = artfile.Curses.unpack_layer_header(fd1)
            # layer_len = struct.unpack('i', fd1.read(4))[0]

            for px_i in xrange(0, (layer_len / 4)):
                px_y, px_x = divmod(px_i, lw)
                px_x += layer.contentX0
                px_y += layer.contentY0
                if px_y > af1.height:
                    print("hey")
                if verbose:
                    print(px_x, px_y)
                px_color = artfile.Curses.unpack_pixel(fd1)
                # px_color = struct.unpack('BBBB', fd1.read(4))
                if verbose:
                    print(fd1.tell(), px_color)
                ldr.point((px_x, px_y), fill=px_color)

            del ldr
            lim.save(os.path.join(test_d, str("layer" + str(li) + ".png")), "PNG")

        plistlib.writePlist(pl_dict, pl_f)

    finally:
        fd1.close()


run_test("/Users/ethan/Pictures/ArtStudio/test5/REtest.art")
run_test("/Users/ethan/Pictures/ArtStudio/Untitled 3.art")
