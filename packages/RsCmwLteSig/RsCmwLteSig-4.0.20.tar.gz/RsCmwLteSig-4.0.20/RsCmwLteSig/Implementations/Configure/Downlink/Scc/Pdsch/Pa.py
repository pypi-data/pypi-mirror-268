from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PaCls:
	"""Pa commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pa", core, parent)

	def set(self, pa: enums.PowerOffset, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL:SCC<Carrier>:PDSCh:PA \n
		Snippet: driver.configure.downlink.scc.pdsch.pa.set(pa = enums.PowerOffset.N3DB, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines the power offset PA. \n
			:param pa: ZERO | N3DB | N6DB Power offset of 0 dB | -3 dB | -6 dB
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(pa, enums.PowerOffset)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:DL:SCC{secondaryCompCarrier_cmd_val}:PDSCh:PA {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.PowerOffset:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL:SCC<Carrier>:PDSCh:PA \n
		Snippet: value: enums.PowerOffset = driver.configure.downlink.scc.pdsch.pa.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Defines the power offset PA. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: pa: ZERO | N3DB | N6DB Power offset of 0 dB | -3 dB | -6 dB"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:DL:SCC{secondaryCompCarrier_cmd_val}:PDSCh:PA?')
		return Conversions.str_to_scalar_enum(response, enums.PowerOffset)
