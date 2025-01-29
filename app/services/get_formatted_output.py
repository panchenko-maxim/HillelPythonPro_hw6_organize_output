type T_ORGANIZED_DATA = dict[str, set[str]]
type T_OUTPUT = str


def get_formatted_output(data: T_ORGANIZED_DATA) -> T_OUTPUT:
    text = "\n"
    for i, group in enumerate(data, 1):
        text += (
            f"{i}). Группа {group} включает {len(data[group])} участников!\n"
            f"    Их имена: {', '.join(data[group])}\n"
        )
    return text
