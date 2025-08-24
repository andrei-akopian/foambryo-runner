
## Installation

For **Unix/Linux and MacOS**, I made an install script.

The script will create a final folder for you, but it needs a parent folder to use as hub. The parent folder can be an existing folder or you can create a new one (avoid using spaces in folder and file names, they mess up terminal commands).

For example my parent folder is called "foambryo-testing".

```
Parent-Folder (your existing folder)
L foambryo-runner (created automatically)
  L foambryo_runner_v001.py
  L Cshaper_4_cells_min-d-3.vtk
  L Cshaper_4_cells_min-d-3.tiff
```

Open terminal and use `cd <folder>` parent folder you would like foambryo runner to be stored at.

> [!TIP]
> If you are on MacOS, in Finder click with 2 fingers on the parent folder to open the menu. Then under "Services" select "New Terminal at Folder" or "New iTerm Window Here"

```bash
curl https://raw.githubusercontent.com/andrei-akopian/foambryo-runner/refs/heads/main/install-macos-unix.sh | sh
cd foambryo-runner
```

**Manual Installation**

(*for advanced users only*)

Downlaod the repository (as zip or git clone) and run `foambryo_runner_v001.py` like a normal python3 script.

```bash
git clone https://github.com/andrei-akopian/foambryo-runner
cd foambryo-runner
pip3 install -r requirements.txt
```

## Usage

> [!TIP]
> If you are on MacOS, in Finder click with 2 fingers on the `foambryo-runner` folder to open the menu. Then under "Services" select "New Terminal at Folder" or "New iTerm Window Here".

`./foambryo_runner_v001.py --help` (prints help message)

`./foambryo_runner_v001.py Cshaper_4_cells_min-d-3.vtk` (run provided example)

> [!TIP]
> Use the TAB key on your keyboard for auto completion of file names.

`./foambryo_runner_v001.py ../foambryo-runner/Cshaper_4_cells_min-d-3.vtk` (`..` means go to the parent folder, you can then access a sibling folder if that is where your files are stored. In this example it accesses itself.)

My script automatically checks the file format, and decides what to do with it. If you give it a (segmentated) .tiff file (produced using [cellpose](https://www.cellpose.org/) for example), it will reconstruct the mesh and save it for later use. For higher resolution mesh use `-d 1` (default is `-d 3`)

`./foambryo_runner_v001.py -d 1 segmentation.tiff` (high resolution mesh, slow, saves as `segmentation_min-d-1.vtk`)

`./foambryo_runner_v001.py -d 3 segmentation.tiff` (low resolution mesh, fast, saves as `segmentation_min-d-3.vtk`)

> [!CAUTION]
> If your file name has a space, it will mess up the terminal command. For example `./foambryo_runner_v001.py segmentation with spaces.tiff` 🚫 won't run. To fix, add a `\` in front of every space when running: `./foambryo_runner_v001.py segmentation\ with\ spaces.tiff` ✅

### Advanced Users

For advanced users. The virtual environment is located at `/.venv-foambryo-runner/`. Activate it with `source .venv-foambryo-runner/bin/activate` and deactivate with `deactivate`. Don't do that to prevent unskilled users from using it my environment elsewhere.

---

Everything below here is a Draft, don't bother reading.

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
