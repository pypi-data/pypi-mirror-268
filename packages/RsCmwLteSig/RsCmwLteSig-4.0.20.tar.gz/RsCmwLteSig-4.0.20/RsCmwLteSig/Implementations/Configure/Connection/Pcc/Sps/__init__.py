from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpsCls:
	"""Sps commands group definition. 5 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sps", core, parent)

	@property
	def sinterval(self):
		"""sinterval commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sinterval'):
			from .Sinterval import SintervalCls
			self._sinterval = SintervalCls(self._core, self._cmd_group)
		return self._sinterval

	@property
	def downlink(self):
		"""downlink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_downlink'):
			from .Downlink import DownlinkCls
			self._downlink = DownlinkCls(self._core, self._cmd_group)
		return self._downlink

	@property
	def uplink(self):
		"""uplink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import UplinkCls
			self._uplink = UplinkCls(self._core, self._cmd_group)
		return self._uplink

	def get_ti_config(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:SPS:TIConfig \n
		Snippet: value: bool = driver.configure.connection.pcc.sps.get_ti_config() \n
		Configures the parameter 'twoIntervalsConfig', signaled to the UE for the scheduling type SPS in TDD mode. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:SPS:TIConfig?')
		return Conversions.str_to_bool(response)

	def set_ti_config(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:SPS:TIConfig \n
		Snippet: driver.configure.connection.pcc.sps.set_ti_config(enable = False) \n
		Configures the parameter 'twoIntervalsConfig', signaled to the UE for the scheduling type SPS in TDD mode. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:SPS:TIConfig {param}')

	def clone(self) -> 'SpsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SpsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
