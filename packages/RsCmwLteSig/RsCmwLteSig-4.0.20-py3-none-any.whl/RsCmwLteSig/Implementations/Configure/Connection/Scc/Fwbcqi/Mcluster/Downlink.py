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
class DownlinkCls:
	"""Downlink commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	def set(self, cluster: str, table: enums.MultiClusterDlTable, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:FWBCqi:MCLuster:DL \n
		Snippet: driver.configure.connection.scc.fwbcqi.mcluster.downlink.set(cluster = rawAbc, table = enums.MultiClusterDlTable.DETermined, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the downlink for the scheduling type 'Follow WB CQI', with multi-cluster allocation. The allowed input ranges
		have dependencies and are described in the background information, see 'CQI channels' and especially Table 'RBG
		parameters'. \n
			:param cluster: binary Bitmap, enabling or disabling the individual RBGs 1 means RBG is allocated, 0 means RBG is not allocated The number of bits depends on the cell bandwidth and equals the total number of RBGs. The bitmap starts with RBG 0 (most significant bit) and continues with increasing RBG index / frequency. Example for BW 1.4 MHz: #B101010 means that the RBGs 0, 2 and 4 are allocated
			:param table: DETermined | UDEFined DETermined: Automatic CQI-MCS mapping table UDEFined: User-defined mapping table
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('cluster', cluster, DataType.RawString), ArgSingle('table', table, DataType.Enum, enums.MultiClusterDlTable))
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:FWBCqi:MCLuster:DL {param}'.rstrip())

	# noinspection PyTypeChecker
	class DownlinkStruct(StructBase):
		"""Response structure. Fields: \n
			- Cluster: str: binary Bitmap, enabling or disabling the individual RBGs 1 means RBG is allocated, 0 means RBG is not allocated The number of bits depends on the cell bandwidth and equals the total number of RBGs. The bitmap starts with RBG 0 (most significant bit) and continues with increasing RBG index / frequency. Example for BW 1.4 MHz: #B101010 means that the RBGs 0, 2 and 4 are allocated
			- Table: enums.MultiClusterDlTable: DETermined | UDEFined DETermined: Automatic CQI-MCS mapping table UDEFined: User-defined mapping table"""
		__meta_args_list = [
			ArgStruct.scalar_raw_str('Cluster'),
			ArgStruct.scalar_enum('Table', enums.MultiClusterDlTable)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Cluster: str = None
			self.Table: enums.MultiClusterDlTable = None

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> DownlinkStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:FWBCqi:MCLuster:DL \n
		Snippet: value: DownlinkStruct = driver.configure.connection.scc.fwbcqi.mcluster.downlink.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the downlink for the scheduling type 'Follow WB CQI', with multi-cluster allocation. The allowed input ranges
		have dependencies and are described in the background information, see 'CQI channels' and especially Table 'RBG
		parameters'. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for DownlinkStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:FWBCqi:MCLuster:DL?', self.__class__.DownlinkStruct())
