from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MselectionCls:
	"""Mselection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mselection", core, parent)

	# noinspection PyTypeChecker
	def get_mimo(self) -> enums.MimoMatrixSelection:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:SCHModel:MSELection:MIMO<Mimo> \n
		Snippet: value: enums.MimoMatrixSelection = driver.configure.connection.pcc.schModel.mselection.get_mimo() \n
		Selects a predefined channel matrix or the user-defined channel matrix for MIMO 4x4. \n
			:return: selection: UDEFined | CM3Gpp | HADamard | IDENtity User-defined matrix, 3GPP channel matrix, Hadamard matrix, identity matrix
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:SCHModel:MSELection:MIMO44?')
		return Conversions.str_to_scalar_enum(response, enums.MimoMatrixSelection)

	def set_mimo(self, selection: enums.MimoMatrixSelection) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:SCHModel:MSELection:MIMO<Mimo> \n
		Snippet: driver.configure.connection.pcc.schModel.mselection.set_mimo(selection = enums.MimoMatrixSelection.CM3Gpp) \n
		Selects a predefined channel matrix or the user-defined channel matrix for MIMO 4x4. \n
			:param selection: UDEFined | CM3Gpp | HADamard | IDENtity User-defined matrix, 3GPP channel matrix, Hadamard matrix, identity matrix
		"""
		param = Conversions.enum_scalar_to_str(selection, enums.MimoMatrixSelection)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:SCHModel:MSELection:MIMO44 {param}')
