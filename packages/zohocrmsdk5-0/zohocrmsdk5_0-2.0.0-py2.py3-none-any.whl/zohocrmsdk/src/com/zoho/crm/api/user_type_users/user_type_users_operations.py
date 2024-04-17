try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class UserTypeUsersOperations(object):
	def __init__(self):
		"""Creates an instance of UserTypeUsersOperations"""
		pass

	def get_users_of_user_type(self, user_type_id, portal_name, param_instance=None):
		"""
		The method to get users of user type

		Parameters:
			user_type_id (int) : An int representing the user_type_id
			portal_name (string) : A string representing the portal_name
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

		if not isinstance(user_type_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: user_type_id EXPECTED TYPE: int', None, None)
		
		if not isinstance(portal_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: portal_name EXPECTED TYPE: str', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v5/settings/portals/'
		api_path = api_path + str(portal_name)
		api_path = api_path + '/user_type/'
		api_path = api_path + str(user_type_id)
		api_path = api_path + '/users'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.user_type_users.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class GetUsersofUserTypeParam(object):
	filters = Param('filters', 'com.zoho.crm.api.UserTypeUsers.GetUsersofUserTypeParam')
	type = Param('type', 'com.zoho.crm.api.UserTypeUsers.GetUsersofUserTypeParam')
