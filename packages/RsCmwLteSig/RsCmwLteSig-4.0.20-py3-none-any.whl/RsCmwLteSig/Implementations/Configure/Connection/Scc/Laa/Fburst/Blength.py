from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BlengthCls:
	"""Blength commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("blength", core, parent)

	def set(self, burst_length: int, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:LAA:FBURst:BLENgth \n
		Snippet: driver.configure.connection.scc.laa.fburst.blength.set(burst_length = 1, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the number of subframes per burst, for LAA with fixed bursts. \n
			:param burst_length: numeric Range: 1 to 10
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.decimal_value_to_str(burst_length)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:LAA:FBURst:BLENgth {param}')

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:SCC<Carrier>:LAA:FBURst:BLENgth \n
		Snippet: value: int = driver.configure.connection.scc.laa.fburst.blength.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Specifies the number of subframes per burst, for LAA with fixed bursts. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: burst_length: numeric Range: 1 to 10"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:SCC{secondaryCompCarrier_cmd_val}:LAA:FBURst:BLENgth?')
		return Conversions.str_to_int(response)
