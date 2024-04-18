from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SeedCls:
	"""Seed commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("seed", core, parent)

	def set(self, seed: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:GLOBal:SEED \n
		Snippet: driver.configure.fading.scc.fadingSimulator.globale.seed.set(seed = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Sets the start seed for the pseudo-random fading algorithm. \n
			:param seed: numeric Range: 0 to 9
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(seed)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:GLOBal:SEED {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:GLOBal:SEED \n
		Snippet: value: int = driver.configure.fading.scc.fadingSimulator.globale.seed.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Sets the start seed for the pseudo-random fading algorithm. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: seed: numeric Range: 0 to 9"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:GLOBal:SEED?')
		return Conversions.str_to_int(response)
