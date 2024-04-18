from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	def get(self, eutraBand=repcap.EutraBand.Default) -> List[str]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:RF:BCOMbination:V<Number>:EUTRa<BandNr>:BCLass:UL \n
		Snippet: value: List[str] = driver.sense.ueCapability.rf.bcombination.v.eutra.bclass.uplink.get(eutraBand = repcap.EutraBand.Default) \n
		Returns the bandwidth classes supported by the UE in the uplink or downlink. The information is returned for a selected
		band of all supported carrier aggregation band combinations. \n
			:param eutraBand: optional repeated capability selector. Default value: Band1 (settable in the interface 'Eutra')
			:return: bandwidth_class: string Comma-separated list of strings, one string per band combination (combination 0 to n) Each string indicates the bandwidth classes supported for the selected band (BandNr) of the combination, for example 'abc'."""
		eutraBand_cmd_val = self._cmd_group.get_repcap_cmd_value(eutraBand, repcap.EutraBand)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:UECapability:RF:BCOMbination:V1020:EUTRa{eutraBand_cmd_val}:BCLass:UL?')
		return Conversions.str_to_str_list(response)
