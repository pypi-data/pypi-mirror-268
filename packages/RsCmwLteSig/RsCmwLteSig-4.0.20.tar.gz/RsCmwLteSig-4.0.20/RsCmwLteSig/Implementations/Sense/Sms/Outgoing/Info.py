from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InfoCls:
	"""Info commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("info", core, parent)

	# noinspection PyTypeChecker
	def get_lmsent(self) -> enums.LastMessageSent:
		"""SCPI: SENSe:LTE:SIGNaling<Instance>:SMS:OUTGoing:INFO:LMSent \n
		Snippet: value: enums.LastMessageSent = driver.sense.sms.outgoing.info.get_lmsent() \n
		Queries whether the last outgoing short message transfer was successful or not. \n
			:return: last_message_sent: SUCCessful | FAILed | NAV NAV is returned during an outgoing short message transfer and if there has been no transfer since the cell was switched on / the session has been started.
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:SMS:OUTGoing:INFO:LMSent?')
		return Conversions.str_to_scalar_enum(response, enums.LastMessageSent)
