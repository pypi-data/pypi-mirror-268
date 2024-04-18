from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MncCls:
	"""Mnc commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mnc", core, parent)

	# noinspection PyTypeChecker
	def get_digits(self) -> enums.NoOfDigits:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:MNC:DIGits \n
		Snippet: value: enums.NoOfDigits = driver.configure.cell.mnc.get_digits() \n
		Specifies the number of digits of the mobile network code (MNC) . For setting the MNC, see method RsCmwLteSig.Configure.
		Cell.Mnc.value. \n
			:return: no_digits: TWO | THRee
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:MNC:DIGits?')
		return Conversions.str_to_scalar_enum(response, enums.NoOfDigits)

	def set_digits(self, no_digits: enums.NoOfDigits) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:MNC:DIGits \n
		Snippet: driver.configure.cell.mnc.set_digits(no_digits = enums.NoOfDigits.THRee) \n
		Specifies the number of digits of the mobile network code (MNC) . For setting the MNC, see method RsCmwLteSig.Configure.
		Cell.Mnc.value. \n
			:param no_digits: TWO | THRee
		"""
		param = Conversions.enum_scalar_to_str(no_digits, enums.NoOfDigits)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:MNC:DIGits {param}')

	def get_value(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:MNC \n
		Snippet: value: int = driver.configure.cell.mnc.get_value() \n
		Specifies the mobile network code (MNC) . You can omit leading zeros. A two or three-digit MNC can be set, see method
		RsCmwLteSig.Configure.Cell.Mnc.digits. \n
			:return: mnc: decimal Range: 0 to 99 or 999
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:MNC?')
		return Conversions.str_to_int(response)

	def set_value(self, mnc: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:MNC \n
		Snippet: driver.configure.cell.mnc.set_value(mnc = 1) \n
		Specifies the mobile network code (MNC) . You can omit leading zeros. A two or three-digit MNC can be set, see method
		RsCmwLteSig.Configure.Cell.Mnc.digits. \n
			:param mnc: decimal Range: 0 to 99 or 999
		"""
		param = Conversions.decimal_value_to_str(mnc)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:MNC {param}')
