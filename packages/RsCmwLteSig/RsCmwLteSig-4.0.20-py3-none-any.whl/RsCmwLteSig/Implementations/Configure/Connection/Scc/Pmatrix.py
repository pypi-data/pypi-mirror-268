from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PmatrixCls:
	"""Pmatrix commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmatrix", core, parent)

	def set(self, mode: enums.PrecodingMatrixMode, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:PMATrix \n
		Snippet: driver.configure.connection.scc.pmatrix.set(mode = enums.PrecodingMatrixMode.PMI0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the precoding matrix. The value must be compatible to the active scenario and transmission mode, see Table
		'Transmission scheme overview'. For TM 8 and TM 9, the matrix is used as beamforming matrix, not for precoding. \n
			:param mode: PMI0 | PMI1 | PMI2 | PMI3 | PMI4 | PMI5 | PMI6 | PMI7 | PMI8 | PMI9 | PMI10 | PMI11 | PMI12 | PMI13 | PMI14 | PMI15 | RANDom_pmi Matrix according to PMI 0, PMI 1, ... PMI15. RANDom_pmi: The PMI value is selected randomly as defined in 3GPP TS 36.521, annex B.4.1 and B.4.2.
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PrecodingMatrixMode)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:PMATrix {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.PrecodingMatrixMode:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:PMATrix \n
		Snippet: value: enums.PrecodingMatrixMode = driver.configure.connection.scc.pmatrix.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the precoding matrix. The value must be compatible to the active scenario and transmission mode, see Table
		'Transmission scheme overview'. For TM 8 and TM 9, the matrix is used as beamforming matrix, not for precoding. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: mode: PMI0 | PMI1 | PMI2 | PMI3 | PMI4 | PMI5 | PMI6 | PMI7 | PMI8 | PMI9 | PMI10 | PMI11 | PMI12 | PMI13 | PMI14 | PMI15 | RANDom_pmi Matrix according to PMI 0, PMI 1, ... PMI15. RANDom_pmi: The PMI value is selected randomly as defined in 3GPP TS 36.521, annex B.4.1 and B.4.2."""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:PMATrix?')
		return Conversions.str_to_scalar_enum(response, enums.PrecodingMatrixMode)
