from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ThresholdsCls:
	"""Thresholds commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("thresholds", core, parent)

	def set(self, high: int, low: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:EVDO:THResholds \n
		Snippet: driver.configure.ncell.evdo.thresholds.set(high = 1, low = 1) \n
		No command help available \n
			:param high: No help available
			:param low: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('high', high, DataType.Integer), ArgSingle('low', low, DataType.Integer))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:NCELl:EVDO:THResholds {param}'.rstrip())

	# noinspection PyTypeChecker
	class ThresholdsStruct(StructBase):
		"""Response structure. Fields: \n
			- High: int: No parameter help available
			- Low: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('High'),
			ArgStruct.scalar_int('Low')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.High: int = None
			self.Low: int = None

	def get(self) -> ThresholdsStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:EVDO:THResholds \n
		Snippet: value: ThresholdsStruct = driver.configure.ncell.evdo.thresholds.get() \n
		No command help available \n
			:return: structure: for return value, see the help for ThresholdsStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:NCELl:EVDO:THResholds?', self.__class__.ThresholdsStruct())

	def get_low(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:EVDO:THResholds:LOW \n
		Snippet: value: int = driver.configure.ncell.evdo.thresholds.get_low() \n
		Configures the reselection threshold value 'threshX-Low' for 1xEV-DO neighbor cells. \n
			:return: low: numeric Range: 0 to 63
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:NCELl:EVDO:THResholds:LOW?')
		return Conversions.str_to_int(response)

	def set_low(self, low: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:EVDO:THResholds:LOW \n
		Snippet: driver.configure.ncell.evdo.thresholds.set_low(low = 1) \n
		Configures the reselection threshold value 'threshX-Low' for 1xEV-DO neighbor cells. \n
			:param low: numeric Range: 0 to 63
		"""
		param = Conversions.decimal_value_to_str(low)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:NCELl:EVDO:THResholds:LOW {param}')
