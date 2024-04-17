try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class EntityScoresOperations(object):
	def __init__(self, fields=None):
		"""
		Creates an instance of EntityScoresOperations with the given parameters

		Parameters:
			fields (string) : A string representing the fields
		"""

		if fields is not None and not isinstance(fields, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: fields EXPECTED TYPE: str', None, None)
		
		self.__fields = fields


	def get_module(self, record_id, module):
		"""
		The method to get module

		Parameters:
			record_id (int) : An int representing the record_id
			module (string) : A string representing the module

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if not isinstance(module, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module EXPECTED TYPE: str', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v5/'
		api_path = api_path + str(module)
		api_path = api_path + '/'
		api_path = api_path + str(record_id)
		api_path = api_path + '/Entity_Scores__s'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('fields', 'com.zoho.crm.api.EntityScores.GetModuleParam'), self.__fields)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.entity_scores.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def get_modules(self):
		"""
		The method to get modules

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v5/Entity_Scores__s'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.add_param(Param('fields', 'com.zoho.crm.api.EntityScores.GetModulesParam'), self.__fields)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.entity_scores.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class GetModuleParam(object):
	pass


class GetModulesParam(object):
	pass
