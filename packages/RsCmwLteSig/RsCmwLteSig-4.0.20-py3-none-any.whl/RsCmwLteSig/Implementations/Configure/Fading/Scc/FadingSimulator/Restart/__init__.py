from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RestartCls:
	"""Restart commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("restart", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import ModeCls
			self._mode = ModeCls(self._core, self._cmd_group)
		return self._mode

	def set(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:RESTart \n
		Snippet: driver.configure.fading.scc.fadingSimulator.restart.set(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Restarts the fading process in MANual mode (see also CONFigure:...:FSIMulator:RESTart:MODE) . \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:RESTart')

	def set_with_opc(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, opc_timeout_ms: int = -1) -> None:
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:RESTart \n
		Snippet: driver.configure.fading.scc.fadingSimulator.restart.set_with_opc(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Restarts the fading process in MANual mode (see also CONFigure:...:FSIMulator:RESTart:MODE) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwLteSig.utilities.opc_timeout_set() to set the timeout value. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:RESTart', opc_timeout_ms)

	def clone(self) -> 'RestartCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RestartCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
