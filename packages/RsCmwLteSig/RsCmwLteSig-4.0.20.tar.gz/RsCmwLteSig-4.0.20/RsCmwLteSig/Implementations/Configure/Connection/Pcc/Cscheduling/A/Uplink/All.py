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
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:CSCHeduling:A:UL:ALL \n
		Snippet: driver.configure.connection.pcc.cscheduling.a.uplink.all.set(number_rb = 1, start_rb = 1, modulation = enums.Modulation.Q1024, trans_block_size_idx = 1) \n
		Configures eMTC compact scheduling, uplink, for CE mode A. The indicated input ranges list all possible values.
		The ranges have dependencies described in the background information, see 'eMTC compact scheduling'. \n
			:param number_rb: numeric Number of allocated resource blocks Range: 0 to 24
			:param start_rb: numeric Position of first resource block Range: 0 to 6
			:param modulation: QPSK | Q16 Modulation type QPSK | 16-QAM
			:param trans_block_size_idx: numeric Range: 0 to 14, 16 to 21
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('number_rb', number_rb, DataType.Integer), ArgSingle('start_rb', start_rb, DataType.Integer), ArgSingle('modulation', modulation, DataType.Enum, enums.Modulation), ArgSingle('trans_block_size_idx', trans_block_size_idx, DataType.Integer))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:CSCHeduling:A:UL:ALL {param}'.rstrip())

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Response structure. Fields: \n
			- Number_Rb: int: numeric Number of allocated resource blocks Range: 0 to 24
			- Start_Rb: int: numeric Position of first resource block Range: 0 to 6
			- Modulation: enums.Modulation: QPSK | Q16 Modulation type QPSK | 16-QAM
			- Trans_Block_Size_Idx: int: numeric Range: 0 to 14, 16 to 21"""
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
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:CSCHeduling:A:UL:ALL \n
		Snippet: value: AllStruct = driver.configure.connection.pcc.cscheduling.a.uplink.all.get() \n
		Configures eMTC compact scheduling, uplink, for CE mode A. The indicated input ranges list all possible values.
		The ranges have dependencies described in the background information, see 'eMTC compact scheduling'. \n
			:return: structure: for return value, see the help for AllStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:CSCHeduling:A:UL:ALL?', self.__class__.AllStruct())
