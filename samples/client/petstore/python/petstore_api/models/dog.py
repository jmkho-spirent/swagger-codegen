# coding: utf-8

"""
    Swagger Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Dog(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, class_name=None, color='red', breed=None):
        """
        Dog - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'class_name': 'str',
            'color': 'str',
            'breed': 'str'
        }

        self.attribute_map = {
            'class_name': 'className',
            'color': 'color',
            'breed': 'breed'
        }

        self._class_name = class_name
        self._color = color
        self._breed = breed

    @property
    def class_name(self):
        """
        Gets the class_name of this Dog.

        :return: The class_name of this Dog.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """
        Sets the class_name of this Dog.

        :param class_name: The class_name of this Dog.
        :type: str
        """
        if class_name is None:
            raise ValueError("Invalid value for `class_name`, must not be `None`")

        self._class_name = class_name

    @property
    def color(self):
        """
        Gets the color of this Dog.

        :return: The color of this Dog.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Sets the color of this Dog.

        :param color: The color of this Dog.
        :type: str
        """

        self._color = color

    @property
    def breed(self):
        """
        Gets the breed of this Dog.

        :return: The breed of this Dog.
        :rtype: str
        """
        return self._breed

    @breed.setter
    def breed(self, breed):
        """
        Sets the breed of this Dog.

        :param breed: The breed of this Dog.
        :type: str
        """

        self._breed = breed

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Dog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
