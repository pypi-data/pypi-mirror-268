from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> enums.PswState:
		"""SCPI: FETCh:LTE:SIGNaling<instance>:PSWitched:STATe \n
		Snippet: value: enums.PswState = driver.pswitched.state.fetch() \n
		Queries the PS domain state, see also 'Packet-switched states'. \n
			:return: ps_state: OFF | ON | ATTached | CESTablished | DISConnect | CONNecting | SIGNaling | SMESsage | RMESsage | IHANdover | OHANdover OFF: signal off ON: signal on ATTached: UE attached CESTablished: connection established DISConnect: disconnect in progress CONNecting: connection setup in progress SIGNaling: signaling in progress SMESsage: sending message RMESsage: receiving message IHANdover: incoming handover in progress OHANdover: outgoing handover in progress"""
		response = self._core.io.query_str(f'FETCh:LTE:SIGNaling<Instance>:PSWitched:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.PswState)
