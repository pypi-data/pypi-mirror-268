from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SnRatioCls:
	"""SnRatio commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("snRatio", core, parent)

	def set(self, ratio: float, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:AWGN:SNRatio \n
		Snippet: driver.configure.fading.scc.awgn.snRatio.set(ratio = 1.0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the signal to noise ratio for the AWGN inserted on the internal fading module. \n
			:param ratio: numeric Range: -50 dB to 40 dB, Unit: dB
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(ratio)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:AWGN:SNRatio {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:AWGN:SNRatio \n
		Snippet: value: float = driver.configure.fading.scc.awgn.snRatio.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the signal to noise ratio for the AWGN inserted on the internal fading module. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: ratio: numeric Range: -50 dB to 40 dB, Unit: dB"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:AWGN:SNRatio?')
		return Conversions.str_to_float(response)
