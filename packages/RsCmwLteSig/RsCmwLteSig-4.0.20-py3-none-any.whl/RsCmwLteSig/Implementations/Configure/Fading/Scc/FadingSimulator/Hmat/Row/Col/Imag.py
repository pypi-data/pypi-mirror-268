from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ImagCls:
	"""Imag commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("imag", core, parent)

	def set(self, imag: float, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default, hMatrixRow=repcap.HMatrixRow.Default, hMatrixColumn=repcap.HMatrixColumn.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing:SCC<Carrier>:FSIMulator:HMAT:ROW<row>:COL<col>:IMAG \n
		Snippet: driver.configure.fading.scc.fadingSimulator.hmat.row.col.imag.set(imag = 1.0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default, hMatrixRow = repcap.HMatrixRow.Default, hMatrixColumn = repcap.HMatrixColumn.Default) \n
		No command help available \n
			:param imag: No help available
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:param hMatrixRow: optional repeated capability selector. Default value: Row1 (settable in the interface 'Row')
			:param hMatrixColumn: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Col')
		"""
		param = Conversions.decimal_value_to_str(imag)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		hMatrixRow_cmd_val = self._cmd_group.get_repcap_cmd_value(hMatrixRow, repcap.HMatrixRow)
		hMatrixColumn_cmd_val = self._cmd_group.get_repcap_cmd_value(hMatrixColumn, repcap.HMatrixColumn)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:SCC{secondaryCompCarrier_cmd_val}:FSIMulator:HMAT:ROW{hMatrixRow_cmd_val}:COL{hMatrixColumn_cmd_val}:IMAG {param}')
