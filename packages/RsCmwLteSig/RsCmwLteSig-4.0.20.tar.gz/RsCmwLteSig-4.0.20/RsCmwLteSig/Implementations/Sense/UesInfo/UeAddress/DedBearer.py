from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DedBearerCls:
	"""DedBearer commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dedBearer", core, parent)

	# noinspection PyTypeChecker
	class SeparateStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Idn: List[str]: string Dedicated bearer ID Example: '6 (-5, Voice) ' means dedicated bearer 6, mapped to default bearer 5, using dedicated bearer profile 'Voice'
			- Tft_Port_Low_Dl: List[int]: decimal Lower end of TFT port range assigned to the downlink Range: 1 to 65535
			- Tft_Port_High_Dl: List[int]: decimal Upper end of TFT port range assigned to the downlink Range: 1 to 65535
			- Tft_Port_Low_Ul: List[int]: decimal Lower end of TFT port range assigned to the uplink Range: 1 to 65535
			- Tft_Port_High_Ul: List[int]: decimal Upper end of TFT port range assigned to the uplink Range: 1 to 65535"""
		__meta_args_list = [
			ArgStruct('Idn', DataType.StringList, None, False, True, 1),
			ArgStruct('Tft_Port_Low_Dl', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Tft_Port_High_Dl', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Tft_Port_Low_Ul', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Tft_Port_High_Ul', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Idn: List[str] = None
			self.Tft_Port_Low_Dl: List[int] = None
			self.Tft_Port_High_Dl: List[int] = None
			self.Tft_Port_Low_Ul: List[int] = None
			self.Tft_Port_High_Ul: List[int] = None

	def get_separate(self) -> SeparateStruct:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UESinfo:UEADdress:DEDBearer:SEParate \n
		Snippet: value: SeparateStruct = driver.sense.uesInfo.ueAddress.dedBearer.get_separate() \n
		Returns information about all established dedicated bearers. Five values are returned per bearer: {<ID>, <TFTPortLowDL>,
		<TFTPortHighDL>, <TFTPortLowUL>, <TFTPortHighUL>}Bearer 1, ..., {...}Bearer n Use this command if you have configured
		separate port ranges for the uplink and the downlink. \n
			:return: structure: for return value, see the help for SeparateStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:LTE:SIGNaling<Instance>:UESinfo:UEADdress:DEDBearer:SEParate?', self.__class__.SeparateStruct())

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Idn: List[str]: string Dedicated bearer ID Example: '6 (-5, Voice) ' means dedicated bearer 6, mapped to default bearer 5, using dedicated bearer profile 'Voice'
			- Tft_Port_Low: List[int]: decimal Lower end of TFT port range assigned to the dedicated bearer Range: 1 to 65535
			- Tft_Port_High: List[int]: decimal Upper end of TFT port range assigned to the dedicated bearer Range: 1 to 65535"""
		__meta_args_list = [
			ArgStruct('Idn', DataType.StringList, None, False, True, 1),
			ArgStruct('Tft_Port_Low', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Tft_Port_High', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Idn: List[str] = None
			self.Tft_Port_Low: List[int] = None
			self.Tft_Port_High: List[int] = None

	def get_value(self) -> ValueStruct:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UESinfo:UEADdress:DEDBearer \n
		Snippet: value: ValueStruct = driver.sense.uesInfo.ueAddress.dedBearer.get_value() \n
		Returns information about all established dedicated bearers. Three values are returned per bearer: {<ID>, <TFTPortLow>,
		<TFTPortHigh>}Bearer 1, ..., {...}Bearer n Use this command if you have configured a single port range per bearer,
		applicable to the uplink and the downlink. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:LTE:SIGNaling<Instance>:UESinfo:UEADdress:DEDBearer?', self.__class__.ValueStruct())
