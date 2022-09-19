"""Generated client library for config version v1alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.config.v1alpha1 import config_v1alpha1_messages as messages


class ConfigV1alpha1(base_api.BaseApiClient):
  """Generated client library for service config version v1alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://config.googleapis.com/'
  MTLS_BASE_URL = 'https://config.mtls.googleapis.com/'

  _PACKAGE = 'config'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1alpha1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'ConfigV1alpha1'
  _URL_VERSION = 'v1alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new config handle."""
    url = url or self.BASE_URL
    super(ConfigV1alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_deployments_revisions = self.ProjectsLocationsDeploymentsRevisionsService(self)
    self.projects_locations_deployments = self.ProjectsLocationsDeploymentsService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations_previews = self.ProjectsLocationsPreviewsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsDeploymentsRevisionsService(base_api.BaseApiService):
    """Service class for the projects_locations_deployments_revisions resource."""

    _NAME = 'projects_locations_deployments_revisions'

    def __init__(self, client):
      super(ConfigV1alpha1.ProjectsLocationsDeploymentsRevisionsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets details of a single Deployment.

      Args:
        request: (ConfigProjectsLocationsDeploymentsRevisionsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Revision) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/deployments/{deploymentsId}/revisions/{revisionsId}',
        http_method='GET',
        method_id='config.projects.locations.deployments.revisions.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='ConfigProjectsLocationsDeploymentsRevisionsGetRequest',
        response_type_name='Revision',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Deployments in a given project and location.

      Args:
        request: (ConfigProjectsLocationsDeploymentsRevisionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListRevisionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/deployments/{deploymentsId}/revisions',
        http_method='GET',
        method_id='config.projects.locations.deployments.revisions.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha1/{+parent}/revisions',
        request_field='',
        request_type_name='ConfigProjectsLocationsDeploymentsRevisionsListRequest',
        response_type_name='ListRevisionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsDeploymentsService(base_api.BaseApiService):
    """Service class for the projects_locations_deployments resource."""

    _NAME = 'projects_locations_deployments'

    def __init__(self, client):
      super(ConfigV1alpha1.ProjectsLocationsDeploymentsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new Deployment in a given project and location.

      Args:
        request: (ConfigProjectsLocationsDeploymentsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/deployments',
        http_method='POST',
        method_id='config.projects.locations.deployments.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['deploymentId', 'requestId'],
        relative_path='v1alpha1/{+parent}/deployments',
        request_field='deployment',
        request_type_name='ConfigProjectsLocationsDeploymentsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single Deployment.

      Args:
        request: (ConfigProjectsLocationsDeploymentsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/deployments/{deploymentsId}',
        http_method='DELETE',
        method_id='config.projects.locations.deployments.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['force', 'requestId'],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='ConfigProjectsLocationsDeploymentsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single Deployment.

      Args:
        request: (ConfigProjectsLocationsDeploymentsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Deployment) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/deployments/{deploymentsId}',
        http_method='GET',
        method_id='config.projects.locations.deployments.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='ConfigProjectsLocationsDeploymentsGetRequest',
        response_type_name='Deployment',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

      Args:
        request: (ConfigProjectsLocationsDeploymentsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/deployments/{deploymentsId}:getIamPolicy',
        http_method='GET',
        method_id='config.projects.locations.deployments.getIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=['options_requestedPolicyVersion'],
        relative_path='v1alpha1/{+resource}:getIamPolicy',
        request_field='',
        request_type_name='ConfigProjectsLocationsDeploymentsGetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Deployments in a given project and location.

      Args:
        request: (ConfigProjectsLocationsDeploymentsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListDeploymentsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/deployments',
        http_method='GET',
        method_id='config.projects.locations.deployments.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha1/{+parent}/deployments',
        request_field='',
        request_type_name='ConfigProjectsLocationsDeploymentsListRequest',
        response_type_name='ListDeploymentsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the parameters of a single Deployment.

      Args:
        request: (ConfigProjectsLocationsDeploymentsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/deployments/{deploymentsId}',
        http_method='PATCH',
        method_id='config.projects.locations.deployments.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId', 'updateMask'],
        relative_path='v1alpha1/{+name}',
        request_field='deployment',
        request_type_name='ConfigProjectsLocationsDeploymentsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

      Args:
        request: (ConfigProjectsLocationsDeploymentsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/deployments/{deploymentsId}:setIamPolicy',
        http_method='POST',
        method_id='config.projects.locations.deployments.setIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1alpha1/{+resource}:setIamPolicy',
        request_field='setIamPolicyRequest',
        request_type_name='ConfigProjectsLocationsDeploymentsSetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

      Args:
        request: (ConfigProjectsLocationsDeploymentsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/deployments/{deploymentsId}:testIamPermissions',
        http_method='POST',
        method_id='config.projects.locations.deployments.testIamPermissions',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1alpha1/{+resource}:testIamPermissions',
        request_field='testIamPermissionsRequest',
        request_type_name='ConfigProjectsLocationsDeploymentsTestIamPermissionsRequest',
        response_type_name='TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(ConfigV1alpha1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

      Args:
        request: (ConfigProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='config.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='ConfigProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (ConfigProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='config.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='ConfigProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (ConfigProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='config.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='ConfigProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. NOTE: the `name` binding allows API services to override the binding to use different resource name schemes, such as `users/*/operations`. To override the binding, API services can add a binding such as `"/v1/{name=users/*}/operations"` to their service configuration. For backwards compatibility, the default name includes the operations collection id, however overriding users must ensure the name binding is the parent resource, without the operations collection id.

      Args:
        request: (ConfigProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='config.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha1/{+name}/operations',
        request_field='',
        request_type_name='ConfigProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsPreviewsService(base_api.BaseApiService):
    """Service class for the projects_locations_previews resource."""

    _NAME = 'projects_locations_previews'

    def __init__(self, client):
      super(ConfigV1alpha1.ProjectsLocationsPreviewsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new Preview in a given project and location.

      Args:
        request: (ConfigProjectsLocationsPreviewsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/previews',
        http_method='POST',
        method_id='config.projects.locations.previews.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['requestId'],
        relative_path='v1alpha1/{+parent}/previews',
        request_field='preview',
        request_type_name='ConfigProjectsLocationsPreviewsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(ConfigV1alpha1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (ConfigProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='config.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='ConfigProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (ConfigProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations',
        http_method='GET',
        method_id='config.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha1/{+name}/locations',
        request_field='',
        request_type_name='ConfigProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(ConfigV1alpha1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
