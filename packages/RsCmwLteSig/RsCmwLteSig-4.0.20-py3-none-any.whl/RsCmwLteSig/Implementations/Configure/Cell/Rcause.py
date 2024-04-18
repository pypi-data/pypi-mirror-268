from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RcauseCls:
	"""Rcause commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rcause", core, parent)

	# noinspection PyTypeChecker
	def get_attach(self) -> enums.RejectAttachCause:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:RCAuse:ATTach \n
		Snippet: value: enums.RejectAttachCause = driver.configure.cell.rcause.get_attach() \n
		Enables or disables the rejection of attach requests and tracking area update requests and selects the rejection cause to
		be transmitted. \n
			:return: cause: IUE3 | EPS7 | PLMN11 | TANA12 | C13 | C17 | CONG22 | C2 | C5 | C6 | C8 | C9 | C10 | C14 | C15 | C16 | C18 | C19 | C20 | C21 | C23 | C24 | C25 | C26 | C35 | C39 | C40 | C42 | C95 | C96 | C97 | C98 | C99 | C100 | C101 | C111 | ON | OFF See table for explanation of values
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:RCAuse:ATTach?')
		return Conversions.str_to_scalar_enum(response, enums.RejectAttachCause)

	def set_attach(self, cause: enums.RejectAttachCause) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:RCAuse:ATTach \n
		Snippet: driver.configure.cell.rcause.set_attach(cause = enums.RejectAttachCause.C10) \n
		Enables or disables the rejection of attach requests and tracking area update requests and selects the rejection cause to
		be transmitted. \n
			:param cause: IUE3 | EPS7 | PLMN11 | TANA12 | C13 | C17 | CONG22 | C2 | C5 | C6 | C8 | C9 | C10 | C14 | C15 | C16 | C18 | C19 | C20 | C21 | C23 | C24 | C25 | C26 | C35 | C39 | C40 | C42 | C95 | C96 | C97 | C98 | C99 | C100 | C101 | C111 | ON | OFF See table for explanation of values
		"""
		param = Conversions.enum_scalar_to_str(cause, enums.RejectAttachCause)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:RCAuse:ATTach {param}')

	# noinspection PyTypeChecker
	def get_tau(self) -> enums.RejectAttachCause:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:RCAuse:TAU \n
		Snippet: value: enums.RejectAttachCause = driver.configure.cell.rcause.get_tau() \n
		Enables or disables the rejection of attach requests and tracking area update requests and selects the rejection cause to
		be transmitted. \n
			:return: cause: IUE3 | EPS7 | PLMN11 | TANA12 | C13 | C17 | CONG22 | C2 | C5 | C6 | C8 | C9 | C10 | C14 | C15 | C16 | C18 | C19 | C20 | C21 | C23 | C24 | C25 | C26 | C35 | C39 | C40 | C42 | C95 | C96 | C97 | C98 | C99 | C100 | C101 | C111 | ON | OFF See table for explanation of values
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:RCAuse:TAU?')
		return Conversions.str_to_scalar_enum(response, enums.RejectAttachCause)

	def set_tau(self, cause: enums.RejectAttachCause) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:RCAuse:TAU \n
		Snippet: driver.configure.cell.rcause.set_tau(cause = enums.RejectAttachCause.C10) \n
		Enables or disables the rejection of attach requests and tracking area update requests and selects the rejection cause to
		be transmitted. \n
			:param cause: IUE3 | EPS7 | PLMN11 | TANA12 | C13 | C17 | CONG22 | C2 | C5 | C6 | C8 | C9 | C10 | C14 | C15 | C16 | C18 | C19 | C20 | C21 | C23 | C24 | C25 | C26 | C35 | C39 | C40 | C42 | C95 | C96 | C97 | C98 | C99 | C100 | C101 | C111 | ON | OFF See table for explanation of values
		"""
		param = Conversions.enum_scalar_to_str(cause, enums.RejectAttachCause)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:RCAuse:TAU {param}')
