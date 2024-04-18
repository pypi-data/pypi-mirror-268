from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EnpModeCls:
	"""EnpMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enpMode", core, parent)

	def set(self, mode: enums.NominalPowerMode, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:ENPMode \n
		Snippet: driver.configure.rfSettings.scc.enpMode.set(mode = enums.NominalPowerMode.AUToranging, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the expected nominal power mode. The expected nominal power of the UL signal can be defined manually or
		calculated automatically, according to the UL power control settings.
			INTRO_CMD_HELP: For manual configuration, see: \n
			- method RsCmwLteSig.Configure.RfSettings.Pcc.envelopePower
			- method RsCmwLteSig.Configure.RfSettings.Pcc.umargin
		For UL power control settings, see 'Uplink power control'. \n
			:param mode: MANual | ULPC MANual The expected nominal power and margin are specified manually. ULPC The expected nominal power is calculated according to the UL power control settings. For the margin, 12 dB are applied.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.NominalPowerMode)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:ENPMode {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.NominalPowerMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:ENPMode \n
		Snippet: value: enums.NominalPowerMode = driver.configure.rfSettings.scc.enpMode.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the expected nominal power mode. The expected nominal power of the UL signal can be defined manually or
		calculated automatically, according to the UL power control settings.
			INTRO_CMD_HELP: For manual configuration, see: \n
			- method RsCmwLteSig.Configure.RfSettings.Pcc.envelopePower
			- method RsCmwLteSig.Configure.RfSettings.Pcc.umargin
		For UL power control settings, see 'Uplink power control'. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: mode: MANual | ULPC MANual The expected nominal power and margin are specified manually. ULPC The expected nominal power is calculated according to the UL power control settings. For the margin, 12 dB are applied."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:ENPMode?')
		return Conversions.str_to_scalar_enum(response, enums.NominalPowerMode)
