import lat_lng as ll


# def test_lat_gt_90():
#     assert ll.lat_lng(100.1, 0) == (79.9, 0)


# def test_lat_lt_90():
#     assert ll.lat_lng(80.1, 0) == (80.1, 0)


# def test_lat_eq_90():
#     assert ll.lat_lng(90.0, 0) == (90.0, 0)


# def test_lat_gt_neg_90():
#     assert ll.lat_lng(-80.1, 0) == (-80.1, 0)


# def test_lat_lt_neg_90():
#     assert ll.lat_lng(-100.1, 0) == (-79.0, 0)


# def test_lat_lt_neg_90_multiple():
#     assert ll.lat_lng(-180.0, 0) == (0.0, 0)


# def test_lat_lt_neg_90_multiple_2():
#     assert ll.lat_lng(-200.1, 0) == (20.1, 0)


# def test_lat_gt_90_multiple():
#     assert ll.lat_lng(180.0, 0) == (0.0, 0)


# def test_lat_gt_90_muliple_2():
#     assert ll.lat_lng(200.1, 0) == (-20.1, 0)


def test_lng_gt_180():
    assert ll.lat_lng(0, 180.1) == (0, -179.9)


def test_lng_lt_180():
    assert ll.lat_lng(0, 80.1) == (0, 80.1)


def test_lng_eq_180():
    assert ll.lat_lng(0, 180.0) == (0, 180.0)


def test_lng_gt_neg_180():
    assert ll.lat_lng(0, -100.1) == (0, -100.1)


def test_lng_lt_neg_180():
    assert ll.lat_lng(0, -180.1) == (0, 179.9)


def test_lng_lt_neg_180_multiple():
    assert ll.lat_lng(0, -360.0) == (0, 0.0)


def test_lng_lt_neg_180_multiple_2():
    assert ll.lat_lng(0, -380.1) == (0, -20.1)


def test_lng_gt_180_multiple():
    assert ll.lat_lng(0, 360.0) == (0, 0.0)


def test_lng_gt_180_muliple_2():
    assert ll.lat_lng(0, 380.1) == (0, 20.1)