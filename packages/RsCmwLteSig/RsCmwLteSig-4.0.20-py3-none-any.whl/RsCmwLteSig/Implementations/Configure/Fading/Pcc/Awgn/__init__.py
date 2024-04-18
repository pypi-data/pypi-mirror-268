from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AwgnCls:
	"""Awgn commands group definition. 6 total commands, 1 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("awgn", core, parent)

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import BandwidthCls
			self._bandwidth = BandwidthCls(self._core, self._cmd_group)
		return self._bandwidth

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:AWGN:ENABle \n
		Snippet: value: bool = driver.configure.fading.pcc.awgn.get_enable() \n
		Enables or disables AWGN insertion via the fading module. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:AWGN:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:AWGN:ENABle \n
		Snippet: driver.configure.fading.pcc.awgn.set_enable(enable = False) \n
		Enables or disables AWGN insertion via the fading module. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:AWGN:ENABle {param}')

	def get_foffset(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:AWGN:FOFFset \n
		Snippet: value: float = driver.configure.fading.pcc.awgn.get_foffset() \n
		Shifts the center frequency of the noise bandwidth relative to the carrier center frequency. \n
			:return: offset: numeric Range: -40 MHz to 40 MHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:AWGN:FOFFset?')
		return Conversions.str_to_float(response)

	def set_foffset(self, offset: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:AWGN:FOFFset \n
		Snippet: driver.configure.fading.pcc.awgn.set_foffset(offset = 1.0) \n
		Shifts the center frequency of the noise bandwidth relative to the carrier center frequency. \n
			:param offset: numeric Range: -40 MHz to 40 MHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:AWGN:FOFFset {param}')

	def get_sn_ratio(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:AWGN:SNRatio \n
		Snippet: value: float = driver.configure.fading.pcc.awgn.get_sn_ratio() \n
		Specifies the signal to noise ratio for the AWGN inserted on the internal fading module. \n
			:return: ratio: numeric Range: -50 dB to 40 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:AWGN:SNRatio?')
		return Conversions.str_to_float(response)

	def set_sn_ratio(self, ratio: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:AWGN:SNRatio \n
		Snippet: driver.configure.fading.pcc.awgn.set_sn_ratio(ratio = 1.0) \n
		Specifies the signal to noise ratio for the AWGN inserted on the internal fading module. \n
			:param ratio: numeric Range: -50 dB to 40 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(ratio)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:AWGN:SNRatio {param}')

	# noinspection PyTypeChecker
	def get_measurement(self) -> enums.AwgnMeasurement:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:AWGN:MEASurement \n
		Snippet: value: enums.AwgnMeasurement = driver.configure.fading.pcc.awgn.get_measurement() \n
		No command help available \n
			:return: measurement: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:AWGN:MEASurement?')
		return Conversions.str_to_scalar_enum(response, enums.AwgnMeasurement)

	def set_measurement(self, measurement: enums.AwgnMeasurement) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:AWGN:MEASurement \n
		Snippet: driver.configure.fading.pcc.awgn.set_measurement(measurement = enums.AwgnMeasurement.NOISe) \n
		No command help available \n
			:param measurement: No help available
		"""
		param = Conversions.enum_scalar_to_str(measurement, enums.AwgnMeasurement)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:AWGN:MEASurement {param}')

	def clone(self) -> 'AwgnCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AwgnCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
