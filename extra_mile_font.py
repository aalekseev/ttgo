# -*- coding: utf-8 -*-
# Converted from /home/robotehnik/Downloads/Extra Mile - Demo.ttf using:
#     font2bitmap.py '/home/robotehnik/Downloads/Extra Mile - Demo.ttf' 24 -c 0x20-0x7f

MAP = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
BPP = 1
HEIGHT = 27
MAX_WIDTH = 20
_WIDTHS = \
    b'\x06\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14'\
    b'\x0a\x06\x0e\x0e\x0d\x0c\x0a\x0c\x0c\x0c\x14\x14\x14\x14\x14\x14'\
    b'\x14\x0c\x0f\x0b\x0e\x0d\x0d\x0e\x0e\x06\x0e\x0e\x0a\x12\x0f\x0a'\
    b'\x0d\x09\x0c\x10\x0d\x0b\x0c\x13\x0d\x0a\x0e\x14\x14\x14\x14\x14'\
    b'\x14\x0a\x0a\x09\x09\x09\x0a\x0b\x09\x05\x0b\x0b\x05\x0f\x0a\x08'\
    b'\x0a\x0a\x08\x08\x09\x08\x08\x0e\x0b\x0a\x0c\x14\x14\x14\x14\x06'

OFFSET_WIDTH = 2
_OFFSETS = \
    b'\x00\x00\x00\xa2\x02\xbe\x04\xda\x06\xf6\x09\x12\x0b\x2e\x0d\x4a'\
    b'\x0f\x66\x11\x82\x13\x9e\x15\xba\x17\xd6\x19\xf2\x1c\x0e\x1e\x2a'\
    b'\x20\x46\x21\x54\x21\xf6\x23\x70\x24\xea\x26\x49\x27\x8d\x28\x9b'\
    b'\x29\xdf\x2b\x23\x2c\x67\x2e\x83\x30\x9f\x32\xbb\x34\xd7\x36\xf3'\
    b'\x39\x0f\x3b\x2b\x3c\x6f\x3e\x04\x3f\x2d\x40\xa7\x42\x06\x43\x65'\
    b'\x44\xdf\x46\x59\x46\xfb\x48\x75\x49\xef\x4a\xfd\x4c\xe3\x4e\x78'\
    b'\x4f\x86\x50\xe5\x51\xd8\x53\x1c\x54\xcc\x56\x2b\x57\x54\x58\x98'\
    b'\x5a\x99\x5b\xf8\x5d\x06\x5e\x80\x60\x9c\x62\xb8\x64\xd4\x66\xf0'\
    b'\x69\x0c\x6b\x28\x6c\x36\x6d\x44\x6e\x37\x6f\x2a\x70\x1d\x71\x2b'\
    b'\x72\x54\x73\x47\x73\xce\x74\xf7\x76\x20\x76\xa7\x78\x3c\x79\x4a'\
    b'\x7a\x22\x7b\x30\x7c\x3e\x7d\x16\x7d\xee\x7e\xe1\x7f\xb9\x80\x91'\
    b'\x82\x0b\x83\x34\x84\x42\x85\x86\x87\xa2\x89\xbe\x8b\xda\x8d\xf6'

_BITMAPS =\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xff\xe0\xff\xfe\x0f\xff'\
    b'\xe0\xff\xaa\x0f\xfa\xa0\xd9\xf6\x0f\xff\xa0\xf6\xee\x0f\xff\xe0'\
    b'\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfe\x0f'\
    b'\xff\xe0\xff\xfe\x0f\xfa\xa0\xff\xaa\x0d\x9f\x60\xff\xfa\x0f\x6e'\
    b'\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0'\
    b'\xff\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xaa\x0f\xfa\xa0\xd9\xf6\x0f'\
    b'\xff\xa0\xf6\xee\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff'\
    b'\xe0\xff\xfe\x0f\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xfa\xa0\xff\xaa'\
    b'\x0d\x9f\x60\xff\xfa\x0f\x6e\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x0f'\
    b'\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff'\
    b'\xaa\x0f\xfa\xa0\xd9\xf6\x0f\xff\xa0\xf6\xee\x0f\xff\xe0\xff\xfe'\
    b'\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfe\x0f\xff\xe0'\
    b'\xff\xfe\x0f\xfa\xa0\xff\xaa\x0d\x9f\x60\xff\xfa\x0f\x6e\xe0\xff'\
    b'\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xfe'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xff'\
    b'\xe0\xff\xfe\x0f\xff\xe0\xff\xaa\x0f\xfa\xa0\xd9\xf6\x0f\xff\xa0'\
    b'\xf6\xee\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff'\
    b'\xfe\x0f\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xfa\xa0\xff\xaa\x0d\x9f'\
    b'\x60\xff\xfa\x0f\x6e\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0'\
    b'\xff\xfe\x0f\xff\xe0\xff\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xaa\x0f'\
    b'\xfa\xa0\xd9\xf6\x0f\xff\xa0\xf6\xee\x0f\xff\xe0\xff\xfe\x0f\xff'\
    b'\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfe\x0f\xff\xe0\xff\xfe'\
    b'\x0f\xfa\xa0\xff\xaa\x0d\x9f\x60\xff\xfa\x0f\x6e\xe0\xff\xfe\x0f'\
    b'\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xff\xe0\xff'\
    b'\xfe\x0f\xff\xe0\xff\xaa\x0f\xfa\xa0\xd9\xf6\x0f\xff\xa0\xf6\xee'\
    b'\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x0f'\
    b'\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xfa\xa0\xff\xaa\x0d\x9f\x60\xff'\
    b'\xfa\x0f\x6e\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xfe'\
    b'\x0f\xff\xe0\xff\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xaa\x0f\xfa\xa0'\
    b'\xd9\xf6\x0f\xff\xa0\xf6\xee\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff'\
    b'\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xfa'\
    b'\xa0\xff\xaa\x0d\x9f\x60\xff\xfa\x0f\x6e\xe0\xff\xfe\x0f\xff\xe0'\
    b'\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xff\xe0\xff\xfe\x0f'\
    b'\xff\xe0\xff\xaa\x0f\xfa\xa0\xd9\xf6\x0f\xff\xa0\xf6\xee\x0f\xff'\
    b'\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x03\xc1\xf8\x7f\x3f'\
    b'\xcf\x73\x8d\xe3\x79\x9c\x67\x1f\x8e\xe7\x3b\xcf\xe1\xf0\x78\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x79\xf7\x8e\x39'\
    b'\xe7\x9c\x71\xc7\x1c\x61\x86\x38\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x01\xf0\x0f\xe0\x7f\xc1\xe7\x00\x3c\x00\xe0\x07\x80\x3c'\
    b'\x00\xe0\x06\x80\x3c\x01\xe0\x07\xfe\x7f\xff\xfe\x0f\xe0\x18\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x1e\x03\xfc\x3f\xf8\x7b\xe0\x1e\x00\xf0\x0f\xf8\x3f\xf0'\
    b'\x00\xc0\x0f\x00\x78\x03\x80\x1d\x03\xa0\x5f\x03\xa0\x07\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x40\x67\x87\x3c\x39\xc1\x9e\x18\xe1\xc7\x0c\x78\xe3\x8f\xfc\x7f'\
    b'\xc0\x0e\x00\x60\x03\x80\x38\x01\xc0\x0e\x00\x40\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x3f\xf9\xff\x8e'\
    b'\x01\xf0\x1e\x01\xc0\x3c\x07\xf8\x1f\xc0\x0e\x01\xe0\x3c\x07\xc1'\
    b'\xf0\x3e\x07\xc0\x70\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x0e\x03\xc1\xf0\x78\x1c\x0f\x03\x81\xe0\x70\x1f\x8f'\
    b'\xf7\xee\xe3\xb0\xae\x73\x78\xfc\x18\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x80\x3c\x3f\xef\xfd\x01\xc0\x38\x03\x80'\
    b'\x30\x07\x01\xe0\x6e\x00\xc0\x1c\x01\x40\x18\x03\x80\x38\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x30\x0f'\
    b'\x01\xfc\x3e\xe7\x84\x70\xe6\x1c\x6f\x87\xe0\x3f\x87\xcc\xf0\xfe'\
    b'\x07\xc0\xfc\x1d\x8f\x9f\xe0\x70\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x06\x00\x7c\x0f\xe3\xce\x79\xc7\x1c\xf3'\
    b'\xce\x79\xff\x8f\xf8\x07\x00\x70\x07\x00\x60\x0e\x00\xe0\x0e\x00'\
    b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x7f\xff\x07\xff\xf0\x7f\xff\x07\xfd\x50\x7f\xd5\x06\xcf'\
    b'\xb0\x7f\xfd\x07\xb7\x70\x7f\xff\x07\xff\xf0\x7f\xff\x07\xff\xf0'\
    b'\x7f\xff\x07\xff\xf0\x7f\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x07\xff\xf0\x7f\xff\x07\xff\xf0\x7f\xd5\x07'\
    b'\xfd\x50\x6c\xfb\x07\xff\xd0\x7b\x77\x07\xff\xf0\x7f\xff\x07\xff'\
    b'\xf0\x7f\xff\x07\xff\xf0\x7f\xff\x07\xff\xf0\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\xff\x07\xff\xf0\x7f\xff'\
    b'\x07\xfd\x50\x7f\xd5\x06\xcf\xb0\x7f\xfd\x07\xb7\x70\x7f\xff\x07'\
    b'\xff\xf0\x7f\xff\x07\xff\xf0\x7f\xff\x07\xff\xf0\x7f\xff\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xff\xf0\x7f'\
    b'\xff\x07\xff\xf0\x7f\xd5\x07\xfd\x50\x6c\xfb\x07\xff\xd0\x7b\x77'\
    b'\x07\xff\xf0\x7f\xff\x07\xff\xf0\x7f\xff\x07\xff\xf0\x7f\xff\x07'\
    b'\xff\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x7f\xff\x07\xff\xf0\x7f\xff\x07\xfd\x50\x7f\xd5\x06\xcf\xb0\x7f'\
    b'\xfd\x07\xb7\x70\x7f\xff\x07\xff\xf0\x7f\xff\x07\xff\xf0\x7f\xff'\
    b'\x07\xff\xf0\x7f\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x07\xff\xf0\x7f\xff\x07\xff\xf0\x7f\xd5\x07\xfd\x50'\
    b'\x6c\xfb\x07\xff\xd0\x7b\x77\x07\xff\xf0\x7f\xff\x07\xff\xf0\x7f'\
    b'\xff\x07\xff\xf0\x7f\xff\x07\xff\xf0\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x7f\xff\x07\xff\xf0\x7f\xff\x07\xfd'\
    b'\x50\x7f\xd5\x06\xcf\xb0\x7f\xfd\x07\xb7\x70\x7f\xff\x07\xff\xf0'\
    b'\x7f\xff\x07\xff\xf0\x7f\xff\x07\xff\xf0\x7f\xff\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38\x07\xc0\x7e\x07\xc0\xfc'\
    b'\x0f\xc1\xfc\x1f\xc3\xdc\x39\xc7\x9c\x7f\xcf\xfc\xf1\xce\x1d\xe1'\
    b'\xc0\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x3f\x80\x7f\x80\xc3\x81\xe7\x03\xdc\x07\xf8\x1f\xe0\x3f\x80\x7f'\
    b'\xc0\xff\xc3\xc1\xc7\x81\xce\x0f\xbc\x3e\x79\xf8\xff\xe3\xfe\x01'\
    b'\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x20\x0e\x03\xe0\xfc\x3e\x0f\x81\xe0\x78\x1e\x03'\
    b'\x80\x70\x1c\x03\x83\x71\xef\xfd\xfe\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x60\x07\xf8\x0f\xf0\x01\xe1\xe1\xc7\x87'\
    b'\x1e\x0c\x78\x39\xe1\xcf\x87\x3c\x3c\xf1\xe3\xcf\x1e\x5c\x78\xc1'\
    b'\xf6\x07\xbc\x1f\xc0\x7c\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\x3f\xe1\x80\x0f\x00\x78'\
    b'\x03\xc0\x3c\x01\xfe\x0f\xf8\xfc\x07\x80\x38\x03\xc2\x1e\x79\xff'\
    b'\xe7\xf8\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x7c\x1f\xf0\xf8\x43\x80\x1c\x00\xe0\x0e\x00\x70\x03'\
    b'\xfc\x1f\xf0\xf0\x0e\x00\x70\x03\x00\x18\x01\xc0\x0e\x00\xc0\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20'\
    b'\x00\xc0\x07\x00\x3e\x00\xf0\x07\xc0\x1e\x00\xf0\x07\x80\x1e\xfe'\
    b'\xff\xfb\x9f\x0e\x0e\x70\xf9\xcf\xc6\xfe\x1f\xe0\x3e\x00\x30\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x38\x20\xf1\xe3'\
    b'\x87\x8e\x1e\x38\x78\xe1\xc7\x07\x1c\x1c\x70\x71\xc1\xc7\x0e\x18'\
    b'\xfc\x7f\xe1\xf3\x9f\x0e\x78\x38\xe1\xc3\x87\x1c\x1c\x00\x70\x01'\
    b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x71'\
    b'\xc7\x3c\xf3\xce\x38\xe7\x9c\x71\xc0\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x79\xff\xe7\xff\x8f\xe0\x03\x80\x0e\x00\x30\x00'\
    b'\xc0\x03\x00\x1c\x1c\x70\x71\x81\xce\x07\x30\x0d\xc0\x3e\x00\x70'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0'\
    b'\x03\xc0\x0f\x00\x38\x00\xe0\x03\x82\x0e\x1c\x78\xf9\xe7\x87\x3c'\
    b'\x1f\xc0\x7e\x01\xf8\x0f\xf0\x39\xe0\xe3\xc3\x87\x9e\x00\x70\x01'\
    b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x70\x1e\x0f\x03\xc0\xf0\x38\x0e\x07\x81\xc0\x70\x1c\x0f'\
    b'\x03\xc0\xdf\xff\xe4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x01\x81\xe0\xf0\x78\x3c\x3e\x1f\x0f\x87\xc3'\
    b'\xe3\xf0\xf8\xfc\x7e\x77\x1d\xdd\xc7\x7f\x71\x9f\xac\xe7\xe3\x39'\
    b'\xf0\xce\x7c\x33\x8e\x0d\xe3\x03\x70\x00\xc0\x00\x10\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03'\
    b'\x84\x07\x1e\x0e\x3e\x1c\x7e\x30\xfe\x61\xfd\xc3\xbb\x0f\x76\x1c'\
    b'\xfc\x39\xf8\x71\xe1\xc3\xc3\x87\x87\x0e\x0e\x1c\x18\x30\x70\x00'\
    b'\x40\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x60\x1f\x0f\xe3\xfd\xf7\x79\xde\x37\x0f\xc6\xf1\xf8'\
    b'\xfe\x7b\x9e\xff\x3f\x87\xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x1f\xe0\xff\x87\x0e\x7c\xf3\xcf\x1e\xf8\xff\x87'\
    b'\xf0\x3f\x01\xe0\x1e\x00\xf0\x07\x00\x38\x01\xc0\x0e\x00\xe0\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x18\x1f\x0f\xcf\xf7\xbb\x8f\xc7\xc3\xe1\xf7\xfb\xfd\xee\xf7\xff'\
    b'\xf0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x83'\
    b'\xfe\x30\xf1\xc7\x1c\x71\xcf\x1d\xe3\xfc\x3f\x03\xf0\x37\x07\x38'\
    b'\x71\xc7\x0e\x60\xf6\x07\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x07\x80\x0f\xc0\x1f\xc0'\
    b'\x3e\x00\x7c\x00\xf0\x00\xff\x80\x7f\xe0\x3f\xe0\x03\xf0\x07\xe0'\
    b'\x1f\xc0\x3f\x00\xfc\x07\xa8\x0f\xd0\x06\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc3\xff'\
    b'\xff\xef\xc0\x03\x80\x1e\x00\xf0\x07\x00\x38\x01\xc0\x1e\x00\xe0'\
    b'\x07\x00\x38\x01\xc0\x0c\x00\xe0\x07\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x0f\xe1\xfc\x1f\x87\xf0'\
    b'\xfe\x1f\x87\x70\xee\x3d\xc7\x39\xc7\x78\xfe\x1f\x81\xe0\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00'\
    b'\x70\x0e\x70\xef\x1c\x71\xc7\xb8\x7b\x83\xf0\x3f\x03\xe0\x3e\x03'\
    b'\xe0\x3c\x03\xc0\x3c\x03\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x66\x00\x0e\xf0'\
    b'\x03\x9e\x00\x73\xc0\x1e\x79\xc3\x8f\x3c\xf1\xef\xbc\x3f\xf7\x87'\
    b'\xf7\xe0\xfc\xfc\x1f\x9f\x83\xe3\xe0\x78\x7c\x1e\x0e\x01\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x07\x98\x3e\xe3\xe3\x1e'\
    b'\x0d\xe0\x7f\x01\xf0\x0f\x00\x78\x07\xc0\x76\x03\xd8\x3c\xc1\xe0'\
    b'\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x18\x07\x01\xf8\xff\x39\xde\x3f\x0f\x81\xe0\x38\x1c\x07'\
    b'\x01\x80\xe0\x38\x0c\x07\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x7c\x1f\xfc\x7d\xf0\x07\x80\x3c\x01\xe0\x07'\
    b'\x80\x3c\x01\xe0\x0f\x00\x38\x01\xe0\x0f\x00\x38\xfc\xff\xff\xfc'\
    b'\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x3f\xff\x83\xff\xf8\x3f\xff\x83\xfe\xa8\x3f'\
    b'\xea\x83\x67\xd8\x3f\xfe\x83\xdb\xb8\x3f\xff\x83\xff\xf8\x3f\xff'\
    b'\x83\xff\xf8\x3f\xff\x83\xff\xf8\x3f\xff\x80\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\xff\xf8\x3f\xff\x83\xff\xf8'\
    b'\x3f\xea\x83\xfe\xa8\x36\x7d\x83\xff\xe8\x3d\xbb\x83\xff\xf8\x3f'\
    b'\xff\x83\xff\xf8\x3f\xff\x83\xff\xf8\x3f\xff\x83\xff\xf8\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3f\xff\x83\xff'\
    b'\xf8\x3f\xff\x83\xfe\xa8\x3f\xea\x83\x67\xd8\x3f\xfe\x83\xdb\xb8'\
    b'\x3f\xff\x83\xff\xf8\x3f\xff\x83\xff\xf8\x3f\xff\x83\xff\xf8\x3f'\
    b'\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03'\
    b'\xff\xf8\x3f\xff\x83\xff\xf8\x3f\xea\x83\xfe\xa8\x36\x7d\x83\xff'\
    b'\xe8\x3d\xbb\x83\xff\xf8\x3f\xff\x83\xff\xf8\x3f\xff\x83\xff\xf8'\
    b'\x3f\xff\x83\xff\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x3f\xff\x83\xff\xf8\x3f\xff\x83\xfe\xa8\x3f\xea\x83'\
    b'\x67\xd8\x3f\xfe\x83\xdb\xb8\x3f\xff\x83\xff\xf8\x3f\xff\x83\xff'\
    b'\xf8\x3f\xff\x83\xff\xf8\x3f\xff\x80\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x03\xff\xf8\x3f\xff\x83\xff\xf8\x3f\xea'\
    b'\x83\xfe\xa8\x36\x7d\x83\xff\xe8\x3d\xbb\x83\xff\xf8\x3f\xff\x83'\
    b'\xff\xf8\x3f\xff\x83\xff\xf8\x3f\xff\x83\xff\xf8\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'\
    b'\xc0\xf0\x3c\x3e\x1f\x8e\xe7\x39\xce\x7f\x3f\xc0\x60\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xe0\x78\x1e\x07\x01'\
    b'\xc0\x70\x38\x0f\xe3\xfc\xe3\x31\xdc\xe7\x71\xfc\x3c\x3e\x0f\x01'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x60\x78\x78\x78\x38\x38\x38\x1c\x3c\xf7\xf0\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x70\x30\x38\x1c'\
    b'\x0e\x07\x03\x07\x87\xc7\xe3\x63\xb1\xdc\x7c\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'\
    b'\xc1\xf1\xe8\xfc\xfc\x70\x60\xb3\xff\xc6\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x06\x03\xc1\xf8\x78\x3c\x0f\x03\x81\xc0\x72'\
    b'\x1f\xdf\xff\xf0\xf0\x38\x0e\x07\x81\xc0\x70\x18\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03'\
    b'\x01\xf8\x7f\x9e\xf7\x9c\xe3\x9b\xf3\xfe\x03\xc0\x70\x0e\x33\x8e'\
    b'\x71\xce\x3f\x83\xf0\x7a\x07\x80\x00\x00\x00\x00\x00\x60\x3c\x1c'\
    b'\x0e\x07\x03\x83\xc1\xc0\xf8\x7f\x3f\xbc\xdc\x6e\x77\x3f\x9c\x0e'\
    b'\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\xc0\x02\x18'\
    b'\xee\x73\x9c\xce\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x0c\x03\xc0\x7c\x00\x00\x00\x10\x03\x00\x60\x1c\x03\x80\x60'\
    b'\x0e\x03\x80\x70\x0e\x3d\xc7\xb8\x7e\x0f\xc0\xf8\x0e\x00\x80\x00'\
    b'\x00\x00\x60\x0f\x01\xc0\x38\x0f\x01\xe0\x38\x0f\x01\xe6\x3b\xe7'\
    b'\xe1\xf0\x3c\x07\xe0\xcf\x18\x76\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x63\x9c\xe7\x73\x9c\xe6\x73\x9c\xc6\x31'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x0e\x00\x1c\x00\x38\x10\xfc\x71\xf8\xe3\xf3\xc7\xef\x8f\xfb\x1d'\
    b'\xe6\x7b\x8c\xe6\x19\xc0\x37\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x01\x80\x73\x19\xe6\xf9\xae\x7b\x1c\xc7\x30\xc8\x44\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x04\x0f\x0f\x9f\x9c\xdd\xf9\xbb\xbb\x1f\x0c\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x0f\xe0'\
    b'\x3c\xe3\x3d\xce\x73\xbc\xfe\x7e\x1f\x07\x01\xc0\x70\x18\x0e\x01'\
    b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x0f\x87\xf3\x39\x9e\xe7\xb1\xef\xf3\xfc\x0f\x03\x80\xe0\x78\x1e'\
    b'\x07\x81\xc8\x7e\x3e\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'\
    b'\xc9\xfd\xf1\xe1\xc1\x83\x83\x83\x03\x02\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x70\xf1\xe3\xf9'\
    b'\xfc\x9c\x78\xf3\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x02\x07\x83\x81\xc0\xe0\xf0\x78\x3f\x7c\x4e\x0f\x07\x83\xc1\xc0'\
    b'\xe0\x70\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x33\x33\xb3\x33\x37\x36\x3e\x3c\x3c\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x39\xb9\xbb\x3b\x3e\x3e\x3c\x38\x38\x30\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x04\xe7\x13\x3c\xcc\xf3\x37\xcc\xdf\x63\xdd\xcf\x7c\x39\xf0'\
    b'\xe3\x82\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\xc7\x89'\
    b'\xe1\xf8\x1e\x03\x80\xf0\x3e\x0d\x63\xcc\x00\x80\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x84\xf3\xdc\xe7\x79\xdc\x7f\x1f\x81\xc0\x70\x38\x0e\x07'\
    b'\x01\xc0\xe0\x30\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x08\x3f\x87\xdc\x03\xc0\x70\x0e\x01\xc0\x38'\
    b'\x0f\x01\xff\x9f\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xfa\xa0'\
    b'\xff\xaa\x0d\x9f\x60\xff\xfa\x0f\x6e\xe0\xff\xfe\x0f\xff\xe0\xff'\
    b'\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\xff\xe0\xff\xfe\x0f\xff'\
    b'\xe0\xff\xaa\x0f\xfa\xa0\xd9\xf6\x0f\xff\xa0\xf6\xee\x0f\xff\xe0'\
    b'\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfe\x0f'\
    b'\xff\xe0\xff\xfe\x0f\xfa\xa0\xff\xaa\x0d\x9f\x60\xff\xfa\x0f\x6e'\
    b'\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff\xe0'\
    b'\xff\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xaa\x0f\xfa\xa0\xd9\xf6\x0f'\
    b'\xff\xa0\xf6\xee\x0f\xff\xe0\xff\xfe\x0f\xff\xe0\xff\xfe\x0f\xff'\
    b'\xe0\xff\xfe\x0f\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
    b'\x00\x00\x00'

WIDTHS = memoryview(_WIDTHS)
OFFSETS = memoryview(_OFFSETS)
BITMAPS = memoryview(_BITMAPS)