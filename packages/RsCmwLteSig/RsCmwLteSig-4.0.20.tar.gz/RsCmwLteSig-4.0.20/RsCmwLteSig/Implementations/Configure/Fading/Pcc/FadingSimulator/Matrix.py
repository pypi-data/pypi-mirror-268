from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MatrixCls:
	"""Matrix commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("matrix", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.FadingMatrixMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:MATRix:MODE \n
		Snippet: value: enums.FadingMatrixMode = driver.configure.fading.pcc.fadingSimulator.matrix.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:MATRix:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FadingMatrixMode)

	def set_mode(self, mode: enums.FadingMatrixMode) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:MATRix:MODE \n
		Snippet: driver.configure.fading.pcc.fadingSimulator.matrix.set_mode(mode = enums.FadingMatrixMode.KRONecker) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FadingMatrixMode)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:MATRix:MODE {param}')
