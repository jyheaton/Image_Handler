# The start of my duplicate image detector
# applies an image hashing function to look for similar images
# stores in database?
from PIL import Image
import imagehash
from typing import Union
import os




# get hash function
# takes in PIL image, returns hash (str)
def getHash(image: Image) -> str:
    if image is None:
        return '' # return empty string, keeps the hash placement in list
    # returns hash - must convert to string or it's read as bool
    return str(imagehash.average_hash(image))


# store hash in a database
def storeHash(hash: str) -> bool:
    # stores hash, image path in library. returns True if there is a collision
    # collisions mean we return True
    pass

# check if file exists
def checkExists(path: str) -> bool:
    # checks if file exists and returns True if so
    pass


# goes through all files in the database and confirms their paths exist/are correct
# does not add to database, only deletes
def reorgFiles(database) -> None:
    pass


def openFile(path: str) -> Image.Image | None:
    if path.endswith(endings):
        return Image.open(path)
    else:
        print(f"Path: {path} does not end with any of: {endings}, skipping")
        return None

# goes through all images in the path (recursively) and adds to database
def orgFiles(dir: str, database) -> None:
    # check path exists - if not, print error message saying to make sure to mount the volume

    if not os.path.isdir(dir):
        print(f"Error, path: {dir} not found")
        exit(0)

    # collect all files
    # combine path with files to generate full address of each image
    paths = []
    for path, folders, files in os.walk(dir):
        paths += [os.path.join(path, i) for i in files]
        
    # check if hash collision occurs
    hashes = []
    for i in paths:
        hashes.append(getHash(openFile(i)))
    print(hashes)
    print(len(paths))
    print(len(hashes))
    # confirm that path is not the same (if it is assume crash happened in previous run after this point or smth and skip)
    # add to database
    # if collision, record paths under dictionary with hashes -> dict = {['hash']=['img1.jpg', 'img2.png']}
    

if __name__ == "__main__":
    # make r so \ doesn't escape
    
    endings = ('.jpg', '.png')
    dir = r"/workspaces/Pictures/3x3"
    orgFiles(dir, None)