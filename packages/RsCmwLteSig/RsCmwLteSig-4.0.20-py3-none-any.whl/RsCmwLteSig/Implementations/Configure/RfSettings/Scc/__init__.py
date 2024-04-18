from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SccCls:
	"""Scc commands group definition. 21 total commands, 9 Subgroups, 0 group commands
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
	def userDefined(self):
		"""userDefined commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_userDefined'):
			from .UserDefined import UserDefinedCls
			self._userDefined = UserDefinedCls(self._core, self._cmd_group)
		return self._userDefined

	@property
	def mixerLevelOffset(self):
		"""mixerLevelOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mixerLevelOffset'):
			from .MixerLevelOffset import MixerLevelOffsetCls
			self._mixerLevelOffset = MixerLevelOffsetCls(self._core, self._cmd_group)
		return self._mixerLevelOffset

	@property
	def eattenuation(self):
		"""eattenuation commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_eattenuation'):
			from .Eattenuation import EattenuationCls
			self._eattenuation = EattenuationCls(self._core, self._cmd_group)
		return self._eattenuation

	@property
	def channel(self):
		"""channel commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import ChannelCls
			self._channel = ChannelCls(self._core, self._cmd_group)
		return self._channel

	@property
	def foffset(self):
		"""foffset commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_foffset'):
			from .Foffset import FoffsetCls
			self._foffset = FoffsetCls(self._core, self._cmd_group)
		return self._foffset

	@property
	def udSeparation(self):
		"""udSeparation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_udSeparation'):
			from .UdSeparation import UdSeparationCls
			self._udSeparation = UdSeparationCls(self._core, self._cmd_group)
		return self._udSeparation

	@property
	def envelopePower(self):
		"""envelopePower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_envelopePower'):
			from .EnvelopePower import EnvelopePowerCls
			self._envelopePower = EnvelopePowerCls(self._core, self._cmd_group)
		return self._envelopePower

	@property
	def enpMode(self):
		"""enpMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enpMode'):
			from .EnpMode import EnpModeCls
			self._enpMode = EnpModeCls(self._core, self._cmd_group)
		return self._enpMode

	@property
	def umargin(self):
		"""umargin commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_umargin'):
			from .Umargin import UmarginCls
			self._umargin = UmarginCls(self._core, self._cmd_group)
		return self._umargin

	def clone(self) -> 'SccCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SccCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
