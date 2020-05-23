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


class V1alpha1CreateCronWorkflowRequest(object):
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
        'create_options': 'IoK8sApimachineryPkgApisMetaV1CreateOptions',
        'cron_workflow': 'V1alpha1CronWorkflow',
        'namespace': 'str'
    }

    attribute_map = {
        'create_options': 'createOptions',
        'cron_workflow': 'cronWorkflow',
        'namespace': 'namespace'
    }

    def __init__(self, create_options=None, cron_workflow=None, namespace=None):  # noqa: E501
        """V1alpha1CreateCronWorkflowRequest - a model defined in Swagger"""  # noqa: E501

        self._create_options = None
        self._cron_workflow = None
        self._namespace = None
        self.discriminator = None

        if create_options is not None:
            self.create_options = create_options
        if cron_workflow is not None:
            self.cron_workflow = cron_workflow
        if namespace is not None:
            self.namespace = namespace

    @property
    def create_options(self):
        """Gets the create_options of this V1alpha1CreateCronWorkflowRequest.  # noqa: E501


        :return: The create_options of this V1alpha1CreateCronWorkflowRequest.  # noqa: E501
        :rtype: IoK8sApimachineryPkgApisMetaV1CreateOptions
        """
        return self._create_options

    @create_options.setter
    def create_options(self, create_options):
        """Sets the create_options of this V1alpha1CreateCronWorkflowRequest.


        :param create_options: The create_options of this V1alpha1CreateCronWorkflowRequest.  # noqa: E501
        :type: IoK8sApimachineryPkgApisMetaV1CreateOptions
        """

        self._create_options = create_options

    @property
    def cron_workflow(self):
        """Gets the cron_workflow of this V1alpha1CreateCronWorkflowRequest.  # noqa: E501


        :return: The cron_workflow of this V1alpha1CreateCronWorkflowRequest.  # noqa: E501
        :rtype: V1alpha1CronWorkflow
        """
        return self._cron_workflow

    @cron_workflow.setter
    def cron_workflow(self, cron_workflow):
        """Sets the cron_workflow of this V1alpha1CreateCronWorkflowRequest.


        :param cron_workflow: The cron_workflow of this V1alpha1CreateCronWorkflowRequest.  # noqa: E501
        :type: V1alpha1CronWorkflow
        """

        self._cron_workflow = cron_workflow

    @property
    def namespace(self):
        """Gets the namespace of this V1alpha1CreateCronWorkflowRequest.  # noqa: E501


        :return: The namespace of this V1alpha1CreateCronWorkflowRequest.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V1alpha1CreateCronWorkflowRequest.


        :param namespace: The namespace of this V1alpha1CreateCronWorkflowRequest.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

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
        if issubclass(V1alpha1CreateCronWorkflowRequest, dict):
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
        if not isinstance(other, V1alpha1CreateCronWorkflowRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
