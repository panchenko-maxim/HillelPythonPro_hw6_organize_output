from app.services import add_group_to_groups
from app.services.classes import Human

type T_ORGANIZED_DATA = dict[str, set[str]]


def organize_data(humans: list[Human]) -> T_ORGANIZED_DATA:
    groups: T_ORGANIZED_DATA = {}
    for human in humans:
        add_group_to_groups(groups=groups, group=human["group"], name=human["name"])
    return groups
