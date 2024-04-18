from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EoPowerCls:
	"""EoPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eoPower", core, parent)

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UL:SCC<Carrier>:APPower:EOPower \n
		Snippet: value: float = driver.sense.uplink.scc.apPower.eoPower.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Queries the expected initial PUSCH power, resulting from the advanced UL power settings. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: expected_ol_power: float Unit: dBm"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:APPower:EOPower?')
		return Conversions.str_to_float(response)
