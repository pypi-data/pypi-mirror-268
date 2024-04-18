from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ReSelectionCls:
	"""ReSelection commands group definition. 4 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reSelection", core, parent)

	@property
	def search(self):
		"""search commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_search'):
			from .Search import SearchCls
			self._search = SearchCls(self._core, self._cmd_group)
		return self._search

	@property
	def quality(self):
		"""quality commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_quality'):
			from .Quality import QualityCls
			self._quality = QualityCls(self._core, self._cmd_group)
		return self._quality

	def get_tslow(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:RESelection:TSLow \n
		Snippet: value: float = driver.configure.cell.reSelection.get_tslow() \n
		Defines ThreshServing,Low. The value divided by 2 is broadcasted to the UE in SIB3. \n
			:return: value: numeric Range: 0 dB to 62 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:RESelection:TSLow?')
		return Conversions.str_to_float(response)

	def set_tslow(self, value: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:RESelection:TSLow \n
		Snippet: driver.configure.cell.reSelection.set_tslow(value = 1.0) \n
		Defines ThreshServing,Low. The value divided by 2 is broadcasted to the UE in SIB3. \n
			:param value: numeric Range: 0 dB to 62 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:RESelection:TSLow {param}')

	def clone(self) -> 'ReSelectionCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ReSelectionCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
