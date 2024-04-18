from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DshiftCls:
	"""Dshift commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dshift", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import ModeCls
			self._mode = ModeCls(self._core, self._cmd_group)
		return self._mode

	def set(self, frequency: float, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:DSHift \n
		Snippet: driver.configure.fading.scc.fadingSimulator.dshift.set(frequency = 1.0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Sets the maximum Doppler frequency for the fading simulator. A setting is only allowed in USER mode (see method
		RsCmwLteSig.Configure.Fading.Pcc.FadingSimulator.Dshift.mode) . \n
			:param frequency: numeric Range: 1 Hz to 2000 Hz, Unit: Hz
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:DSHift {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:DSHift \n
		Snippet: value: float = driver.configure.fading.scc.fadingSimulator.dshift.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Sets the maximum Doppler frequency for the fading simulator. A setting is only allowed in USER mode (see method
		RsCmwLteSig.Configure.Fading.Pcc.FadingSimulator.Dshift.mode) . \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: frequency: numeric Range: 1 Hz to 2000 Hz, Unit: Hz"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:DSHift?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'DshiftCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DshiftCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
