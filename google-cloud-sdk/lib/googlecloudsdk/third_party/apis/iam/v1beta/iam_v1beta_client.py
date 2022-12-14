"""Generated client library for iam version v1beta."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.iam.v1beta import iam_v1beta_messages as messages


class IamV1beta(base_api.BaseApiClient):
  """Generated client library for service iam version v1beta."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://iam.googleapis.com/'
  MTLS_BASE_URL = 'https://iam.mtls.googleapis.com/'

  _PACKAGE = 'iam'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1beta'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'IamV1beta'
  _URL_VERSION = 'v1beta'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new iam handle."""
    url = url or self.BASE_URL
    super(IamV1beta, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_workloadIdentityPools_operations = self.ProjectsLocationsWorkloadIdentityPoolsOperationsService(self)
    self.projects_locations_workloadIdentityPools_providers_operations = self.ProjectsLocationsWorkloadIdentityPoolsProvidersOperationsService(self)
    self.projects_locations_workloadIdentityPools_providers = self.ProjectsLocationsWorkloadIdentityPoolsProvidersService(self)
    self.projects_locations_workloadIdentityPools = self.ProjectsLocationsWorkloadIdentityPoolsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsWorkloadIdentityPoolsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_workloadIdentityPools_operations resource."""

    _NAME = 'projects_locations_workloadIdentityPools_operations'

    def __init__(self, client):
      super(IamV1beta.ProjectsLocationsWorkloadIdentityPoolsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (IamProjectsLocationsWorkloadIdentityPoolsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/workloadIdentityPools/{workloadIdentityPoolsId}/operations/{operationsId}',
        http_method='GET',
        method_id='iam.projects.locations.workloadIdentityPools.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='IamProjectsLocationsWorkloadIdentityPoolsOperationsGetRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

  class ProjectsLocationsWorkloadIdentityPoolsProvidersOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_workloadIdentityPools_providers_operations resource."""

    _NAME = 'projects_locations_workloadIdentityPools_providers_operations'

    def __init__(self, client):
      super(IamV1beta.ProjectsLocationsWorkloadIdentityPoolsProvidersOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (IamProjectsLocationsWorkloadIdentityPoolsProvidersOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/workloadIdentityPools/{workloadIdentityPoolsId}/providers/{providersId}/operations/{operationsId}',
        http_method='GET',
        method_id='iam.projects.locations.workloadIdentityPools.providers.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='IamProjectsLocationsWorkloadIdentityPoolsProvidersOperationsGetRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

  class ProjectsLocationsWorkloadIdentityPoolsProvidersService(base_api.BaseApiService):
    """Service class for the projects_locations_workloadIdentityPools_providers resource."""

    _NAME = 'projects_locations_workloadIdentityPools_providers'

    def __init__(self, client):
      super(IamV1beta.ProjectsLocationsWorkloadIdentityPoolsProvidersService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new WorkloadIdentityPoolProvider in a WorkloadIdentityPool. You cannot reuse the name of a deleted provider until 30 days after deletion.

      Args:
        request: (IamProjectsLocationsWorkloadIdentityPoolsProvidersCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/workloadIdentityPools/{workloadIdentityPoolsId}/providers',
        http_method='POST',
        method_id='iam.projects.locations.workloadIdentityPools.providers.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['workloadIdentityPoolProviderId'],
        relative_path='v1beta/{+parent}/providers',
        request_field='googleIamV1betaWorkloadIdentityPoolProvider',
        request_type_name='IamProjectsLocationsWorkloadIdentityPoolsProvidersCreateRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a WorkloadIdentityPoolProvider. Deleting a provider does not revoke credentials that have already been issued; they continue to grant access. You can undelete a provider for 30 days. After 30 days, deletion is permanent. You cannot update deleted providers. However, you can view and list them.

      Args:
        request: (IamProjectsLocationsWorkloadIdentityPoolsProvidersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/workloadIdentityPools/{workloadIdentityPoolsId}/providers/{providersId}',
        http_method='DELETE',
        method_id='iam.projects.locations.workloadIdentityPools.providers.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='IamProjectsLocationsWorkloadIdentityPoolsProvidersDeleteRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets an individual WorkloadIdentityPoolProvider.

      Args:
        request: (IamProjectsLocationsWorkloadIdentityPoolsProvidersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV1betaWorkloadIdentityPoolProvider) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/workloadIdentityPools/{workloadIdentityPoolsId}/providers/{providersId}',
        http_method='GET',
        method_id='iam.projects.locations.workloadIdentityPools.providers.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='IamProjectsLocationsWorkloadIdentityPoolsProvidersGetRequest',
        response_type_name='GoogleIamV1betaWorkloadIdentityPoolProvider',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all non-deleted WorkloadIdentityPoolProviders in a WorkloadIdentityPool. If `show_deleted` is set to `true`, then deleted providers are also listed.

      Args:
        request: (IamProjectsLocationsWorkloadIdentityPoolsProvidersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV1betaListWorkloadIdentityPoolProvidersResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/workloadIdentityPools/{workloadIdentityPoolsId}/providers',
        http_method='GET',
        method_id='iam.projects.locations.workloadIdentityPools.providers.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken', 'showDeleted'],
        relative_path='v1beta/{+parent}/providers',
        request_field='',
        request_type_name='IamProjectsLocationsWorkloadIdentityPoolsProvidersListRequest',
        response_type_name='GoogleIamV1betaListWorkloadIdentityPoolProvidersResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates an existing WorkloadIdentityPoolProvider.

      Args:
        request: (IamProjectsLocationsWorkloadIdentityPoolsProvidersPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/workloadIdentityPools/{workloadIdentityPoolsId}/providers/{providersId}',
        http_method='PATCH',
        method_id='iam.projects.locations.workloadIdentityPools.providers.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1beta/{+name}',
        request_field='googleIamV1betaWorkloadIdentityPoolProvider',
        request_type_name='IamProjectsLocationsWorkloadIdentityPoolsProvidersPatchRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Undelete(self, request, global_params=None):
      r"""Undeletes a WorkloadIdentityPoolProvider, as long as it was deleted fewer than 30 days ago.

      Args:
        request: (IamProjectsLocationsWorkloadIdentityPoolsProvidersUndeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Undelete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Undelete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/workloadIdentityPools/{workloadIdentityPoolsId}/providers/{providersId}:undelete',
        http_method='POST',
        method_id='iam.projects.locations.workloadIdentityPools.providers.undelete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}:undelete',
        request_field='googleIamV1betaUndeleteWorkloadIdentityPoolProviderRequest',
        request_type_name='IamProjectsLocationsWorkloadIdentityPoolsProvidersUndeleteRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

  class ProjectsLocationsWorkloadIdentityPoolsService(base_api.BaseApiService):
    """Service class for the projects_locations_workloadIdentityPools resource."""

    _NAME = 'projects_locations_workloadIdentityPools'

    def __init__(self, client):
      super(IamV1beta.ProjectsLocationsWorkloadIdentityPoolsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new WorkloadIdentityPool. You cannot reuse the name of a deleted pool until 30 days after deletion.

      Args:
        request: (IamProjectsLocationsWorkloadIdentityPoolsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/workloadIdentityPools',
        http_method='POST',
        method_id='iam.projects.locations.workloadIdentityPools.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['workloadIdentityPoolId'],
        relative_path='v1beta/{+parent}/workloadIdentityPools',
        request_field='googleIamV1betaWorkloadIdentityPool',
        request_type_name='IamProjectsLocationsWorkloadIdentityPoolsCreateRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a WorkloadIdentityPool. You cannot use a deleted pool to exchange external credentials for Google Cloud credentials. However, deletion does not revoke credentials that have already been issued. Credentials issued for a deleted pool do not grant access to resources. If the pool is undeleted, and the credentials are not expired, they grant access again. You can undelete a pool for 30 days. After 30 days, deletion is permanent. You cannot update deleted pools. However, you can view and list them.

      Args:
        request: (IamProjectsLocationsWorkloadIdentityPoolsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/workloadIdentityPools/{workloadIdentityPoolsId}',
        http_method='DELETE',
        method_id='iam.projects.locations.workloadIdentityPools.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='IamProjectsLocationsWorkloadIdentityPoolsDeleteRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets an individual WorkloadIdentityPool.

      Args:
        request: (IamProjectsLocationsWorkloadIdentityPoolsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV1betaWorkloadIdentityPool) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/workloadIdentityPools/{workloadIdentityPoolsId}',
        http_method='GET',
        method_id='iam.projects.locations.workloadIdentityPools.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='IamProjectsLocationsWorkloadIdentityPoolsGetRequest',
        response_type_name='GoogleIamV1betaWorkloadIdentityPool',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all non-deleted WorkloadIdentityPools in a project. If `show_deleted` is set to `true`, then deleted pools are also listed.

      Args:
        request: (IamProjectsLocationsWorkloadIdentityPoolsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV1betaListWorkloadIdentityPoolsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/workloadIdentityPools',
        http_method='GET',
        method_id='iam.projects.locations.workloadIdentityPools.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken', 'showDeleted'],
        relative_path='v1beta/{+parent}/workloadIdentityPools',
        request_field='',
        request_type_name='IamProjectsLocationsWorkloadIdentityPoolsListRequest',
        response_type_name='GoogleIamV1betaListWorkloadIdentityPoolsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates an existing WorkloadIdentityPool.

      Args:
        request: (IamProjectsLocationsWorkloadIdentityPoolsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/workloadIdentityPools/{workloadIdentityPoolsId}',
        http_method='PATCH',
        method_id='iam.projects.locations.workloadIdentityPools.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1beta/{+name}',
        request_field='googleIamV1betaWorkloadIdentityPool',
        request_type_name='IamProjectsLocationsWorkloadIdentityPoolsPatchRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

    def Undelete(self, request, global_params=None):
      r"""Undeletes a WorkloadIdentityPool, as long as it was deleted fewer than 30 days ago.

      Args:
        request: (IamProjectsLocationsWorkloadIdentityPoolsUndeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleLongrunningOperation) The response message.
      """
      config = self.GetMethodConfig('Undelete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Undelete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/workloadIdentityPools/{workloadIdentityPoolsId}:undelete',
        http_method='POST',
        method_id='iam.projects.locations.workloadIdentityPools.undelete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}:undelete',
        request_field='googleIamV1betaUndeleteWorkloadIdentityPoolRequest',
        request_type_name='IamProjectsLocationsWorkloadIdentityPoolsUndeleteRequest',
        response_type_name='GoogleLongrunningOperation',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(IamV1beta.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(IamV1beta.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
