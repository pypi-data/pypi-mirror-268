from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpfSubframeCls:
	"""SpfSubframe commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spfSubframe", core, parent)

	def set(self, starting_pos: enums.StartingPosition, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:LAA:FBURst:SPFSubframe \n
		Snippet: driver.configure.connection.scc.laa.fburst.spfSubframe.set(starting_pos = enums.StartingPosition.OFDM0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the first allocated OFDM symbol for initial subframes, for LAA with fixed bursts. \n
			:param starting_pos: OFDM0 | OFDM7 OFDM0: symbol 0 (full allocation) OFDM7: symbol 7 (partial allocation, needs burst length 1)
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(starting_pos, enums.StartingPosition)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:LAA:FBURst:SPFSubframe {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.StartingPosition:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:LAA:FBURst:SPFSubframe \n
		Snippet: value: enums.StartingPosition = driver.configure.connection.scc.laa.fburst.spfSubframe.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the first allocated OFDM symbol for initial subframes, for LAA with fixed bursts. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: starting_pos: OFDM0 | OFDM7 OFDM0: symbol 0 (full allocation) OFDM7: symbol 7 (partial allocation, needs burst length 1)"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:LAA:FBURst:SPFSubframe?')
		return Conversions.str_to_scalar_enum(response, enums.StartingPosition)
