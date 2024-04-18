from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	def get_minimum(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDEFined:FREQuency:DL:MINimum \n
		Snippet: value: int = driver.configure.rfSettings.pcc.userDefined.frequency.downlink.get_minimum() \n
		Configures the carrier center frequency corresponding to the minimum downlink channel number for the user-defined band.
		The other frequencies are calculated from the settings as follows: FREQ:DL:MAX = FREQ:DL:MIN + (CHAN:DL:MAX -
		CHAN:DL:MIN) * 100 kHz FREQ:UL:MIN = FREQ:DL:MIN - UDSeparation FREQ:UL:MAX = FREQ:DL:MIN - UDSeparation + (CHAN:DL:MAX -
		CHAN:DL:MIN) * 100 kHz \n
			:return: frequency: numeric The allowed range depends on the remaining user-defined band settings. All frequencies resulting from the calculations stated above must be located within the following frequency range. Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		response = self._core.io.query_str_with_opc('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDEFined:FREQuency:DL:MINimum?')
		return Conversions.str_to_int(response)

	def set_minimum(self, frequency: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDEFined:FREQuency:DL:MINimum \n
		Snippet: driver.configure.rfSettings.pcc.userDefined.frequency.downlink.set_minimum(frequency = 1) \n
		Configures the carrier center frequency corresponding to the minimum downlink channel number for the user-defined band.
		The other frequencies are calculated from the settings as follows: FREQ:DL:MAX = FREQ:DL:MIN + (CHAN:DL:MAX -
		CHAN:DL:MIN) * 100 kHz FREQ:UL:MIN = FREQ:DL:MIN - UDSeparation FREQ:UL:MAX = FREQ:DL:MIN - UDSeparation + (CHAN:DL:MAX -
		CHAN:DL:MIN) * 100 kHz \n
			:param frequency: numeric The allowed range depends on the remaining user-defined band settings. All frequencies resulting from the calculations stated above must be located within the following frequency range. Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDEFined:FREQuency:DL:MINimum {param}')

	def get_maximum(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings[:PCC]:UDEFined:FREQuency:DL:MAXimum \n
		Snippet: value: int = driver.configure.rfSettings.pcc.userDefined.frequency.downlink.get_maximum() \n
		Queries the maximum downlink carrier center frequency resulting from the user-defined band settings. For calculation, see
		method RsCmwLteSig.Configure.RfSettings.Pcc.UserDefined.Frequency.Downlink.minimum. \n
			:return: frequency: decimal Range: 70 MHz to 6 GHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:RFSettings:PCC:UDEFined:FREQuency:DL:MAXimum?')
		return Conversions.str_to_int(response)
