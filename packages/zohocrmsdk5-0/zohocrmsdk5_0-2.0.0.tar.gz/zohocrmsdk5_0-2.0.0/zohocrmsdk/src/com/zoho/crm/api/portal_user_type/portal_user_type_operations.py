try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class PortalUserTypeOperations(object):
	def __init__(self, portal):
		"""
		Creates an instance of PortalUserTypeOperations with the given parameters

		Parameters:
			portal (string) : A string representing the portal
		"""

		if not isinstance(portal, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: portal EXPECTED TYPE: str', None, None)
		
		self.__portal = portal


	def get_user_types(self, param_instance=None):
		"""
		The method to get user types

		Parameters:
			param_instance (ParameterMap) : An instance of ParameterMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
		except Exception:
			from ..parameter_map import ParameterMap

		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v5/settings/portals/'
		api_path = api_path + str(self.__portal)
		api_path = api_path + '/user_type'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.portal_user_type.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def get_user_type(self, user_type_id):
		"""
		The method to get user type

		Parameters:
			user_type_id (string) : A string representing the user_type_id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(user_type_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user_type_id EXPECTED TYPE: str', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v5/settings/portals/'
		api_path = api_path + str(self.__portal)
		api_path = api_path + '/user_type/'
		api_path = api_path + str(user_type_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.portal_user_type.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class GetUserTypesParam(object):
	include = Param('include', 'com.zoho.crm.api.PortalUserType.GetUserTypesParam')
