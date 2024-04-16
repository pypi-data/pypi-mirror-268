import copy
from ...Zonevu import Zonevu
from tests.test_globals import get_test_zonevu


def main_list_projects(zonevu: Zonevu):
    project_svc = zonevu.project_service

    print('Projects:')
    project_entries = project_svc.get_projects()
    project_entries.sort(key=lambda x: x.name)

    for entry in project_entries:
        print('%s (%s)' % (entry.name, entry.id))
        project = project_svc.find_project(entry.id)
        if project.strat_column is not None:
            print('   Strat column = %s' % project.strat_column.name)
        print('   Num wells = %s' % len(project.wells))
        if len(project.seismic_surveys) > 0:
            print('   Seismic 3D survey = %s' % project.seismic_surveys[0].name)
        if project.geomodel is not None:
            print('   Geomodel = %s' % project.geomodel.name)
        if len(project.layers) > 0:
            print('   Num map layers = %s' % len(project.layers))

    print("Execution was successful")

