# python3


def compute_min_number_of_refills(distance_between_cities, max_distance, distances_gas):
    """
    Function for a greedy algorithm to find minimal number of stops to be made in trip between cities.
    Args:
        distance_between_cities: integer of total distance to be traveled
        max_distance: maximum distance the car can go within one go
        distances_gas: list of distance between gas stations (accumulative) e.g. [100, 300, 200, 100, ...]

    Returns:
        int minimum number of stops required
    """
    assert 1 <= distance_between_cities <= 10 ** 5
    assert 1 <= max_distance <= 400
    assert 1 <= len(distances_gas) <= 300
    assert 0 < distances_gas[0] and all(
        distances_gas[i] < distances_gas[i + 1] for i in range(len(distances_gas) - 1)) and distances_gas[
               -1] < distance_between_cities

    stops_made, dist_traveled = 0, 0
    # append the last stop as element to the list of potential destinations
    distances_gas.append(distance_between_cities)

    while dist_traveled < distance_between_cities:
        # find list of gas stations that we can reach
        reachable_stations = [i for i in distances_gas if i - dist_traveled <= max_distance]
        # if the list is empty return -1
        if not reachable_stations:
            return -1
        # update the traveled distance for exit condition
        dist_traveled = reachable_stations[-1]
        # skip the first element, because we already traveled there
        distances_gas = distances_gas[distances_gas.index(reachable_stations[-1]) + 1:]
        stops_made += 1
    # return the number of stops excluding the arrival at the destination
    return stops_made - 1


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
