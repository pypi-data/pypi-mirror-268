from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QualityCls:
	"""Quality commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("quality", core, parent)

	def get_rx_lev_min(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:RESelection:QUALity:RXLevmin \n
		Snippet: value: float = driver.configure.cell.reSelection.quality.get_rx_lev_min() \n
		Defines the level Qrxlevmin. The value divided by 2 is broadcasted to the UE in SIB1. \n
			:return: qrxlevmin: numeric Range: -140 dBm to -44 dBm, Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:RESelection:QUALity:RXLevmin?')
		return Conversions.str_to_float(response)

	def set_rx_lev_min(self, qrxlevmin: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:RESelection:QUALity:RXLevmin \n
		Snippet: driver.configure.cell.reSelection.quality.set_rx_lev_min(qrxlevmin = 1.0) \n
		Defines the level Qrxlevmin. The value divided by 2 is broadcasted to the UE in SIB1. \n
			:param qrxlevmin: numeric Range: -140 dBm to -44 dBm, Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(qrxlevmin)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:RESelection:QUALity:RXLevmin {param}')
