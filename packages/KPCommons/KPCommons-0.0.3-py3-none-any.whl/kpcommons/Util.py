from typing import Tuple


def calculate_overlap(start_1: int, end_1: int, start_2: int, end_2: int) -> int:
    """
    Calculates the overlap between two ranges.
    :param start_1: Start of the first range
    :param end_1: End of the first range
    :param start_2: Start of the second range
    :param end_2: End of the second range
    :return: Length of the overlap, can be negative if there is no overlap
    """
    __check_values(start_1, end_1, start_2, end_2)

    overlap_start = max(start_1, start_2)
    overlap_end = min(end_1, end_2)
    overlap_length = overlap_end - overlap_start
    return overlap_length


def calculate_overlap_ratios(start_1: int, end_1: int, start_2: int, end_2: int) -> Tuple[float, float]:
    """
    Calculates the overlap ratios between two ranges.
    :param start_1: Start of the first range
    :param end_1: End of the first range
    :param start_2: Start of the second range
    :param end_2: End of the second range
    :return: The overlap ratios between start and end ranges
    """
    __check_values(start_1, end_1, start_2, end_2)
    overlap_length = calculate_overlap(start_1, end_1, start_2, end_2)

    if overlap_length <= 0:
        return 0, 0

    overlap_ratio_1 = overlap_length / (end_1 - start_1)
    overlap_ratio_2 = overlap_length / (end_2 - start_2)
    return overlap_ratio_1, overlap_ratio_2


def __check_values(start_1: int, end_1: int, start_2: int, end_2: int):

    if start_1 == end_1 or start_2 == end_2:
        raise ValueError(f'Start and end are the same')

    if start_1 > end_1:
        raise ValueError(f'Start value ({start_1}) is greater end value ({end_1})')

    if start_2 > end_2:
        raise ValueError(f'Start value ({start_2}) is greater end value ({end_2})')
