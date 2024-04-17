import logging
import os
import json
import collections
import itertools
import uuid
import ibm_aigov_facts_client._wrappers.requests as requests
import hashlib

from typing import Optional
from datetime import datetime

from typing import BinaryIO, Dict, List, TextIO, Union, Any
from ibm_aigov_facts_client.factsheet import assets
from ibm_aigov_facts_client.factsheet.asset_utils_model import ModelAssetUtilities
from ibm_aigov_facts_client.factsheet.asset_utils_me_prompt import AIUsecaseUtilities
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, CloudPakForDataAuthenticator
from ibm_aigov_facts_client.utils.enums import AssetContainerSpaceMap, AssetContainerSpaceMapExternal, ContainerType, FactsType, ModelEntryContainerType, AllowedDefinitionType, FormatType, RenderingHints
from ibm_aigov_facts_client.utils.utils import validate_enum, validate_type, STR_TYPE
from ibm_aigov_facts_client.factsheet.asset_utils_me import ModelUsecaseUtilities
from ibm_aigov_facts_client.factsheet.asset_utils_experiments import NotebookExperimentUtilities
from ibm_cloud_sdk_core.utils import convert_model
from ibm_aigov_facts_client.utils.metrics_utils import convert_metric_value_to_float_if_possible
from ibm_aigov_facts_client.utils.cell_facts import CellFactsMagic
from ibm_aigov_facts_client.factsheet.assets import *

from ibm_aigov_facts_client.factsheet.approaches import ApproachUtilities
from ibm_aigov_facts_client.utils.config import *
from ibm_aigov_facts_client.utils.client_errors import *
from ibm_aigov_facts_client.utils.constants import *


from ibm_aigov_facts_client.factsheet.external_deployments import Deployment
from ibm_aigov_facts_client.factsheet.html_parser import FactHTMLParser
from ibm_aigov_facts_client.utils.doc_annotations import deprecated

_logger = logging.getLogger(__name__)


class AIGovAssetUtilities(ModelAssetUtilities):

    """
        AI asset utilities. Running `client.assets.get_prompt()` makes all methods in AIGovAssetUtilities object available to use.

    """

    def __init__(self, assets_client: 'assets.Assets', model_id: str = None, container_type: str = None, container_id: str = None, facts_type: str = None) -> None:

        self._asset_id = model_id
        self._container_type = container_type
        self._container_id = container_id
        self._facts_type = facts_type

        self._assets_client = assets_client
        self._facts_client = self._assets_client._facts_client
        self._is_cp4d = self._assets_client._is_cp4d
        self._external_model = self._assets_client._external_model

        if self._is_cp4d:
            self._cpd_configs = self._assets_client._cpd_configs
            self._cp4d_version = self._assets_client._cp4d_version

        self._facts_definitions = self._get_fact_definitions()
        self._facts_definitions_op = self._get_fact_definitions(
            type_name=FactsType.MODEL_FACTS_USER_OP)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AIGovAssetUtilities':
        """Initialize a AIGovAssetUtilities object from a json dictionary."""
        args = {}
        # if '_assets_client' in _dict:
        #     #added by Lakshmi as in __init__() , as assets_client is expected
        #     args['assets_client'] = _dict.get('_assets_client')

        if '_asset_id' in _dict:
            # args['asset_id'] = _dict.get('_asset_id') #commented by Lakshmi as in __init__() , asset_id is not expected
            args['model_id'] = _dict.get('_asset_id')

        if '_container_type' in _dict:
            # [convert_model(x) for x in metrics]
            args['container_type'] = _dict.get('_container_type')
        else:
            raise ValueError(
                'Required property \'container_type\' not present in AssetProps JSON')

        if '_container_id' in _dict:
            # [convert_model(x) for x in metrics]
            args['container_id'] = _dict.get('_container_id')
        else:
            raise ValueError(
                'Required property \'container_id\' not present in AssetProps JSON')

        if '_facts_type' in _dict:
            # [convert_model(x) for x in metrics]
            args['facts_type'] = _dict.get('_facts_type')
        else:
            raise ValueError(
                'Required property \'facts_type\' not present in AssetProps JSON')
        # return cls(**args)
        return cls(_dict.get('_assets_client'), **args)

    @classmethod
    def _from_dict(cls, _dict):
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, '_asset_id') and self._asset_id is not None:
            _dict['asset_id'] = self._asset_id
        if hasattr(self, '_container_type') and self._container_type is not None:
            _dict['container_type'] = self._container_type
        if hasattr(self, '_container_id') and self._container_id is not None:
            _dict['container_id'] = self._container_id
        if hasattr(self, '_facts_type') and self._facts_type is not None:
            _dict['facts_type'] = self._facts_type

        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AIGovAssetUtilities object."""
        return json.dumps(self.to_dict(), indent=2)

    def __repr__(self):
        """Return a `repr` version of this AIGovAssetUtilities object."""
        return json.dumps(self.to_dict(), indent=2)

    def set_environment_type(self, from_container: str, to_container: str) -> None:
        """
            This method is not available for prompt.
        """
        _logger.info("This method is not available for prompt")

    def get_experiment(self, experiment_name: str = None) -> NotebookExperimentUtilities:
        """
            This method is not available for prompt.
        """
        _logger.info("This method is not available for prompt")

    # def track(self,ai_usecase:AIUsecaseUtilities=None,approach:ApproachUtilities=None,grc_model:dict=None, version_number:str=None, version_comment:str=None):

    #     """
    #         Link Model to model use case. Model asset should be stored in either Project or Space and corrsponding ID should be provided when registering to model use case.

    #         Supported for CPD version >=4.7.0

    #         :param AIUsecaseUtilities ai_usecase: Instance of AIUsecaseUtilities
    #         :param ApproachUtilities approach: Instance of ApproachUtilities
    #         :param str grc_model: (Optional) Openpages model id. Only applicable for CPD environments. This should be dictionary, output of get_grc_model()
    #         :param str version_number: Version number of model. supports either a semantic versioning string or one of the following keywords for auto-incrementing based on the latest version in the approach: "patch", "minor", "major"
    #         :param str version_comment: (Optional) An optional comment describing the changes made in this version

    #         :rtype: AIGovAssetUtilities

    #         For tracking model with ai usecase:

    #         >>> prompt.track(ai_usecase=<instance of AIUsecaseUtilities>,approach=<instance of ApproachUtilities>,version_number=<version>)

    #     """

    #     if (ai_usecase is None or ai_usecase == ""):
    #         raise MissingValue("ai_usecase", "AIUsecaseUtilities object or instance is missing")

    #     if ( not isinstance(ai_usecase, AIUsecaseUtilities)):
    #         raise ClientError("Provide AIUsecaseUtilities object for ai_usecase")

    #     super().track(ai_usecase,approach,grc_model,version_number,version_comment)

    def untrack(self):
        """
            Unlink prompt from it's usecase and approach

            Example for IBM Cloud or CPD:

            >>> prompt.untrack()

        """

        wkc_unregister_url = WKC_MODEL_REGISTER.format(self._asset_id)

        params = {}
        params[self._container_type + '_id'] = self._container_id

        if self._is_cp4d:
            url = self._cpd_configs["url"] + \
                wkc_unregister_url
        else:
            if get_env() == 'dev':
                url = dev_config["DEFAULT_DEV_SERVICE_URL"] + \
                    wkc_unregister_url
            elif get_env() == 'test':
                url = test_config["DEFAULT_TEST_SERVICE_URL"] + \
                    wkc_unregister_url
            else:
                url = prod_config["DEFAULT_SERVICE_URL"] + \
                    wkc_unregister_url

        response = requests.delete(url,
                                   headers=self._get_headers(),
                                   params=params,
                                   )

        if response.status_code == 204:
            _logger.info("Successfully finished unregistering prompt {} from AI use case.".format(
                self._asset_id))
        else:
            error_msg = u'AI use case unregistering failed'
            reason = response.text
            _logger.info(error_msg)
            raise ClientError(error_msg + '. Error: ' +
                              str(response.status_code) + '. ' + reason)

    def get_deployments(self) -> List:
        """
            This method is not available for prompt.
        """
        _logger.info("This method is not available for prompt")

    def delete_deployments(self, deployment_ids: list = None):
        """
            This method is not available for prompt.
        """
        _logger.info("This method is not available for prompt")

    def add_deployments(self, deployments: list = None) -> list:
        """
            This method is not available for prompt.
        """
        _logger.info("This method is not available for prompt")

    # override get_version from parent class for prompt
    def get_version(self) -> Dict:
        """
            Get prompt template version details. Supported for CPD version >=4.7.0

            :rtype: dict

            The way to use me is:

            >>> get_prompt.get_version()

        """

        if self._is_cp4d and self._cp4d_version < "4.7.0":
            raise ClientError(
                "Version mismatch: Model version functionality is only supported in CP4D version 4.7.0 or higher. Current version of CP4D is "+self._cp4d_version)
        linked_ai_usecase_info = {}
        try:
            linked_ai_usecase_info = self._assets_client.get_tracking_model_usecase().to_dict()
            if "model_usecase_id" in linked_ai_usecase_info:
                linked_ai_usecase = linked_ai_usecase_info['model_usecase_id']

            else:
                raise ClientError(
                    f"Version information will be unavailable for untracked Prompt template asset. Please track the Prompt Asset {self._asset_id} to a ai usecase to view the version of the prompt template.", category=UserWarning)

            if linked_ai_usecase:
                _logger.info(
                    f"Prompt Asset {self._asset_id} is tracked to ai usecase : {str(linked_ai_usecase)}")

                url = self._get_assets_url(
                    self._asset_id, self._container_type, self._container_id)
                response = requests.get(url, headers=self._get_headers())
                if response.status_code == 200:
                    model_version_details = {}
                    if "model_version" in (response.json()["entity"]["wx_prompt"]):
                        model_version = response.json(
                        )["entity"]["wx_prompt"]["model_version"].get("number")
                        model_version_description = response.json(
                        )["entity"]["wx_prompt"]["model_version"].get("description")

                        model_version_details["number"] = model_version
                        model_version_details["description"] = model_version_description

                        _logger.info(
                            "Model version details retrieved successfully")
                        return model_version_details
                else:
                    raise ClientError("Failed to retrieve model version details information. ERROR {}. {}".format(
                        response.status_code, response.text))

        except ClientError as ce:
            if ce.error_msg.endswith("lmid is missing") or ce.error_msg.endswith("is not tracked by a model use case"):
                warnings.warn(
                    f"Version information unavailable for untracked Prompt template asset. Please track the Prompt Asset {self._asset_id} to ai usecase to view the version of the prompt template.", category=UserWarning)

            else:
                _logger.info(
                    f"Error getting version details for prompt asset {self._asset_id} due to following issue : {ce.error_msg}")
