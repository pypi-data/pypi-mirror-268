from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DownlinkCls:
	"""Downlink commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	def set(self, cluster: str, modulation: enums.Modulation, trans_block_size_idx: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:FPMI:MCLuster:DL \n
		Snippet: driver.configure.connection.pcc.fpmi.mcluster.downlink.set(cluster = rawAbc, modulation = enums.Modulation.Q1024, trans_block_size_idx = 1) \n
		Configures the downlink for the scheduling type 'Follow WB PMI', with multi-cluster allocation. The allowed input ranges
		have dependencies and are described in the background information, see 'CQI channels' and especially Table 'RBG
		parameters'. \n
			:param cluster: binary Bitmap, enabling or disabling the individual RBGs 1 means RBG is allocated, 0 means RBG is not allocated The number of bits depends on the cell bandwidth and equals the total number of RBGs. The bitmap starts with RBG 0 (most significant bit) and continues with increasing RBG index / frequency. Example for BW 1.4 MHz: #B101010 means that the RBGs 0, 2 and 4 are allocated
			:param modulation: QPSK | Q16 | Q64 | Q256 | Q1024 QPSK | 16-QAM | 64-QAM | 256-QAM | 1024-QAM
			:param trans_block_size_idx: numeric Transport block size index
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cluster', cluster, DataType.RawString), ArgSingle('modulation', modulation, DataType.Enum, enums.Modulation), ArgSingle('trans_block_size_idx', trans_block_size_idx, DataType.Integer))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:FPMI:MCLuster:DL {param}'.rstrip())

	# noinspection PyTypeChecker
	class DownlinkStruct(StructBase):
		"""Response structure. Fields: \n
			- Cluster: str: binary Bitmap, enabling or disabling the individual RBGs 1 means RBG is allocated, 0 means RBG is not allocated The number of bits depends on the cell bandwidth and equals the total number of RBGs. The bitmap starts with RBG 0 (most significant bit) and continues with increasing RBG index / frequency. Example for BW 1.4 MHz: #B101010 means that the RBGs 0, 2 and 4 are allocated
			- Modulation: enums.Modulation: QPSK | Q16 | Q64 | Q256 | Q1024 QPSK | 16-QAM | 64-QAM | 256-QAM | 1024-QAM
			- Trans_Block_Size_Idx: int: numeric Transport block size index"""
		__meta_args_list = [
			ArgStruct.scalar_raw_str('Cluster'),
			ArgStruct.scalar_enum('Modulation', enums.Modulation),
			ArgStruct.scalar_int('Trans_Block_Size_Idx')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cluster: str = None
			self.Modulation: enums.Modulation = None
			self.Trans_Block_Size_Idx: int = None

	def get(self) -> DownlinkStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:FPMI:MCLuster:DL \n
		Snippet: value: DownlinkStruct = driver.configure.connection.pcc.fpmi.mcluster.downlink.get() \n
		Configures the downlink for the scheduling type 'Follow WB PMI', with multi-cluster allocation. The allowed input ranges
		have dependencies and are described in the background information, see 'CQI channels' and especially Table 'RBG
		parameters'. \n
			:return: structure: for return value, see the help for DownlinkStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:FPMI:MCLuster:DL?', self.__class__.DownlinkStruct())
