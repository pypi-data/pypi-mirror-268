from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	def set(self, tti: float, number_rb: int or bool, start_rb: int or bool, modulation: enums.Modulation, trans_block_size_idx: int or bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDTTibased:UL \n
		Snippet: driver.configure.connection.pcc.udttiBased.uplink.set(tti = 1.0, number_rb = 1, start_rb = 1, modulation = enums.Modulation.Q1024, trans_block_size_idx = 1) \n
		Configures a selected uplink subframe for all scheduling types with a TTI-based UL definition. The allowed input ranges
		have dependencies and are described in the background information, see 'User-defined channels'. A query for TDD can also
		return OFF,OFF,OFF,OFF, indicating that the queried subframe is no UL subframe. For UL-DL configuration 0, use the
		command method RsCmwLteSig.Configure.Connection.Scc.UdttiBased.Uplink.All.set. \n
			:param tti: numeric Number of the subframe to be configured/queried. Range: 0 to 9
			:param number_rb: (integer or boolean) numeric | OFF Number of allocated resource blocks
			:param start_rb: (integer or boolean) numeric | OFF Position of first resource block
			:param modulation: QPSK | Q16 | Q64 | Q256 | OFF QPSK | 16-QAM | 64-QAM | 256-QAM | no UL subframe
			:param trans_block_size_idx: (integer or boolean) numeric | OFF Transport block size index
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('tti', tti, DataType.Float), ArgSingle('number_rb', number_rb, DataType.IntegerExt), ArgSingle('start_rb', start_rb, DataType.IntegerExt), ArgSingle('modulation', modulation, DataType.Enum, enums.Modulation), ArgSingle('trans_block_size_idx', trans_block_size_idx, DataType.IntegerExt))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDTTibased:UL {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Number_Rb: int or bool: numeric | OFF Number of allocated resource blocks
			- Start_Rb: int or bool: numeric | OFF Position of first resource block
			- Modulation: enums.Modulation: QPSK | Q16 | Q64 | Q256 | OFF QPSK | 16-QAM | 64-QAM | 256-QAM | no UL subframe
			- Trans_Block_Size_Idx: int or bool: numeric | OFF Transport block size index"""
		__meta_args_list = [
			ArgStruct.scalar_int_ext('Number_Rb'),
			ArgStruct.scalar_int_ext('Start_Rb'),
			ArgStruct.scalar_enum('Modulation', enums.Modulation),
			ArgStruct.scalar_int_ext('Trans_Block_Size_Idx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number_Rb: int or bool = None
			self.Start_Rb: int or bool = None
			self.Modulation: enums.Modulation = None
			self.Trans_Block_Size_Idx: int or bool = None

	def get(self, tti: float) -> GetStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDTTibased:UL \n
		Snippet: value: GetStruct = driver.configure.connection.pcc.udttiBased.uplink.get(tti = 1.0) \n
		Configures a selected uplink subframe for all scheduling types with a TTI-based UL definition. The allowed input ranges
		have dependencies and are described in the background information, see 'User-defined channels'. A query for TDD can also
		return OFF,OFF,OFF,OFF, indicating that the queried subframe is no UL subframe. For UL-DL configuration 0, use the
		command method RsCmwLteSig.Configure.Connection.Scc.UdttiBased.Uplink.All.set. \n
			:param tti: numeric Number of the subframe to be configured/queried. Range: 0 to 9
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.decimal_value_to_str(tti)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDTTibased:UL? {param}', self.__class__.GetStruct())

	def clone(self) -> 'UplinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UplinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
