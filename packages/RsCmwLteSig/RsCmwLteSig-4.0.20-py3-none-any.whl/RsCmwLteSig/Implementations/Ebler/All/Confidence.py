from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConfidenceCls:
	"""Confidence commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("confidence", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.Confidence:
		"""SCPI: FETCh:LTE:SIGNaling<instance>:EBLer:ALL:CONFidence \n
		Snippet: value: enums.Confidence = driver.ebler.all.confidence.fetch() \n
		Returns the overall pass/fail result of a confidence BLER measurement. \n
		Use RsCmwLteSig.reliability.last_value to read the updated reliability indicator. \n
			:return: confidence: EPASs | EFAil | PASS | FAIL | UNDecided EPASs, EFAil: early pass, early fail PASS, FAIL: pass, fail UNDecided: undecided"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:LTE:SIGNaling<Instance>:EBLer:ALL:CONFidence?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.Confidence)
