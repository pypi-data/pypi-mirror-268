from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UdSeparationCls:
	"""UdSeparation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("udSeparation", core, parent)

	def set(self, frequency: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:UDEFined:UDSeparation \n
		Snippet: driver.configure.rfSettings.scc.userDefined.udSeparation.set(frequency = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the UL/DL separation FDL - FUL for the user-defined band. The allowed range depends on the remaining
		user-defined band settings: The resulting uplink carrier center frequencies must be within the allowed frequency range.
		For calculations, see method RsCmwLteSig.Configure.RfSettings.Pcc.UserDefined.Frequency.Downlink.minimum. \n
			:param frequency: numeric Depending on the other settings, only a part of the following range is allowed. Range: -5930 MHz to 5930 MHz , Unit: Hz
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:UDEFined:UDSeparation {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:UDEFined:UDSeparation \n
		Snippet: value: int = driver.configure.rfSettings.scc.userDefined.udSeparation.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the UL/DL separation FDL - FUL for the user-defined band. The allowed range depends on the remaining
		user-defined band settings: The resulting uplink carrier center frequencies must be within the allowed frequency range.
		For calculations, see method RsCmwLteSig.Configure.RfSettings.Pcc.UserDefined.Frequency.Downlink.minimum. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: frequency: numeric Depending on the other settings, only a part of the following range is allowed. Range: -5930 MHz to 5930 MHz , Unit: Hz"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:UDEFined:UDSeparation?')
		return Conversions.str_to_int(response)
