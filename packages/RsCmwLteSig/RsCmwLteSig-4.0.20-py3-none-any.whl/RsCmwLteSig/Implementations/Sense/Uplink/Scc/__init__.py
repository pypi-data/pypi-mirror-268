from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SccCls:
	"""Scc commands group definition. 8 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: SecondaryCompCarrier, default value after init: SecondaryCompCarrier.CC1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scc", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_secondaryCompCarrier_get', 'repcap_secondaryCompCarrier_set', repcap.SecondaryCompCarrier.CC1)

	def repcap_secondaryCompCarrier_set(self, secondaryCompCarrier: repcap.SecondaryCompCarrier) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SecondaryCompCarrier.Default
		Default value after init: SecondaryCompCarrier.CC1"""
		self._cmd_group.set_repcap_enum_value(secondaryCompCarrier)

	def repcap_secondaryCompCarrier_get(self) -> repcap.SecondaryCompCarrier:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def apPower(self):
		"""apPower commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_apPower'):
			from .ApPower import ApPowerCls
			self._apPower = ApPowerCls(self._core, self._cmd_group)
		return self._apPower

	def clone(self) -> 'SccCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SccCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
