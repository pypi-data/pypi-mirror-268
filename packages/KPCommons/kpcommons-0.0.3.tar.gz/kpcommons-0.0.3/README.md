# Readme

KPCommons is a collection of methods which are regularly needed.

## Util
Util.py contains the following methods:

- `calculate_overlap` is a method to calculate the overlap between two ranges.
  ~~~
  overlap = Util.calculate_overlap(0, 10, 5, 10)
  ~~~
  would return a result of 5. The first two arguments are the start and end position of the first range, and the last
  two arguments are the positions of the second range.
  
  **Note**: In case of no overlap, the distance between the two ranges is returned as a negative result.
- `calculate_overlap_ratios` is a method to calculate the overlap ratios of two ranges.
  ~~~
  ratio_1, ratio_2 = Util.calculate_overlap_ratio(0, 10, 5, 10)
  ~~~

## Footnote
Footnote.py contains a collection of methods for working with footnotes.

- `get_footnotes_ranges` takes a text and returns two list of tuples of start and end character positions of footnote
  ranges, that is, text surrounded by '[[[' and ']]]'. The first list is without an offset, that is, the actual
  positions, and the second list is with an offset, that is, as if the footnotes were removed.
- `get_footnote_ranges_without_offset` and `get_footnote_ranges_with_offset` are variants of `get_footnotes_ranges`
  which only return one of the lists.
- `is_position_in_ranges` checks if a position is in one of the ranges.
- `is_range_in_ranges` checks if a range given by a start and end position overlaps with one of the given ranges.
- `remove_footnotes` removes footnotes from a text. Footnotes are marked by '[[[' and ']]]'.
- `map_to_real_pos` maps start and end character positions of a text with footnotes removed to real positions, that is,
  positions before footnotes where removed.