from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PeriodCls:
	"""Period commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("period", core, parent)

	def set(self, period: enums.LaaUePeriod, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:SCC<Carrier>:RSSI:RMTC:PERiod \n
		Snippet: driver.configure.ueReport.scc.rssi.rmtc.period.set(period = enums.LaaUePeriod.MS160, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the periodicity of UE measurements for LAA. \n
			:param period: MS40 | MS80 | MS160 | MS320 | MS640 Periodicity in ms
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(period, enums.LaaUePeriod)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:SCC{secondaryCompCarrier_cmd_val}:RSSI:RMTC:PERiod {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.LaaUePeriod:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:SCC<Carrier>:RSSI:RMTC:PERiod \n
		Snippet: value: enums.LaaUePeriod = driver.configure.ueReport.scc.rssi.rmtc.period.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the periodicity of UE measurements for LAA. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: period: MS40 | MS80 | MS160 | MS320 | MS640 Periodicity in ms"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:SCC{secondaryCompCarrier_cmd_val}:RSSI:RMTC:PERiod?')
		return Conversions.str_to_scalar_enum(response, enums.LaaUePeriod)
