from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, enable: List[bool] = None, band: List[enums.OperatingBandC] = None) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UECapability:RFBands:ALL \n
		Snippet: driver.configure.ueCapability.rfBands.all.set(enable = [True, False, True], band = [OperatingBandC.OB1, OperatingBandC.UDEFined]) \n
		Configures the list of operating bands for the information element 'requestedFrequencyBands' of the 'ueCapabilityEnquiry'
		message. The command has 32 parameters, for 16 entries with two parameters each: {<Enable>, <Band>}entry 1, {<Enable>,
		<Band>}entry 2, ..., {<Enable>, <Band>}entry 16 \n
			:param enable: OFF | ON Disables or enables the entry
			:param band: UDEFined | OB1 | ... | OB46 | OB48 | ... | OB53 | OB65 | ... | OB76 | OB85 | OB87 | OB88 | OB250 | OB252 | OB255 Assigns a band to the entry
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.BooleanList, None, True, True, 1), ArgSingle('band', band, DataType.EnumList, enums.OperatingBandC, True, True, 1))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UECapability:RFBands:ALL {param}'.rstrip())

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: List[bool]: OFF | ON Disables or enables the entry
			- Band: List[enums.OperatingBandC]: UDEFined | OB1 | ... | OB46 | OB48 | ... | OB53 | OB65 | ... | OB76 | OB85 | OB87 | OB88 | OB250 | OB252 | OB255 Assigns a band to the entry"""
		__meta_args_list = [
			ArgStruct('Enable', DataType.BooleanList, None, False, True, 1),
			ArgStruct('Band', DataType.EnumList, enums.OperatingBandC, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: List[bool] = None
			self.Band: List[enums.OperatingBandC] = None

	def get(self) -> AllStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UECapability:RFBands:ALL \n
		Snippet: value: AllStruct = driver.configure.ueCapability.rfBands.all.get() \n
		Configures the list of operating bands for the information element 'requestedFrequencyBands' of the 'ueCapabilityEnquiry'
		message. The command has 32 parameters, for 16 entries with two parameters each: {<Enable>, <Band>}entry 1, {<Enable>,
		<Band>}entry 2, ..., {<Enable>, <Band>}entry 16 \n
			:return: structure: for return value, see the help for AllStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:UECapability:RFBands:ALL?', self.__class__.AllStruct())
