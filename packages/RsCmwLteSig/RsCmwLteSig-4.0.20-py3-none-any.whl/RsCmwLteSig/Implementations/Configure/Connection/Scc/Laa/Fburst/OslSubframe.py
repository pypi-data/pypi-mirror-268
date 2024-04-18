from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OslSubframeCls:
	"""OslSubframe commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("oslSubframe", core, parent)

	def set(self, occ_ofdm_symbols: enums.OccOfdmSymbols, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:LAA:FBURst:OSLSubframe \n
		Snippet: driver.configure.connection.scc.laa.fburst.oslSubframe.set(occ_ofdm_symbols = enums.OccOfdmSymbols.SYM0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the number of allocated OFDM symbols for ending subframes, for LAA with fixed bursts. At least one subframe of
		each burst must have full allocation. This rule restricts the allowed values for the burst lengths 1 and 2. \n
			:param occ_ofdm_symbols: SYM6 | SYM9 | SYM10 | SYM11 | SYM12 | SYM14 6 to 12 OFDM symbols (partial allocation) 14 OFDM symbols (full allocation)
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(occ_ofdm_symbols, enums.OccOfdmSymbols)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:LAA:FBURst:OSLSubframe {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.OccOfdmSymbols:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:LAA:FBURst:OSLSubframe \n
		Snippet: value: enums.OccOfdmSymbols = driver.configure.connection.scc.laa.fburst.oslSubframe.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the number of allocated OFDM symbols for ending subframes, for LAA with fixed bursts. At least one subframe of
		each burst must have full allocation. This rule restricts the allowed values for the burst lengths 1 and 2. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: occ_ofdm_symbols: SYM6 | SYM9 | SYM10 | SYM11 | SYM12 | SYM14 6 to 12 OFDM symbols (partial allocation) 14 OFDM symbols (full allocation)"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:LAA:FBURst:OSLSubframe?')
		return Conversions.str_to_scalar_enum(response, enums.OccOfdmSymbols)
