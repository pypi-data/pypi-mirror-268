from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PccCls:
	"""Pcc commands group definition. 13 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcc", core, parent)

	@property
	def confidence(self):
		"""confidence commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_confidence'):
			from .Confidence import ConfidenceCls
			self._confidence = ConfidenceCls(self._core, self._cmd_group)
		return self._confidence

	@property
	def absolute(self):
		"""absolute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_absolute'):
			from .Absolute import AbsoluteCls
			self._absolute = AbsoluteCls(self._core, self._cmd_group)
		return self._absolute

	@property
	def relative(self):
		"""relative commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_relative'):
			from .Relative import RelativeCls
			self._relative = RelativeCls(self._core, self._cmd_group)
		return self._relative

	@property
	def stream(self):
		"""stream commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_stream'):
			from .Stream import StreamCls
			self._stream = StreamCls(self._core, self._cmd_group)
		return self._stream

	@property
	def harq(self):
		"""harq commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_harq'):
			from .Harq import HarqCls
			self._harq = HarqCls(self._core, self._cmd_group)
		return self._harq

	@property
	def cqiReporting(self):
		"""cqiReporting commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cqiReporting'):
			from .CqiReporting import CqiReportingCls
			self._cqiReporting = CqiReportingCls(self._core, self._cmd_group)
		return self._cqiReporting

	@property
	def ri(self):
		"""ri commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ri'):
			from .Ri import RiCls
			self._ri = RiCls(self._core, self._cmd_group)
		return self._ri

	@property
	def pmi(self):
		"""pmi commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmi'):
			from .Pmi import PmiCls
			self._pmi = PmiCls(self._core, self._cmd_group)
		return self._pmi

	@property
	def uplink(self):
		"""uplink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uplink'):
			from .Uplink import UplinkCls
			self._uplink = UplinkCls(self._core, self._cmd_group)
		return self._uplink

	def clone(self) -> 'PccCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PccCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
