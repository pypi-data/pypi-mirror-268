from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CexecuteCls:
	"""Cexecute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cexecute", core, parent)

	def set(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:CEXecute \n
		Snippet: driver.configure.connection.scc.cexecute.set(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Copies PCC DL settings to the SCC number <c>. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:CEXecute')

	def set_with_opc(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, opc_timeout_ms: int = -1) -> None:
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:CEXecute \n
		Snippet: driver.configure.connection.scc.cexecute.set_with_opc(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Copies PCC DL settings to the SCC number <c>. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwLteSig.utilities.opc_timeout_set() to set the timeout value. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:CEXecute', opc_timeout_ms)
