from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SupportedCls:
	"""Supported commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("supported", core, parent)

	def get(self, uTddFreq=repcap.UTddFreq.Default) -> List[bool]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:IRAT:UTDD<frequency>:SUPPorted \n
		Snippet: value: List[bool] = driver.sense.ueCapability.interRat.utdd.supported.get(uTddFreq = repcap.UTddFreq.Default) \n
		Returns a list of values indicating the support of the individual UTRA TDD operating bands by the UE, according to the UE
		capability information. \n
			:param uTddFreq: optional repeated capability selector. Default value: Freq128 (settable in the interface 'Utdd')
			:return: supported_band: OFF | ON 26 values: band a to band z"""
		uTddFreq_cmd_val = self._cmd_group.get_repcap_cmd_value(uTddFreq, repcap.UTddFreq)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:UECapability:IRAT:UTDD{uTddFreq_cmd_val}:SUPPorted?')
		return Conversions.str_to_bool_list(response)
