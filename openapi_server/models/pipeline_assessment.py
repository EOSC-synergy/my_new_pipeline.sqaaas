# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model_ import Model
from openapi_server.models.repository import Repository
from openapi_server import util


class PipelineAssessment(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, repo_code: Repository=None, repo_docs: Repository=None):
        """PipelineAssessment - a model defined in OpenAPI

        :param repo_code: The repo_code of this PipelineAssessment.
        :param repo_docs: The repo_docs of this PipelineAssessment.
        """
        self.openapi_types = {
            'repo_code': Repository,
            'repo_docs': Repository
        }

        self.attribute_map = {
            'repo_code': 'repo_code',
            'repo_docs': 'repo_docs'
        }

        self._repo_code = repo_code
        self._repo_docs = repo_docs

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PipelineAssessment':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Pipeline_assessment of this PipelineAssessment.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def repo_code(self):
        """Gets the repo_code of this PipelineAssessment.


        :return: The repo_code of this PipelineAssessment.
        :rtype: Repository
        """
        return self._repo_code

    @repo_code.setter
    def repo_code(self, repo_code):
        """Sets the repo_code of this PipelineAssessment.


        :param repo_code: The repo_code of this PipelineAssessment.
        :type repo_code: Repository
        """
        if repo_code is None:
            raise ValueError("Invalid value for `repo_code`, must not be `None`")

        self._repo_code = repo_code

    @property
    def repo_docs(self):
        """Gets the repo_docs of this PipelineAssessment.


        :return: The repo_docs of this PipelineAssessment.
        :rtype: Repository
        """
        return self._repo_docs

    @repo_docs.setter
    def repo_docs(self, repo_docs):
        """Sets the repo_docs of this PipelineAssessment.


        :param repo_docs: The repo_docs of this PipelineAssessment.
        :type repo_docs: Repository
        """

        self._repo_docs = repo_docs
