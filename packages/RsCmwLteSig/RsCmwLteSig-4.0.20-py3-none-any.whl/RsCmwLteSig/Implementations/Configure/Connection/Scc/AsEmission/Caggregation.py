from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CaggregationCls:
	"""Caggregation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("caggregation", core, parent)

	def set(self, value: enums.SemissionValue, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:ASEMission:CAGGregation \n
		Snippet: driver.configure.connection.scc.asEmission.caggregation.set(value = enums.SemissionValue.NS01, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects a value signaled to the UE as additional ACLR and spectrum emission requirement for the SCC<c>. The setting is
		only relevant if the SCC uplink is enabled. \n
			:param value: NS01 | ... | NS32 Value CA_NS_01 to CA_NS_32
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(value, enums.SemissionValue)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:ASEMission:CAGGregation {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.SemissionValue:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:ASEMission:CAGGregation \n
		Snippet: value: enums.SemissionValue = driver.configure.connection.scc.asEmission.caggregation.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects a value signaled to the UE as additional ACLR and spectrum emission requirement for the SCC<c>. The setting is
		only relevant if the SCC uplink is enabled. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: value: NS01 | ... | NS32 Value CA_NS_01 to CA_NS_32"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:ASEMission:CAGGregation?')
		return Conversions.str_to_scalar_enum(response, enums.SemissionValue)
