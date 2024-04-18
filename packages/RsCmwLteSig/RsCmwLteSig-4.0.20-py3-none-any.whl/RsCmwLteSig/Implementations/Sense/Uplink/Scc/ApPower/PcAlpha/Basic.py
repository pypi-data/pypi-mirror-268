from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BasicCls:
	"""Basic commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("basic", core, parent)

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.PathCompAlpha:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UL:SCC<Carrier>:APPower:PCALpha:BASic \n
		Snippet: value: enums.PathCompAlpha = driver.sense.uplink.scc.apPower.pcAlpha.basic.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Queries the value of parameter 'alpha', signaled to the UE if basic UL power configuration applies. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: path_comp_alpha: ZERO | DOT4 | DOT5 | DOT6 | DOT7 | DOT8 | DOT9 | ONE ZERO: 0 DOT4 ... DOT9: 0.4 ... 0.9 ONE: 1.0"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:APPower:PCALpha:BASic?')
		return Conversions.str_to_scalar_enum(response, enums.PathCompAlpha)
