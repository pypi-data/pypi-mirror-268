from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UmarginCls:
	"""Umargin commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("umargin", core, parent)

	def set(self, user_margin: float, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:UMARgin \n
		Snippet: driver.configure.rfSettings.scc.umargin.set(user_margin = 1.0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Sets the margin that the R&S CMW adds to the expected nominal power to determine the reference level in manual mode.
		If the expected nominal power is calculated automatically according to the UL power control settings, a fix margin of 12
		dB is used instead. The reference level minus the external input attenuation must be within the power range of the
		selected input connector; refer to the data sheet.
			INTRO_CMD_HELP: Refer also to the following commands: \n
			- method RsCmwLteSig.Configure.RfSettings.Pcc.enpMode
			- method RsCmwLteSig.Configure.RfSettings.Pcc.envelopePower
			- method RsCmwLteSig.Configure.RfSettings.Pcc.Eattenuation.inputPy \n
			:param user_margin: numeric Range: 0 dB to (42 dB + external attenuation - expected nominal power) , Unit: dB
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(user_margin)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:UMARgin {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:UMARgin \n
		Snippet: value: float = driver.configure.rfSettings.scc.umargin.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Sets the margin that the R&S CMW adds to the expected nominal power to determine the reference level in manual mode.
		If the expected nominal power is calculated automatically according to the UL power control settings, a fix margin of 12
		dB is used instead. The reference level minus the external input attenuation must be within the power range of the
		selected input connector; refer to the data sheet.
			INTRO_CMD_HELP: Refer also to the following commands: \n
			- method RsCmwLteSig.Configure.RfSettings.Pcc.enpMode
			- method RsCmwLteSig.Configure.RfSettings.Pcc.envelopePower
			- method RsCmwLteSig.Configure.RfSettings.Pcc.Eattenuation.inputPy \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: user_margin: numeric Range: 0 dB to (42 dB + external attenuation - expected nominal power) , Unit: dB"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:UMARgin?')
		return Conversions.str_to_float(response)
