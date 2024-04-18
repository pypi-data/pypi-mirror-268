# pyLevelSet

![Github License](https://img.shields.io/github/license/Yihao-Shi/pyLevelSet)          ![Github stars](https://img.shields.io/github/stars/Yihao-Shi/pyLevelSet)          ![Github forks](https://img.shields.io/github/forks/Yihao-Shi/pyLevelSet)         [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) 

## Brief description
Generate 3D level set particles, including surface mesh and signed distance field (SDF) with __pure Python__ API. 
Developed by [Multiscale Geomechanics Lab](https://person.zju.edu.cn/en/nguo), Zhejiang University.

## Overview
The library have a series of user-friendly features:
1. Given a set of point cloud, the library can reconstruct the surface mesh and generate the signed distance field. 
2. Given a triangle mesh (e.g., STL, PLY, OBJ, GLB, GLTF ...), the library can generate the signed distance field.
3. Given a surface function (e.g., poly-super-quadric, poly-super-ellipsoid or a user-defined function), the library can generate surface node, constrcut surface mesh and generate signed distance field.
4. The library is capable of generating level-set particles from several SDF primitives, including the use of boolean operations to create more intricate particle shapes.

## Example

Here is an example of a level-set particles contructed from SDF primitives. Special credits to [sdf](https://github.com/fogleman/sdf).

<img width=268 align="right" src="images/sdf.png">

```
import pyLevelSet as pls
sf = pls.sphere(1) & pls.box(1.5)
cy = pls.cylinder(0.5)
sf -= cy.orient([1, 0, 0]) | cy.orient([0, 1, 0]) | cz.orient([0, 0, 1])
sf.grids(space=0.1).reset(False).visualize(samples=10002)
```

## Quick start
### Dependencies
Note that the dependencies will be automatically installed by setup.py when following the directions below.

|Package name|Version|Features|
|:----------:|:-----:|:------:|
|[numpy](https://pypi.org/project/numpy/)|lastest version|Pre-processing|
|[scipy](https://pypi.org/project/SciPy/)|lastest version|Find roots|
|[scikit-image](https://scikit-image.org/)|lastest version|Marching cube method|
|[open3d](https://pypi.org/project/pybind11/)|lastest version|Reconstruct surface mesh|
|[trimesh](https://pypi.org/project/trimesh/)|lastest version|Import stl/obj files|
|[rtree](https://pypi.org/project/Rtree/)|lastest version|Neighbor search|
|[pyevtk](https://pypi.org/project/pyevtk/)|lastest version|Postprocessing on Paraview|
|[matplotlib](https://matplotlib.org/)|lastest version|Visualization|

### Installation
#### Install from pip (recommended)
```
pip install pyLevelSet
```

#### Install from source code
```
git clone https://github.com/Yihao-Shi/pyLevelSet.git
cd pyLevelSet-main
pip install .
```

### Check Installation
```
python -c "import pyLevelSet as pls; print('pyLevelSet version is:', pls.__version__)"
```

### Visualization
Several built-in functions support visualize the final result through 3D mesh viewer, such as gmsh, MeshLab or Paraview. The related function are listed as follows:
1. pyLevelSet.save()
2. pyLevelSet.visualize()
3. pyLevelSet.show()
4. pyLevelSet.show_slice()
5. pyLevelSet.dump_files()


## API
### Primitives
#### PointCloud

#### Polyhedron
<img width=200 align="right" src="images/mesh.png">

```
f = pl.polyhedron(file='../assets/sand.stl')
f = f.grids(space=5)
f.save('sand.stl')
f.visualize()
```

#### SurfaceFunction

#### PolySuperQuadrics
<img width=200 align="right" src="images/superquadric.png">

```
f = pl.polysuperquadrics(xrad1=0.35, yrad1=0.75, zrad1=0.65, xrad2=0.25, yrad2=0.65, zrad2=0.5, epsilon_x=1.8, epsilon_y=1.2, epsilon_z=0.7)
f = f.grids(space=0.05)
f.save('ellipsoid.stl', samples=10002, sparse=False)
f.visualize()
```

#### PolySuperEllipsoid
<img width=200 align="right" src="images/superellipsoid.png">

```
f = pl.polysuperellipsoid(xrad1=0.5, yrad1=0.25, zrad1=0.75, xrad2=0.25, yrad2=0.75, zrad2=0.5, epsilon_e=1.5, epsilon_n=1.5)
f = f.grids(space=0.05)
f.save('ellipsoid.stl', samples=2502, sparse=False)
f.visualize()
```

#### Sphere

### Variables

## License
This project is licensed under the GNU General Public License v3 - see the [LICENSE](https://www.gnu.org/licenses/) for details.

## Acknowledgements
The project is inspired by [sdf](https://github.com/fogleman/sdf). Besides, we deliver special thanks to the excellent documentation on signed distance functions: [3D](https://iquilezles.org/articles/distfunctions/) and [2D]().

### Contributors
<a href="https://github.com/Yihao-Shi/pyLevelSet/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Yihao-Shi/pyLevelSet" />
</a>

### Contact us
- If you spot any issue or need any help, please mail directly to <a href = "mailto:syh-1999@outlook.com">syh-1999@outlook.com</a>.

## Release Notes
V0.1 (April 15, 2024)

- First release pyLevelSet
