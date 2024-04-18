from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LanguageCls:
	"""Language commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("language", core, parent)

	def set(self, language: int, lng_indication: str) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:LANGuage \n
		Snippet: driver.configure.cbs.message.language.set(language = 1, lng_indication = 'abc') \n
		Specifies the language of the message for the data source INTernal. The mapping of language codes to language indication
		strings is listed in the table below. If you specify a value pair that does not match, the specified code is used and the
		correct string is set automatically. \n
			:param language: numeric Range: 0 to 15
			:param lng_indication: string Language indication
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('language', language, DataType.Integer), ArgSingle('lng_indication', lng_indication, DataType.String))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:LANGuage {param}'.rstrip())

	# noinspection PyTypeChecker
	class LanguageStruct(StructBase):
		"""Response structure. Fields: \n
			- Language: int: numeric Range: 0 to 15
			- Lng_Indication: str: string Language indication"""
		__meta_args_list = [
			ArgStruct.scalar_int('Language'),
			ArgStruct.scalar_str('Lng_Indication')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Language: int = None
			self.Lng_Indication: str = None

	def get(self) -> LanguageStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:LANGuage \n
		Snippet: value: LanguageStruct = driver.configure.cbs.message.language.get() \n
		Specifies the language of the message for the data source INTernal. The mapping of language codes to language indication
		strings is listed in the table below. If you specify a value pair that does not match, the specified code is used and the
		correct string is set automatically. \n
			:return: structure: for return value, see the help for LanguageStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:LANGuage?', self.__class__.LanguageStruct())
