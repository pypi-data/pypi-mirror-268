from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MselectionCls:
	"""Mselection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mselection", core, parent)

	def set(self, selection: enums.MimoMatrixSelection, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:TM<nr>:CMATrix:MIMO<Mimo>:MSELection \n
		Snippet: driver.configure.connection.scc.tm.cmatrix.mimo.mselection.set(selection = enums.MimoMatrixSelection.CM3Gpp, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects a predefined channel matrix or the user-defined channel matrix for MIMO 4x4 plus TM 9. \n
			:param selection: UDEFined | CM3Gpp | HADamard | IDENtity User-defined matrix, 3GPP channel matrix, Hadamard matrix, identity matrix
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(selection, enums.MimoMatrixSelection)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TM9:CMATrix:MIMO44:MSELection {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.MimoMatrixSelection:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:TM<nr>:CMATrix:MIMO<Mimo>:MSELection \n
		Snippet: value: enums.MimoMatrixSelection = driver.configure.connection.scc.tm.cmatrix.mimo.mselection.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects a predefined channel matrix or the user-defined channel matrix for MIMO 4x4 plus TM 9. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: selection: UDEFined | CM3Gpp | HADamard | IDENtity User-defined matrix, 3GPP channel matrix, Hadamard matrix, identity matrix"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:TM9:CMATrix:MIMO44:MSELection?')
		return Conversions.str_to_scalar_enum(response, enums.MimoMatrixSelection)
