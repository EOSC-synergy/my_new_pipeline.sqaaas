# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ToolDocker(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, image: str=None, reviewed: date=None):
        """ToolDocker - a model defined in OpenAPI

        :param image: The image of this ToolDocker.
        :param reviewed: The reviewed of this ToolDocker.
        """
        self.openapi_types = {
            'image': str,
            'reviewed': date
        }

        self.attribute_map = {
            'image': 'image',
            'reviewed': 'reviewed'
        }

        self._image = image
        self._reviewed = reviewed

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ToolDocker':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Tool_docker of this ToolDocker.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def image(self):
        """Gets the image of this ToolDocker.


        :return: The image of this ToolDocker.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ToolDocker.


        :param image: The image of this ToolDocker.
        :type image: str
        """

        self._image = image

    @property
    def reviewed(self):
        """Gets the reviewed of this ToolDocker.


        :return: The reviewed of this ToolDocker.
        :rtype: date
        """
        return self._reviewed

    @reviewed.setter
    def reviewed(self, reviewed):
        """Sets the reviewed of this ToolDocker.


        :param reviewed: The reviewed of this ToolDocker.
        :type reviewed: date
        """

        self._reviewed = reviewed
