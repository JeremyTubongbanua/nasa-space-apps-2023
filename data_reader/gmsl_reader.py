from gmsl_entry import GMSLEntry


def get_lines_from_file(file_path: str) -> list[str]:
    """Returns a list of lines from a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        list[str]: List of lines from the file.
    """
    with open(file_path, 'r') as file:
        return file.readlines()


def get_gmsl_entries(file_path: str) -> list[GMSLEntry]:
    """
    Returns a list of GMSLEntry objects from a file.

    Example:
        gmsl_entries = get_gmsl_entries('./assets/GMSL_TPJAOS_5.1_199209_202305.txt')
        print(gmsl_entries[0].smoothed_gmsl_variation)

    Args:
        file_path (str): Path to the file.

    Returns: 
        list[GMSLEntry]: List of GMSLEntry objects from the file.

    """

    lines_raw = get_lines_from_file(file_path)

    # if line starts with HDR, remove it
    lines = [line for line in lines_raw if not line.startswith('HDR')]

    gmsl_entries: list[GMSLEntry] = []

    for i in range(len(lines)):
        column = lines[i].split()
        if (len(column) != 13):
            raise Exception(
                f'Line {i} has {len(column)} columns instead of 13.')
        entry: GMSLEntry = GMSLEntry(
            int(column[0]),
            int(column[1]),
            float(column[2]),
            int(column[3]),
            float(column[4]),
            float(column[5]),
            float(column[6]),
            float(column[7]),
            float(column[8]),
            float(column[9]),
            float(column[10]),
            float(column[11]),
            float(column[12])
        )
        gmsl_entries.append(entry)

    return gmsl_entries
