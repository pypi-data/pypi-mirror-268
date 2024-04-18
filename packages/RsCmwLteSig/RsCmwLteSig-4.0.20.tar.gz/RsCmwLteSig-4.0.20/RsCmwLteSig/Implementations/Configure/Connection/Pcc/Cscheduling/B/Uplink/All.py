from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, number_rb: int, start_rb: int, modulation: enums.Modulation, trans_block_size_idx: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:CSCHeduling:B:UL:ALL \n
		Snippet: driver.configure.connection.pcc.cscheduling.b.uplink.all.set(number_rb = 1, start_rb = 1, modulation = enums.Modulation.Q1024, trans_block_size_idx = 1) \n
		No command help available \n
			:param number_rb: No help available
			:param start_rb: No help available
			:param modulation: No help available
			:param trans_block_size_idx: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('number_rb', number_rb, DataType.Integer), ArgSingle('start_rb', start_rb, DataType.Integer), ArgSingle('modulation', modulation, DataType.Enum, enums.Modulation), ArgSingle('trans_block_size_idx', trans_block_size_idx, DataType.Integer))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:CSCHeduling:B:UL:ALL {param}'.rstrip())

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Response structure. Fields: \n
			- Number_Rb: int: No parameter help available
			- Start_Rb: int: No parameter help available
			- Modulation: enums.Modulation: No parameter help available
			- Trans_Block_Size_Idx: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Number_Rb'),
			ArgStruct.scalar_int('Start_Rb'),
			ArgStruct.scalar_enum('Modulation', enums.Modulation),
			ArgStruct.scalar_int('Trans_Block_Size_Idx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number_Rb: int = None
			self.Start_Rb: int = None
			self.Modulation: enums.Modulation = None
			self.Trans_Block_Size_Idx: int = None

	def get(self) -> AllStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:CSCHeduling:B:UL:ALL \n
		Snippet: value: AllStruct = driver.configure.connection.pcc.cscheduling.b.uplink.all.get() \n
		No command help available \n
			:return: structure: for return value, see the help for AllStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:CSCHeduling:B:UL:ALL?', self.__class__.AllStruct())
