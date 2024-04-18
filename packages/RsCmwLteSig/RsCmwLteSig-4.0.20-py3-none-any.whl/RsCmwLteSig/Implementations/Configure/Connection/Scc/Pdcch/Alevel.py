from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AlevelCls:
	"""Alevel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alevel", core, parent)

	def set(self, aggregationlevel: enums.Aggregationlevel, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:PDCCh:ALEVel \n
		Snippet: driver.configure.connection.scc.pdcch.alevel.set(aggregationlevel = enums.Aggregationlevel.AUTO, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the aggregation levels for DCI messages with C-RNTI. The individual values have prerequisites, see manual
		operation. \n
			:param aggregationlevel: AUTO | D8U4 | D4U4 | D4U2 | D1U1 | D8U8 AUTO: automatic configuration DaUb: a CCE for DCI messages for the DL, b CCE for messages for the UL
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(aggregationlevel, enums.Aggregationlevel)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:PDCCh:ALEVel {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.Aggregationlevel:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:PDCCh:ALEVel \n
		Snippet: value: enums.Aggregationlevel = driver.configure.connection.scc.pdcch.alevel.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the aggregation levels for DCI messages with C-RNTI. The individual values have prerequisites, see manual
		operation. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: aggregationlevel: AUTO | D8U4 | D4U4 | D4U2 | D1U1 | D8U8 AUTO: automatic configuration DaUb: a CCE for DCI messages for the DL, b CCE for messages for the UL"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:PDCCh:ALEVel?')
		return Conversions.str_to_scalar_enum(response, enums.Aggregationlevel)
