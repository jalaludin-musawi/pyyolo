"""
    File name: yolo_data
    Author: rameshpr
    Date: 10/25/18
"""
from enum import Enum
from typing import Tuple, Union


class BBox(object):

    class Location(Enum):
        TOP_LEFT = 0
        TOP_RIGHT = 1
        BOTTOM_LEFT = 2
        BOTTOM_RIGHT = 3
        MID = 4

    def __init__(self, x=0, y=0, w=0, h=0, c=0):
        # type: (float, float, float, float, float) -> None
        """
        Collect information of a bounding box

        :param x: x co-ordinate of top left corner
        :param y: y co-ordinate of top left corner
        :param w: width
        :param h: height
        :param c: confidence
        """
        self.x = float(x)  # type: float
        self.y = float(y)  # type: float
        self.w = float(w)  # type: float
        self.h = float(h)  # type: float
        self.c = float(c)  # type: float

    def get_mid(self, is_int=False):
        # type: (bool) -> Tuple[Union[int, float], Union[int, float]]
        """
        Get the mid point of the Bounding Box
        :param is_int: If True the output co-ordinate will be cast to int. Else co-ordinate will be float
        :return: Mid point as a tuple in the format (x, y)
        """
        x = self.x + self.w / 2
        y = self.y + self.h / 2
        if is_int:
            return int(x), int(y)
        return x, y

    def get_point(self, location, is_int=False):
        # type: (BBox.Location, bool) -> Tuple[Union[int, float], Union[int, float]]
        """
        This function will give the co-ordinates of the location you send
        :param location: One of the locations available in BBox.Location
        :param is_int: if True the output co-ordinate will cast to int. Else co-ordinate will be float
        :return: Tuple of co-ordinates in the format (x, y)
        """
        if location == BBox.Location.TOP_LEFT:
            x = self.x
            y = self.y
        elif location == BBox.Location.TOP_RIGHT:
            x = self.x + self.w
            y = self.y
        elif location == BBox.Location.BOTTOM_LEFT:
            x = self.x
            y = self.y + self.h
        elif location == BBox.Location.BOTTOM_RIGHT:
            x = self.x + self.w
            y = self.y + self.h
        elif location == BBox.Location.MID:
            return self.get_mid(is_int)
        else:
            x = 0.0
            y = 0.0
        if is_int:
            x = int(x)
            y = int(y)
        return x, y


class YoloData(object):
    def __init__(self, id, name, bbox):
        # type: (int, str, BBox) -> None
        self.id = id        # type: int
        self.name = name    # type: str
        self.bbox = bbox    # type: BBox

