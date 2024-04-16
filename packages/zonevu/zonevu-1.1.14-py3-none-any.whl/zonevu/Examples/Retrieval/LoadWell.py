from ...Zonevu import Zonevu
from ...Services.Client import ZonevuError
from ...DataModels.Wells.Well import Well
from ...Services.WellData import WellData
from typing import Set


def main(zonevu: Zonevu, well_name: str, well_data: Set[WellData]) -> Well:
    print('Retrieve a named well and load some of its well data')
    print('Loading the following well data:')
    for d in well_data:
        print('  - %s' % d)
    well_svc = zonevu.well_service
    well = well_svc.get_first_named(well_name)
    if well is None:
        raise ZonevuError.local('Could not find the well "%s"' % well_name)

    # Load up specified well data
    # well_svc.load_well(well, {WellData.logs, WellData.curves})
    well_svc.load_well(well, well_data)
    wellbore = well.primary_wellbore
    print('Successfully loaded well data')
    print()
    return well




