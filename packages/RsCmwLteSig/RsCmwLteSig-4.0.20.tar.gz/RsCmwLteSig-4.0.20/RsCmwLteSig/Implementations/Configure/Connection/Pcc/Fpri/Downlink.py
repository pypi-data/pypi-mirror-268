from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	def get_stti(self) -> List[bool]:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:FPRI:DL:STTI \n
		Snippet: value: List[bool] = driver.configure.connection.pcc.fpri.downlink.get_stti() \n
		Configures which subframes are scheduled for the DL of the scheduling type 'Follow WB PMI-RI'. For most subframes, the
		setting is fixed, depending on the duplex mode and the UL-DL configuration. For these subframes, your setting is ignored. \n
			:return: scheduled: OFF | ON Comma-separated list of 10 values, for subframe 0 to 9
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:FPRI:DL:STTI?')
		return Conversions.str_to_bool_list(response)

	def set_stti(self, scheduled: List[bool]) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:FPRI:DL:STTI \n
		Snippet: driver.configure.connection.pcc.fpri.downlink.set_stti(scheduled = [True, False, True]) \n
		Configures which subframes are scheduled for the DL of the scheduling type 'Follow WB PMI-RI'. For most subframes, the
		setting is fixed, depending on the duplex mode and the UL-DL configuration. For these subframes, your setting is ignored. \n
			:param scheduled: OFF | ON Comma-separated list of 10 values, for subframe 0 to 9
		"""
		param = Conversions.list_to_csv_str(scheduled)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:FPRI:DL:STTI {param}')

	def set(self, number_rb: int, start_rb: int, modulation: enums.Modulation, trans_block_size_idx: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:FPRI:DL \n
		Snippet: driver.configure.connection.pcc.fpri.downlink.set(number_rb = 1, start_rb = 1, modulation = enums.Modulation.Q1024, trans_block_size_idx = 1) \n
		Configures the downlink for the scheduling type 'Follow WB PMI-RI', with contiguous allocation. The allowed input ranges
		have dependencies and are described in the background information, see 'CQI channels'. \n
			:param number_rb: numeric Number of allocated resource blocks
			:param start_rb: numeric Position of first resource block
			:param modulation: QPSK | Q16 | Q64 | Q256 | Q1024 QPSK | 16-QAM | 64-QAM | 256-QAM | 1024-QAM
			:param trans_block_size_idx: numeric Transport block size index
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('number_rb', number_rb, DataType.Integer), ArgSingle('start_rb', start_rb, DataType.Integer), ArgSingle('modulation', modulation, DataType.Enum, enums.Modulation), ArgSingle('trans_block_size_idx', trans_block_size_idx, DataType.Integer))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:FPRI:DL {param}'.rstrip())

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

	def get(self) -> DownlinkStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:FPRI:DL \n
		Snippet: value: DownlinkStruct = driver.configure.connection.pcc.fpri.downlink.get() \n
		Configures the downlink for the scheduling type 'Follow WB PMI-RI', with contiguous allocation. The allowed input ranges
		have dependencies and are described in the background information, see 'CQI channels'. \n
			:return: structure: for return value, see the help for DownlinkStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:FPRI:DL?', self.__class__.DownlinkStruct())
