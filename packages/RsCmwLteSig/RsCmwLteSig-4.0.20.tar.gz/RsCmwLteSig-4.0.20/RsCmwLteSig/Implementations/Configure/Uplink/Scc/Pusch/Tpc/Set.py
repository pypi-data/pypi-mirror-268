from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SetCls:
	"""Set commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("set", core, parent)

	def set(self, set_type: enums.SetType, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PUSCh:TPC:SET \n
		Snippet: driver.configure.uplink.scc.pusch.tpc.set.set(set_type = enums.SetType.ALT0, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the active TPC setup to be executed for power control of the PUSCH. For some TPC setups, the execution must be
		explicitly triggered via method RsCmwLteSig.Configure.Uplink.Pcc.Pusch.Tpc.Pexecute.set. \n
			:param set_type: MINPower | MAXPower | CONStant | SINGle | UDSingle | UDContinuous | ALT0 | CLOop | RPControl | FULPower MINPower: command the UE to minimum power MAXPower: command the UE to maximum power CONStant: command the UE to keep the power constant SINGle: send a pattern once (only one type of TPC command) UDSingle: send a pattern once (mixed TPC commands allowed) UDContinuous: send a pattern continuously ALT0: send an alternating pattern continuously CLOop: command the UE to a configurable target power RPControl: patterns for 3GPP relative power control test FULPower: flexible uplink power
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(set_type, enums.SetType)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PUSCh:TPC:SET {param}')

	# noinspection PyTypeChecker
	def get(self, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> enums.SetType:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL:SCC<Carrier>:PUSCh:TPC:SET \n
		Snippet: value: enums.SetType = driver.configure.uplink.scc.pusch.tpc.set.get(secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Selects the active TPC setup to be executed for power control of the PUSCH. For some TPC setups, the execution must be
		explicitly triggered via method RsCmwLteSig.Configure.Uplink.Pcc.Pusch.Tpc.Pexecute.set. \n
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
			:return: set_type: MINPower | MAXPower | CONStant | SINGle | UDSingle | UDContinuous | ALT0 | CLOop | RPControl | FULPower MINPower: command the UE to minimum power MAXPower: command the UE to maximum power CONStant: command the UE to keep the power constant SINGle: send a pattern once (only one type of TPC command) UDSingle: send a pattern once (mixed TPC commands allowed) UDContinuous: send a pattern continuously ALT0: send an alternating pattern continuously CLOop: command the UE to a configurable target power RPControl: patterns for 3GPP relative power control test FULPower: flexible uplink power"""
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:UL:SCC{secondaryCompCarrier_cmd_val}:PUSCh:TPC:SET?')
		return Conversions.str_to_scalar_enum(response, enums.SetType)
