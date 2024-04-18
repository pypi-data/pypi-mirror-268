from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PbtrCls:
	"""Pbtr commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pbtr", core, parent)

	def set(self, periodicity: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:LAA:FBURst:PBTR \n
		Snippet: driver.configure.connection.scc.laa.fburst.pbtr.set(periodicity = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the burst transmission periodicity, for LAA with fixed bursts. The minimum allowed value equals the configured
		burst length, see method RsCmwLteSig.Configure.Connection.Scc.Laa.Fburst.Blength.set. \n
			:param periodicity: numeric Range: 1 to 100
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(periodicity)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:LAA:FBURst:PBTR {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:LAA:FBURst:PBTR \n
		Snippet: value: int = driver.configure.connection.scc.laa.fburst.pbtr.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the burst transmission periodicity, for LAA with fixed bursts. The minimum allowed value equals the configured
		burst length, see method RsCmwLteSig.Configure.Connection.Scc.Laa.Fburst.Blength.set. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: periodicity: numeric Range: 1 to 100"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:LAA:FBURst:PBTR?')
		return Conversions.str_to_int(response)
