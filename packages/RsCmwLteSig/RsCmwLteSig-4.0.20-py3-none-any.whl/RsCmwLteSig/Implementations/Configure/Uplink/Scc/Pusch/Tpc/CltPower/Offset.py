from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OffsetCls:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, offset: float, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PUSCh:TPC:CLTPower:OFFSet \n
		Snippet: driver.configure.uplink.scc.pusch.tpc.cltPower.offset.set(offset = 1.0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines a target power offset relative to the power primary carrier, for power control with the TPC setup CLOop.
		The setting is irrelevant for carriers with independent UL power control. \n
			:param offset: numeric Target power = primary carrier target power + Offset Range: -7 dB to 7 dB, Unit: dB
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(offset)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PUSCh:TPC:CLTPower:OFFSet {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PUSCh:TPC:CLTPower:OFFSet \n
		Snippet: value: float = driver.configure.uplink.scc.pusch.tpc.cltPower.offset.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines a target power offset relative to the power primary carrier, for power control with the TPC setup CLOop.
		The setting is irrelevant for carriers with independent UL power control. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: offset: numeric Target power = primary carrier target power + Offset Range: -7 dB to 7 dB, Unit: dB"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PUSCh:TPC:CLTPower:OFFSet?')
		return Conversions.str_to_float(response)
