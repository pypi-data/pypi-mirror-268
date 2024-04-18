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
	def fetch(self) -> enums.SyncState:
		"""SCPI: FETCh:LTE:SIGNaling<instance>:B:STATe \n
		Snippet: value: enums.SyncState = driver.b.state.fetch() \n
		Query the state of the SCC synchronization set A or B, see also 'SCC states'. \n
			:return: sync_set_bstate: OFF | ON | RRCadded | MACactivated OFF: SCC off ON: SCC on RRCadded: RRC added MACactivated: MAC activated"""
		response = self._core.io.query_str(f'FETCh:LTE:SIGNaling<Instance>:B:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.SyncState)
