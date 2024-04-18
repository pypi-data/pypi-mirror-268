from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RperiodCls:
	"""Rperiod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rperiod", core, parent)

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CQIReporting:SCC<Carrier>:RPERiod \n
		Snippet: value: int = driver.sense.cqiReporting.scc.rperiod.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Queries the reporting period Np in subframes, resulting from the configured 'cqi-pmi-ConfigIndex'. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: period: decimal Range: 1 to 160"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:CQIReporting:SCC{secondaryCompCarrier_cmd_val}:RPERiod?')
		return Conversions.str_to_int(response)
