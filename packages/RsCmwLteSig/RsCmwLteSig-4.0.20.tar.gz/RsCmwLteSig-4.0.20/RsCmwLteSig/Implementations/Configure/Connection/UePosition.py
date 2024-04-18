from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UePositionCls:
	"""UePosition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uePosition", core, parent)

	def reset(self) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UEPosition:RESet \n
		Snippet: driver.configure.connection.uePosition.reset() \n
		No command help available \n
		"""
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:UEPosition:RESet')

	def reset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UEPosition:RESet \n
		Snippet: driver.configure.connection.uePosition.reset_with_opc() \n
		No command help available \n
		Same as reset, but waits for the operation to complete before continuing further. Use the RsCmwLteSig.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:UEPosition:RESet', opc_timeout_ms)
