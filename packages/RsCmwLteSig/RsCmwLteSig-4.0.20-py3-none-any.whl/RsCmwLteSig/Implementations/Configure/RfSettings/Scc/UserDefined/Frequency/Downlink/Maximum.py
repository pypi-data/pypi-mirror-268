from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:RFSettings:SCC<Carrier>:UDEFined:FREQuency:DL:MAXimum \n
		Snippet: value: int = driver.configure.rfSettings.scc.userDefined.frequency.downlink.maximum.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Queries the maximum downlink carrier center frequency resulting from the user-defined band settings. For calculation, see
		method RsCmwLteSig.Configure.RfSettings.Pcc.UserDefined.Frequency.Downlink.minimum. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: frequency: decimal Range: 70 MHz to 6 GHz, Unit: Hz"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:RFSettings:SCC{secondaryCompCarrier_cmd_val}:UDEFined:FREQuency:DL:MAXimum?')
		return Conversions.str_to_int(response)
