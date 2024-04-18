from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ActionCls:
	"""Action commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("action", core, parent)

	def set(self, scc_action: enums.SccAction, secondaryCompCarrier=repcap.SecondaryCompCarrier.Default) -> None:
		"""SCPI: CALL:LTE:SIGNaling<instance>:SCC<Carrier>:ACTion \n
		Snippet: driver.call.scc.action.set(scc_action = enums.SccAction.MACactivate, secondaryCompCarrier = repcap.SecondaryCompCarrier.Default) \n
		Controls the state of the secondary component carrier (SCC) number <c>. \n
			:param scc_action: OFF | ON | RRCadd | MACactivate | MACDeactivat | RRCDelete OFF: Switch off SCC ON: Switch on SCC RRCadd: Add SCC RRC connection MACactivate: Activate MAC for the SCC MACDeactivat: Deactivate MAC for the SCC RRCDelete: Delete SCC RRC connection
			:param secondaryCompCarrier: optional repeated capability selector. Default value: CC1 (settable in the interface 'Scc')
		"""
		param = Conversions.enum_scalar_to_str(scc_action, enums.SccAction)
		secondaryCompCarrier_cmd_val = self._cmd_group.get_repcap_cmd_value(secondaryCompCarrier, repcap.SecondaryCompCarrier)
		self._core.io.write_with_opc(f'CALL:LTE:SIGNaling<Instance>:SCC{secondaryCompCarrier_cmd_val}:ACTion {param}')
