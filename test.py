import pytest
import lat_lng as ll


def test_lat_gt_90():
    assert ll.lat_lng(100.1, 0) == (79.9, 0)


def test_lat_lt_90():
    assert ll.lat_lng(80.1, 0) == (80.1, 0)


def test_lat_eq_90():
    assert ll.lat_lng(90.0, 0) == (90.0, 0)


def test_lat_gt_neg_90():
    assert ll.lat_lng(-80.1, 0) == (-80.1, 0)


def test_lat_lt_neg_90():
    assert ll.lat_lng(-100.1, 0) == (-79.0, 0)


def test_lat_lt_neg_90_multiple():
    assert ll.lat_lng(-180.0, 0) == (0.0, 0)


def test_lat_lt_neg_90_multiple_2():
    assert ll.lat_lng(-200.1, 0) == (20.1, 0)


def test_lat_gt_90_multiple():
    assert ll.lat_lng(180.0, 0) == (0.0, 0)


def test_lat_gt_90_muliple_2():
    assert ll.lat_lng(200.1, 0) == (-20.1, 0)
