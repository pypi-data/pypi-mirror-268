from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdcchCls:
	"""Pdcch commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdcch", core, parent)

	# noinspection PyTypeChecker
	def get_symbol(self) -> enums.PdcchSymbolsCount:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:PDCCh:SYMBol \n
		Snippet: value: enums.PdcchSymbolsCount = driver.configure.connection.pcc.pdcch.get_symbol() \n
		Configures the number of PDCCH symbols per normal subframe. \n
			:return: pdcch: AUTO | P1 | P2 | P3 | P4 AUTO: automatic configuration depending on scheduling type P1 to P4: 1, 2, 3, 4 symbols
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:PDCCh:SYMBol?')
		return Conversions.str_to_scalar_enum(response, enums.PdcchSymbolsCount)

	def set_symbol(self, pdcch: enums.PdcchSymbolsCount) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:PDCCh:SYMBol \n
		Snippet: driver.configure.connection.pcc.pdcch.set_symbol(pdcch = enums.PdcchSymbolsCount.AUTO) \n
		Configures the number of PDCCH symbols per normal subframe. \n
			:param pdcch: AUTO | P1 | P2 | P3 | P4 AUTO: automatic configuration depending on scheduling type P1 to P4: 1, 2, 3, 4 symbols
		"""
		param = Conversions.enum_scalar_to_str(pdcch, enums.PdcchSymbolsCount)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:PDCCh:SYMBol {param}')

	# noinspection PyTypeChecker
	def get_alevel(self) -> enums.Aggregationlevel:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:PDCCh:ALEVel \n
		Snippet: value: enums.Aggregationlevel = driver.configure.connection.pcc.pdcch.get_alevel() \n
		Configures the aggregation levels for DCI messages with C-RNTI. The individual values have prerequisites, see manual
		operation. \n
			:return: aggregationlevel: AUTO | D8U4 | D4U4 | D4U2 | D1U1 | D8U8 AUTO: automatic configuration DaUb: a CCE for DCI messages for the DL, b CCE for messages for the UL
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:PDCCh:ALEVel?')
		return Conversions.str_to_scalar_enum(response, enums.Aggregationlevel)

	def set_alevel(self, aggregationlevel: enums.Aggregationlevel) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:PDCCh:ALEVel \n
		Snippet: driver.configure.connection.pcc.pdcch.set_alevel(aggregationlevel = enums.Aggregationlevel.AUTO) \n
		Configures the aggregation levels for DCI messages with C-RNTI. The individual values have prerequisites, see manual
		operation. \n
			:param aggregationlevel: AUTO | D8U4 | D4U4 | D4U2 | D1U1 | D8U8 AUTO: automatic configuration DaUb: a CCE for DCI messages for the DL, b CCE for messages for the UL
		"""
		param = Conversions.enum_scalar_to_str(aggregationlevel, enums.Aggregationlevel)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:PDCCh:ALEVel {param}')
