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


class V1WindowsSecurityContextOptions(object):
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
        'gmsa_credential_spec': 'str',
        'gmsa_credential_spec_name': 'str'
    }

    attribute_map = {
        'gmsa_credential_spec': 'gmsaCredentialSpec',
        'gmsa_credential_spec_name': 'gmsaCredentialSpecName'
    }

    def __init__(self, gmsa_credential_spec=None, gmsa_credential_spec_name=None):  # noqa: E501
        """V1WindowsSecurityContextOptions - a model defined in Swagger"""  # noqa: E501

        self._gmsa_credential_spec = None
        self._gmsa_credential_spec_name = None
        self.discriminator = None

        if gmsa_credential_spec is not None:
            self.gmsa_credential_spec = gmsa_credential_spec
        if gmsa_credential_spec_name is not None:
            self.gmsa_credential_spec_name = gmsa_credential_spec_name

    @property
    def gmsa_credential_spec(self):
        """Gets the gmsa_credential_spec of this V1WindowsSecurityContextOptions.  # noqa: E501

        GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. This field is alpha-level and is only honored by servers that enable the WindowsGMSA feature flag.  # noqa: E501

        :return: The gmsa_credential_spec of this V1WindowsSecurityContextOptions.  # noqa: E501
        :rtype: str
        """
        return self._gmsa_credential_spec

    @gmsa_credential_spec.setter
    def gmsa_credential_spec(self, gmsa_credential_spec):
        """Sets the gmsa_credential_spec of this V1WindowsSecurityContextOptions.

        GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field. This field is alpha-level and is only honored by servers that enable the WindowsGMSA feature flag.  # noqa: E501

        :param gmsa_credential_spec: The gmsa_credential_spec of this V1WindowsSecurityContextOptions.  # noqa: E501
        :type: str
        """

        self._gmsa_credential_spec = gmsa_credential_spec

    @property
    def gmsa_credential_spec_name(self):
        """Gets the gmsa_credential_spec_name of this V1WindowsSecurityContextOptions.  # noqa: E501

        GMSACredentialSpecName is the name of the GMSA credential spec to use. This field is alpha-level and is only honored by servers that enable the WindowsGMSA feature flag.  # noqa: E501

        :return: The gmsa_credential_spec_name of this V1WindowsSecurityContextOptions.  # noqa: E501
        :rtype: str
        """
        return self._gmsa_credential_spec_name

    @gmsa_credential_spec_name.setter
    def gmsa_credential_spec_name(self, gmsa_credential_spec_name):
        """Sets the gmsa_credential_spec_name of this V1WindowsSecurityContextOptions.

        GMSACredentialSpecName is the name of the GMSA credential spec to use. This field is alpha-level and is only honored by servers that enable the WindowsGMSA feature flag.  # noqa: E501

        :param gmsa_credential_spec_name: The gmsa_credential_spec_name of this V1WindowsSecurityContextOptions.  # noqa: E501
        :type: str
        """

        self._gmsa_credential_spec_name = gmsa_credential_spec_name

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
        if issubclass(V1WindowsSecurityContextOptions, dict):
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
        if not isinstance(other, V1WindowsSecurityContextOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
