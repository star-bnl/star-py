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
