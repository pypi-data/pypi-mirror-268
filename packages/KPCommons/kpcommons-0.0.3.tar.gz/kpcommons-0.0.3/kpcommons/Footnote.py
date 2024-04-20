from typing import List, Tuple
import re


def get_footnote_ranges_without_offset(input_text: str) -> List[Tuple[int, int]]:
    """
    Extract ranges of footnotes from a text.
    :param input_text: The input text where footnotes are marked by '[[[' and ']]]'.
    :return: A list of tuples of start and end character positions of footnote ranges.
    """
    ranges, _ = get_footnote_ranges(input_text)
    return ranges


def get_footnote_ranges_with_offset(input_text: str) -> List[Tuple[int, int]]:
    """
    Extract ranges of footnotes from a text. The ranges are offset by the length of previous footnotes.
    :param input_text: The input text where footnotes are marked by '[[[' and ']]]'.
    :return: A list of tuples of start and end character positions of footnote ranges with an offset. The
    returned positions are as if the footnotes were removed.
    """
    _, ranges_with_offset = get_footnote_ranges(input_text)
    return ranges_with_offset


def get_footnote_ranges(input_text: str) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    """
    Extract ranges of footnotes from a text. The first returned list is without an offset, that is, the actual
    positions, and the second list is with an offset by the length of previous footnotes.
    :param input_text: The input text where footnotes are marked by '[[[' and ']]]'.
    :return: A tuple of two lists where both lists are lists of tuples of start and end character positions of footnote
    ranges. The first list is without an offset, that is, the actual positions, and the second list is with an offset,
    that is, as if the footnotes were removed.
    """
    result: List[Tuple[int, int]] = []
    result_with_offset: List[Tuple[int, int]] = []

    offset = 0
    for re_match in re.finditer(r'\[\[\[((?:.|\n)+?)]]]', input_text):
        start = re_match.start()
        end = re_match.end()
        result.append((start, end))
        result_with_offset.append((start - offset, end - offset))
        offset += end - start

    return result, result_with_offset


def is_position_in_ranges(start: int, ranges: List[Tuple[int, int]]) -> bool:
    """
    Check if a position is in one of the ranges.
    :param start: The position to check
    :param ranges: A list of tuples of start and end character positions of ranges
    :return: True if the position is in the ranges, otherwise False.
    """
    for rf in ranges:
        if rf[0] <= start < rf[1]:
            return True

    return False


def is_range_in_ranges(start: int, end: int, ranges: List[Tuple[int, int]]) -> bool:
    """
    Check if a range given by a start and end position overlaps with one of the given ranges.
    :param start: A start character position
    :param end: A end character position
    :param ranges: A list of tuples of start and end character positions of ranges
    :return: True if the start or end position is in the ranges, otherwise False.
    """
    for rf in ranges:
        if (rf[0] <= start < rf[1]) or (rf[0] <= end <= rf[1]):
            return True

    return False


def remove_footnotes(input_text: str):
    """
    Remove footnotes from a text. Footnotes are marked by '[[[' and ']]]'.
    :param input_text: The input text.
    :return: Text with footnotes removed.
    """
    result_text = re.sub(r'\[\[\[((?:.|\n)+?)]]]', '', input_text)
    return result_text


def map_to_real_pos(start, end, fn_ranges):
    """
    Map start and end character positions of text with footnote removed to real positions, that is, positions before
    footnotes where removed.
    :param start: A start character position
    :param end: A end character position
    :param fn_ranges: Ranges of footnotes in the original text, that is, footnote ranges with offset.
    :return:
    """
    start_offset = 0
    end_offset = 0

    for fn_range in fn_ranges:
        if fn_range[0] < start:
            start_offset += fn_range[1] - fn_range[0]
            end_offset += fn_range[1] - fn_range[0]
        elif fn_range[0] < end:
            end_offset += fn_range[1] - fn_range[0]
        else:
            break

    return start + start_offset, end + end_offset
