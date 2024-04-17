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

    divisions = [w.division.name for w in wells]
    unique_divisions = set(divisions)
    print()
    print()
    print('Wells exist in the following divisions:')
    for d in unique_divisions:
        print('   %s' % d)

    return wells

