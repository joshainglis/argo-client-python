# coding: utf-8

"""
    Argo

    Python client for Argo Workflows  # noqa: E501

    OpenAPI spec version: v2.8.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1alpha1TarStrategy(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'compression_level': 'int'
    }

    attribute_map = {
        'compression_level': 'compressionLevel'
    }

    def __init__(self, compression_level=None):  # noqa: E501
        """V1alpha1TarStrategy - a model defined in Swagger"""  # noqa: E501

        self._compression_level = None
        self.discriminator = None

        if compression_level is not None:
            self.compression_level = compression_level

    @property
    def compression_level(self):
        """Gets the compression_level of this V1alpha1TarStrategy.  # noqa: E501

        CompressionLevel specifies the gzip compression level to use for the artifact. Defaults to gzip.DefaultCompression.  # noqa: E501

        :return: The compression_level of this V1alpha1TarStrategy.  # noqa: E501
        :rtype: int
        """
        return self._compression_level

    @compression_level.setter
    def compression_level(self, compression_level):
        """Sets the compression_level of this V1alpha1TarStrategy.

        CompressionLevel specifies the gzip compression level to use for the artifact. Defaults to gzip.DefaultCompression.  # noqa: E501

        :param compression_level: The compression_level of this V1alpha1TarStrategy.  # noqa: E501
        :type: int
        """

        self._compression_level = compression_level

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(V1alpha1TarStrategy, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1TarStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
