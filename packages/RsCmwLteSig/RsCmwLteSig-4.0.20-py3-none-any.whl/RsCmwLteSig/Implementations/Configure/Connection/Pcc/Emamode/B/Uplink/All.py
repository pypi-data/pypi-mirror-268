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

	def set(self, number_rb: enums.NumberRb, start_rb: int, narrow_band: int, modulation: enums.Modulation, transp_block_size_idx: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:EMAMode:B:UL:ALL \n
		Snippet: driver.configure.connection.pcc.emamode.b.uplink.all.set(number_rb = enums.NumberRb.N1, start_rb = 1, narrow_band = 1, modulation = enums.Modulation.Q1024, transp_block_size_idx = 1) \n
		Configures the eMTC auto mode, uplink, for CE mode B. The indicated input ranges list all possible values. The ranges
		have dependencies described in the background information, see 'eMTC auto mode'. \n
			:param number_rb: ZERO | N1 | N2 Number of allocated resource blocks
			:param start_rb: numeric Position of first resource block Range: 0 to 5
			:param narrow_band: numeric Narrowband for the first transmission Range: 0 to 15
			:param modulation: QPSK Modulation type QPSK
			:param transp_block_size_idx: numeric Transport block size index Range: 0 to 10
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('number_rb', number_rb, DataType.Enum, enums.NumberRb), ArgSingle('start_rb', start_rb, DataType.Integer), ArgSingle('narrow_band', narrow_band, DataType.Integer), ArgSingle('modulation', modulation, DataType.Enum, enums.Modulation), ArgSingle('transp_block_size_idx', transp_block_size_idx, DataType.Integer))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:EMAMode:B:UL:ALL {param}'.rstrip())

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Response structure. Fields: \n
			- Number_Rb: enums.NumberRb: ZERO | N1 | N2 Number of allocated resource blocks
			- Start_Rb: int: numeric Position of first resource block Range: 0 to 5
			- Narrow_Band: int: numeric Narrowband for the first transmission Range: 0 to 15
			- Modulation: enums.Modulation: QPSK Modulation type QPSK
			- Transp_Block_Size_Idx: int: numeric Transport block size index Range: 0 to 10"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Number_Rb', enums.NumberRb),
			ArgStruct.scalar_int('Start_Rb'),
			ArgStruct.scalar_int('Narrow_Band'),
			ArgStruct.scalar_enum('Modulation', enums.Modulation),
			ArgStruct.scalar_int('Transp_Block_Size_Idx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number_Rb: enums.NumberRb = None
			self.Start_Rb: int = None
			self.Narrow_Band: int = None
			self.Modulation: enums.Modulation = None
			self.Transp_Block_Size_Idx: int = None

	def get(self) -> AllStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:EMAMode:B:UL:ALL \n
		Snippet: value: AllStruct = driver.configure.connection.pcc.emamode.b.uplink.all.get() \n
		Configures the eMTC auto mode, uplink, for CE mode B. The indicated input ranges list all possible values. The ranges
		have dependencies described in the background information, see 'eMTC auto mode'. \n
			:return: structure: for return value, see the help for AllStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:EMAMode:B:UL:ALL?', self.__class__.AllStruct())
