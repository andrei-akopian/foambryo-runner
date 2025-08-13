
Common issues: Recurring nuisances are going to be the following:
- `python` vs `python3` and `pip` vs `pip3` (if one of these doesn't work, change the command to the other.)
- These tools were initially developed as libraries or commandline only (to be quickly used as part of larger workflows) so activating GUIs requires more steps.
- 2D vs 3D. Everything runs faster in 2D and file sizes are much less. 2D is usually the default. For 3D, the Z-layer has to be specifically manually activated.
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
