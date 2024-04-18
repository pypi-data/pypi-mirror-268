from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RpControlCls:
	"""RpControl commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rpControl", core, parent)

	def set(self, pattern: enums.RpControlPattern, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PUSCh:TPC:RPControl \n
		Snippet: driver.configure.uplink.scc.pusch.tpc.rpControl.set(pattern = enums.RpControlPattern.RDA, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects a TPC pattern for 3GPP relative power control tests with the TPC setup RPControl. \n
			:param pattern: RUA | RDA | RUB | RDB | RUC | RDC RUA | RUB | RUC: ramping up A | B | C RDA | RDB | RDC: ramping down A | B | C
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(pattern, enums.RpControlPattern)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PUSCh:TPC:RPControl {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.RpControlPattern:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PUSCh:TPC:RPControl \n
		Snippet: value: enums.RpControlPattern = driver.configure.uplink.scc.pusch.tpc.rpControl.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects a TPC pattern for 3GPP relative power control tests with the TPC setup RPControl. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: pattern: RUA | RDA | RUB | RDB | RUC | RDC RUA | RUB | RUC: ramping up A | B | C RDA | RDB | RDC: ramping down A | B | C"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PUSCh:TPC:RPControl?')
		return Conversions.str_to_scalar_enum(response, enums.RpControlPattern)
