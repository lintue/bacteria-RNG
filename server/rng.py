"""RNG from images

* Primarily to be used as part of the web app backend;
* but can also be used to convert single images using command line.

pixel-tree, 2020.
"""

# TO DO:
# function to preprocess images
# function to find hash
# function for RNG algorithm
# route to Flask

import argparse
import os
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
    resize = cv2.resize(image, (hashSize + 1, hashSize))
    # Compute horizontal gradient between pixels
    # (adjacent pixel brighter or darker).
    difference = resize[:, 1:] > resize[:, :-1]
    # Convert processed image to 64bit integer (hash).
    return sum([2 ** i for (i, j) in enumerate(difference.flatten()) if j])


# Extract image hash using dHash.
def image2hash(img_path):
    # Load image from path.
    image = cv2.imread(img_path)
    # Convert image to grayscale.
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Compute hash.
    return dHash(image)


# Convert from dataset.
if __name__ == "__main__":
    # Start counter.
    print("\n" + "Conversion initiated...")
    start = time.time()

    # If image path is given, extract hash for chosen file;
    # else find path to latest image in dataset.
    if args.image:
        latest = os.path.join(dataset_dir, args.image)
    else:
        latest = nu_image()

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
