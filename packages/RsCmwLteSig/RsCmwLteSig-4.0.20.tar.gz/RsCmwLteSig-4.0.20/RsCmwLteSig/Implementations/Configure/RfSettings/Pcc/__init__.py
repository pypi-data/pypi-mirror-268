from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PccCls:
	"""Pcc commands group definition. 24 total commands, 5 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcc", core, parent)

	@property
	def afBands(self):
		"""afBands commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_afBands'):
			from .AfBands import AfBandsCls
			self._afBands = AfBandsCls(self._core, self._cmd_group)
		return self._afBands

	@property
	def userDefined(self):
		"""userDefined commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_userDefined'):
			from .UserDefined import UserDefinedCls
			self._userDefined = UserDefinedCls(self._core, self._cmd_group)
		return self._userDefined

	@property
	def eattenuation(self):
		"""eattenuation commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_eattenuation'):
			from .Eattenuation import EattenuationCls
			self._eattenuation = EattenuationCls(self._core, self._cmd_group)
		return self._eattenuation

	@property
	def channel(self):
		"""channel commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import ChannelCls
			self._channel = ChannelCls(self._core, self._cmd_group)
		return self._channel

	@property
	def foffset(self):
		"""foffset commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_foffset'):
			from .Foffset import FoffsetCls
			self._foffset = FoffsetCls(self._core, self._cmd_group)
		return self._foffset

	def get_mixer_level_offset(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:MLOFfset \n
		Snippet: value: int = driver.configure.rfSettings.pcc.get_mixer_level_offset() \n
		Varies the input level of the mixer in the analyzer path. \n
			:return: mix_lev_offset: numeric Range: -10 dB to 10 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:MLOFfset?')
		return Conversions.str_to_int(response)

	def set_mixer_level_offset(self, mix_lev_offset: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:MLOFfset \n
		Snippet: driver.configure.rfSettings.pcc.set_mixer_level_offset(mix_lev_offset = 1) \n
		Varies the input level of the mixer in the analyzer path. \n
			:param mix_lev_offset: numeric Range: -10 dB to 10 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(mix_lev_offset)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:MLOFfset {param}')

	def get_ud_separation(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDSeparation \n
		Snippet: value: int = driver.configure.rfSettings.pcc.get_ud_separation() \n
		Configures the UL/DL separation. For most operating bands, this setting is fixed. \n
			:return: frequency: numeric UL/DL separation Range: see table , Unit: Hz
		"""
		response = self._core.io.query_str_with_opc('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDSeparation?')
		return Conversions.str_to_int(response)

	def set_ud_separation(self, frequency: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDSeparation \n
		Snippet: driver.configure.rfSettings.pcc.set_ud_separation(frequency = 1) \n
		Configures the UL/DL separation. For most operating bands, this setting is fixed. \n
			:param frequency: numeric UL/DL separation Range: see table , Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDSeparation {param}')

	def get_envelope_power(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:ENPower \n
		Snippet: value: float = driver.configure.rfSettings.pcc.get_envelope_power() \n
		Sets the expected nominal power of the UL signal in manual mode. If the expected nominal power is calculated
		automatically according to the UL power control settings, you can only query the result. To configure the expected
		nominal power mode, see method RsCmwLteSig.Configure.RfSettings.Pcc.enpMode. \n
			:return: expected_power: numeric In manual mode, the range of the expected nominal power can be calculated as follows: Range (expected nominal power) = range (input power) + external attenuation - margin The input power range is stated in the data sheet. Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:ENPower?')
		return Conversions.str_to_float(response)

	def set_envelope_power(self, expected_power: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:ENPower \n
		Snippet: driver.configure.rfSettings.pcc.set_envelope_power(expected_power = 1.0) \n
		Sets the expected nominal power of the UL signal in manual mode. If the expected nominal power is calculated
		automatically according to the UL power control settings, you can only query the result. To configure the expected
		nominal power mode, see method RsCmwLteSig.Configure.RfSettings.Pcc.enpMode. \n
			:param expected_power: numeric In manual mode, the range of the expected nominal power can be calculated as follows: Range (expected nominal power) = range (input power) + external attenuation - margin The input power range is stated in the data sheet. Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(expected_power)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:ENPower {param}')

	# noinspection PyTypeChecker
	def get_enp_mode(self) -> enums.NominalPowerMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:ENPMode \n
		Snippet: value: enums.NominalPowerMode = driver.configure.rfSettings.pcc.get_enp_mode() \n
		Selects the expected nominal power mode. The expected nominal power of the UL signal can be defined manually or
		calculated automatically, according to the UL power control settings.
			INTRO_CMD_HELP: For manual configuration, see: \n
			- method RsCmwLteSig.Configure.RfSettings.Pcc.envelopePower
			- method RsCmwLteSig.Configure.RfSettings.Pcc.umargin
		For UL power control settings, see 'Uplink power control'. \n
			:return: mode: MANual | ULPC MANual The expected nominal power and margin are specified manually. ULPC The expected nominal power is calculated according to the UL power control settings. For the margin, 12 dB are applied.
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:ENPMode?')
		return Conversions.str_to_scalar_enum(response, enums.NominalPowerMode)

	def set_enp_mode(self, mode: enums.NominalPowerMode) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:ENPMode \n
		Snippet: driver.configure.rfSettings.pcc.set_enp_mode(mode = enums.NominalPowerMode.AUToranging) \n
		Selects the expected nominal power mode. The expected nominal power of the UL signal can be defined manually or
		calculated automatically, according to the UL power control settings.
			INTRO_CMD_HELP: For manual configuration, see: \n
			- method RsCmwLteSig.Configure.RfSettings.Pcc.envelopePower
			- method RsCmwLteSig.Configure.RfSettings.Pcc.umargin
		For UL power control settings, see 'Uplink power control'. \n
			:param mode: MANual | ULPC MANual The expected nominal power and margin are specified manually. ULPC The expected nominal power is calculated according to the UL power control settings. For the margin, 12 dB are applied.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.NominalPowerMode)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:ENPMode {param}')

	def get_umargin(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UMARgin \n
		Snippet: value: float = driver.configure.rfSettings.pcc.get_umargin() \n
		Sets the margin that the R&S CMW adds to the expected nominal power to determine the reference level in manual mode.
		If the expected nominal power is calculated automatically according to the UL power control settings, a fix margin of 12
		dB is used instead. The reference level minus the external input attenuation must be within the power range of the
		selected input connector; refer to the data sheet.
			INTRO_CMD_HELP: Refer also to the following commands: \n
			- method RsCmwLteSig.Configure.RfSettings.Pcc.enpMode
			- method RsCmwLteSig.Configure.RfSettings.Pcc.envelopePower
			- method RsCmwLteSig.Configure.RfSettings.Pcc.Eattenuation.inputPy \n
			:return: user_margin: numeric Range: 0 dB to (42 dB + external attenuation - expected nominal power) , Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UMARgin?')
		return Conversions.str_to_float(response)

	def set_umargin(self, user_margin: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UMARgin \n
		Snippet: driver.configure.rfSettings.pcc.set_umargin(user_margin = 1.0) \n
		Sets the margin that the R&S CMW adds to the expected nominal power to determine the reference level in manual mode.
		If the expected nominal power is calculated automatically according to the UL power control settings, a fix margin of 12
		dB is used instead. The reference level minus the external input attenuation must be within the power range of the
		selected input connector; refer to the data sheet.
			INTRO_CMD_HELP: Refer also to the following commands: \n
			- method RsCmwLteSig.Configure.RfSettings.Pcc.enpMode
			- method RsCmwLteSig.Configure.RfSettings.Pcc.envelopePower
			- method RsCmwLteSig.Configure.RfSettings.Pcc.Eattenuation.inputPy \n
			:param user_margin: numeric Range: 0 dB to (42 dB + external attenuation - expected nominal power) , Unit: dB
		"""
		param = Conversions.decimal_value_to_str(user_margin)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UMARgin {param}')

	def clone(self) -> 'PccCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PccCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
