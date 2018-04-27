import os, imghdr
from shutil import copyfile

def get_images_dir(directory):
    '''
    Return filenames of all image in dir (recursively).
    '''
    orig =[]
    denoise = []

    if not os.path.isdir('static'):
        os.mkdir('static')

    #walk the tree
    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath_root = os.path.join(root, filename)

            # check if files are images
            if imghdr.what(filepath_root) != None:
                filepath_static = os.path.join('static', filename)
                copyfile(filepath_root, filepath_static)
                if 'noisy' in filename:
                    orig.append(filename)
                if 'denoised' in filename:
                    denoise.append(filename)
    orig.sort()
    denoise.sort()
    nimages = range(len(orig))
    return nimages, orig, denoise

