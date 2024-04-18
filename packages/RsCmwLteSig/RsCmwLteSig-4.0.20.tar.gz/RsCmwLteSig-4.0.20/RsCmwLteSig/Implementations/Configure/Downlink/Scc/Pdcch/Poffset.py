from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PoffsetCls:
	"""Poffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("poffset", core, parent)

	def set(self, offset: float, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL:SCC<Carrier>:PDCCh:POFFset \n
		Snippet: driver.configure.downlink.scc.pdcch.poffset.set(offset = 1.0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines the power level of a physical downlink control channel (PDCCH) resource element. \n
			:param offset: numeric PDCCH power relative to RS EPRE Range: -30 dB to 0 dB, Unit: dB
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(offset)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:DL:SCC{secondaryCompCarrier_cmd_val}:PDCCh:POFFset {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL:SCC<Carrier>:PDCCh:POFFset \n
		Snippet: value: float = driver.configure.downlink.scc.pdcch.poffset.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines the power level of a physical downlink control channel (PDCCH) resource element. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: offset: numeric PDCCH power relative to RS EPRE Range: -30 dB to 0 dB, Unit: dB"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:DL:SCC{secondaryCompCarrier_cmd_val}:PDCCh:POFFset?')
		return Conversions.str_to_float(response)
