from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EblerCls:
	"""Ebler commands group definition. 8 total commands, 1 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ebler", core, parent)

	@property
	def confidence(self):
		"""confidence commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_confidence'):
			from .Confidence import ConfidenceCls
			self._confidence = ConfidenceCls(self._core, self._cmd_group)
		return self._confidence

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:EBLer:TOUT \n
		Snippet: value: float = driver.configure.ebler.get_timeout() \n
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
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:EBLer:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:EBLer:TOUT \n
		Snippet: driver.configure.ebler.set_timeout(timeout = 1.0) \n
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
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:EBLer:TOUT {param}')

	def get_sframes(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:EBLer:SFRames \n
		Snippet: value: int = driver.configure.ebler.get_sframes() \n
		Defines the number of subframes (= number of transport blocks) to be processed per measurement cycle. For confidence BLER
		measurements, this parameter specifies only the length of the throughput result trace but does not influence the duration
		of the measurement. \n
			:return: sub_frames: integer Range: 100 to 400E+3
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:EBLer:SFRames?')
		return Conversions.str_to_int(response)

	def set_sframes(self, sub_frames: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:EBLer:SFRames \n
		Snippet: driver.configure.ebler.set_sframes(sub_frames = 1) \n
		Defines the number of subframes (= number of transport blocks) to be processed per measurement cycle. For confidence BLER
		measurements, this parameter specifies only the length of the throughput result trace but does not influence the duration
		of the measurement. \n
			:param sub_frames: integer Range: 100 to 400E+3
		"""
		param = Conversions.decimal_value_to_str(sub_frames)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:EBLer:SFRames {param}')

	# noinspection PyTypeChecker
	def get_er_calc(self) -> enums.BlerAlgorithm:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:EBLer:ERCalc \n
		Snippet: value: enums.BlerAlgorithm = driver.configure.ebler.get_er_calc() \n
		Selects the formula to be used for calculation of the BLER from the number of ACK, NACK and DTX. \n
			:return: algorithm: ERC1 | ERC2 | ERC3 | ERC4 ERC1: BLER = (NACK + DTX) / (ACK + NACK + DTX) ERC2: BLER = DTX / (ACK + NACK + DTX) ERC3: BLER = NACK / (ACK + NACK + DTX) ERC4: BLER = NACK / (ACK + NACK)
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:EBLer:ERCalc?')
		return Conversions.str_to_scalar_enum(response, enums.BlerAlgorithm)

	def set_er_calc(self, algorithm: enums.BlerAlgorithm) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:EBLer:ERCalc \n
		Snippet: driver.configure.ebler.set_er_calc(algorithm = enums.BlerAlgorithm.ERC1) \n
		Selects the formula to be used for calculation of the BLER from the number of ACK, NACK and DTX. \n
			:param algorithm: ERC1 | ERC2 | ERC3 | ERC4 ERC1: BLER = (NACK + DTX) / (ACK + NACK + DTX) ERC2: BLER = DTX / (ACK + NACK + DTX) ERC3: BLER = NACK / (ACK + NACK + DTX) ERC4: BLER = NACK / (ACK + NACK)
		"""
		param = Conversions.enum_scalar_to_str(algorithm, enums.BlerAlgorithm)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:EBLer:ERCalc {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:EBLer:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.ebler.get_repetition() \n
		Specifies whether the measurement is stopped after a single shot or repeated continuously. \n
			:return: repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:EBLer:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:EBLer:REPetition \n
		Snippet: driver.configure.ebler.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		Specifies whether the measurement is stopped after a single shot or repeated continuously. \n
			:param repetition: SINGleshot | CONTinuous SINGleshot: Single-shot measurement CONTinuous: Continuous measurement
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:EBLer:REPetition {param}')

	# noinspection PyTypeChecker
	def get_scondition(self) -> enums.EblerStopCondition:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:EBLer:SCONdition \n
		Snippet: value: enums.EblerStopCondition = driver.configure.ebler.get_scondition() \n
		Selects whether a BLER measurement without stop condition or a confidence BLER measurement with early decision concept is
		performed. \n
			:return: stop_condition: NONE | CLEVel NONE: no stop condition, no early termination of measurement CLEVel: confidence BLER measurement
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:EBLer:SCONdition?')
		return Conversions.str_to_scalar_enum(response, enums.EblerStopCondition)

	def set_scondition(self, stop_condition: enums.EblerStopCondition) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:EBLer:SCONdition \n
		Snippet: driver.configure.ebler.set_scondition(stop_condition = enums.EblerStopCondition.CLEVel) \n
		Selects whether a BLER measurement without stop condition or a confidence BLER measurement with early decision concept is
		performed. \n
			:param stop_condition: NONE | CLEVel NONE: no stop condition, no early termination of measurement CLEVel: confidence BLER measurement
		"""
		param = Conversions.enum_scalar_to_str(stop_condition, enums.EblerStopCondition)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:EBLer:SCONdition {param}')

	def clone(self) -> 'EblerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EblerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
