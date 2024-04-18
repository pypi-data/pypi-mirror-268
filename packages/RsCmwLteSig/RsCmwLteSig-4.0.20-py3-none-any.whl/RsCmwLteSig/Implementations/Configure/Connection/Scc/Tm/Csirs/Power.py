from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PowerCls:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, power: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:TM<nr>:CSIRs:POWer \n
		Snippet: driver.configure.connection.scc.tm.csirs.power.set(power = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Sets the value Pc to be signaled to the UE. Pc is the assumed ratio of the RS EPRE to the CSI-RS EPRE. \n
			:param power: integer Range: -8 dB to 15 dB, Unit: dB
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(power)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TM9:CSIRs:POWer {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<carrier>:TM<nr>:CSIRs:POWer \n
		Snippet: value: int = driver.configure.connection.scc.tm.csirs.power.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Sets the value Pc to be signaled to the UE. Pc is the assumed ratio of the RS EPRE to the CSI-RS EPRE. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: power: integer Range: -8 dB to 15 dB, Unit: dB"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TM9:CSIRs:POWer?')
		return Conversions.str_to_int(response)
