from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RestartCls:
	"""Restart commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("restart", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.RestartMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:RESTart:MODE \n
		Snippet: value: enums.RestartMode = driver.configure.fading.pcc.fadingSimulator.restart.get_mode() \n
		Sets the restart mode of the fading simulator. \n
			:return: restart_mode: AUTO | MANual AUTO: fading automatically starts with the DL signal MANual: fading is started and restarted manually (see CONFigure:...:FSIMulator:RESTart)
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:RESTart:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.RestartMode)

	def set_mode(self, restart_mode: enums.RestartMode) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:RESTart:MODE \n
		Snippet: driver.configure.fading.pcc.fadingSimulator.restart.set_mode(restart_mode = enums.RestartMode.AUTO) \n
		Sets the restart mode of the fading simulator. \n
			:param restart_mode: AUTO | MANual AUTO: fading automatically starts with the DL signal MANual: fading is started and restarted manually (see CONFigure:...:FSIMulator:RESTart)
		"""
		param = Conversions.enum_scalar_to_str(restart_mode, enums.RestartMode)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:RESTart:MODE {param}')

	def set(self) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:RESTart \n
		Snippet: driver.configure.fading.pcc.fadingSimulator.restart.set() \n
		Restarts the fading process in MANual mode (see also CONFigure:...:FSIMulator:RESTart:MODE) . \n
		"""
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:RESTart')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:RESTart \n
		Snippet: driver.configure.fading.pcc.fadingSimulator.restart.set_with_opc() \n
		Restarts the fading process in MANual mode (see also CONFigure:...:FSIMulator:RESTart:MODE) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwLteSig.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:RESTart', opc_timeout_ms)
