from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UplinkCls:
	"""Uplink commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	def get(self, uLqam=repcap.ULqam.QAM64) -> int:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:RF:UL<qam> \n
		Snippet: value: int = driver.sense.ueCapability.rf.uplink.get(uLqam = repcap.ULqam.QAM64) \n
		Returns a list of values indicating whether the UE supports UL 64-QAM in the individual E-UTRA operating bands. \n
			:param uLqam: optional repeated capability selector. Default value: QAM64
			:return: capabilities: 0 | 1 256 values: user-defined band, band 1 to band 255"""
		uLqam_cmd_val = self._cmd_group.get_repcap_cmd_value(uLqam, repcap.ULqam)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:UECapability:RF:UL{uLqam_cmd_val}?')
		return Conversions.str_to_int(response)
