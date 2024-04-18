from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DcSchemeCls:
	"""DcScheme commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dcScheme", core, parent)

	def set(self, coding_group: int, language: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:DCSCheme \n
		Snippet: driver.configure.cbs.message.dcScheme.set(coding_group = 1, language = 1) \n
		No command help available \n
			:param coding_group: No help available
			:param language: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('coding_group', coding_group, DataType.Integer), ArgSingle('language', language, DataType.Integer))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:DCSCheme {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Coding_Group: int: No parameter help available
			- Language: int: No parameter help available
			- Lng_Indication: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Coding_Group'),
			ArgStruct.scalar_int('Language'),
			ArgStruct.scalar_str('Lng_Indication')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Coding_Group: int = None
			self.Language: int = None
			self.Lng_Indication: str = None

	def get(self) -> GetStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:DCSCheme \n
		Snippet: value: GetStruct = driver.configure.cbs.message.dcScheme.get() \n
		No command help available \n
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:DCSCheme?', self.__class__.GetStruct())

	def get_ucoded(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:DCSCheme:UCODed \n
		Snippet: value: float = driver.configure.cbs.message.dcScheme.get_ucoded() \n
		Defines the data coding scheme octet for the data source UCODed. \n
			:return: dcoding_scheme: hex Range: #H0 to #HFF
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:DCSCheme:UCODed?')
		return Conversions.str_to_float(response)

	def set_ucoded(self, dcoding_scheme: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CBS:MESSage:DCSCheme:UCODed \n
		Snippet: driver.configure.cbs.message.dcScheme.set_ucoded(dcoding_scheme = 1.0) \n
		Defines the data coding scheme octet for the data source UCODed. \n
			:param dcoding_scheme: hex Range: #H0 to #HFF
		"""
		param = Conversions.decimal_value_to_str(dcoding_scheme)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CBS:MESSage:DCSCheme:UCODed {param}')
