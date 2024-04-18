from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApPowerCls:
	"""ApPower commands group definition. 6 total commands, 5 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apPower", core, parent)

	@property
	def rsPower(self):
		"""rsPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rsPower'):
			from .RsPower import RsPowerCls
			self._rsPower = RsPowerCls(self._core, self._cmd_group)
		return self._rsPower

	@property
	def pirPower(self):
		"""pirPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pirPower'):
			from .PirPower import PirPowerCls
			self._pirPower = PirPowerCls(self._core, self._cmd_group)
		return self._pirPower

	@property
	def pnpusch(self):
		"""pnpusch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pnpusch'):
			from .Pnpusch import PnpuschCls
			self._pnpusch = PnpuschCls(self._core, self._cmd_group)
		return self._pnpusch

	@property
	def pcAlpha(self):
		"""pcAlpha commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcAlpha'):
			from .PcAlpha import PcAlphaCls
			self._pcAlpha = PcAlphaCls(self._core, self._cmd_group)
		return self._pcAlpha

	@property
	def tprrcSetup(self):
		"""tprrcSetup commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tprrcSetup'):
			from .TprrcSetup import TprrcSetupCls
			self._tprrcSetup = TprrcSetupCls(self._core, self._cmd_group)
		return self._tprrcSetup

	def get_ea_settings(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETB:APPower:EASettings \n
		Snippet: value: bool = driver.configure.uplink.setb.apPower.get_ea_settings() \n
		Enables or disables advanced configuration of the PRACH and open loop power settings via the other
		CONFigure:LTE:SIGN:UL:PCC/SCC<c>:APPower:... commands. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UL:SETB:APPower:EASettings?')
		return Conversions.str_to_bool(response)

	def set_ea_settings(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETB:APPower:EASettings \n
		Snippet: driver.configure.uplink.setb.apPower.set_ea_settings(enable = False) \n
		Enables or disables advanced configuration of the PRACH and open loop power settings via the other
		CONFigure:LTE:SIGN:UL:PCC/SCC<c>:APPower:... commands. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SETB:APPower:EASettings {param}')

	def clone(self) -> 'ApPowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ApPowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
