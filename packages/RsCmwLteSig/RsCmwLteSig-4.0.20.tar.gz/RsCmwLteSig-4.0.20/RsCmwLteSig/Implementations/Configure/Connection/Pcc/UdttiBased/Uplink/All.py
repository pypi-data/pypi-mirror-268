from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, number_rb: List[int or bool], start_rb: List[int or bool], modulation: List[enums.Modulation], trans_block_size_idx: List[int or bool]) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDTTibased:UL:ALL \n
		Snippet: driver.configure.connection.pcc.udttiBased.uplink.all.set(number_rb = [1, True, 2, False, 3], start_rb = [1, True, 2, False, 3], modulation = [Modulation.Q1024, Modulation.QPSK], trans_block_size_idx = [1, True, 2, False, 3]) \n
		Configures the uplink channel for all scheduling types with a TTI-based UL definition. The parameters are entered 10
		times, so that all subframes are configured by a single command (index = subframe number 0 to 9) : <NumberRB>0, ...
		, <NumberRB>9, <StartRB>0, ..., <StartRB>9, <Modulation>0, ..., <Modulation>9, <TransBlockSizeIdx>0, ...
		, <TransBlockSizeIdx>9 The allowed input ranges have dependencies and are described in the background information, see
		'User-defined channels'. For TDD DL and special subframes, you can set OFF or specify a number from the allowed input
		range. The effect is the same. A query returns OFF for non-UL subframes. For UL-DL configuration 0, the settings
		specified for subframe number 2 are automatically applied to all UL subframes. \n
			:param number_rb: (integer or boolean items) numeric | OFF Number of allocated resource blocks
			:param start_rb: (integer or boolean items) numeric | OFF Position of first resource block
			:param modulation: QPSK | Q16 | Q64 | Q256 | OFF QPSK | 16-QAM | 64-QAM | 256-QAM | no UL subframe
			:param trans_block_size_idx: (integer or boolean items) numeric | OFF Transport block size index
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('number_rb', number_rb, DataType.IntegerExtList, None, False, False, 10), ArgSingle('start_rb', start_rb, DataType.IntegerExtList, None, False, False, 10), ArgSingle('modulation', modulation, DataType.EnumList, enums.Modulation, False, False, 10), ArgSingle('trans_block_size_idx', trans_block_size_idx, DataType.IntegerExtList, None, False, False, 10))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDTTibased:UL:ALL {param}'.rstrip())

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Response structure. Fields: \n
			- Number_Rb: List[int or bool]: numeric | OFF Number of allocated resource blocks
			- Start_Rb: List[int or bool]: numeric | OFF Position of first resource block
			- Modulation: List[enums.Modulation]: QPSK | Q16 | Q64 | Q256 | OFF QPSK | 16-QAM | 64-QAM | 256-QAM | no UL subframe
			- Trans_Block_Size_Idx: List[int or bool]: numeric | OFF Transport block size index"""
		__meta_args_list = [
			ArgStruct('Number_Rb', DataType.IntegerExtList, None, False, False, 10),
			ArgStruct('Start_Rb', DataType.IntegerExtList, None, False, False, 10),
			ArgStruct('Modulation', DataType.EnumList, enums.Modulation, False, False, 10),
			ArgStruct('Trans_Block_Size_Idx', DataType.IntegerExtList, None, False, False, 10)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number_Rb: List[int or bool] = None
			self.Start_Rb: List[int or bool] = None
			self.Modulation: List[enums.Modulation] = None
			self.Trans_Block_Size_Idx: List[int or bool] = None

	def get(self) -> AllStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDTTibased:UL:ALL \n
		Snippet: value: AllStruct = driver.configure.connection.pcc.udttiBased.uplink.all.get() \n
		Configures the uplink channel for all scheduling types with a TTI-based UL definition. The parameters are entered 10
		times, so that all subframes are configured by a single command (index = subframe number 0 to 9) : <NumberRB>0, ...
		, <NumberRB>9, <StartRB>0, ..., <StartRB>9, <Modulation>0, ..., <Modulation>9, <TransBlockSizeIdx>0, ...
		, <TransBlockSizeIdx>9 The allowed input ranges have dependencies and are described in the background information, see
		'User-defined channels'. For TDD DL and special subframes, you can set OFF or specify a number from the allowed input
		range. The effect is the same. A query returns OFF for non-UL subframes. For UL-DL configuration 0, the settings
		specified for subframe number 2 are automatically applied to all UL subframes. \n
			:return: structure: for return value, see the help for AllStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDTTibased:UL:ALL?', self.__class__.AllStruct())
