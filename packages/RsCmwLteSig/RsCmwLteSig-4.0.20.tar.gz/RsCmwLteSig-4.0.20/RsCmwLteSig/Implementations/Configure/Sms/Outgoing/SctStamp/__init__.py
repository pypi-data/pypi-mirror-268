from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SctStampCls:
	"""SctStamp commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sctStamp", core, parent)

	@property
	def date(self):
		"""date commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_date'):
			from .Date import DateCls
			self._date = DateCls(self._core, self._cmd_group)
		return self._date

	@property
	def time(self):
		"""time commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Time import TimeCls
			self._time = TimeCls(self._core, self._cmd_group)
		return self._time

	# noinspection PyTypeChecker
	def get_tsource(self) -> enums.SourceTime:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:SCTStamp:TSOurce \n
		Snippet: value: enums.SourceTime = driver.configure.sms.outgoing.sctStamp.get_tsource() \n
		Selects the source for the service center time stamp.
			INTRO_CMD_HELP: The date and time for the source DATE is configured via the following commands: \n
			- method RsCmwLteSig.Configure.Sms.Outgoing.SctStamp.Date.set
			- method RsCmwLteSig.Configure.Sms.Outgoing.SctStamp.Time.set \n
			:return: source_time: CMWTime | DATE CMWTime: Current date and time of the operation system DATE: Date and time specified via remote commands
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:SCTStamp:TSOurce?')
		return Conversions.str_to_scalar_enum(response, enums.SourceTime)

	def set_tsource(self, source_time: enums.SourceTime) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:SCTStamp:TSOurce \n
		Snippet: driver.configure.sms.outgoing.sctStamp.set_tsource(source_time = enums.SourceTime.CMWTime) \n
		Selects the source for the service center time stamp.
			INTRO_CMD_HELP: The date and time for the source DATE is configured via the following commands: \n
			- method RsCmwLteSig.Configure.Sms.Outgoing.SctStamp.Date.set
			- method RsCmwLteSig.Configure.Sms.Outgoing.SctStamp.Time.set \n
			:param source_time: CMWTime | DATE CMWTime: Current date and time of the operation system DATE: Date and time specified via remote commands
		"""
		param = Conversions.enum_scalar_to_str(source_time, enums.SourceTime)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:SMS:OUTGoing:SCTStamp:TSOurce {param}')

	def clone(self) -> 'SctStampCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SctStampCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
