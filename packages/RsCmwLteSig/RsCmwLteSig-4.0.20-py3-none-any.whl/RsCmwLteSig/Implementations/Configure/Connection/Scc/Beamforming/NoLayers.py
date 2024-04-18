from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NoLayersCls:
	"""NoLayers commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("noLayers", core, parent)

	def set(self, number: enums.BeamformingNoOfLayers, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:BEAMforming:NOLayers \n
		Snippet: driver.configure.connection.scc.beamforming.noLayers.set(number = enums.BeamformingNoOfLayers.L1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the number of layers for transmission mode 8. \n
			:param number: L1 | L2 L1: single-layer beamforming L2: dual-layer beamforming
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(number, enums.BeamformingNoOfLayers)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:BEAMforming:NOLayers {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.BeamformingNoOfLayers:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:BEAMforming:NOLayers \n
		Snippet: value: enums.BeamformingNoOfLayers = driver.configure.connection.scc.beamforming.noLayers.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the number of layers for transmission mode 8. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: number: L1 | L2 L1: single-layer beamforming L2: dual-layer beamforming"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:BEAMforming:NOLayers?')
		return Conversions.str_to_scalar_enum(response, enums.BeamformingNoOfLayers)
