try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants


class CurrenciesOperations(object):
	def __init__(self):
		"""Creates an instance of CurrenciesOperations"""
		pass

	def get_currencies(self):
		"""
		The method to get currencies

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v5/org/currencies'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.currencies.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def create_currencies(self, request):
		"""
		The method to create currencies

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.currencies.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v5/org/currencies'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_CREATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.currencies.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def update_currencies(self, request):
		"""
		The method to update currencies

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.currencies.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v5/org/currencies'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.currencies.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def get_currency(self, currency):
		"""
		The method to get currency

		Parameters:
			currency (int) : An int representing the currency

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(currency, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: currency EXPECTED TYPE: int', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v5/org/currencies/'
		api_path = api_path + str(currency)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.currencies.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def update_currency(self, currency, request):
		"""
		The method to update currency

		Parameters:
			currency (int) : An int representing the currency
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.currencies.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if not isinstance(currency, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: currency EXPECTED TYPE: int', None, None)
		
		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v5/org/currencies/'
		api_path = api_path + str(currency)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_UPDATE)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		handler_instance.set_mandatory_checker(True)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.currencies.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def enable_currency(self, request):
		"""
		The method to enable currency

		Parameters:
			request (BaseCurrencyWrapper) : An instance of BaseCurrencyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.currencies.base_currency_wrapper import BaseCurrencyWrapper
		except Exception:
			from .base_currency_wrapper import BaseCurrencyWrapper

		if request is not None and not isinstance(request, BaseCurrencyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BaseCurrencyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v5/org/currencies/actions/enable'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_ACTION)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.currencies.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')

	def update_base_currency(self, request):
		"""
		The method to update base currency

		Parameters:
			request (BaseCurrencyWrapper) : An instance of BaseCurrencyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.currencies.base_currency_wrapper import BaseCurrencyWrapper
		except Exception:
			from .base_currency_wrapper import BaseCurrencyWrapper

		if request is not None and not isinstance(request, BaseCurrencyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BaseCurrencyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v5/org/currencies/actions/enable'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_PUT)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_ACTION)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.currencies.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')
