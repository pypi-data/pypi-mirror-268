from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PexecuteCls:
	"""Pexecute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pexecute", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETC:PUSCh:TPC:PEXecute \n
		Snippet: driver.configure.uplink.setc.pusch.tpc.pexecute.set() \n
		Execute the active TPC setup for power control of the PUSCH. This command is only relevant for setups which are not
		executed automatically (SINGle, UDSingle, RPControl, FULPower) . \n
		"""
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SETC:PUSCh:TPC:PEXecute')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SETC:PUSCh:TPC:PEXecute \n
		Snippet: driver.configure.uplink.setc.pusch.tpc.pexecute.set_with_opc() \n
		Execute the active TPC setup for power control of the PUSCH. This command is only relevant for setups which are not
		executed automatically (SINGle, UDSingle, RPControl, FULPower) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwLteSig.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:UL:SETC:PUSCh:TPC:PEXecute', opc_timeout_ms)
