from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllCls:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def set(self, number_rb: List[int or bool], start_rb: List[int or bool], modulation: List[enums.Modulation], trans_block_size_idx: List[int or bool], secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, stream=repcap.Stream.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:UDTTibased:DL<Stream>:ALL \n
		Snippet: driver.configure.connection.scc.udttiBased.downlink.all.set(number_rb = [1, True, 2, False, 3], start_rb = [1, True, 2, False, 3], modulation = [Modulation.Q1024, Modulation.QPSK], trans_block_size_idx = [1, True, 2, False, 3], secondaryCompCarrier = repcap.SecondaryCompCarrier.Default, stream = repcap.Stream.Default) \n
		Configures all downlink subframes for the scheduling type 'User-defined TTI-Based'. The parameters are entered 10 times,
		so that all subframes are configured by a single command (index = subframe number 0 to 9) : <NumberRB>0, ..., <NumberRB>9,
		<StartRB>0, ..., <StartRB>9, <Modulation>0, ..., <Modulation>9, <TransBlockSizeIdx>0, ..., <TransBlockSizeIdx>9 The
		allowed input ranges have dependencies and are described in the background information, see 'User-defined channels'. For
		TDD UL and special subframes, you can set OFF or specify a number from the allowed input range. The effect is the same. A
		query returns OFF for non-DL subframes. \n
			:param number_rb: (integer or boolean items) numeric | OFF Number of allocated resource blocks. The same value must be configured for all streams of the carrier.
			:param start_rb: (integer or boolean items) numeric | OFF Position of first resource block. The same value must be configured for all streams of the carrier.
			:param modulation: QPSK | Q16 | Q64 | Q256 | Q1024 | OFF QPSK | 16-QAM | 64-QAM | 256-QAM | 1024-QAM | no DL subframe
			:param trans_block_size_idx: (integer or boolean items) numeric | OFF Transport block size index
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Downlink')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('number_rb', number_rb, DataType.IntegerExtList, None, False, False, 10), ArgSingle('start_rb', start_rb, DataType.IntegerExtList, None, False, False, 10), ArgSingle('modulation', modulation, DataType.EnumList, enums.Modulation, False, False, 10), ArgSingle('trans_block_size_idx', trans_block_size_idx, DataType.IntegerExtList, None, False, False, 10))
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:UDTTibased:DL{stream_cmd_val}:ALL {param}'.rstrip())

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Response structure. Fields: \n
			- Number_Rb: List[int or bool]: numeric | OFF Number of allocated resource blocks. The same value must be configured for all streams of the carrier.
			- Start_Rb: List[int or bool]: numeric | OFF Position of first resource block. The same value must be configured for all streams of the carrier.
			- Modulation: List[enums.Modulation]: QPSK | Q16 | Q64 | Q256 | Q1024 | OFF QPSK | 16-QAM | 64-QAM | 256-QAM | 1024-QAM | no DL subframe
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

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, stream=repcap.Stream.Default) -> AllStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:UDTTibased:DL<Stream>:ALL \n
		Snippet: value: AllStruct = driver.configure.connection.scc.udttiBased.downlink.all.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default, stream = repcap.Stream.Default) \n
		Configures all downlink subframes for the scheduling type 'User-defined TTI-Based'. The parameters are entered 10 times,
		so that all subframes are configured by a single command (index = subframe number 0 to 9) : <NumberRB>0, ..., <NumberRB>9,
		<StartRB>0, ..., <StartRB>9, <Modulation>0, ..., <Modulation>9, <TransBlockSizeIdx>0, ..., <TransBlockSizeIdx>9 The
		allowed input ranges have dependencies and are described in the background information, see 'User-defined channels'. For
		TDD UL and special subframes, you can set OFF or specify a number from the allowed input range. The effect is the same. A
		query returns OFF for non-DL subframes. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param stream: optional repeated capability selector. Default value: S1 (settable in the interface 'Downlink')
			:return: structure: for return value, see the help for AllStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:UDTTibased:DL{stream_cmd_val}:ALL?', self.__class__.AllStruct())
