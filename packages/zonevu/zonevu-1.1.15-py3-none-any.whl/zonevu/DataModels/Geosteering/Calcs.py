from dataclasses import dataclass, field
from ...DataModels.Geosteering.Horizon import TypewellHorizonDepth, Horizon
from ...DataModels.Geosteering.Interpretation import Interpretation
from ...DataModels.Wells.Station import Station
from ...DataModels.Wells.Survey import Survey
from shapely.geometry import Polygon, LineString
from typing import List
from itertools import groupby
import math

"""
Utilities to convert geosteering interpretation into blocks, and to compute percent in zone
"""


@dataclass
class Layer:
    """
    A layer in a geosteering block corresponding to a horizon in a geosteering interpretation
    """
    horz: Horizon
    md_start: float
    md_end: float
    tvd_start: float
    tvd_end: float
    thickness: float

    @property
    def polygon(self) -> Polygon:
        """
        A polygon in (md, tvd) space that is a layer in a geosteering block
        :return:
        """
        s = self
        x1 = s.md_start
        x2 = s.md_end
        y1a = s.tvd_start
        y1b = y1a + s.thickness
        y2a = s.tvd_end
        y2b = y2a + s.thickness
        coordinates = ((x1, y1a), (x2, y2a), (x2, y2b), (x1, y1b))
        p = Polygon(coordinates)
        return p


@dataclass
class Block:
    """
    A geosteering block derived from a geosteering interpretation pick
    """
    md_start: float
    md_end: float
    layers: List[Layer] = field(default_factory=list[Layer])


@dataclass
class ZoneCalc:
    horizon: Horizon
    length: float = 0
    layers: List[Layer] = field(default_factory=list[Layer])
    percent: float = 0


def make_blocks(interp: Interpretation) -> List[Block]:
    """
    Computes the blocks for a geosteering interpretation
    :param interp: A geosteering interpretation
    :return: a list of geosteering blocks
    """
    # Make a list of layer thicknesses for each employed typewell
    interp.typewell_horizon_depths.sort(key=lambda d: d.type_wellbore_id)  # Make sure horz depths in type well order
    type_well_groups = groupby(interp.typewell_horizon_depths, key=lambda d: d.type_wellbore_id)  # Group by type well
    type_well_depth_dict = {key: list(group) for key, group in type_well_groups}  # Make depth list LUT by type well id
    for wellbore_id, h_depths in type_well_depth_dict.items():
        h_depths.sort(key=lambda h_depth: h_depth.tvt)  # Make sure lists are in TVT order

    # Create a list of geosteering blocks
    horizons_dict = {h.id: h for h in interp.horizons}  # Make a horizon lookup dictionary
    picks = interp.picks
    blocks: List[Block] = []
    for p1, p2 in zip(picks, picks[1:]):
        if p1.block_flag and p2.md > p1.md:  # We process block picks, not fault picks
            block = Block(p1.md, p2.md)
            blocks.append(block)
            h_depths = type_well_depth_dict[p1.type_wellbore_id]  # Get type well horizon depths for this pick
            depth_pairs = zip(h_depths, h_depths[1:])
            for d1, d2 in depth_pairs:
                tvd1 = p1.target_tvd + d1.tvt  # Compute geometry of the layer for this horizon pair
                tvd2 = p2.target_tvd + d1.tvt
                thickness = d2.tvt - d1.tvt
                horizon = horizons_dict[d1.horizon_id]  # Find horizon for this type well depth
                layer = Layer(horizon, p1.md, p2.md, tvd1, tvd2, thickness)
                block.layers.append(layer)  # Create layer and add to block for this pick

    return blocks


def calc_percent_in_zone(interp: Interpretation, stations: List[Station]) -> List[ZoneCalc]:
    """
    Computes the percent in zone for a wellbore (that is, a deviation survey) for a geosteering interpretation
    :param interp:
    :param stations: a list of survey stations that defines the wellbore that was geosteered
    :return:
    """
    blocks = make_blocks(interp)  # Get a list of blocks for this geosteering interpretation
    zone_calcs = {h.id: ZoneCalc(h) for h in interp.horizons}  # Dictionary to accumulate zone lengths

    for block in blocks:
        for layer in block.layers:
            for s1, s2 in zip(stations, stations[1:]):
                try:
                    line = LineString(((s1.md, s1.tvd), (s2.md, s2.tvd)))  # Make a line from survey station pair
                    intersection = line.intersection(layer.polygon)  # Get intersection of line with layer polygon
                    zone_calcs[layer.horz.id].length += intersection.length  # Accumulate intersection length
                    if intersection.length > 0:
                        zone_calcs[layer.horz.id].layers.append(layer)
                except BaseException as intersect_err:
                    print("Fail intersection!")
                    raise intersect_err

    zone_calc_list = list(zone_calcs.values())
    zones_length = sum(calc.length for calc in zone_calc_list)  # Sum of all horizon/formation traversals
    for calc in zone_calc_list:
        calc.percent = 100 * calc.length / zones_length  # Compute percent in zone for this horizon
    return zone_calc_list
