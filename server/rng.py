"""RNG from images

Primarily to be used as part of included web app;
but may also be used as a stand-alone program.

pixel-tree, 2020.
"""

# TO DO:
# function for PRNG algorithm (replace random library)
# route to Flask
# fix imread error

import argparse
import os
import random
import sys
import time

import cv2

# Arguments.
parser = argparse.ArgumentParser(description=None)
parser.add_argument("-i", "--image",
                    type=str,
                    help="Enter image filename.extension (e.g., data.png).")
parser.add_argument("-r", "--range",
                    help="Enter two integers for RNG range (e.g., 1 100).",
                    type=int,
                    nargs=2)
args = parser.parse_args()

# Set RNG range.
if args.range:
    MIN, MAX = args.range[0], args.range[1]
    range_msg = "Range: " + str(MIN) + "-" + str(MAX) + "."
else:
    MIN, MAX = 1, 100
    range_msg = "Default range: " + str(MIN) + "-" + str(MAX) + "."

# Absolute path for dataset.
script_dir = os.path.dirname(__file__)
rel_path = "./images/"
dataset_dir = os.path.join(script_dir, rel_path)


# Find newest image (from data stream, e.g., live video).
def nu_image():
    # List files in dataset directory.
    files = os.listdir(dataset_dir)
    # Array of paths for files.
    paths = [os.path.join(dataset_dir, basename) for basename in files]
    # Return newest file.
    return max(paths, key=os.path.getctime)


# Difference hashing.
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
    # Load image.
    image = cv2.imread(img_path)
    # Convert image to grayscale.
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Compute hash.
    return dHash(grayscale)


# Mersenne Twister (/Python's random library - TO DO replace)
def rng(seed):
    random.seed(seed)
    return random.randint(MIN, MAX)


# When used as a stand-along program.
if __name__ == "__main__":
    # Count number of images in dataset directory (if any).
    count = len([f for f in os.listdir(dataset_dir) if not f.startswith(".")])

    # If image is given in argument, extract hash for specified file;
    # if not explicitly defined and directory has images, extract hash for newest file;
    # else, print error message and exit.
    if args.image:
        latest = os.path.join(dataset_dir, args.image)
    elif count > 0:
        latest = nu_image()
    else:
        print("\n" + "Please provide an image: -i <filename>.<ext>" + "\n"
              "OR add images to dataset directory:", rel_path + "\n")
        sys.exit()

    # Extract hash and compute random integer using hash as seed.
    print("\n" + "Conversion initiated...")
    print(range_msg)
    start = time.time()
    hash = image2hash(latest)
    RNG = rng(hash)

    # Display hash and time elapsed.
    end = time.time()
    elapsed = round(end - start, 1)
    print("COMPLETED. Time elapsed:", elapsed, "s." + "\n")
    print("Hash:", hash, "\n")
    print("RNG:", RNG, "\n")


"""
Folder/live stream of images
=> latest = nu_image()
=> run image2hash(latest)

Single images
=> Display images in browser
=> onclick send ID to backend => {id: path} or something similar?
=> image2hash(path_from_dictionary)
"""
