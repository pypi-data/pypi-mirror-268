from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MappingCls:
	"""Mapping commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mapping", core, parent)

	def set(self, port: enums.PortsMapping, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:PZERo:MAPPing \n
		Snippet: driver.configure.connection.scc.pzero.mapping.set(port = enums.PortsMapping.R1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the mapping of antenna port 0 to the RF output paths. Only for TM 7 in scenarios with two RF output paths,
		without fading. \n
			:param port: R1 | R1R2 R1: Map port 0 to the first RF output path. R1R2: Map port 0 to both RF output paths.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(port, enums.PortsMapping)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:PZERo:MAPPing {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.PortsMapping:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:PZERo:MAPPing \n
		Snippet: value: enums.PortsMapping = driver.configure.connection.scc.pzero.mapping.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the mapping of antenna port 0 to the RF output paths. Only for TM 7 in scenarios with two RF output paths,
		without fading. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: port: R1 | R1R2 R1: Map port 0 to the first RF output path. R1R2: Map port 0 to both RF output paths."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:PZERo:MAPPing?')
		return Conversions.str_to_scalar_enum(response, enums.PortsMapping)
