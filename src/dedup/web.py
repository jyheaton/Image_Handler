from itertools import chain
from flask import Flask, render_template, send_from_directory, send_file
import os
from pathlib import Path
import marimo as mo

if mo.running_in_notebook():
    from src.dedup.detector import main
else:
    from detector import main


web = Flask(__name__)

@web.route("/i/<path:uuid>")
def get_image(uuid, dir="/workspace/data/3x3"):
    p = Path(dir)/Path(uuid)
    return send_file(p)

def new_images(paths):
    images = [ image for image in paths ]
    images = [ f"<img style='width: 175px' src='/i/{image}'>" for image in images ]
    return "\n".join(images)

@web.route('/i/dups')
def show_dups(dir="/workspace/data/3x3"):
    dups = main(dir, store=0, displayDups=True)
    pics = chain.from_iterable([d for d in dups])
    paths = [os.path.relpath(path, dir) for path in pics]
    return new_images(paths)

@web.route('/')
def show_images(dir="/workspace/data/3x3"):
    images = main(dir, displayDups=False)
    pics = chain.from_iterable([d for d in images])
    paths =  [os.path.relpath(path, dir) for path in pics]
    
    return new_images(paths)
    # print(pics)

    # print(paths)
    # pics = [p for p in pics]
    # exit(0)
    # print(dir)
    # print(paths[0])
    # return send_file(pics)
    # return send_from_directory(dir, paths)
    # print(paths)
    # return render_template('test.html', links=paths, dir=dir) #paths)
    #print(pics)



if __name__ == '__main__':  
#    show_images()
   web.run(debug=True) 