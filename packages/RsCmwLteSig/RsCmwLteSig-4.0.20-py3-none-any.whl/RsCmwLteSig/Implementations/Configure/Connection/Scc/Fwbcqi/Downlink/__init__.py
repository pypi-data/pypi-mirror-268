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
	"""Downlink commands group definition. 5 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	@property
	def stti(self):
		"""stti commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stti'):
			from .Stti import SttiCls
			self._stti = SttiCls(self._core, self._cmd_group)
		return self._stti

	@property
	def mcsTable(self):
		"""mcsTable commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mcsTable'):
			from .McsTable import McsTableCls
			self._mcsTable = McsTableCls(self._core, self._cmd_group)
		return self._mcsTable

	def set(self, number_rb: int, start_rb: int, table: enums.MultiClusterDlTable, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:FWBCqi:DL \n
		Snippet: driver.configure.connection.scc.fwbcqi.downlink.set(number_rb = 1, start_rb = 1, table = enums.MultiClusterDlTable.DETermined, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the downlink for the scheduling type 'Follow WB CQI', with contiguous RB allocation. The allowed input ranges
		have dependencies and are described in the background information, see 'CQI channels'. \n
			:param number_rb: numeric Number of allocated resource blocks
			:param start_rb: numeric Position of first resource block
			:param table: DETermined | UDEFined DETermined: Automatic CQI-MCS mapping table UDEFined: User-defined mapping table
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('number_rb', number_rb, DataType.Integer), ArgSingle('start_rb', start_rb, DataType.Integer), ArgSingle('table', table, DataType.Enum, enums.MultiClusterDlTable))
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:FWBCqi:DL {param}'.rstrip())

	# noinspection PyTypeChecker
	class DownlinkStruct(StructBase):
		"""Response structure. Fields: \n
			- Number_Rb: int: numeric Number of allocated resource blocks
			- Start_Rb: int: numeric Position of first resource block
			- Table: enums.MultiClusterDlTable: DETermined | UDEFined DETermined: Automatic CQI-MCS mapping table UDEFined: User-defined mapping table"""
		__meta_args_list = [
			ArgStruct.scalar_int('Number_Rb'),
			ArgStruct.scalar_int('Start_Rb'),
			ArgStruct.scalar_enum('Table', enums.MultiClusterDlTable)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Number_Rb: int = None
			self.Start_Rb: int = None
			self.Table: enums.MultiClusterDlTable = None

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> DownlinkStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:FWBCqi:DL \n
		Snippet: value: DownlinkStruct = driver.configure.connection.scc.fwbcqi.downlink.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the downlink for the scheduling type 'Follow WB CQI', with contiguous RB allocation. The allowed input ranges
		have dependencies and are described in the background information, see 'CQI channels'. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: structure: for return value, see the help for DownlinkStruct structure arguments."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:FWBCqi:DL?', self.__class__.DownlinkStruct())

	def clone(self) -> 'DownlinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DownlinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
