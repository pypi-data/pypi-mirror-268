from ...Zonevu import Zonevu
from ...Services.Client import ZonevuError
from ...Services.WellData import WellData
from ...Services.Storage import Storage
import time
from typing import Optional
import sys


def main_wells_to_storage(zonevu: Zonevu, storage: Storage, save_docs: Optional[bool] = True,
                          max_doc_size: Optional[int] = 10000000):
    """
    Write or update all wells from a ZoneVu account to user storage.
    :param max_doc_size:
    :param save_docs:
    :param zonevu: Zonevu client instance
    :param storage: User storage to save wells to
    """

    # file = open('c:/delme/pythonruns/output.txt', 'w')
    # sys.stdout = file
    try:
        print('Write all wells in ZoneVu account to disk - Running...')
        well_svc = zonevu.well_service          # Reference to Zonevu well service

        # List wells in account.  Write them out to storage.
        well_entries = well_svc.find_by_name()     # Get a list of all wells in zonevu account
        print('Number of wells retrieved = %s' % len(well_entries))
        num_updated = 0
        for index, well_entry in enumerate(well_entries):
            print('%s, ' % well_entry.full_name, end="")
            if index % 8 == 0:
                print()

            well = well_entry.well
            up_to_date = well.current(storage)  # See if there is a copy of well in storage & if it is current
            if up_to_date:
                continue        # If the row version of the stored version of the well the same, no need to save it.

            try:
                well_svc.load_well(well, {WellData.all})    # Load well with all well data
                well.save(storage)                  # Save well to storage. Overwrite the well if it  already exists
                if save_docs:
                    well.save_documents(zonevu.document_service, storage, max_doc_size)
                num_updated += 1
                # time.sleep(1)       # Give Zonevu a 1-second break.
            except ZonevuError as err:
                print('Could not update well "%s" because %s' % (well.full_name, err.message))

        print()
        print('%s wells were written or updated' % num_updated)

    finally:
        print('Write all wells in ZoneVu account to disk - Done.')
        # file.close()
        # sys.stdout = sys.__stdout__


