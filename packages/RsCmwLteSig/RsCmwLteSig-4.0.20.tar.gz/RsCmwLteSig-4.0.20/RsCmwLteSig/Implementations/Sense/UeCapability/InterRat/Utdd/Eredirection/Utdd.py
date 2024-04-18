from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UtddCls:
	"""Utdd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("utdd", core, parent)

	def get(self, uTddFreq=repcap.UTddFreq.Default) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:IRAT:UTDD<frequency>:EREDirection:UTDD \n
		Snippet: value: bool = driver.sense.ueCapability.interRat.utdd.eredirection.utdd.get(uTddFreq = repcap.UTddFreq.Default) \n
		Returns whether the UE supports an enhanced redirection to UTRA TDD or not. \n
			:param uTddFreq: optional repeated capability selector. Default value: Freq128 (settable in the interface 'Utdd')
			:return: supported: OFF | ON"""
		uTddFreq_cmd_val = self._cmd_group.get_repcap_cmd_value(uTddFreq, repcap.UTddFreq)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:UECapability:IRAT:UTDD{uTddFreq_cmd_val}:EREDirection:UTDD?')
		return Conversions.str_to_bool(response)
