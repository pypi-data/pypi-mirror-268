from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MimoCls:
	"""Mimo commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mimo", core, parent)

	@property
	def line(self):
		"""line commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_line'):
			from .Line import LineCls
			self._line = LineCls(self._core, self._cmd_group)
		return self._line

	# noinspection PyTypeChecker
	def get_mselection(self) -> enums.MimoMatrixSelection:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:CMATrix:MIMO<Mimo>:MSELection \n
		Snippet: value: enums.MimoMatrixSelection = driver.configure.connection.pcc.tm.cmatrix.mimo.get_mselection() \n
		Selects a predefined channel matrix or the user-defined channel matrix for MIMO 4x4 plus TM 9. \n
			:return: selection: UDEFined | CM3Gpp | HADamard | IDENtity User-defined matrix, 3GPP channel matrix, Hadamard matrix, identity matrix
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:CMATrix:MIMO44:MSELection?')
		return Conversions.str_to_scalar_enum(response, enums.MimoMatrixSelection)

	def set_mselection(self, selection: enums.MimoMatrixSelection) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:TM<nr>:CMATrix:MIMO<Mimo>:MSELection \n
		Snippet: driver.configure.connection.pcc.tm.cmatrix.mimo.set_mselection(selection = enums.MimoMatrixSelection.CM3Gpp) \n
		Selects a predefined channel matrix or the user-defined channel matrix for MIMO 4x4 plus TM 9. \n
			:param selection: UDEFined | CM3Gpp | HADamard | IDENtity User-defined matrix, 3GPP channel matrix, Hadamard matrix, identity matrix
		"""
		param = Conversions.enum_scalar_to_str(selection, enums.MimoMatrixSelection)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:TM9:CMATrix:MIMO44:MSELection {param}')

	def clone(self) -> 'MimoCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MimoCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
