from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 1 total commands, 0 Subgroups, 1 group commands
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

	def set(self, number_rb: int, start_rb: int, modulation: enums.Modulation, trans_block_size_idx: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, stream=repcap.Stream.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:UDCHannels:DL<Stream> \n
		Snippet: driver.configure.connection.scc.udChannels.downlink.set(number_rb = 1, start_rb = 1, modulation = enums.Modulation.Q1024, trans_block_size_idx = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default, stream = repcap.Stream.Default) \n
		Configures a user-defined downlink channel with contiguous allocation (no LAA, no eMTC) . The <NumberRB> and <StartRB>
		settings apply to all DL streams. The other settings apply to DL stream <s>. The allowed input ranges have dependencies
		and are described in the background information, see 'User-defined channels'. \n
			:param number_rb: numeric Number of allocated resource blocks
			:param start_rb: numeric Position of first resource block
			:param modulation: QPSK | Q16 | Q64 | Q256 | Q1024 QPSK | 16-QAM | 64-QAM | 256-QAM | 1024-QAM
			:param trans_block_size_idx: numeric Transport block size index
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Downlink')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('number_rb', number_rb, DataType.Integer), ArgSingle('start_rb', start_rb, DataType.Integer), ArgSingle('modulation', modulation, DataType.Enum, enums.Modulation), ArgSingle('trans_block_size_idx', trans_block_size_idx, DataType.Integer))
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:UDCHannels:DL{stream_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class DownlinkStruct(StructBase):
		"""Response structure. Fields: \n
			- Number_Rb: int: numeric Number of allocated resource blocks
			- Start_Rb: int: numeric Position of first resource block
			- Modulation: enums.Modulation: QPSK | Q16 | Q64 | Q256 | Q1024 QPSK | 16-QAM | 64-QAM | 256-QAM | 1024-QAM
			- Trans_Block_Size_Idx: int: numeric Transport block size index"""
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

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, stream=repcap.Stream.Default) -> DownlinkStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:UDCHannels:DL<Stream> \n
		Snippet: value: DownlinkStruct = driver.configure.connection.scc.udChannels.downlink.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default, stream = repcap.Stream.Default) \n
		Configures a user-defined downlink channel with contiguous allocation (no LAA, no eMTC) . The <NumberRB> and <StartRB>
		settings apply to all DL streams. The other settings apply to DL stream <s>. The allowed input ranges have dependencies
		and are described in the background information, see 'User-defined channels'. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Downlink')
			:return: structure: for return value, see the help for DownlinkStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:UDCHannels:DL{stream_cmd_val}?', self.__class__.DownlinkStruct())

	def clone(self) -> 'DownlinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DownlinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
