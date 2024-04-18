from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CltPowerCls:
	"""CltPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cltPower", core, parent)

	def set(self, power: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PUCCh:CLTPower \n
		Snippet: driver.configure.uplink.scc.pucch.cltPower.set(power = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		No command help available \n
			:param power: No help available
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(power)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PUCCh:CLTPower {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PUCCh:CLTPower \n
		Snippet: value: int = driver.configure.uplink.scc.pucch.cltPower.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		No command help available \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: power: No help available"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PUCCh:CLTPower?')
		return Conversions.str_to_int(response)
