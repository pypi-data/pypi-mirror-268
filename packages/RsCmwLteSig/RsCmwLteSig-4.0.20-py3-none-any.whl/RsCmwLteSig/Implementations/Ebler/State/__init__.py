from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StateCls:
	"""State commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import AllCls
			self._all = AllCls(self._core, self._cmd_group)
		return self._all

	# noinspection PyTypeChecker
	def fetch(self) -> enums.ResourceState:
		"""SCPI: FETCh:LTE:SIGNaling<instance>:EBLer:STATe \n
		Snippet: value: enums.ResourceState = driver.ebler.state.fetch() \n
		Queries the main measurement state. Use FETCh:...:STATe:ALL? to query the measurement state including the substates. Use
		INITiate..., STOP..., ABORt... to change the measurement state. \n
			:return: state: OFF | RUN | RDY OFF: measurement off, no resources allocated, no results RUN: measurement running, synchronization pending or adjusted, resources active or queued RDY: measurement terminated, valid results can be available"""
		response = self._core.io.query_str(f'FETCh:LTE:SIGNaling<Instance>:EBLer:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.ResourceState)

	def clone(self) -> 'StateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = StateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
