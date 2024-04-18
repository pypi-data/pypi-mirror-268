from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApPowerCls:
	"""ApPower commands group definition. 8 total commands, 5 Subgroups, 3 group commands"""

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

	def get_pathloss(self) -> float:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UL:SETA:APPower:PATHloss \n
		Snippet: value: float = driver.sense.uplink.seta.apPower.get_pathloss() \n
		Queries the pathloss resulting from the advanced UL power settings. \n
			:return: pathloss: float Unit: dB
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UL:SETA:APPower:PATHloss?')
		return Conversions.str_to_float(response)

	def get_epp_power(self) -> float:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UL:SETA:APPower:EPPPower \n
		Snippet: value: float = driver.sense.uplink.seta.apPower.get_epp_power() \n
		Queries the expected power of the first preamble, resulting from the advanced UL power settings. \n
			:return: power: float Unit: dBm
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UL:SETA:APPower:EPPPower?')
		return Conversions.str_to_float(response)

	def get_eo_power(self) -> float:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UL:SETA:APPower:EOPower \n
		Snippet: value: float = driver.sense.uplink.seta.apPower.get_eo_power() \n
		Queries the expected initial PUSCH power, resulting from the advanced UL power settings. \n
			:return: expected_ol_power: float Unit: dBm
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UL:SETA:APPower:EOPower?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'ApPowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ApPowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
