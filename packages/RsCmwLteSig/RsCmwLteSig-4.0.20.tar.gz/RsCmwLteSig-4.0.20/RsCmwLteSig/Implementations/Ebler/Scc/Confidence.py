from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ....Internal.Types import DataType
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConfidenceCls:
	"""Confidence commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("confidence", core, parent)

	# noinspection PyTypeChecker
	def fetch(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.Confidence:
		"""SCPI: FETCh:LTE:SIGNaling<instance>:EBLer:SCC<Carrier>:CONFidence \n
		Snippet: value: enums.Confidence = driver.ebler.scc.confidence.fetch(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Returns the pass/fail result of a confidence BLER measurement, for one carrier. \n
		Use RsCmwLteSig.reliability.last_value to read the updated reliability indicator. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: confidence: EPASs | EFAil | PASS | FAIL | UNDecided EPASs, EFAil: early pass, early fail PASS, FAIL: pass, fail UNDecided: undecided"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:LTE:SIGNaling<Instance>:EBLer:SCC{secondaryCompCarrier_cmd_val}:CONFidence?', suppressed)
		return Conversions.str_to_scalar_enum(response, enums.Confidence)
