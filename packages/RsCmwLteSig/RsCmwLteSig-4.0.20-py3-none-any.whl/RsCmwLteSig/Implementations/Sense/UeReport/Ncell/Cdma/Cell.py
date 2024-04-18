from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CellCls:
	"""Cell commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Pilot_Pn_Phase: int: decimal Reported pilot PN phase value Range: 0 PN chips to 32767 PN chips, Unit: PN chips
			- Pilot_Strength: int: decimal Reported pilot strength value Range: 0 to 63"""
		__meta_args_list = [
			ArgStruct.scalar_int('Pilot_Pn_Phase'),
			ArgStruct.scalar_int('Pilot_Strength')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Pilot_Pn_Phase: int = None
			self.Pilot_Strength: int = None

	def get(self, cellNo=repcap.CellNo.Default) -> GetStruct:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UEReport:NCELl:CDMA:CELL<nr> \n
		Snippet: value: GetStruct = driver.sense.ueReport.ncell.cdma.cell.get(cellNo = repcap.CellNo.Default) \n
		Returns measurement report values for the CDMA2000 neighbor cell number <no>. \n
			:param cellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		cellNo_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNo, repcap.CellNo)
		return self._core.io.query_struct(f'SENSe:LTE:SIGNaling<Instance>:UEReport:NCELl:CDMA:CELL{cellNo_cmd_val}?', self.__class__.GetStruct())
