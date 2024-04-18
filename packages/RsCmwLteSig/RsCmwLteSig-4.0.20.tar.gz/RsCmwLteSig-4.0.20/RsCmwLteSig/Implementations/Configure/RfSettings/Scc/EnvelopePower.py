from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnvelopePowerCls:
	"""EnvelopePower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("envelopePower", core, parent)

	def set(self, expected_power: float, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:ENPower \n
		Snippet: driver.configure.rfSettings.scc.envelopePower.set(expected_power = 1.0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Sets the expected nominal power of the UL signal in manual mode. If the expected nominal power is calculated
		automatically according to the UL power control settings, you can only query the result. To configure the expected
		nominal power mode, see method RsCmwLteSig.Configure.RfSettings.Pcc.enpMode. \n
			:param expected_power: numeric In manual mode, the range of the expected nominal power can be calculated as follows: Range (expected nominal power) = range (input power) + external attenuation - margin The input power range is stated in the data sheet. Unit: dBm
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(expected_power)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:ENPower {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:ENPower \n
		Snippet: value: float = driver.configure.rfSettings.scc.envelopePower.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Sets the expected nominal power of the UL signal in manual mode. If the expected nominal power is calculated
		automatically according to the UL power control settings, you can only query the result. To configure the expected
		nominal power mode, see method RsCmwLteSig.Configure.RfSettings.Pcc.enpMode. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: expected_power: numeric In manual mode, the range of the expected nominal power can be calculated as follows: Range (expected nominal power) = range (input power) + external attenuation - margin The input power range is stated in the data sheet. Unit: dBm"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:ENPower?')
		return Conversions.str_to_float(response)
