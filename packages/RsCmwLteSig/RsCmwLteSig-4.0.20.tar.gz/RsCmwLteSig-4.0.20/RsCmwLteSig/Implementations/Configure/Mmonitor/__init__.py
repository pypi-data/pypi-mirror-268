from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MmonitorCls:
	"""Mmonitor commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mmonitor", core, parent)

	@property
	def ipAddress(self):
		"""ipAddress commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipAddress'):
			from .IpAddress import IpAddressCls
			self._ipAddress = IpAddressCls(self._core, self._cmd_group)
		return self._ipAddress

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:MMONitor:ENABle \n
		Snippet: value: bool = driver.configure.mmonitor.get_enable() \n
		Enables or disables message monitoring for the LTE signaling application. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:MMONitor:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:MMONitor:ENABle \n
		Snippet: driver.configure.mmonitor.set_enable(enable = False) \n
		Enables or disables message monitoring for the LTE signaling application. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:MMONitor:ENABle {param}')

	def clone(self) -> 'MmonitorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MmonitorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
