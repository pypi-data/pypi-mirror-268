from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NoiseCls:
	"""Noise commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("noise", core, parent)

	@property
	def total(self):
		"""total commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_total'):
			from .Total import TotalCls
			self._total = TotalCls(self._core, self._cmd_group)
		return self._total

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:POWer:NOISe \n
		Snippet: value: float = driver.configure.fading.scc.power.noise.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Queries the calculated noise power on the DL channel, i.e. within the cell bandwidth. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: noise_power: float Unit: dBm"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:POWer:NOISe?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'NoiseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NoiseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
