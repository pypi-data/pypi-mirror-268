try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ComposeSettings(object):
	def __init__(self):
		"""Creates an instance of ComposeSettings"""

		self.__default_from_address = None
		self.__font_size = None
		self.__font_family = None
		self.__email_signatures = None
		self.__key_modified = dict()

	def get_default_from_address(self):
		"""
		The method to get the default_from_address

		Returns:
			DefaultForm: An instance of DefaultForm
		"""

		return self.__default_from_address

	def set_default_from_address(self, default_from_address):
		"""
		The method to set the value to default_from_address

		Parameters:
			default_from_address (DefaultForm) : An instance of DefaultForm
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.email_compose_meta.default_form import DefaultForm
		except Exception:
			from .default_form import DefaultForm

		if default_from_address is not None and not isinstance(default_from_address, DefaultForm):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: default_from_address EXPECTED TYPE: DefaultForm', None, None)
		
		self.__default_from_address = default_from_address
		self.__key_modified['default_from_address'] = 1

	def get_font_size(self):
		"""
		The method to get the font_size

		Returns:
			int: An int representing the font_size
		"""

		return self.__font_size

	def set_font_size(self, font_size):
		"""
		The method to set the value to font_size

		Parameters:
			font_size (int) : An int representing the font_size
		"""

		if font_size is not None and not isinstance(font_size, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: font_size EXPECTED TYPE: int', None, None)
		
		self.__font_size = font_size
		self.__key_modified['font_size'] = 1

	def get_font_family(self):
		"""
		The method to get the font_family

		Returns:
			string: A string representing the font_family
		"""

		return self.__font_family

	def set_font_family(self, font_family):
		"""
		The method to set the value to font_family

		Parameters:
			font_family (string) : A string representing the font_family
		"""

		if font_family is not None and not isinstance(font_family, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: font_family EXPECTED TYPE: str', None, None)
		
		self.__font_family = font_family
		self.__key_modified['font_family'] = 1

	def get_email_signatures(self):
		"""
		The method to get the email_signatures

		Returns:
			list: An instance of list
		"""

		return self.__email_signatures

	def set_email_signatures(self, email_signatures):
		"""
		The method to set the value to email_signatures

		Parameters:
			email_signatures (list) : An instance of list
		"""

		if email_signatures is not None and not isinstance(email_signatures, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email_signatures EXPECTED TYPE: list', None, None)
		
		self.__email_signatures = email_signatures
		self.__key_modified['email_signatures'] = 1

	def is_key_modified(self, key):
		"""
		The method to check if the user has modified the given key

		Parameters:
			key (string) : A string representing the key

		Returns:
			int: An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if key in self.__key_modified:
			return self.__key_modified.get(key)
		
		return None

	def set_key_modified(self, key, modification):
		"""
		The method to mark the given key as modified

		Parameters:
			key (string) : A string representing the key
			modification (int) : An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if modification is not None and not isinstance(modification, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modification EXPECTED TYPE: int', None, None)
		
		self.__key_modified[key] = modification
