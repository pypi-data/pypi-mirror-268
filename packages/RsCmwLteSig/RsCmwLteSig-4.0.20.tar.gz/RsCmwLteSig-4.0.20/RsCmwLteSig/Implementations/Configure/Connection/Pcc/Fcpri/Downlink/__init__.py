from typing import List

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
class DownlinkCls:
	"""Downlink commands group definition. 5 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("downlink", core, parent)

	@property
	def mcsTable(self):
		"""mcsTable commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcsTable'):
			from .McsTable import McsTableCls
			self._mcsTable = McsTableCls(self._core, self._cmd_group)
		return self._mcsTable

	def get_stti(self) -> List[bool]:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:FCPRi:DL:STTI \n
		Snippet: value: List[bool] = driver.configure.connection.pcc.fcpri.downlink.get_stti() \n
		Configures which subframes are scheduled for the DL of the scheduling type 'Follow WB CQI-PMI-RI'. For most subframes,
		the setting is fixed, depending on the duplex mode and the UL-DL configuration. For these subframes, your setting is
		ignored. \n
			:return: scheduled: OFF | ON Comma-separated list of 10 values, for subframe 0 to 9
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:FCPRi:DL:STTI?')
		return Conversions.str_to_bool_list(response)

	def set_stti(self, scheduled: List[bool]) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:FCPRi:DL:STTI \n
		Snippet: driver.configure.connection.pcc.fcpri.downlink.set_stti(scheduled = [True, False, True]) \n
		Configures which subframes are scheduled for the DL of the scheduling type 'Follow WB CQI-PMI-RI'. For most subframes,
		the setting is fixed, depending on the duplex mode and the UL-DL configuration. For these subframes, your setting is
		ignored. \n
			:param scheduled: OFF | ON Comma-separated list of 10 values, for subframe 0 to 9
		"""
		param = Conversions.list_to_csv_str(scheduled)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:FCPRi:DL:STTI {param}')

	def set(self, number_rb: int, start_rb: int, table: enums.MultiClusterDlTable) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:FCPRi:DL \n
		Snippet: driver.configure.connection.pcc.fcpri.downlink.set(number_rb = 1, start_rb = 1, table = enums.MultiClusterDlTable.DETermined) \n
		Configures the downlink for the scheduling type 'Follow WB CQI-PMI-RI', with contiguous allocation. The allowed input
		ranges have dependencies and are described in the background information, see 'CQI channels'. \n
			:param number_rb: numeric Number of allocated resource blocks
			:param start_rb: numeric Position of first resource block
			:param table: DETermined | UDEFined DETermined: Automatic CQI-MCS mapping table UDEFined: User-defined mapping table
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('number_rb', number_rb, DataType.Integer), ArgSingle('start_rb', start_rb, DataType.Integer), ArgSingle('table', table, DataType.Enum, enums.MultiClusterDlTable))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:FCPRi:DL {param}'.rstrip())

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

	def get(self) -> DownlinkStruct:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:FCPRi:DL \n
		Snippet: value: DownlinkStruct = driver.configure.connection.pcc.fcpri.downlink.get() \n
		Configures the downlink for the scheduling type 'Follow WB CQI-PMI-RI', with contiguous allocation. The allowed input
		ranges have dependencies and are described in the background information, see 'CQI channels'. \n
			:return: structure: for return value, see the help for DownlinkStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:FCPRi:DL?', self.__class__.DownlinkStruct())

	def clone(self) -> 'DownlinkCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DownlinkCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
