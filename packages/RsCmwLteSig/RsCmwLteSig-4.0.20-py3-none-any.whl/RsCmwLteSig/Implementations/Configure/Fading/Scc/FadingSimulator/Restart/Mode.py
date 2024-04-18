from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModeCls:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, restart_mode: enums.RestartMode, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:RESTart:MODE \n
		Snippet: driver.configure.fading.scc.fadingSimulator.restart.mode.set(restart_mode = enums.RestartMode.AUTO, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Sets the restart mode of the fading simulator. \n
			:param restart_mode: AUTO | MANual AUTO: fading automatically starts with the DL signal MANual: fading is started and restarted manually (see CONFigure:...:FSIMulator:RESTart)
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(restart_mode, enums.RestartMode)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:RESTart:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.RestartMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:RESTart:MODE \n
		Snippet: value: enums.RestartMode = driver.configure.fading.scc.fadingSimulator.restart.mode.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Sets the restart mode of the fading simulator. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: restart_mode: AUTO | MANual AUTO: fading automatically starts with the DL signal MANual: fading is started and restarted manually (see CONFigure:...:FSIMulator:RESTart)"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:RESTart:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.RestartMode)
