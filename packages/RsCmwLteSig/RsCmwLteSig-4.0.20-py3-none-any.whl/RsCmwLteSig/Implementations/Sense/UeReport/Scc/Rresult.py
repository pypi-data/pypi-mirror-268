from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RresultCls:
	"""Rresult commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rresult", core, parent)

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UEReport:SCC<Carrier>:RRESult \n
		Snippet: value: int = driver.sense.ueReport.scc.rresult.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Returns the RSSI value reported as dimensionless index for an SCC DL with LAA. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: result: decimal Range: 0 to 76"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:UEReport:SCC{secondaryCompCarrier_cmd_val}:RRESult?')
		return Conversions.str_to_int(response)
