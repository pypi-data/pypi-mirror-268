from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BasicCls:
	"""Basic commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("basic", core, parent)

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UL:SCC<Carrier>:APPower:TPRRcsetup:BASic \n
		Snippet: value: bool = driver.sense.uplink.scc.apPower.tprrcSetup.basic.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Queries the state of P0-UE-PUSCH toggling, determining the P0-UE-PUSCH values signaled to the UE during RRC connection
		setup if basic UL power configuration applies. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: enable: OFF | ON"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:APPower:TPRRcsetup:BASic?')
		return Conversions.str_to_bool(response)
