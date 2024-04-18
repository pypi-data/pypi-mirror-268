from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NasCls:
	"""Nas commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nas", core, parent)

	def get_eps_network(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:NAS:EPSNetwork \n
		Snippet: value: bool = driver.configure.cell.nas.get_eps_network() \n
		Enables or disables sending of the information element 'EPS Network Feature Support' to the UE in the ATTACH ACCEPT
		message. For configuration of the information element contents, see other CONFigure:LTE:SIGN<i>:CELL:NAS:... commands. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:NAS:EPSNetwork?')
		return Conversions.str_to_bool(response)

	def set_eps_network(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:NAS:EPSNetwork \n
		Snippet: driver.configure.cell.nas.set_eps_network(enable = False) \n
		Enables or disables sending of the information element 'EPS Network Feature Support' to the UE in the ATTACH ACCEPT
		message. For configuration of the information element contents, see other CONFigure:LTE:SIGN<i>:CELL:NAS:... commands. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:NAS:EPSNetwork {param}')

	# noinspection PyTypeChecker
	def get_imsvops(self) -> enums.SupportedLong:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:NAS:IMSVops \n
		Snippet: value: enums.SupportedLong = driver.configure.cell.nas.get_imsvops() \n
		Configures the field 'IMS voice over PS session indicator' of the information element 'EPS Network Feature Support'. \n
			:return: support: NSUPported | SUPPorted NSUPported: not supported SUPPorted: supported
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:NAS:IMSVops?')
		return Conversions.str_to_scalar_enum(response, enums.SupportedLong)

	def set_imsvops(self, support: enums.SupportedLong) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:NAS:IMSVops \n
		Snippet: driver.configure.cell.nas.set_imsvops(support = enums.SupportedLong.NSUPported) \n
		Configures the field 'IMS voice over PS session indicator' of the information element 'EPS Network Feature Support'. \n
			:param support: NSUPported | SUPPorted NSUPported: not supported SUPPorted: supported
		"""
		param = Conversions.enum_scalar_to_str(support, enums.SupportedLong)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:NAS:IMSVops {param}')

	# noinspection PyTypeChecker
	def get_emcbs(self) -> enums.SupportedLong:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:NAS:EMCBs \n
		Snippet: value: enums.SupportedLong = driver.configure.cell.nas.get_emcbs() \n
		Configures the field 'Emergency bearer services indicator' of the information element 'EPS Network Feature Support'. \n
			:return: support: NSUPported | SUPPorted NSUPported: not supported SUPPorted: supported
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:NAS:EMCBs?')
		return Conversions.str_to_scalar_enum(response, enums.SupportedLong)

	def set_emcbs(self, support: enums.SupportedLong) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:NAS:EMCBs \n
		Snippet: driver.configure.cell.nas.set_emcbs(support = enums.SupportedLong.NSUPported) \n
		Configures the field 'Emergency bearer services indicator' of the information element 'EPS Network Feature Support'. \n
			:param support: NSUPported | SUPPorted NSUPported: not supported SUPPorted: supported
		"""
		param = Conversions.enum_scalar_to_str(support, enums.SupportedLong)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:NAS:EMCBs {param}')

	# noinspection PyTypeChecker
	def get_epclcs(self) -> enums.SupportedLong:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:NAS:EPCLcs \n
		Snippet: value: enums.SupportedLong = driver.configure.cell.nas.get_epclcs() \n
		Configures the field 'Location services indicator in EPC' of the information element 'EPS Network Feature Support'. \n
			:return: support: NSUPported | SUPPorted NSUPported: not supported SUPPorted: supported
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:NAS:EPCLcs?')
		return Conversions.str_to_scalar_enum(response, enums.SupportedLong)

	def set_epclcs(self, support: enums.SupportedLong) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:NAS:EPCLcs \n
		Snippet: driver.configure.cell.nas.set_epclcs(support = enums.SupportedLong.NSUPported) \n
		Configures the field 'Location services indicator in EPC' of the information element 'EPS Network Feature Support'. \n
			:param support: NSUPported | SUPPorted NSUPported: not supported SUPPorted: supported
		"""
		param = Conversions.enum_scalar_to_str(support, enums.SupportedLong)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:NAS:EPCLcs {param}')

	# noinspection PyTypeChecker
	def get_cslcs(self) -> enums.SupportedExt:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:NAS:CSLCs \n
		Snippet: value: enums.SupportedExt = driver.configure.cell.nas.get_cslcs() \n
		Configures the field 'Location services indicator in CS' of the information element 'EPS Network Feature Support'. \n
			:return: support: NSUPported | SUPPorted | NINFormation NSUPported: not supported SUPPorted: supported NINFormation: no information
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:NAS:CSLCs?')
		return Conversions.str_to_scalar_enum(response, enums.SupportedExt)

	def set_cslcs(self, support: enums.SupportedExt) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:NAS:CSLCs \n
		Snippet: driver.configure.cell.nas.set_cslcs(support = enums.SupportedExt.NINFormation) \n
		Configures the field 'Location services indicator in CS' of the information element 'EPS Network Feature Support'. \n
			:param support: NSUPported | SUPPorted | NINFormation NSUPported: not supported SUPPorted: supported NINFormation: no information
		"""
		param = Conversions.enum_scalar_to_str(support, enums.SupportedExt)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:NAS:CSLCs {param}')
