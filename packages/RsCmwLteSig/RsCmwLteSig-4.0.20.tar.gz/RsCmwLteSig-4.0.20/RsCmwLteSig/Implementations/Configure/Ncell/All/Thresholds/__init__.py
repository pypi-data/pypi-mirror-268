from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ThresholdsCls:
	"""Thresholds commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("thresholds", core, parent)

	@property
	def low(self):
		"""low commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_low'):
			from .Low import LowCls
			self._low = LowCls(self._core, self._cmd_group)
		return self._low

	def set(self, valid: bool, high: int, low: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:ALL:THResholds \n
		Snippet: driver.configure.ncell.all.thresholds.set(valid = False, high = 1, low = 1) \n
		No command help available \n
			:param valid: No help available
			:param high: No help available
			:param low: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('valid', valid, DataType.Boolean), ArgSingle('high', high, DataType.Integer), ArgSingle('low', low, DataType.Integer))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:NCELl:ALL:THResholds {param}'.rstrip())

	# noinspection PyTypeChecker
	class ThresholdsStruct(StructBase):
		"""Response structure. Fields: \n
			- Valid: bool: No parameter help available
			- High: int: No parameter help available
			- Low: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Valid'),
			ArgStruct.scalar_int('High'),
			ArgStruct.scalar_int('Low')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Valid: bool = None
			self.High: int = None
			self.Low: int = None

	def get(self) -> ThresholdsStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:NCELl:ALL:THResholds \n
		Snippet: value: ThresholdsStruct = driver.configure.ncell.all.thresholds.get() \n
		No command help available \n
			:return: structure: for return value, see the help for ThresholdsStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:NCELl:ALL:THResholds?', self.__class__.ThresholdsStruct())

	def clone(self) -> 'ThresholdsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ThresholdsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
