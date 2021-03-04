import os
def get_path(to):
    pathforscripttwo = os.path.realpath(__file__)
    pathforscripttwo = pathforscripttwo.replace('lib/tools/getPath.py', to)
    return pathforscripttwo
