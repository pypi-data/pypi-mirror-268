from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TimeoutCls:
	"""Timeout commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("timeout", core, parent)

	@property
	def t(self):
		"""t commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_t'):
			from .T import TCls
			self._t = TCls(self._core, self._cmd_group)
		return self._t

	@property
	def text(self):
		"""text commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_text'):
			from .Text import TextCls
			self._text = TextCls(self._core, self._cmd_group)
		return self._text

	def get_osynch(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:TOUT:OSYNch \n
		Snippet: value: int = driver.configure.cell.timeout.get_osynch() \n
		Specifies the time after which the instrument, having waited for a signal from the connected UE, releases the connection. \n
			:return: value: numeric Range: 1 s to 50 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:TOUT:OSYNch?')
		return Conversions.str_to_int(response)

	def set_osynch(self, value: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:TOUT:OSYNch \n
		Snippet: driver.configure.cell.timeout.set_osynch(value = 1) \n
		Specifies the time after which the instrument, having waited for a signal from the connected UE, releases the connection. \n
			:param value: numeric Range: 1 s to 50 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(value)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:TOUT:OSYNch {param}')

	def clone(self) -> 'TimeoutCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TimeoutCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
