from math import atan, tan, radians, degrees


def lat_lng(lat, lng):
    """
    Return corrected lat/lng.
    Lat: -90 to 90
    Lng: -180 to 180
    """

    # lat
    # if lat > 180:   # reduce to value less than 180
    #     lat = lat - (lat//180)*180

    # if lat < -180:  # increase to value greater than -180
    #     lat = lat
    # if lat > 90.0:
    #     amt_gt_90 = lat - (lat//90)*90
    #     lat = 90 - amt_gt_90
    lng = degrees(-2*atan(1/tan((radians(lng)-180)/2)))

    return lat, lng
