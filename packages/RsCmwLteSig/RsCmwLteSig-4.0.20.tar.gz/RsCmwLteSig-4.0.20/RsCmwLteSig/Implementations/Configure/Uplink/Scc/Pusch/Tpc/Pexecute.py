from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PexecuteCls:
	"""Pexecute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pexecute", core, parent)

	def set(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PUSCh:TPC:PEXecute \n
		Snippet: driver.configure.uplink.scc.pusch.tpc.pexecute.set(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Execute the active TPC setup for power control of the PUSCH. This command is only relevant for setups which are not
		executed automatically (SINGle, UDSingle, RPControl, FULPower) . \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PUSCh:TPC:PEXecute')

	def set_with_opc(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, opc_timeout_ms: int = -1) -> None:
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PUSCh:TPC:PEXecute \n
		Snippet: driver.configure.uplink.scc.pusch.tpc.pexecute.set_with_opc(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Execute the active TPC setup for power control of the PUSCH. This command is only relevant for setups which are not
		executed automatically (SINGle, UDSingle, RPControl, FULPower) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwLteSig.utilities.opc_timeout_set() to set the timeout value. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PUSCh:TPC:PEXecute', opc_timeout_ms)
