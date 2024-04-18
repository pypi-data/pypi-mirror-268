from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	@property
	def anb(self):
		"""anb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_anb'):
			from .Anb import AnbCls
			self._anb = AnbCls(self._core, self._cmd_group)
		return self._anb

	def set(self, number_rb: int, start_rb: int, modulation: enums.Modulation, trans_block_size_idx: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDCHannels:EMTC:A:DL \n
		Snippet: driver.configure.connection.pcc.udChannels.emtc.a.downlink.set(number_rb = 1, start_rb = 1, modulation = enums.Modulation.Q1024, trans_block_size_idx = 1) \n
		Configures a user-defined downlink channel for eMTC, CE mode A. The ranges have dependencies described in the background
		information, see 'User-defined channels for eMTC'. \n
			:param number_rb: numeric Number of allocated resource blocks Range: 0 to 4
			:param start_rb: numeric Range: 0 to 4
			:param modulation: QPSK | Q16 Modulation type QPSK | 16-QAM
			:param trans_block_size_idx: numeric Range: 0 to 14
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('number_rb', number_rb, DataType.Integer), ArgSingle('start_rb', start_rb, DataType.Integer), ArgSingle('modulation', modulation, DataType.Enum, enums.Modulation), ArgSingle('trans_block_size_idx', trans_block_size_idx, DataType.Integer))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDCHannels:EMTC:A:DL {param}'.rstrip())

	# noinspection PyTypeChecker
	class DownlinkStruct(StructBase):
		"""Response structure. Fields: \n
			- Number_Rb: int: numeric Number of allocated resource blocks Range: 0 to 4
			- Start_Rb: int: numeric Range: 0 to 4
			- Modulation: enums.Modulation: QPSK | Q16 Modulation type QPSK | 16-QAM
			- Trans_Block_Size_Idx: int: numeric Range: 0 to 14"""
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

	def get(self) -> DownlinkStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDCHannels:EMTC:A:DL \n
		Snippet: value: DownlinkStruct = driver.configure.connection.pcc.udChannels.emtc.a.downlink.get() \n
		Configures a user-defined downlink channel for eMTC, CE mode A. The ranges have dependencies described in the background
		information, see 'User-defined channels for eMTC'. \n
			:return: structure: for return value, see the help for DownlinkStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDCHannels:EMTC:A:DL?', self.__class__.DownlinkStruct())

	def clone(self) -> 'DownlinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DownlinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
