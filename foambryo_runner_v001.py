#!/.venv-foambryo-runner/bin/python3
"""
Foambryo runner that calculates meshes, tensions, pressures, etc. and automatically saves them to files.
The script contains heavy I/O and UX functionality, which overrides the foambryo library on several occasions. Further modifications might be difficult.

Created by Andrei Akopian for Mariia Akhmanova at Sloan Kettering Institute

Development Notes:
    - Many imports are inline to prevent long loading times for unnecessary modules
    - types are messy, so syntax highlighters might show red squigly lines while the code will still work

List of libraries used:
    - foambryo and its dependencies
    - argparse for user interface
    - pathlib for managing the file structure during I/O
    - icecream for debugging
"""

__version__ = "1.0.0"

import argparse
import pathlib
from foambryo.pressure_inference import infer_pressures
from foambryo.tension_inference import infer_tensions
from foambryo.viewing import plot_force_inference, plot_tension_inference, ps
from foambryo.dcel import DcelData
from foambryo.io import get_default_mesh_reconstruction_algorithm, dcel_mesh_from_file

parser = argparse.ArgumentParser(
                    prog='Foambryo runner',
                    description='Takes segmentation as input and creates a foambryo visualization.',
                    epilog='Example: ./foambryo_runner_v001.py Cshaper_4_cells_min-d-3.vtk\nDocumentation: https://github.com/andrei-akopian/foambryo-runner')
# parser.add_argument('-f', '--force', action='store_true')
parser.add_argument('-d','--min-distance',help="min distances between mesh nodes. default 3. integers only. Decrease for higher res, increase for speed.",default=3,type=int)
parser.add_argument('filename')
parser.add_argument('-t','--save-tensions',help="Saves the tensions to a file.",action='store_true')
parser.add_argument('-p','--save-pressures',help="Saves the pressures to a file.",action='store_true')

args = parser.parse_args()
filename = args.filename
min_distance = args.min_distance
save_mesh_to_vtk = False

purepath = pathlib.PurePath(filename)
suffix = purepath.suffix
mesh: DcelData
points, triangles, labels = None,None,None

# Set Polyscope window title to filename (usefull if multiple files are open)
ps.set_program_name(filename) # https://polyscope.run/py/basics/program_options/

if suffix == '.tif':
    # Manually run dcel_mesh_from_segmentation_mask internal code to grab internal variables
    # https://github.com/VirtualEmbryo/foambryo/blob/144b387dc76e517be316448a379057e2820aa9f7/src/foambryo/io.py#L41
    print("Reading Image...")
    import skimage.io as io
    segmentation_mask = io.imread(filename)
    print("...Image read")
    mesh_reconstruction_algorithm = get_default_mesh_reconstruction_algorithm(min_distance,print_info=True)
    print("Starting to reconstruct mesh from segementation mask (this might take a few minutes)...")
    points, triangles, labels = mesh_reconstruction_algorithm.construct_mesh_from_segmentation_mask(segmentation_mask)
    print("...Finished to reconstruct mesh from segementation mask")
    # labels variable is necessary for saving meshes but impossible to access without hijacking
    mesh = DcelData(points, triangles, labels)
    save_mesh_to_vtk = True
elif suffix == '.vtk':
    mesh = dcel_mesh_from_file(filename)
elif suffix == '.rec' or suffix == '.arec':
    mesh = dcel_mesh_from_file(filename)
# elif suffix =='.pkl': # hard to implement
#     # https://github.com/VirtualEmbryo/foambryo/blob/144b387dc76e517be316448a379057e2820aa9f7/src/foambryo/dcel.py#L524
#     import pickle
#     with open(filename,'rb') as f:
#         vertices = pickle.load(f)
#         half_edges = pickle.load(f)
#         faces = pickle.load(f)

if save_mesh_to_vtk:
    from dw3d import save_vtk, save_rec
    vtk_save_path = f"{purepath.stem}_min-d-{min_distance}.vtk"
    print("Saving mesh to", vtk_save_path)
    save_vtk(vtk_save_path,points, triangles, labels)


dict_tensions: dict
if args.save_tensions:
    print("Printing Tension Information")
    dict_tensions = print(infer_tensions(mesh,mean_tension=1,mode='YD'))
    #TODO add save to file
if args.save_pressures:
    print("Printing Pressures Information")
    if not(args.save_tensions):
        dict_tensions = infer_tensions(mesh,mean_tension=1,mode='YD')
    pressures = print(infer_pressures(mesh,dict_tensions))
    #TODO add save to file

# Infer and view the forces
plot_force_inference(mesh, scalar_quantities = True)

# #Or just the tensions
# plot_tension_inference(mesh)
