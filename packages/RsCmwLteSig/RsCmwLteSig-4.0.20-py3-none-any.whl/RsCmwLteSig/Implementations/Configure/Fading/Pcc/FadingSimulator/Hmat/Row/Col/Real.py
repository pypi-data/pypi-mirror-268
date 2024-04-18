from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RealCls:
	"""Real commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("real", core, parent)

	def set(self, real: float, hMatrixRow=repcap.HMatrixRow.Default, hMatrixColumn=repcap.HMatrixColumn.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:HMAT:ROW<row>:COL<col>:REAL \n
		Snippet: driver.configure.fading.pcc.fadingSimulator.hmat.row.col.real.set(real = 1.0, hMatrixRow = repcap.HMatrixRow.Default, hMatrixColumn = repcap.HMatrixColumn.Default) \n
		No command help available \n
			:param real: No help available
			:param hMatrixRow: optional repeated capability selector. Default value: Row1 (settable in the interface 'Row')
			:param hMatrixColumn: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Col')
		"""
		param = Conversions.decimal_value_to_str(real)
		hMatrixRow_cmd_val = self._cmd_group.get_repcap_cmd_value(hMatrixRow, repcap.HMatrixRow)
		hMatrixColumn_cmd_val = self._cmd_group.get_repcap_cmd_value(hMatrixColumn, repcap.HMatrixColumn)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:HMAT:ROW{hMatrixRow_cmd_val}:COL{hMatrixColumn_cmd_val}:REAL {param}')
