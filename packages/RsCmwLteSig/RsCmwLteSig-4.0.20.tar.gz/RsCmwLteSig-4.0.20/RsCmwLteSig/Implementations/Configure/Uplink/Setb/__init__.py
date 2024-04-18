from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SetbCls:
	"""Setb commands group definition. 17 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setb", core, parent)

	@property
	def pusch(self):
		"""pusch commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_pusch'):
			from .Pusch import PuschCls
			self._pusch = PuschCls(self._core, self._cmd_group)
		return self._pusch

	@property
	def apPower(self):
		"""apPower commands group. 5 Sub-classes, 1 commands."""
		if not hasattr(self, '_apPower'):
			from .ApPower import ApPowerCls
			self._apPower = ApPowerCls(self._core, self._cmd_group)
		return self._apPower

	@property
	def pucch(self):
		"""pucch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pucch'):
			from .Pucch import PucchCls
			self._pucch = PucchCls(self._core, self._cmd_group)
		return self._pucch

	def get_pmax(self) -> float or bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETB:PMAX \n
		Snippet: value: float or bool = driver.configure.uplink.setb.get_pmax() \n
		Specifies the maximum allowed UE power. \n
			:return: power: (float or boolean) numeric | ON | OFF Range: -30 dBm to 33 dBm, Unit: dBm ON | OFF enables or disables signaling of the value to the UE.
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UL:SETB:PMAX?')
		return Conversions.str_to_float_or_bool(response)

	def set_pmax(self, power: float or bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETB:PMAX \n
		Snippet: driver.configure.uplink.setb.set_pmax(power = 1.0) \n
		Specifies the maximum allowed UE power. \n
			:param power: (float or boolean) numeric | ON | OFF Range: -30 dBm to 33 dBm, Unit: dBm ON | OFF enables or disables signaling of the value to the UE.
		"""
		param = Conversions.decimal_or_bool_value_to_str(power)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SETB:PMAX {param}')

	def clone(self) -> 'SetbCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SetbCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
