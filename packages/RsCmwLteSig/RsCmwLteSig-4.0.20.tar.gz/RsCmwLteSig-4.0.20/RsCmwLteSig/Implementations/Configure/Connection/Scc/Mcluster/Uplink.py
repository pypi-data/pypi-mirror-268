from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	def set(self, multi_cluster: bool, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:MCLuster:UL \n
		Snippet: driver.configure.connection.scc.mcluster.uplink.set(multi_cluster = False, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Enables/disables multi-cluster allocation for the UL. \n
			:param multi_cluster: OFF | ON OFF: contiguous allocation, resource allocation type 0 ON: multi-cluster allocation, resource allocation type 1
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.bool_to_str(multi_cluster)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:MCLuster:UL {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:MCLuster:UL \n
		Snippet: value: bool = driver.configure.connection.scc.mcluster.uplink.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Enables/disables multi-cluster allocation for the UL. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: multi_cluster: OFF | ON OFF: contiguous allocation, resource allocation type 0 ON: multi-cluster allocation, resource allocation type 1"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:MCLuster:UL?')
		return Conversions.str_to_bool(response)
