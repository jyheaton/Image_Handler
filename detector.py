# The start of my duplicate image detector
# applies an image hashing function to look for similar images
# stores in database?
from PIL import Image
import imagehash
from typing import Union, Iterable, Generator
import os
import psycopg as pg
from typing import NamedTuple




class ImageRecord(NamedTuple):
    path: str
    hash: str

# look into duckdb, sqlalchemy, etc instead of psycopg
# just for connecting to database
# look into using with marimo - get the table to interact with

def startDb(name:str = "postgres", user:str = "postgres", host:str = "postgres", password: str = "S3cret"):
    with pg.connect(dbname=name, user=user, host=host, password=password) as conn:
        with conn.cursor() as cur:
            # make table with hash for id, address (string), and tags (multi string?)
            cur.execute("CREATE TABLE IF NOT EXISTS pics(id serial, num integer, data text)")

# get hash function
# takes in PIL image, returns hash (str)
# TODO: apply data augmentation (pytorch) to compare hashes
def getHash(image: Image.Image | None) -> str:
    if image is None:
        return '' # return empty string, keeps the hash placement in list
    # returns hash - must convert to string or it's read as bool
    return str(imagehash.average_hash(image))


# store hash in a database
def storeHash(pic: ImageRecord) -> bool:
    # stores hash, image path in library. returns True if there is a collision
    # collisions mean we return True
    pass

# check if file exists
def checkExists(path: str) -> bool:
    # checks if file exists in db already and returns True if so
    pass


# goes through all files in the database and confirms their paths exist/are correct
# does not add to database, only deletes from database
def reorgFiles(database) -> None:
    pass


def openFile(path: str) -> Image.Image | None:
    if path.endswith(endings):
        return Image.open(path)
    else:
        print(f"Path: {path} does not end with any of: {endings}, skipping")
        return None
    



def write_to_database(item: ImageRecord) -> None:
    pass

def iter_image_paths(root_dir: str | os.PathLike, *, exts: set[str] | None = None) -> Iterable[str | os.PathLike]:
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if not exts or filename.endswith(exts):
                yield os.path.join(dirpath, filename)

# TODO: look into iter tools and iter tools.slice
def iter_images(paths: Iterable[str | os.PathLike]) -> Iterable[str]:
    for path in paths:
        yield getHash(openFile(path))


def iter_records(paths: Iterable[str], hashes: Iterable[str]) -> Iterable[ImageRecord]:
    for path, hash in zip(paths, hashes):
        yield ImageRecord(path, hash)


def main(root_dir: str | os.PathLike):
    paths = iter_image_paths(root_dir, exts=(".jpg", ".png"))
    hashes =  iter_images(paths)
    records = iter_records(paths, hashes)

    for c, record in enumerate(records, start=1):
        print(f"Image #{c}: {record}")
        storeHash(record)


# goes through all images in the path (recursively) and adds to database
def orgFiles(dir: str, database) -> None:
    # check path exists - if not, print error message saying to make sure to mount the volume

    if not os.path.isdir(dir):
        print(f"Error, path: {dir} not found")
        exit(0)

    # collect all files
    # combine path with files to generate full address of each image
    # each processing stage consuming iterable and being a generator itself
    paths = []
    for path, folders, files in os.walk(dir):
        paths.extend(os.path.join(path, file_name) for file_name in files)
        image_path = ''
        getHash(openFile(image_path))

    # check if hash collision occurs
    # hashes = []
    # for i in paths:
    #     hashes.append(getHash(openFile(i)))
    # print(hashes)
    # print(len(paths))
    # print(len(hashes))
    # confirm that path is not the same (if it is assume crash happened in previous run after this point or smth and skip)
    # add to database
    # if collision, record paths under dictionary with hashes -> dict = {['hash']=['img1.jpg', 'img2.png']}
    

if __name__ == "__main__":
    # make r so \ doesn't escape
    
    endings = ('.jpg', '.png')
    dir = r"/workspace/data/3x3"
    main(dir)
    #orgFiles(dir, None)