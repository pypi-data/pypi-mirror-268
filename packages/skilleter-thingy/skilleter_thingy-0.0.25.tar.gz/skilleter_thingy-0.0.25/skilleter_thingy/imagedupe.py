#!/usr/bin/env python3
"""Hash photos to find closely-similar images and report them"""

# TODO: Configurable hash type and stored in pickle data
# TODO: Option to pickle duplicates
# TODO: Check for files that are no longer present after scanning and remove them from the data
# TODO: Display duplicates - borrow code from imagedup
# TODO: Note that if a==b, we get reports for a==b and b==a so we need to do some filtering and decide on what's likely to be an original and what is a duplicate
# TODO: Maybe store file date, size and image dimensions in 'updated' for better comparisons
# TODO: Pickle data named for directories
# TODO: Use database instead of pickling - very slow to load big pickles - would facilitate scanning/checking specific directories
# TODO: If directories specified, the only scan and compare within those directories (but keep everything in pickle file (yes, it will get biggerer, and biggererer)

import threading
import queue
import sys
import os
import pickle
import argparse
from pathlib import PurePath
from typing import List, Union

from imagededup.methods import PHash

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
from matplotlib import figure

import numpy as np
from PIL import Image

################################################################################

PICKLE_FILE = 'imagedupe.pickle'

IMAGE_EXT_LIST =  ('.jpeg', '.jpg', '.png', '.bmp', '.mpo', '.ppm', '.tif', '.tiff', '.gif', '.svg', '.pgm', '.pbm', '.webp')

PICKLE_VERSION = 1

NUM_THREADS = 24

################################################################################

def queue_files_to_hash(file_queue, directories):
    """Read all the specfied directories queue every file therein"""

    # Walk each directory tree

    for directory in directories:
        print(f'Scanning directory tree {directory}')

        for root, _, files in os.walk(directory):
            print(f'Scanning directory {root}')

            for file in files:
                file_queue.put(os.path.join(root, file))

################################################################################

def hasher_thread(method, file_queue, hash_queue, hashes, updated):
    """Thread - reads a file from the queue and, if it is an unhashed or updated image
       calculate the hash and post it and the modification time on the updated queue"""

    while not file_queue.empty():
        filepath = file_queue.get()

        fileext = os.path.splitext(filepath)[1]
        mod_time = os.path.getmtime(filepath)

        # If the file type is an image and the file hasn't been hashed or the modification time has changed
        # then save the hash and the modification time

        if fileext.lower() in IMAGE_EXT_LIST and (filepath not in hashes or mod_time != updated[filepath]):
            # Calculate the hash and store path, dimensions and file size under the hash entry in the hashes table

            print(f'Calculating hash for {filepath}')
            encoding = method.encode_image(image_file=filepath)

            if encoding:
                hash_queue.put({'filepath': filepath, 'encoding': encoding, 'updated': mod_time})
            else:
                print(f'Invalid image {filepath}')

        file_queue.task_done()

################################################################################

def hash_directories(directories, method, hashes, updated):
    """Scan for new files and calculate their hashes"""

    # Create the I/O queues

    file_queue = queue.Queue()
    hash_queue = queue.Queue()

    # Queue the list of files to hash

    queue_files_to_hash(file_queue, directories)

    # Start the threads hashing away

    thread_list = []
    for _ in range(NUM_THREADS):
        thread = threading.Thread(target=hasher_thread, daemon=True, args=(method, file_queue, hash_queue, hashes, updated))
        thread.start()
        thread_list.append(thread)

    # Wait for the threads to stop working

    print('Waiting for threads to terminate')

    for thread in thread_list:
        thread.join()

    # Process the results

    while not hash_queue.empty():
        entry = hash_queue.get()

        filepath = entry['filepath']
        hashes[filepath] = entry['encoding']
        updated[filepath] = entry['updated']

################################################################################

def plot_images(
    orig: str,
    image_list: List,
    scores: bool = False,
    outfile: str = None,
) -> None:
    """
    Plotting function for plot_duplicates() defined below.

    Args:
        orig: filename for which duplicates are to be plotted.
        image_list: List of duplicate filenames, could also be with scores (filename, score).
        scores: Whether only filenames are present in the image_list or scores as well.
        outfile:  Name of the file to save the plot.
    """

    def formatter(val: Union[int, np.float32]):
        """
        For printing floats only upto 3rd precision. Ints are unchanged.
        """
        if isinstance(val, np.float32):
            return f'{val:.3f}'

        return val

    n_ims = len(image_list)
    ncols = 4  # fixed for a consistent layout
    nrows = int(np.ceil(n_ims / ncols)) + 1
    fig = figure.Figure(figsize=(10, 14))

    gs = gridspec.GridSpec(nrows=nrows, ncols=ncols)
    ax = plt.subplot(
        gs[0, 1:3]
    )  # Always plot the original image in the middle of top row
    ax.imshow(Image.open(orig))
    ax.set_title(f'Original Image: {format(orig)}')
    ax.axis('off')

    for i in range(0, n_ims):
        row_num = (i // ncols) + 1
        col_num = i % ncols

        ax = plt.subplot(gs[row_num, col_num])
        if scores:
            ax.imshow(Image.open(image_list[i][0]))
            val = formatter(image_list[i][1])
            title = ' '.join([image_list[i][0], f'({val})'])
        else:
            ax.imshow(Image.open(image_list[i]))
            title = image_list[i]

        ax.set_title(title, fontsize=6)
        ax.axis('off')
    gs.tight_layout(fig)

    if outfile:
        plt.savefig(outfile)

    plt.show()
    plt.close()

################################################################################

def main():
    """Read the hashes and report duplicates in a vaguely civilised way"""

    # Hashing and comparison method

    method = PHash()

    # Handle command line arguments

    parser = argparse.ArgumentParser(description='Search for similar images')
    parser.add_argument('--no-scan', action='store_true', help='Use pickled scan data without updating it')
    parser.add_argument('--no-compare', action='store_true', help='Use pickled comparison data without updating it')
    parser.add_argument('--show', action='store_true', help='Show duplicate images')
    parser.add_argument('directories', nargs='*', action='store', help='Directories to search')

    args = parser.parse_args()

    breakpoint()
    
    if not args.no_scan and not args.directories:
        print('You must be specify at least one directory in order to perform a scan')
        sys.exit(1)

    # We pickle the current set of files, hashes and comparisons

    try:
        print('Loading cached data')

        with open(PICKLE_FILE, 'rb') as pickles:
            data = pickle.load(pickles)

            if data['version'] != PICKLE_VERSION:
                print(f'WARNING: Current version is {PICKLE_VERSION} but saved data is from version {data["version"]}. Interesting things could happen....')

            hashes = data['hashes']
            updated = data['updated']
            duplicates = data.get('duplicates', None)

    except (FileNotFoundError, EOFError):
        if args.no_scan:
            print('ERROR: Cannot use no-scan option as no cached scan data is available')
            sys.exit(1)

        hashes = {}
        updated = {}
        duplicates = {}

    if args.no_compare and not duplicates:
        print('ERROR: Cannot use no-compare option as no cached comparison data is available')
        sys.exit(1)

    if not args.no_scan:
        # Scan for new values and calculate hashes

        hash_directories(method, args.directories, hashes, updated)

    if not args.no_compare:
        # Look for duplicates

        duplicates = method.find_duplicates(encoding_map=hashes)

    # Pickle the updated results

    with open(PICKLE_FILE, 'wb') as pickles:
        dupe_data = {'hashes': hashes, 'updated': updated, 'version': PICKLE_VERSION, 'duplicates': duplicates}
        pickle.dump(dupe_data, pickles)

    # Report them

    for entry in duplicates:
        if duplicates[entry]:
            print(f'{entry}: {duplicates[entry]}')
            if args.show:
                plot_duplicates(entry, duplicates[entry])

################################################################################

def photodupe():
    """Entry point"""

    try:
        main()

    except KeyboardInterrupt:
        sys.exit(1)

    except BrokenPipeError:
        sys.exit(2)

################################################################################

if __name__ == '__main__':
    photodupe()
