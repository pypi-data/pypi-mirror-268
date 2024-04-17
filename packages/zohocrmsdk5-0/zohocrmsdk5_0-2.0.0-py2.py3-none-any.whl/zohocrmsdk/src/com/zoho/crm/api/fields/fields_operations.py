try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants
	from ..param import Param


class FieldsOperations(object):
	def __init__(self):
		"""Creates an instance of FieldsOperations"""
		pass

	def get_fields(self, param_instance=None):
		"""
		The method to get fields

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
		api_path = api_path + '/crm/v5/settings/fields'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def get_field(self, field, param_instance=None):
		"""
		The method to get field

		Parameters:
			field (int) : An int representing the field
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

		if not isinstance(field, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: field EXPECTED TYPE: int', None, None)
		
		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v5/settings/fields/'
		api_path = api_path + str(field)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.fields.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class GetFieldsParam(object):
	module = Param('module', 'com.zoho.crm.api.Fields.GetFieldsParam')
	data_type = Param('data_type', 'com.zoho.crm.api.Fields.GetFieldsParam')
	type = Param('type', 'com.zoho.crm.api.Fields.GetFieldsParam')
	include = Param('include', 'com.zoho.crm.api.Fields.GetFieldsParam')
	feature_name = Param('feature_name', 'com.zoho.crm.api.Fields.GetFieldsParam')
	component = Param('component', 'com.zoho.crm.api.Fields.GetFieldsParam')
	layout_id = Param('layout_id', 'com.zoho.crm.api.Fields.GetFieldsParam')


class GetFieldParam(object):
	module = Param('module', 'com.zoho.crm.api.Fields.GetFieldParam')
	include = Param('include', 'com.zoho.crm.api.Fields.GetFieldParam')
