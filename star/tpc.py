import numpy as np

SECTOR_ENDS = np.deg2rad(np.linspace(-180 + 15, 180 + 15, 12, endpoint=False))
SECTOR_CENTERS = np.deg2rad(np.linspace(-180, 180, 12, endpoint=False))

_starts = np.concatenate(([-np.pi], SECTOR_ENDS))
_stops  = np.concatenate((SECTOR_ENDS, [np.pi]))
SECTOR_EDGES = np.array([_starts, _stops])

SECTOR_IDS_WEST = (np.arange(12, 0, -1) - 4) % 12 + 1
SECTOR_IDS_EAST = 24 - SECTOR_IDS_WEST % 12

SECTORS_EAST = np.append(SECTOR_IDS_EAST, SECTOR_IDS_EAST[0])
SECTORS_WEST = np.append(SECTOR_IDS_WEST, SECTOR_IDS_WEST[0])


def sectors(angles, half='east'):
    """
    Returns TPC sector IDs corresponding to the given angles
    """
    # Each angle is tested to lie between sector boundaries, i.e. _start <= angle < _stop
    tpc_sector_indices = np.less_equal(_starts, angles[:, np.newaxis]) & np.greater(_stops, angles[:, np.newaxis])
    # Get indices of non-zero elements along the second dimension
    tpc_sector_indices = tpc_sector_indices.nonzero()[1]
    if half == 'east':
        return np.fromiter((SECTORS_EAST[i] for i in tpc_sector_indices), 'int64', len(tpc_sector_indices))
    elif half == 'west':
        return np.fromiter((SECTORS_WEST[i] for i in tpc_sector_indices), 'int64', len(tpc_sector_indices))
    else:
        return None
