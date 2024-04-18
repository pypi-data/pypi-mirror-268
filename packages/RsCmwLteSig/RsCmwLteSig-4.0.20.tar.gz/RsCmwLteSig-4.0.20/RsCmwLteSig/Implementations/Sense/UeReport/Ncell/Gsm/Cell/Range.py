from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RangeCls:
	"""Range commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("range", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Rssi_Lower: int: decimal RSSI minimum value Range: -110 dBm to -48 dBm, Unit: dBm
			- Rssi_Upper: int: decimal RSSI maximum value Range: -110 dBm to -48 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rssi_Lower'),
			ArgStruct.scalar_int('Rssi_Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rssi_Lower: int = None
			self.Rssi_Upper: int = None

	def get(self, cellNo=repcap.CellNo.Default) -> GetStruct:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UEReport:NCELl:GSM:CELL<nr>:RANGe \n
		Snippet: value: GetStruct = driver.sense.ueReport.ncell.gsm.cell.range.get(cellNo = repcap.CellNo.Default) \n
		Returns the value range corresponding to the dimensionless RSSI index value reported for the GSM neighbor cell number
		<no>. \n
			:param cellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		cellNo_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNo, repcap.CellNo)
		return self._core.io.query_struct(f'SENSe:LTE:SIGNaling<Instance>:UEReport:NCELl:GSM:CELL{cellNo_cmd_val}:RANGe?', self.__class__.GetStruct())
