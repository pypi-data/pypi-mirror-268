from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FcPowerCls:
	"""FcPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fcPower", core, parent)

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:DL:SCC<Carrier>:FCPower \n
		Snippet: value: float = driver.sense.downlink.scc.fcPower.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Queries the 'Full Cell BW Power'. The power results from the configured RS EPRE and the cell bandwidth. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: level: float Range: -220 dBm to 48 dBm, Unit: dBm"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:DL:SCC{secondaryCompCarrier_cmd_val}:FCPower?')
		return Conversions.str_to_float(response)
