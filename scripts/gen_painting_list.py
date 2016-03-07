import json
from glob import glob
import os.path as path
from os.path import relpath, join, isfile

def main():
    # thumb_fn = [relpath(fn, '..') for fn in glob('../img/thumbs/*Thumb_KittyYeung.jpg') if ('Frontpage' not in fn)]
    # thumb_fn.sort()
    hires_fn = [relpath(fn, '..') for fn in glob('../img/hires/*_KittyYeung.jpg') if ('Frontpage' not in fn)]
    hires_fn.sort()

    thumb_fn = [join('img/thumbs', relpath(fn, 'img/hires')).replace('_KittyYeung.jpg', 'Thumb_KittyYeung.jpg') for fn in hires_fn]

    for t,h in zip(thumb_fn, hires_fn):
        print t, h, isfile('../' + t)

    s = json.dumps([{
        'hires': h,
        'thumb': t
    } for h,t in zip(hires_fn, thumb_fn)])

    f = open('../paintings.json', 'w')
    f.write(s)
    f.close()

    return 0

if __name__ == '__main__':
    main()
