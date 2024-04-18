from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AcauseCls:
	"""Acause commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("acause", core, parent)

	# noinspection PyTypeChecker
	def get_attach(self) -> enums.AcceptAttachCause:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:ACAuse:ATTach \n
		Snippet: value: enums.AcceptAttachCause = driver.configure.cell.acause.get_attach() \n
		Selects whether a cause is added to ATTACH ACCEPT messages or not. \n
			:return: cause: C18 | ON | OFF OFF: disables sending of a cause ON / C18: enables sending of attach accept cause 18 (CS domain not available)
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:ACAuse:ATTach?')
		return Conversions.str_to_scalar_enum(response, enums.AcceptAttachCause)

	def set_attach(self, cause: enums.AcceptAttachCause) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:ACAuse:ATTach \n
		Snippet: driver.configure.cell.acause.set_attach(cause = enums.AcceptAttachCause.C18) \n
		Selects whether a cause is added to ATTACH ACCEPT messages or not. \n
			:param cause: C18 | ON | OFF OFF: disables sending of a cause ON / C18: enables sending of attach accept cause 18 (CS domain not available)
		"""
		param = Conversions.enum_scalar_to_str(cause, enums.AcceptAttachCause)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:ACAuse:ATTach {param}')
