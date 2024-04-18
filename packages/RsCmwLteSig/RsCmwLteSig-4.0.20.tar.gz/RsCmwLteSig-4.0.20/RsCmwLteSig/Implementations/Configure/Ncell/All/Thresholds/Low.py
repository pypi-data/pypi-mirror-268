from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LowCls:
	"""Low commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("low", core, parent)

	def set(self, valid: bool, low: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:ALL:THResholds:LOW \n
		Snippet: driver.configure.ncell.all.thresholds.low.set(valid = False, low = 1) \n
		Configures a common reselection threshold value 'threshX-Low' applicable to all technologies. Alternatively to a common
		threshold you can also use individual thresholds. They are defined per technology via the commands
		CONFigure:LTE:SIGN<i>:NCELl:<Technology>:THResholds:LOW. The parameter <Valid> selects whether common or individual
		thresholds are used. \n
			:param valid: OFF | ON OFF: use individual thresholds defined by separate commands ON: use common threshold defined by this command
			:param low: numeric Range: 0 to 31
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('valid', valid, DataType.Boolean), ArgSingle('low', low, DataType.Integer))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:NCELl:ALL:THResholds:LOW {param}'.rstrip())

	# noinspection PyTypeChecker
	class LowStruct(StructBase):
		"""Response structure. Fields: \n
			- Valid: bool: OFF | ON OFF: use individual thresholds defined by separate commands ON: use common threshold defined by this command
			- Low: int: numeric Range: 0 to 31"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Valid'),
			ArgStruct.scalar_int('Low')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Valid: bool = None
			self.Low: int = None

	def get(self) -> LowStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:ALL:THResholds:LOW \n
		Snippet: value: LowStruct = driver.configure.ncell.all.thresholds.low.get() \n
		Configures a common reselection threshold value 'threshX-Low' applicable to all technologies. Alternatively to a common
		threshold you can also use individual thresholds. They are defined per technology via the commands
		CONFigure:LTE:SIGN<i>:NCELl:<Technology>:THResholds:LOW. The parameter <Valid> selects whether common or individual
		thresholds are used. \n
			:return: structure: for return value, see the help for LowStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:NCELl:ALL:THResholds:LOW?', self.__class__.LowStruct())
