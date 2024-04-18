from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PcidCls:
	"""Pcid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcid", core, parent)

	def set(self, idn: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<Carrier>:PCID \n
		Snippet: driver.configure.cell.scc.pcid.set(idn = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines the physical cell ID used for generation of the DL physical synchronization signals.
		If you use carrier aggregation, configure different values for the component carriers. \n
			:param idn: decimal Range: 0 to 503
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(idn)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:PCID {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<Carrier>:PCID \n
		Snippet: value: int = driver.configure.cell.scc.pcid.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines the physical cell ID used for generation of the DL physical synchronization signals.
		If you use carrier aggregation, configure different values for the component carriers. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: idn: decimal Range: 0 to 503"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:PCID?')
		return Conversions.str_to_int(response)
