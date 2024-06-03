# Using the Haversine formula for geographic Great Circle Distance
#
# As per https://en.wikipedia.org/wiki/Haversine_formula

#!/usr/bin/env python3

from math import cos, radians, sin, pow, asin, sqrt

def distance(lat1, long1, lat2, long2):
    """
    Calculate the great-circle distance between two points 
    on the Earth's surface given their latitude and longitude.

    Parameters:
    lat1 (float): Latitude of the first point in degrees.
    long1 (float): Longitude of the first point in degrees.
    lat2 (float): Latitude of the second point in degrees.
    long2 (float): Longitude of the second point in degrees.

    Returns:
    float: Distance between the two points in kilometers.
    """
    radius = 6371 # Radius of the Earth in kilometers.

    # Convert latitude and longitude from degrees to radians.
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    long1 = radians(long1)
    long2 = radians(long2)

    # Compute differences in coordinates.
    dlat = lat2 - lat1
    dlon = long2 - long1

    # Haversine formula to calculate the distance.
    a = pow(sin(dlat / 2), 2) + cos(lat1) * cos(lat2) * pow(sin(dlon / 2), 2)
    distance = 2 * radius * asin(sqrt(a))

    return distance

def main():
    # Example usage with Simpson Desert coordinates:
    # Coordinates of the western edge (latitude and longitude in degrees).
    lat1, long1 = -24.570, 137.225
    # Coordinates of the eastern edge (latitude and longitude in degrees).
    lat2, long2 = -25.000, 138.500

    # Calculate distance between the points.
    dist = distance(lat1, long1, lat2, long2)
    
    print(f"The distance between the points is: {dist:.2f} km")

if __name__ == "__main__":
    main()
