from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LrMessageCls:
	"""LrMessage commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lrMessage", core, parent)

	def get_rflag(self) -> bool:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:SMS:INFO:LRMessage:RFLag \n
		Snippet: value: bool = driver.sense.sms.info.lrMessage.get_rflag() \n
		Queries the 'message read' flag for the last received message.
			INTRO_CMD_HELP: The flag is true (ON) in the following cases: \n
			- No SMS message has been received.
			- The last received SMS message has been read, see method RsCmwLteSig.Sense.Sms.Incoming.Info.mtext.
			- The last received SMS message has been deleted, see method RsCmwLteSig.Clean.Sms.Incoming.Info.Mtext.set. \n
			:return: last_rec_mess_read: OFF | ON OFF: unread message available ON: no unread message available
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:SMS:INFO:LRMessage:RFLag?')
		return Conversions.str_to_bool(response)
