from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	def set(self, position: enums.RbPosition, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:RMC:RBPosition:UL \n
		Snippet: driver.configure.connection.scc.rmc.rbPosition.uplink.set(position = enums.RbPosition.FULL, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the position of the allocated uplink resource blocks, for contiguous allocation.
			INTRO_CMD_HELP: Depending on other settings, only a subset of the listed values is allowed, see: \n
			- 'Scheduling type RMC'
			- 'Scheduling type RMC for eMTC'
			- 'Scheduling type RMC for LAA' \n
			:param position: LOW | HIGH | MID | P0 | P1 | P2 | P3 | P4 | P6 | P7 | P8 | P9 | P10 | P11 | P12 | P13 | P14 | P15 | P16 | P19 | P20 | P21 | P22 | P24 | P25 | P28 | P30 | P31 | P33 | P36 | P37 | P39 | P40 | P43 | P44 | P45 | P48 | P49 | P50 | P51 | P52 | P54 | P56 | P57 | P58 | P62 | P63 | P66 | P68 | P70 | P74 | P75 | P83 | P96 | P99
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(position, enums.RbPosition)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:RMC:RBPosition:UL {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.RbPosition:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:RMC:RBPosition:UL \n
		Snippet: value: enums.RbPosition = driver.configure.connection.scc.rmc.rbPosition.uplink.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the position of the allocated uplink resource blocks, for contiguous allocation.
			INTRO_CMD_HELP: Depending on other settings, only a subset of the listed values is allowed, see: \n
			- 'Scheduling type RMC'
			- 'Scheduling type RMC for eMTC'
			- 'Scheduling type RMC for LAA' \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: position: LOW | HIGH | MID | P0 | P1 | P2 | P3 | P4 | P6 | P7 | P8 | P9 | P10 | P11 | P12 | P13 | P14 | P15 | P16 | P19 | P20 | P21 | P22 | P24 | P25 | P28 | P30 | P31 | P33 | P36 | P37 | P39 | P40 | P43 | P44 | P45 | P48 | P49 | P50 | P51 | P52 | P54 | P56 | P57 | P58 | P62 | P63 | P66 | P68 | P70 | P74 | P75 | P83 | P96 | P99"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:RMC:RBPosition:UL?')
		return Conversions.str_to_scalar_enum(response, enums.RbPosition)
