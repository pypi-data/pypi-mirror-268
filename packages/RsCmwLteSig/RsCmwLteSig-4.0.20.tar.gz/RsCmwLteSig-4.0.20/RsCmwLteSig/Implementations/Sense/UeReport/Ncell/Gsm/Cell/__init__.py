from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CellCls:
	"""Cell commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cell", core, parent)

	@property
	def range(self):
		"""range commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_range'):
			from .Range import RangeCls
			self._range = RangeCls(self._core, self._cmd_group)
		return self._range

	def get(self, cellNo=repcap.CellNo.Default) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UEReport:NCELl:GSM:CELL<nr> \n
		Snippet: value: int = driver.sense.ueReport.ncell.gsm.cell.get(cellNo = repcap.CellNo.Default) \n
		Returns the RSSI value reported as dimensionless index for the GSM neighbor cell number <no>. \n
			:param cellNo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ncell')
			:return: rssi: decimal Range: 0 to 63"""
		cellNo_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNo, repcap.CellNo)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:UEReport:NCELl:GSM:CELL{cellNo_cmd_val}?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'CellCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CellCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
