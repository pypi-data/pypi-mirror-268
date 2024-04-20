import os
import numpy as np
from math import floor
import math
import mrcfile


class MapProcessor:
    """
        MapProcessor class contains methods deal with map processing method and model associated map processing methods
        Instance can be initialized with either full map file path or a mrcfile map object
    """

    def __init__(self, input_map=None):
        if isinstance(input_map, str):
            if os.path.isfile(input_map):
                self.map = mrcfile.open(input_map)
            else:
                self.map = None
        elif isinstance(input_map, mrcfile.mrcfile.MrcFile):
            self.map = input_map
        else:
            self.map = None

    def getindices(self, onecoor):
        """
            Find one atom's indices corresponding to its cubic or plane
            the 8 (cubic) or 4 (plane) indices are saved in indices variable

        :param onecoor: List contains the atom coordinates in (x, y, z) order
        :return: Tuple contains two list of index: first has the 8 or 4 indices in the cubic;
                 second has the float index of the input atom
        """
        # For non-cubic or skewed density maps, they might have different apix on different axes
        zdim = self.map.header.cella.z
        znintervals = self.map.header.mz
        z_apix = zdim / znintervals

        ydim = self.map.header.cella.y
        ynintervals = self.map.header.my
        y_apix = ydim / ynintervals

        xdim = self.map.header.cella.x
        xnintervals = self.map.header.mx
        x_apix = xdim / xnintervals

        map_zsize = self.map.header.nz
        map_ysize = self.map.header.ny
        map_xsize = self.map.header.nx

        if self.map.header.cellb.alpha == self.map.header.cellb.beta == self.map.header.cellb.gamma == 90.:
            zindex = float(onecoor[2] - self.map.header.origin.z) / z_apix - self.map.header.nzstart
            yindex = float(onecoor[1] - self.map.header.origin.y) / y_apix - self.map.header.nystart
            xindex = float(onecoor[0] - self.map.header.origin.x) / x_apix - self.map.header.nxstart

        else:
            # fractional coordinate matrix
            xindex, yindex, zindex = self.matrix_indices(onecoor)

        zfloor = int(floor(zindex))
        if zfloor >= map_zsize - 1:
            zceil = zfloor
        else:
            zceil = zfloor + 1

        yfloor = int(floor(yindex))
        if yfloor >= map_ysize - 1:
            yceil = yfloor
        else:
            yceil = yfloor + 1

        xfloor = int(floor(xindex))
        if xfloor >= map_xsize - 1:
            xceil = xfloor
        else:
            xceil = xfloor + 1

        indices = np.array(np.meshgrid(np.arange(xfloor, xceil + 1), np.arange(yfloor, yceil + 1),
                                       np.arange(zfloor, zceil + 1))).T.reshape(-1, 3)
        oneindex = [xindex, yindex, zindex]

        return (indices, oneindex)

    def matrix_indices(self, onecoor):
        """
            using the fractional coordinate matrix to calculate the indices when the maps are non-orthogonal

        :param onecoor: list contains the atom coordinates in (x, y, z) order
        :return: tuple of indices in x, y, z order
        """

        # Figure out the order of the x, y, z based on crs info in the header
        apixs = self.map.voxel_size.tolist()
        angs = [self.map.header.cellb.alpha, self.map.header.cellb.beta, self.map.header.cellb.gamma]
        matrix = self.map_matrix(apixs, angs)
        result = matrix.dot(np.asarray(onecoor))
        xindex = result[0] - self.map.header.nxstart
        yindex = result[1] - self.map.header.nystart
        zindex = result[2] - self.map.header.nzstart

        return xindex, yindex, zindex

    @staticmethod
    def map_matrix(apixs, angs):
        """
            calculate the matrix to transform Cartesian coordinates to fractional coordinates
            (check the definition to see the matrix formular)

        :param apixs: array of apix/voxel size
        :param angs: array of angles in alpha, beta, gamma order
        :return: a numpy array to be used for calculated fractional coordinates
        """

        ang = (angs[0] * math.pi / 180, angs[1] * math.pi / 180, angs[2] * math.pi / 180)
        insidesqrt = 1 + 2 * math.cos(ang[0]) * math.cos(ang[1]) * math.cos(ang[2]) - \
                     math.cos(ang[0]) ** 2 - \
                     math.cos(ang[1]) ** 2 - \
                     math.cos(ang[2]) ** 2

        cellvolume = apixs[0] * apixs[1] * apixs[2] * math.sqrt(insidesqrt)

        m11 = 1 / apixs[0]
        m12 = -math.cos(ang[2]) / (apixs[0] * math.sin(ang[2]))

        m13 = apixs[1] * apixs[2] * (math.cos(ang[0]) * math.cos(ang[2]) - math.cos(ang[1])) / (
                    cellvolume * math.sin(ang[2]))
        m21 = 0
        m22 = 1 / (apixs[1] * math.sin(ang[2]))
        m23 = apixs[0] * apixs[2] * (math.cos(ang[1]) * math.cos(ang[2]) - math.cos(ang[0])) / (
                    cellvolume * math.sin(ang[2]))
        m31 = 0
        m32 = 0
        m33 = apixs[0] * apixs[1] * math.sin(ang[2]) / cellvolume
        prematrix = [[m11, m12, m13], [m21, m22, m23], [m31, m32, m33]]
        matrix = np.asarray(prematrix)

        return matrix

    def get_close_voxels_indices(self, onecoor, n):
        """
            Given onecoor, return the nearby voxels indices; radius defined by n

        :param onecoor: list contains the atom coordinates in (x, y, z) order
        :param n: a number integer of float which define radius voxel check range radius = (n*average_voxel_size)
        :return: a list of tuples of indices in (z, y, x) format to adapt to mrcfile data format
        """

        xind, yind, zind = self.getindices(onecoor)[1]
        voxel_sizes = self.map.voxel_size.tolist()
        atom_xind = int(xind)
        atom_yind = int(yind)
        atom_zind = int(zind)

        average_voxel_size = sum(voxel_sizes) / 3.
        radius = n * average_voxel_size
        rx = int(round(radius / voxel_sizes[0]))
        ry = int(round(radius / voxel_sizes[1]))
        rz = int(round(radius / voxel_sizes[2]))

        indices = []
        for x in range(atom_xind - rx, atom_xind + rx):
            for y in range(atom_yind - ry, atom_yind + ry):
                for z in range(atom_zind - rz, atom_zind + rz):
                    d = average_voxel_size * math.sqrt(
                        (x - atom_xind) ** 2 + (y - atom_yind) ** 2 + (z - atom_zind) ** 2)
                    if d <= radius:
                        indices.append([x, y, z])
        result = [tuple(x[::-1]) for x in indices]

        return result

    def generate_mask(self, coords, radius):
        """
            Based on the coordinates, generate a mask based on the radius
            The mask based on the map initialized in the MapProcessor class

        :param coords: a list of tuples in (x, y, z) format
        :param radius: an integer or float define the radius of mask range around the coordinate
        """

        dir_name = os.path.dirname(self.map._iostream.name)
        map_name = os.path.basename(self.map._iostream.name)
        mask = np.zeros_like(self.map.data)
        for coord in coords:
            near_indices = self.get_close_voxels_indices(coord, radius)
            for ind in near_indices:
                mask[ind] = 1
        out_map = mrcfile.new(f'{dir_name}/{map_name}_residue_mask.mrc', overwrite=True)
        out_map.set_data(mask)
        out_map.voxel_size = self.map.voxel_size
        out_map.close()

    def residue_average_resolution(self, indices, mapdata=None):
        """
            given mapdata and indices, calculate the average value of these density values

        :param mapdata: numpy array of map data
        :param indices: list of tuples of (x, y, z) coordinates
        return: average value of these density values
        """

        sum_local_resolution = 0.
        if mapdata is None:
            mapdata = self.map.data
        for ind in indices:
            sum_local_resolution += mapdata[ind]

        return sum_local_resolution / len(indices)

