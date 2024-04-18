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
			- Rscp_Lower: int: decimal RSCP minimum value Range: -120 dBm to -25 dBm, Unit: dBm
			- Rscp_Upper: int: decimal RSCP maximum value Range: -120 dBm to -25 dBm, Unit: dBm"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rscp_Lower'),
			ArgStruct.scalar_int('Rscp_Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rscp_Lower: int = None
			self.Rscp_Upper: int = None

	def get(self, cellNo=repcap.CellNo.Default) -> GetStruct:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UEReport:NCELl:TDSCdma:CELL<nr>:RANGe \n
		Snippet: value: GetStruct = driver.sense.ueReport.ncell.tdscdma.cell.range.get(cellNo = repcap.CellNo.Default) \n
		Returns the value ranges corresponding to the dimensionless index values reported for the TD-SCDMA neighbor cell number
		<no>. \n
			:param cellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		cellNo_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNo, repcap.CellNo)
		return self._core.io.query_struct(f'SENSe:LTE:SIGNaling<Instance>:UEReport:NCELl:TDSCdma:CELL{cellNo_cmd_val}:RANGe?', self.__class__.GetStruct())
