from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class QrxlevminCls:
	"""Qrxlevmin commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("qrxlevmin", core, parent)

	def set(self, level: int, qrxlevmin: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:CE:LEVel:QRXLevmin \n
		Snippet: driver.configure.pcc.emtc.ce.level.qrxlevmin.set(level = 1, qrxlevmin = 1) \n
		Defines the Qrxlevmin for CE level selection for PRACH. The value divided by two is signaled to the UE. The value is
		defined per CE level. With increasing CE level, the Qrxlevmin must decrease. \n
			:param level: integer Selects a CE level Range: 1 to 3
			:param qrxlevmin: numeric Qrxlevmin for the selected CE level Range: -140 dBm to -44 dBm
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('level', level, DataType.Integer), ArgSingle('qrxlevmin', qrxlevmin, DataType.Integer))
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:CE:LEVel:QRXLevmin {param}'.rstrip())

	def get(self, level: int) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:CE:LEVel:QRXLevmin \n
		Snippet: value: int = driver.configure.pcc.emtc.ce.level.qrxlevmin.get(level = 1) \n
		Defines the Qrxlevmin for CE level selection for PRACH. The value divided by two is signaled to the UE. The value is
		defined per CE level. With increasing CE level, the Qrxlevmin must decrease. \n
			:param level: integer Selects a CE level Range: 1 to 3
			:return: qrxlevmin: numeric Qrxlevmin for the selected CE level Range: -140 dBm to -44 dBm"""
		param = Conversions.decimal_value_to_str(level)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:CE:LEVel:QRXLevmin? {param}')
		return Conversions.str_to_int(response)
