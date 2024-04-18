from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 2 total commands, 1 Subgroups, 1 group commands
	Repeated Capability: Stream, default value after init: Stream.S1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_stream_get', 'repcap_stream_set', repcap.Stream.S1)

	def repcap_stream_set(self, stream: repcap.Stream) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Stream.Default
		Default value after init: Stream.S1"""
		self._cmd_group.set_repcap_enum_value(stream)

	def repcap_stream_get(self) -> repcap.Stream:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	def set(self, tti: float, number_rb: int or bool, start_rb: int or bool, modulation: enums.Modulation, trans_block_size_idx: int or bool, stream=repcap.Stream.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDTTibased:DL<Stream> \n
		Snippet: driver.configure.connection.pcc.udttiBased.downlink.set(tti = 1.0, number_rb = 1, start_rb = 1, modulation = enums.Modulation.Q1024, trans_block_size_idx = 1, stream = repcap.Stream.Default) \n
		Configures a selected downlink subframe for the scheduling type 'User-defined TTI-Based'. The allowed input ranges have
		dependencies and are described in the background information, see 'User-defined channels'. A query for TDD can also
		return OFF,OFF,OFF,OFF, indicating that the queried subframe is no DL subframe. \n
			:param tti: numeric Number of the subframe to be configured/queried. Range: 0 to 9
			:param number_rb: (integer or boolean) numeric | OFF Number of allocated resource blocks. The same value must be configured for all streams.
			:param start_rb: (integer or boolean) numeric | OFF Position of first resource block. The same value must be configured for all streams of the carrier.
			:param modulation: QPSK | Q16 | Q64 | Q256 | Q1024 | OFF QPSK | 16-QAM | 64-QAM | 256-QAM | 1024-QAM | no DL subframe
			:param trans_block_size_idx: (integer or boolean) numeric | OFF Transport block size index
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Downlink')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('tti', tti, DataType.Float), ArgSingle('number_rb', number_rb, DataType.IntegerExt), ArgSingle('start_rb', start_rb, DataType.IntegerExt), ArgSingle('modulation', modulation, DataType.Enum, enums.Modulation), ArgSingle('trans_block_size_idx', trans_block_size_idx, DataType.IntegerExt))
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDTTibased:DL{stream_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Number_Rb: int or bool: numeric | OFF Number of allocated resource blocks. The same value must be configured for all streams.
			- Start_Rb: int or bool: numeric | OFF Position of first resource block. The same value must be configured for all streams of the carrier.
			- Modulation: enums.Modulation: QPSK | Q16 | Q64 | Q256 | Q1024 | OFF QPSK | 16-QAM | 64-QAM | 256-QAM | 1024-QAM | no DL subframe
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

	def get(self, tti: float, stream=repcap.Stream.Default) -> GetStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:UDTTibased:DL<Stream> \n
		Snippet: value: GetStruct = driver.configure.connection.pcc.udttiBased.downlink.get(tti = 1.0, stream = repcap.Stream.Default) \n
		Configures a selected downlink subframe for the scheduling type 'User-defined TTI-Based'. The allowed input ranges have
		dependencies and are described in the background information, see 'User-defined channels'. A query for TDD can also
		return OFF,OFF,OFF,OFF, indicating that the queried subframe is no DL subframe. \n
			:param tti: numeric Number of the subframe to be configured/queried. Range: 0 to 9
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Downlink')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = Conversions.decimal_value_to_str(tti)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:UDTTibased:DL{stream_cmd_val}? {param}', self.__class__.GetStruct())

	def clone(self) -> 'DownlinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DownlinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
