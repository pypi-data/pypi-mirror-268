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
			- Rsrp_Lower: int: decimal RSRP minimum value Range: -140 dBm to -44 dBm, Unit: dBm
			- Rsrp_Upper: int: decimal RSRP maximum value Range: -140 dBm to -44 dBm, Unit: dBm
			- Rsrq_Lower: float: float RSRQ minimum value Range: -19.5 dB to -3 dB, Unit: dB
			- Rsrq_Upper: float: float RSRQ maximum value Range: -19.5 dB to -3 dB, Unit: dB"""
		__meta_args_list = [
			ArgStruct.scalar_int('Rsrp_Lower'),
			ArgStruct.scalar_int('Rsrp_Upper'),
			ArgStruct.scalar_float('Rsrq_Lower'),
			ArgStruct.scalar_float('Rsrq_Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rsrp_Lower: int = None
			self.Rsrp_Upper: int = None
			self.Rsrq_Lower: float = None
			self.Rsrq_Upper: float = None

	def get(self, cellNo=repcap.CellNo.Default) -> GetStruct:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UEReport:NCELl:LTE:CELL<nr>:RANGe \n
		Snippet: value: GetStruct = driver.sense.ueReport.ncell.lte.cell.range.get(cellNo = repcap.CellNo.Default) \n
		Returns the value ranges corresponding to the dimensionless index values reported for the LTE neighbor cell number <no>. \n
			:param cellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		cellNo_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNo, repcap.CellNo)
		return self._core.io.query_struct(f'SENSe:LTE:SIGNaling<Instance>:UEReport:NCELl:LTE:CELL{cellNo_cmd_val}:RANGe?', self.__class__.GetStruct())
