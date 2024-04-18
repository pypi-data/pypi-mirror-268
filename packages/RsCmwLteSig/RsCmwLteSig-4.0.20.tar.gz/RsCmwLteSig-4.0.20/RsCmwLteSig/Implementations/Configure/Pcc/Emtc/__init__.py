from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EmtcCls:
	"""Emtc commands group definition. 33 total commands, 6 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("emtc", core, parent)

	@property
	def mpdcch(self):
		"""mpdcch commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_mpdcch'):
			from .Mpdcch import MpdcchCls
			self._mpdcch = MpdcchCls(self._core, self._cmd_group)
		return self._mpdcch

	@property
	def pdsch(self):
		"""pdsch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdsch'):
			from .Pdsch import PdschCls
			self._pdsch = PdschCls(self._core, self._cmd_group)
		return self._pdsch

	@property
	def pucch(self):
		"""pucch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pucch'):
			from .Pucch import PucchCls
			self._pucch = PucchCls(self._core, self._cmd_group)
		return self._pucch

	@property
	def pusch(self):
		"""pusch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pusch'):
			from .Pusch import PuschCls
			self._pusch = PuschCls(self._core, self._cmd_group)
		return self._pusch

	@property
	def ce(self):
		"""ce commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_ce'):
			from .Ce import CeCls
			self._ce = CeCls(self._core, self._cmd_group)
		return self._ce

	@property
	def hopping(self):
		"""hopping commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_hopping'):
			from .Hopping import HoppingCls
			self._hopping = HoppingCls(self._core, self._cmd_group)
		return self._hopping

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:ENABle \n
		Snippet: value: bool = driver.configure.pcc.emtc.get_enable() \n
		Enables or disables eMTC. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:ENABle \n
		Snippet: driver.configure.pcc.emtc.set_enable(enable = False) \n
		Enables or disables eMTC. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:ENABle {param}')

	def get_mb(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:MB<number> \n
		Snippet: value: bool = driver.configure.pcc.emtc.get_mb() \n
		Selects the maximum bandwidth for an eMTC connection. \n
			:return: enable: OFF | ON OFF: Max bandwidth 1.4 MHz ON: Max bandwidth 5 MHz
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:MB5?')
		return Conversions.str_to_bool(response)

	def set_mb(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>[:PCC]:EMTC:MB<number> \n
		Snippet: driver.configure.pcc.emtc.set_mb(enable = False) \n
		Selects the maximum bandwidth for an eMTC connection. \n
			:param enable: OFF | ON OFF: Max bandwidth 1.4 MHz ON: Max bandwidth 5 MHz
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:PCC:EMTC:MB5 {param}')

	def clone(self) -> 'EmtcCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EmtcCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
