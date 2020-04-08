# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    """
    Method to find the minimal amount of points to touche all overlapping lines
    Args:
        segments: line objects that overlap in 2D space

    Returns:
        List of points on 2D number-line where most lines intersect
    """
    # sort segments in ascending order
    segments = sorted(segments, key=lambda item: item[0])
    # define exit criterion
    necessary_signatures = len(segments)

    result = []
    count = 0
    # loop as long as signatures are still outstanding
    while necessary_signatures != count:
        # start from the left end of first unconsidered line
        starting_value = segments[count][0]
        end_value = segments[count][1] + 1
        temp_counts = []
        # go through coordinates of the line and see how many lines lie parallel to it
        for coordinate in range(starting_value, end_value):
            temp_counts.append(len([i for i in segments[count:] if i[0] <= coordinate]))
        # find the point with the maximum amount of parallel lines and append it to the result list
        result.append(temp_counts.index(max(temp_counts)) + starting_value)
        # shift right for as many signatures as have been collected
        count += max(temp_counts)
    return result


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
    # compute_optimal_points([Segment(4, 7), Segment(1, 3), Segment(2, 5), Segment(5, 6)])
