from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UserDefinedCls:
	"""UserDefined commands group definition. 10 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("userDefined", core, parent)

	@property
	def channel(self):
		"""channel commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import ChannelCls
			self._channel = ChannelCls(self._core, self._cmd_group)
		return self._channel

	@property
	def frequency(self):
		"""frequency commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	def get_ud_separation(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDEFined:UDSeparation \n
		Snippet: value: int = driver.configure.rfSettings.pcc.userDefined.get_ud_separation() \n
		Configures the UL/DL separation FDL - FUL for the user-defined band. The allowed range depends on the remaining
		user-defined band settings: The resulting uplink carrier center frequencies must be within the allowed frequency range.
		For calculations, see method RsCmwLteSig.Configure.RfSettings.Pcc.UserDefined.Frequency.Downlink.minimum. \n
			:return: frequency: numeric Depending on the other settings, only a part of the following range is allowed. Range: -5930 MHz to 5930 MHz , Unit: Hz
		"""
		response = self._core.io.query_str_with_opc('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDEFined:UDSeparation?')
		return Conversions.str_to_int(response)

	def set_ud_separation(self, frequency: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDEFined:UDSeparation \n
		Snippet: driver.configure.rfSettings.pcc.userDefined.set_ud_separation(frequency = 1) \n
		Configures the UL/DL separation FDL - FUL for the user-defined band. The allowed range depends on the remaining
		user-defined band settings: The resulting uplink carrier center frequencies must be within the allowed frequency range.
		For calculations, see method RsCmwLteSig.Configure.RfSettings.Pcc.UserDefined.Frequency.Downlink.minimum. \n
			:param frequency: numeric Depending on the other settings, only a part of the following range is allowed. Range: -5930 MHz to 5930 MHz , Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDEFined:UDSeparation {param}')

	def get_bindicator(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDEFined:BINDicator \n
		Snippet: value: int = driver.configure.rfSettings.pcc.userDefined.get_bindicator() \n
		Configures the frequency band indicator, identifying the user-defined band in signaling messages. \n
			:return: band_indicator: numeric Range: 1 to 256
		"""
		response = self._core.io.query_str_with_opc('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDEFined:BINDicator?')
		return Conversions.str_to_int(response)

	def set_bindicator(self, band_indicator: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDEFined:BINDicator \n
		Snippet: driver.configure.rfSettings.pcc.userDefined.set_bindicator(band_indicator = 1) \n
		Configures the frequency band indicator, identifying the user-defined band in signaling messages. \n
			:param band_indicator: numeric Range: 1 to 256
		"""
		param = Conversions.decimal_value_to_str(band_indicator)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDEFined:BINDicator {param}')

	def clone(self) -> 'UserDefinedCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UserDefinedCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
