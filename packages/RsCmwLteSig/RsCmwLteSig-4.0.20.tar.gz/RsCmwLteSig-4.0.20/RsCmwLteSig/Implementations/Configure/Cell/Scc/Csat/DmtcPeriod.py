from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DmtcPeriodCls:
	"""DmtcPeriod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dmtcPeriod", core, parent)

	def set(self, period: enums.LdsPeriod, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<Carrier>:CSAT:DMTCperiod \n
		Snippet: driver.configure.cell.scc.csat.dmtcPeriod.set(period = enums.LdsPeriod.M160, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the LDS periodicity. \n
			:param period: M40 | M80 | M160 40 ms, 80 ms, 160 ms
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(period, enums.LdsPeriod)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:CSAT:DMTCperiod {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.LdsPeriod:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:SCC<Carrier>:CSAT:DMTCperiod \n
		Snippet: value: enums.LdsPeriod = driver.configure.cell.scc.csat.dmtcPeriod.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Configures the LDS periodicity. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: period: M40 | M80 | M160 40 ms, 80 ms, 160 ms"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CELL:SCC{secondaryCompCarrier_cmd_val}:CSAT:DMTCperiod?')
		return Conversions.str_to_scalar_enum(response, enums.LdsPeriod)
