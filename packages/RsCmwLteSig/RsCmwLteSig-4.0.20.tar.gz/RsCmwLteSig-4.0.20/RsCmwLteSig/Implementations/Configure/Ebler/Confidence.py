from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConfidenceCls:
	"""Confidence commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("confidence", core, parent)

	# noinspection PyTypeChecker
	def get_oas_condition(self) -> enums.BlerStopCondition:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:EBLer:CONFidence:OASCondition \n
		Snippet: value: enums.BlerStopCondition = driver.configure.ebler.confidence.get_oas_condition() \n
		Configures the stop decision and the overall result calculation for confidence BLER measurements with carrier aggregation. \n
			:return: condition: PCC | SCC1 | SCC2 | AC1St | ACWait PCC: PCC only SCC1: SCC1 only SCC2: SCC2 only AC1St: all carriers, stop on 1st fail ACWait: all carriers, wait for all CCs
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:EBLer:CONFidence:OASCondition?')
		return Conversions.str_to_scalar_enum(response, enums.BlerStopCondition)

	def set_oas_condition(self, condition: enums.BlerStopCondition) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:EBLer:CONFidence:OASCondition \n
		Snippet: driver.configure.ebler.confidence.set_oas_condition(condition = enums.BlerStopCondition.AC1St) \n
		Configures the stop decision and the overall result calculation for confidence BLER measurements with carrier aggregation. \n
			:param condition: PCC | SCC1 | SCC2 | AC1St | ACWait PCC: PCC only SCC1: SCC1 only SCC2: SCC2 only AC1St: all carriers, stop on 1st fail ACWait: all carriers, wait for all CCs
		"""
		param = Conversions.enum_scalar_to_str(condition, enums.BlerStopCondition)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:EBLer:CONFidence:OASCondition {param}')

	def get_mt_time(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:EBLer:CONFidence:MTTime \n
		Snippet: value: int = driver.configure.ebler.confidence.get_mt_time() \n
		Specifies a minimum test time for confidence BLER measurements. \n
			:return: time: numeric Minimum number of processed subframes Range: 0 to 500E+3
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:EBLer:CONFidence:MTTime?')
		return Conversions.str_to_int(response)

	def set_mt_time(self, time: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:EBLer:CONFidence:MTTime \n
		Snippet: driver.configure.ebler.confidence.set_mt_time(time = 1) \n
		Specifies a minimum test time for confidence BLER measurements. \n
			:param time: numeric Minimum number of processed subframes Range: 0 to 500E+3
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:EBLer:CONFidence:MTTime {param}')

	# noinspection PyTypeChecker
	def get_lerate(self) -> enums.LimitErrRation:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:EBLer:CONFidence:LERate \n
		Snippet: value: enums.LimitErrRation = driver.configure.ebler.confidence.get_lerate() \n
		Selects the limit error ratio for a confidence BLER measurement. \n
			:return: rate: P001 | P010 | P050 P001: 0.1 %, 3GPP TS 36.521 annex G.4 P010: 1 %, 3GPP TS 36.521 annex G.4 P050: 5 %, 3GPP TS 36.521 annex G.2
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:EBLer:CONFidence:LERate?')
		return Conversions.str_to_scalar_enum(response, enums.LimitErrRation)

	def set_lerate(self, rate: enums.LimitErrRation) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:EBLer:CONFidence:LERate \n
		Snippet: driver.configure.ebler.confidence.set_lerate(rate = enums.LimitErrRation.P001) \n
		Selects the limit error ratio for a confidence BLER measurement. \n
			:param rate: P001 | P010 | P050 P001: 0.1 %, 3GPP TS 36.521 annex G.4 P010: 1 %, 3GPP TS 36.521 annex G.4 P050: 5 %, 3GPP TS 36.521 annex G.2
		"""
		param = Conversions.enum_scalar_to_str(rate, enums.LimitErrRation)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:EBLer:CONFidence:LERate {param}')
