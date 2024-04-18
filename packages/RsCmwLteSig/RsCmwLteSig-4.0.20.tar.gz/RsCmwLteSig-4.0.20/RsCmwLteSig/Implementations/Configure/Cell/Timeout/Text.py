from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TextCls:
	"""Text commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Text, default value after init: Text.T3324"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("text", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_text_get', 'repcap_text_set', repcap.Text.T3324)

	def repcap_text_set(self, text: repcap.Text) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Text.Default
		Default value after init: Text.T3324"""
		self._cmd_group.set_repcap_enum_value(text)

	def repcap_text_get(self) -> repcap.Text:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, value: int or bool, text=repcap.Text.Default) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:TOUT:TEXT<nr> \n
		Snippet: driver.configure.cell.timeout.text.set(value = 1, text = repcap.Text.Default) \n
		Configures an extended value for timer T3412. The information element supports the values 1 to 31 combined with the units
		2 s, 30 s, 1 min, 10 min, 1 h, 10 h and 320 h. This command configures the timer value in seconds. So there are subranges
		with different increments. \n
			:param value: (integer or boolean) numeric | ON | OFF Range: 2 s to 35712000 s ON | OFF enables or disables the timer.
			:param text: optional repeated capability selector. Default value: T3324 (settable in the interface 'Text')
		"""
		param = Conversions.decimal_or_bool_value_to_str(value)
		text_cmd_val = self._cmd_group.get_repcap_cmd_value(text, repcap.Text)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:TOUT:TEXT{text_cmd_val} {param}')

	def get(self, text=repcap.Text.Default) -> int or bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:TOUT:TEXT<nr> \n
		Snippet: value: int or bool = driver.configure.cell.timeout.text.get(text = repcap.Text.Default) \n
		Configures an extended value for timer T3412. The information element supports the values 1 to 31 combined with the units
		2 s, 30 s, 1 min, 10 min, 1 h, 10 h and 320 h. This command configures the timer value in seconds. So there are subranges
		with different increments. \n
			:param text: optional repeated capability selector. Default value: T3324 (settable in the interface 'Text')
			:return: value: (integer or boolean) numeric | ON | OFF Range: 2 s to 35712000 s ON | OFF enables or disables the timer."""
		text_cmd_val = self._cmd_group.get_repcap_cmd_value(text, repcap.Text)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CELL:TOUT:TEXT{text_cmd_val}?')
		return Conversions.str_to_int_or_bool(response)

	def clone(self) -> 'TextCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = TextCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
