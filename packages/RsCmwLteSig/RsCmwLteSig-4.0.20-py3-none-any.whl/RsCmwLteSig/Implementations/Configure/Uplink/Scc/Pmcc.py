from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PmccCls:
	"""Pmcc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmcc", core, parent)

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.UlPwrMaster:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PMCC \n
		Snippet: value: enums.UlPwrMaster = driver.configure.uplink.scc.pmcc.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Queries the UL power primary carrier for the SCC<c>. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: master: No help available"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PMCC?')
		return Conversions.str_to_scalar_enum(response, enums.UlPwrMaster)
