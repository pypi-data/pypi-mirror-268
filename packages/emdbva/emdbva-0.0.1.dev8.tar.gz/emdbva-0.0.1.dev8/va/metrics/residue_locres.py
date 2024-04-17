from scipy.interpolate import RegularGridInterpolator
from collections import OrderedDict
import numpy as np
from math import floor
import math
from va.utils.misc import floatohex, scale_values



def getindices(map, onecoor):
    """
        Find one atom's indices correspoding to its cubic or plane
        the 8 (cubic) or 4 (plane) indices are saved in indices variable

    :param map: Density map instance from TEMPy.MapParser
    :param onecoor: List contains the atom coordinates in (x, y, z) order
    :return: Tuple contains two list of index: first has the 8 or 4 indices in the cubic;
             second has the float index of the input atom

    """

    # For non-cubic or skewed density maps, they might have different apix on different axises
    # map = self.map
    zdim = map.header.cella.z
    znintervals = map.header.mz
    z_apix = zdim / znintervals

    ydim = map.header.cella.y
    ynintervals = map.header.my
    y_apix = ydim / ynintervals

    xdim = map.header.cella.x
    xnintervals = map.header.mx
    x_apix = xdim / xnintervals

    map_zsize = map.header.nz
    map_ysize = map.header.ny
    map_xsize = map.header.nx

    if not map.header.cellb.alpha == map.header.cellb.beta == map.header.cellb.gamma == 90.:
        zindex = float(onecoor[2] - map.header.origin.z) / z_apix - map.header.nzstart
        yindex = float(onecoor[1] - map.header.origin.y) / y_apix - map.header.nystart
        xindex = float(onecoor[0] - map.header.origin.x) / x_apix - map.header.nxstart

    else:
        apixs = [x_apix, y_apix, z_apix]
        xindex, yindex, zindex = matrix_indices(map, apixs, onecoor)

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

def matrix_indices(map, apixs, onecoor):
    """
        using the fractional coordinate matrix to calculate the indices when the maps are non-orthogonal

    :param onecoor: list contains the atom coordinates in (x, y, z) order
    :return: tuple of indices in x, y, z order
    """

    crs = [map.header.mapc, map.header.mapr, map.header.maps]
    angs = [map.header.cellb.alpha, map.header.cellb.beta, map.header.cellb.gamma]
    matrix = map_matrix(apixs, angs)
    result = matrix.dot(np.asarray(onecoor))
    xindex = result[0] - map.header.nxstart
    yindex = result[1] - map.header.nystart
    zindex = result[2] - map.header.nzstart

    return xindex, yindex, zindex

def map_matrix(apixs, angs):
    """

        calculate the matrix to transform Cartesian coordinates to fractional coordinates
        (check the definition to see the matrix formular)

    :param apixs: array of apix/voxel size
    :param angs: array of angles in alpha, beta, gamma order
    :return: a numpy array to be used for calculated fractional coordinates
    """

    ang = (angs[0]*math.pi/180, angs[1]*math.pi/180, angs[2]*math.pi/180)
    insidesqrt = 1 + 2 * math.cos(ang[0]) * math.cos(ang[1]) * math.cos(ang[2]) - \
                 math.cos(ang[0])**2 - \
                 math.cos(ang[1])**2 - \
                 math.cos(ang[2])**2

    cellvolume = apixs[0]*apixs[1]*apixs[2]*math.sqrt(insidesqrt)

    m11 = 1/apixs[0]
    m12 = -math.cos(ang[2])/(apixs[0]*math.sin(ang[2]))

    m13 = apixs[1] * apixs[2] * (math.cos(ang[0]) * math.cos(ang[2]) - math.cos(ang[1])) / (cellvolume * math.sin(ang[2]))
    m21 = 0
    m22 = 1 / (apixs[1] * math.sin(ang[2]))
    m23 = apixs[0] * apixs[2] * (math.cos(ang[1]) * math.cos(ang[2]) - math.cos(ang[0])) / (cellvolume * math.sin(ang[2]))
    m31 = 0
    m32 = 0
    m33 = apixs[0] * apixs[1] * math.sin(ang[2]) / cellvolume
    prematrix = [[m11, m12, m13], [m21, m22, m23], [m31, m32, m33]]
    matrix = np.asarray(prematrix)

    return matrix

def get_close_voxels_indices(map, atom_indices, n):
    """

    """

    xind, yind, zind = atom_indices
    atom_xind = int(xind)
    atom_yind = int(yind)
    atom_zind = int(zind)
    voxelsizes = map.voxel_size.tolist()

    average_voxel_size = sum(voxelsizes) / 3.
    radius = n * average_voxel_size
    rx = int(round(radius / voxelsizes[0]))
    ry = int(round(radius / voxelsizes[1]))
    rz = int(round(radius / voxelsizes[2]))

    indices = []
    for x in range(atom_xind - rx, atom_xind + rx):
        for y in range(atom_yind - ry, atom_yind + ry):
            for z in range(atom_zind - rz, atom_zind + rz):
                d = average_voxel_size * math.sqrt((x - atom_xind) ** 2 + (y - atom_yind) ** 2 + (z - atom_zind)**2)
                if d <= radius:
                    if atom_xind > map.header.nx - 1 or atom_xind < 0 or \
                            atom_yind > map.header.ny - 1 or atom_yind < 0 or \
                            atom_zind > map.header.nz - 1 or atom_zind < 0:
                        continue
                    indices.append((z, y, x))
    return indices


def residue_average_resolution(mapdata, indices):
    """
        given mapdata and indices, calculate the average value of these density values
    :param mapdata: numpy array of map data
    :param indices: list of tuples of (x, y, z) coordinates
    return: average value of these density values
    """
    sum_local_resolution = 0.
    for ind in indices:
        sum_local_resolution += mapdata[ind]

    return sum_local_resolution / len(indices)


def local_resolution_json(map, inmodels, radius):
    """

        Interpolate density value of one atom, if indices are on the same plane use nearest method
        otherwise use linear

    :param map: TEMPy map instance
    :param model: Structure instance from TEMPy package mmcif parser
    :return: List contains all density interpolations of atoms from model

    """

    models = []
    if isinstance(inmodels, list):
        models = inmodels
    else:
        models.append(inmodels)
    result = {}
    modelcount = 0
    for model in models:
        modelcount += 1
        modelname = model.filename.split('/')[-1]
        atomcount = 0
        chainaiscore = {}
        data_result = {}
        allkeys = []
        allvalues = []
        colors = []
        chainai_atomsno = {}
        for chain in model.get_chains():
            chain_name = chain.id
            chain_residue_count = 0
            chain_resolution = 0.
            for residue in chain.get_residues():
                residue_atom_count = 0
                chain_residue_count += 1
                residue_name = residue.resname
                residue_no = residue.id[1]
                nearresidue_voxels = set()
                for atom in residue.get_atoms():
                    if atom.name.startswith('H') or atom.get_parent().resname == 'HOH':
                        continue
                    atomcount += 1
                    residue_atom_count += 1
                    onecoor = atom.coord
                    atom_indices = getindices(map, onecoor)[1]
                    around_indices = get_close_voxels_indices(map, atom_indices, radius)
                    nearresidue_voxels.update(around_indices)
                if residue_atom_count == 0:
                    continue
                # residue inclusion section
                keystr = chain_name + ':' + str(residue_no) + residue_name
                allkeys.append(keystr)
                cur_residue_resolution = residue_average_resolution(map.data, list(nearresidue_voxels))
                value = float('%.4f' % cur_residue_resolution)
                residue_color = floatohex([value])[0]
                chain_resolution += value
                allvalues.append(value)
                colors.append(residue_color)
            # chain inclusion section
            if chain_name in chainai_atomsno.keys():
                chain_resolution += chainai_atomsno[chain_name]['value']
                chain_residue_count += chainai_atomsno[chain_name]['residuesinchain']
            # For cases where one water molecule has a sigle but different chain id
            if chain_residue_count == 0:
                continue
            chainai_atomsno[chain_name] = {'value': chain_resolution, 'residuesinchain': chain_residue_count}

        for chainname, chain_scores in chainai_atomsno.items():
            chain_ai = float('%.3f' % round((float(chain_scores['value']) / chain_scores['residuesinchain']), 4))
            aicolor = floatohex([chain_ai])[0]
            chainaiscore[chainname] = {'value': chain_ai, 'color': aicolor, 'numberOfResidues': chain_scores['residuesinchain']}
        data_result['residue'] = allkeys
        data_result['localResolution'] = allvalues
        data_result['color'] = floatohex(scale_values(allvalues, 1, 0))
        data_result['chainResolution'] = chainaiscore
        result[str(modelcount-1)] = {'name': modelname, 'data': data_result}

    return result
