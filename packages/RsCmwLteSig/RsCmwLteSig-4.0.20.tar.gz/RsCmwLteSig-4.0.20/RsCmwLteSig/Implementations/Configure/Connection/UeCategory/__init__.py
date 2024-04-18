from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeCategoryCls:
	"""UeCategory commands group definition. 5 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ueCategory", core, parent)

	@property
	def manual(self):
		"""manual commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_manual'):
			from .Manual import ManualCls
			self._manual = ManualCls(self._core, self._cmd_group)
		return self._manual

	@property
	def reported(self):
		"""reported commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_reported'):
			from .Reported import ReportedCls
			self._reported = ReportedCls(self._core, self._cmd_group)
		return self._reported

	def get_cz_allowed(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UECategory:CZALlowed \n
		Snippet: value: bool = driver.configure.connection.ueCategory.get_cz_allowed() \n
		Specifies whether category 0 UEs are allowed to access the cell. This information is sent to the UE via broadcast in
		system information block 1. \n
			:return: allowed: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:UECategory:CZALlowed?')
		return Conversions.str_to_bool(response)

	def set_cz_allowed(self, allowed: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UECategory:CZALlowed \n
		Snippet: driver.configure.connection.ueCategory.set_cz_allowed(allowed = False) \n
		Specifies whether category 0 UEs are allowed to access the cell. This information is sent to the UE via broadcast in
		system information block 1. \n
			:param allowed: OFF | ON
		"""
		param = Conversions.bool_to_str(allowed)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:UECategory:CZALlowed {param}')

	def clone(self) -> 'UeCategoryCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UeCategoryCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
