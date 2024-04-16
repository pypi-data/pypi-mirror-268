from ...Zonevu import Zonevu
from typing import List
from ...DataModels.Wells.Well import WellEntry
from typing import Optional


def main(zonevu: Zonevu, exact_match: bool = True, name: Optional[str] = None) -> List[WellEntry]:
    print('List all wells in ZoneVu account')
    well_svc = zonevu.well_service
    wells = well_svc.find_by_name(name, exact_match)
    print('Number of wells retrieved = %s' % len(wells))
    for index, well in enumerate(wells):
        print('%s, ' % well.full_name, end="")
        if index % 5 == 0:
            print()

    return wells

