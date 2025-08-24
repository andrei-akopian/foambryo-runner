
## Installation

Downlaod the repo and run it as a normal python3 script.

**General**
```bash
git clone https://github.com/andrei-akopian/foambryo-runner
cd foambryo-runner
pip3 install -r requirements.txt
```

For **Unix/Linux and MacOS**, I made an install script. (Warning, it uses virtual environment)
```bash
curl https://raw.githubusercontent.com/andrei-akopian/foambryo-runner/refs/heads/main/install-macos-unix.sh | sh
```

## Usage
The foambryo_runner_v001.py works by itself, so you can just copy it to other files or wherever.

`./foambryo_runner_v001.py --help`

`./foambryo_runner_v001.py Cshaper_4_cells_min-d-3.vtk`

My script automatically checks the file format, and decides what to do with it. If you give it a (segmentated) .tiff file (produced using [cellpose](https://www.cellpose.org/) for example), it will reconstruct the mesh and save it for later use. For higher resolution mesh use `-d 1` (default is `-d 3`)

`./foambryo_runner_v001.py -d 1 segmentation.tiff` (high resolution mesh, slow, saves as `segmentation_min-d-1.vtk`)

`./foambryo_runner_v001.py -d 3 segmentation.tiff` (low resolution mesh, fast, saves as `segmentation_min-d-3.vtk`)

> [!TIP]
> The virtual environment is located at `/.venv-foambryo-runner/`. Activate it with `source .venv-foambryo-runner/bin/activate` and deactivate with `deactivate`. Don't do that to prevent unskilled users from using it my environment elsewhere.

## Misc

Common issues: Recurring nuisances are going to be the following:
- `python` vs `python3` and `pip` vs `pip3` (if one of these doesn't work, change the command to the other.)
- These tools were initially developed as libraries or commandline only (to be quickly used as part of larger workflows) so activating GUIs requires more steps.
- Platform and package versions. These are unavoidable and annoying. For example, some code works only on GPUs, but Macbooks have an integrated-GPU, which makes all GPU related settings ambiguous.

## Cellpose

https://www.cellpose.org/

Docs https://cellpose.readthedocs.io/en/latest/

Installing `pip install 'cellpose[gui]'`

The default cellpose will run in 2d. To start it in 3d mode: `python3 -m cellpose --Zstack`

On M1,M2,M3 Macs for 3D cellpose run `python -m cellpose --dir path --gpu_device mps --use_gpu --Zstack `

## FoamBryo

PyPi Package: https://pypi.org/project/foambryo/
`pip install foambryo`

https://github.com/VirtualEmbryo/foambryo2D (but we need 3d)

Github and Docs: https://github.com/sacha-ichbiah/foambryo

### How to Use

After opening the file. To see the tensions arrows, under "Strctures > Surface Mesh > Embryo " unclick the "Enabled" or decrease transparency under "Options > Transparency".

Similarly, disabling "Graph Nodes" removes the nuclei. "Stress tensor principal direction" removes the arrows. "Graph Edges" removes the endges showing contacts between cells.

Increasing Mesh resolution: `mesh = dcel_mesh_from_segmentation_mask(segmentation,min_distance=3)` the min_distance forces the minimal distances to be a smaller amount, thus leading to higher resolution. Default min_distance=3. **Mesh reconstruction is the longest step.**

### Notes on dependencies

Cellpose for making the segmentation masks.

Delaunay Watershed is the library for building meshes from segmentation masks. https://github.com/VirtualEmbryo/delaunay-watershed it is developed by the same people.

Polyscope for 3d mesh viewing https://github.com/nmwsharp/polyscope



# TODO

- [X] Add filenames to windows
- [X] Figure out scale
- [X] Figure out mesh exports
- [ ] Figure out tension, pressure, etc. exports
- [ ] Make useable tool for opening multiple files
- [ ] Make Fiji Easy to open
