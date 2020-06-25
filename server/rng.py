"""RNG from images

Primarily to be used as part of the web app backend;
but may also be used as a stand-along program.

pixel-tree, 2020.
"""

# TO DO:
# function for RNG algorithm (use hash to seed)
# route to Flask
# fix imread error

import argparse
import os
import sys
import time

import cv2

# Arguments (used for command line implementation).
parser = argparse.ArgumentParser(description=None)
parser.add_argument("-i", "--image",
                    help="Enter image filename.extension (e.g., data.png).")
args = parser.parse_args()

# Absolute path for dataset.
script_dir = os.path.dirname(__file__)
rel_path = "./images/"
dataset_dir = os.path.join(script_dir, rel_path)


# Find newest image (used in converting from data stream, e.g., live video).
def nu_image():
    # List files in dataset directory.
    files = os.listdir(dataset_dir)
    # Array of paths for files.
    paths = [os.path.join(dataset_dir, basename) for basename in files]
    # Return newest file.
    return max(paths, key=os.path.getctime)


# Difference hashing function.
def dHash(image, hashSize=8):
    # Add extra column to image.
    resized = cv2.resize(image, (hashSize + 1, hashSize))
    # Compute horizontal gradient between pixels
    # (adjacent pixel brighter or darker).
    difference = resized[:, 1:] > resized[:, :-1]
    # Convert processed image to 64-bit integer (hash).
    return sum([2 ** i for (i, j) in enumerate(difference.flatten()) if j])


# Extract image hash using dHash.
def image2hash(img_path):
    # Load image from path.
    image = cv2.imread(img_path)
    # Convert image to grayscale.
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Compute hash.
    return dHash(grayscale)


# If used as stand-alone program.
if __name__ == "__main__":
    # Count number of images in dataset directory (if any).
    count = len([f for f in os.listdir(dataset_dir) if not f.startswith(".")])

    # If image is given in argument, extract hash for provided file;
    # else if ./images directory has images, extract hash for newest file;
    # else, print error message and exit.
    if args.image:
        latest = os.path.join(dataset_dir, args.image)
    elif count > 0:
        latest = nu_image()
    else:
        print("\n" + "Please provide image in argument: -i <name>.<ext>" + "\n"
              "OR add images to dataset directory (default ./images/)." + "\n")
        sys.exit()

    # Start counter.
    print("\n" + "Conversion initiated...")
    start = time.time()

    # Extract hash.
    hash = image2hash(latest)

    # Display hash and time elapsed.
    end = time.time()
    elapsed = round(end - start, 1)
    print("\n" + "COMPLETED.")
    print("Hash:", hash)
    print("Time Elapsed:", elapsed, "s" + "\n")

"""
Folder/live stream of images
=> latest = nu_image()
=> run image2hash(latest)

Single images
=> Display images in browser
=> onclick (JS) send ID to Python backend => {id: path} or something similar?
=> image2hash(path_from_dictionary)
"""
