from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NoLayersCls:
	"""NoLayers commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("noLayers", core, parent)

	def set(self, number: enums.NoOfLayers, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:NOLayers \n
		Snippet: driver.configure.connection.scc.noLayers.set(number = enums.NoOfLayers.L2, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the number of layers for MIMO 4x4 with spatial multiplexing (TM 3 and 4) . \n
			:param number: L2 | L4 Two layers or four layers
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(number, enums.NoOfLayers)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:NOLayers {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.NoOfLayers:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:NOLayers \n
		Snippet: value: enums.NoOfLayers = driver.configure.connection.scc.noLayers.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the number of layers for MIMO 4x4 with spatial multiplexing (TM 3 and 4) . \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: number: L2 | L4 Two layers or four layers"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:NOLayers?')
		return Conversions.str_to_scalar_enum(response, enums.NoOfLayers)
