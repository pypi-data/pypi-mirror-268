from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> List[float]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:UDCHannels:UL:CRATe:ALL \n
		Snippet: value: List[float] = driver.sense.connection.scc.udChannels.uplink.crate.all.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Queries the code rate for all uplink subframes for the scheduling type 'User-defined Channels'. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: coderate: float Comma-separated list of 10 values (subframe 0 to subframe 9) Range: 0 to 10"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_bin_or_ascii_float_list(f'SENSe:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:UDCHannels:UL:CRATe:ALL?')
		return response
