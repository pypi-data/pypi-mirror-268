from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PeriodCls:
	"""Period commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("period", core, parent)

	def set(self, period: enums.LaaPeriod, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:SCC<Carrier>:DMTC:PERiod \n
		Snippet: driver.configure.ueReport.scc.dmtc.period.set(period = enums.LaaPeriod.MS160, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the periodicity of the DRS for LAA. \n
			:param period: MS40 | MS80 | MS160 Periodicity in ms
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(period, enums.LaaPeriod)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:SCC{secondaryCompCarrier_cmd_val}:DMTC:PERiod {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.LaaPeriod:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UEReport:SCC<Carrier>:DMTC:PERiod \n
		Snippet: value: enums.LaaPeriod = driver.configure.ueReport.scc.dmtc.period.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the periodicity of the DRS for LAA. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: period: MS40 | MS80 | MS160 Periodicity in ms"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:UEReport:SCC{secondaryCompCarrier_cmd_val}:DMTC:PERiod?')
		return Conversions.str_to_scalar_enum(response, enums.LaaPeriod)
