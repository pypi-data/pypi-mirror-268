from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RstCls:
	"""Rst commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rst", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:HMAT:RST \n
		Snippet: driver.configure.fading.pcc.fadingSimulator.hmat.rst.set() \n
		No command help available \n
		"""
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:HMAT:RST')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:HMAT:RST \n
		Snippet: driver.configure.fading.pcc.fadingSimulator.hmat.rst.set_with_opc() \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwLteSig.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:HMAT:RST', opc_timeout_ms)
