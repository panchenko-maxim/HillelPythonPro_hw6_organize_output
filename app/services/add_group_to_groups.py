def add_group_to_groups(groups: dict[str, set[str]], group: str, name: str) -> None:
    if group not in groups:
        groups[group] = set()
    groups[group].add(name)
