from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TburstsCls:
	"""Tbursts commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tbursts", core, parent)

	def set(self, bursts: enums.Bursts, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:LAA:TBURsts \n
		Snippet: driver.configure.connection.scc.laa.tbursts.set(bursts = enums.Bursts.FBURst, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects between fixed transmission bursts and random transmission bursts for LAA. \n
			:param bursts: FBURst | RBURst FBURst: fixed transmission bursts RBURst: random transmission bursts
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(bursts, enums.Bursts)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:LAA:TBURsts {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.Bursts:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:LAA:TBURsts \n
		Snippet: value: enums.Bursts = driver.configure.connection.scc.laa.tbursts.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects between fixed transmission bursts and random transmission bursts for LAA. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: bursts: FBURst | RBURst FBURst: fixed transmission bursts RBURst: random transmission bursts"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:LAA:TBURsts?')
		return Conversions.str_to_scalar_enum(response, enums.Bursts)
