from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FoffsetCls:
	"""Foffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("foffset", core, parent)

	def set(self, offset: float, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:AWGN:FOFFset \n
		Snippet: driver.configure.fading.scc.awgn.foffset.set(offset = 1.0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Shifts the center frequency of the noise bandwidth relative to the carrier center frequency. \n
			:param offset: numeric Range: -40 MHz to 40 MHz, Unit: Hz
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(offset)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:AWGN:FOFFset {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:AWGN:FOFFset \n
		Snippet: value: float = driver.configure.fading.scc.awgn.foffset.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Shifts the center frequency of the noise bandwidth relative to the carrier center frequency. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: offset: numeric Range: -40 MHz to 40 MHz, Unit: Hz"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:AWGN:FOFFset?')
		return Conversions.str_to_float(response)
