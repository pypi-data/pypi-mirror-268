import copy
from ...Zonevu import Zonevu
from ...Services.Error import ZonevuError


def main_project_copy(zonevu: Zonevu, project_name: str, delete_code: str):
    print('Making a copy of project "%s"' % project_name)
    project_service = zonevu.project_service

    project = project_service.get_first_named(project_name)
    if project is None:
        raise ZonevuError.local('No project named "%s" could be found')

    project_copy = copy.deepcopy(project)
    project_copy.name = '%s_Copy' % project.name
    print('Name of copy will be "%s"' % project_copy.name)

    # See if a project with that name exists already. If so, delete it so we avoid making copies
    existing_copy = project_service.get_first_named(project_copy.name)
    if existing_copy is not None:
        project_service.delete_project(existing_copy.id, delete_code)
        print('Deleted existing copy of project')

    project_service.create_project(project_copy)

    print("Execution was successful")

