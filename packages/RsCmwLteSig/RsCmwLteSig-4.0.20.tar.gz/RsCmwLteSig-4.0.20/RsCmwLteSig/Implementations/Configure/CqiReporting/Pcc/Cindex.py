from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CindexCls:
	"""Cindex commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cindex", core, parent)

	def get_fdd(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CQIReporting[:PCC]:CINDex[:FDD] \n
		Snippet: value: int = driver.configure.cqiReporting.pcc.cindex.get_fdd() \n
		Specifies the FDD 'cqi-pmi-ConfigIndex' (ICQI/PMI) . \n
			:return: index: integer Range: 0 to 316, 318 to 541
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CQIReporting:PCC:CINDex:FDD?')
		return Conversions.str_to_int(response)

	def set_fdd(self, index: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CQIReporting[:PCC]:CINDex[:FDD] \n
		Snippet: driver.configure.cqiReporting.pcc.cindex.set_fdd(index = 1) \n
		Specifies the FDD 'cqi-pmi-ConfigIndex' (ICQI/PMI) . \n
			:param index: integer Range: 0 to 316, 318 to 541
		"""
		param = Conversions.decimal_value_to_str(index)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CQIReporting:PCC:CINDex:FDD {param}')

	def get_tdd(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CQIReporting[:PCC]:CINDex:TDD \n
		Snippet: value: int = driver.configure.cqiReporting.pcc.cindex.get_tdd() \n
		Specifies the TDD 'cqi-pmi-ConfigIndex' (ICQI/PMI) . \n
			:return: index: integer Range: 1 to 315
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CQIReporting:PCC:CINDex:TDD?')
		return Conversions.str_to_int(response)

	def set_tdd(self, index: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CQIReporting[:PCC]:CINDex:TDD \n
		Snippet: driver.configure.cqiReporting.pcc.cindex.set_tdd(index = 1) \n
		Specifies the TDD 'cqi-pmi-ConfigIndex' (ICQI/PMI) . \n
			:param index: integer Range: 1 to 315
		"""
		param = Conversions.decimal_value_to_str(index)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CQIReporting:PCC:CINDex:TDD {param}')
