from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ThroughputCls:
	"""Throughput commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("throughput", core, parent)

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:THRoughput:TOUT \n
		Snippet: value: float = driver.configure.throughput.get_timeout() \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:return: timeout: numeric Unit: s
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:THRoughput:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:THRoughput:TOUT \n
		Snippet: driver.configure.throughput.set_timeout(timeout = 1.0) \n
		Defines a timeout for the measurement. The timer is started when the measurement is initiated via a READ or INIT command.
		It is not started if the measurement is initiated manually ([ON | OFF] key or [RESTART | STOP] key) .
		When the measurement has completed the first measurement cycle (first single shot) , the statistical depth is reached and
		the timer is reset. If the first measurement cycle has not been completed when the timer expires, the measurement is
		stopped. The measurement state changes to RDY. The reliability indicator is set to 1, indicating that a measurement
		timeout occurred. Still running READ, FETCh or CALCulate commands are completed, returning the available results.
		At least for some results, there are no values at all or the statistical depth has not been reached. A timeout of 0 s
		corresponds to an infinite measurement timeout. \n
			:param timeout: numeric Unit: s
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:THRoughput:TOUT {param}')

	def get_update(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:THRoughput:UPDate \n
		Snippet: value: float = driver.configure.throughput.get_update() \n
		Configures the number of subframes used to derive a single throughput result. \n
			:return: interval: numeric Range: 200 to 10000
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:THRoughput:UPDate?')
		return Conversions.str_to_float(response)

	def set_update(self, interval: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:THRoughput:UPDate \n
		Snippet: driver.configure.throughput.set_update(interval = 1.0) \n
		Configures the number of subframes used to derive a single throughput result. \n
			:param interval: numeric Range: 200 to 10000
		"""
		param = Conversions.decimal_value_to_str(interval)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:THRoughput:UPDate {param}')

	def get_window(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:THRoughput:WINDow \n
		Snippet: value: float = driver.configure.throughput.get_window() \n
		Configures the number of subframes on the X-axis of the throughput diagram (duration of a single-shot measurement) . The
		size cannot be smaller than the update interval. \n
			:return: size: numeric Range: 200 to 120000
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:THRoughput:WINDow?')
		return Conversions.str_to_float(response)

	def set_window(self, size: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:THRoughput:WINDow \n
		Snippet: driver.configure.throughput.set_window(size = 1.0) \n
		Configures the number of subframes on the X-axis of the throughput diagram (duration of a single-shot measurement) . The
		size cannot be smaller than the update interval. \n
			:param size: numeric Range: 200 to 120000
		"""
		param = Conversions.decimal_value_to_str(size)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:THRoughput:WINDow {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:THRoughput:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.throughput.get_repetition() \n
		Specifies whether the measurement is stopped after a single shot (window size) or repeated continuously. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:THRoughput:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:THRoughput:REPetition \n
		Snippet: driver.configure.throughput.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies whether the measurement is stopped after a single shot (window size) or repeated continuously. \n
			:param repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:THRoughput:REPetition {param}')
