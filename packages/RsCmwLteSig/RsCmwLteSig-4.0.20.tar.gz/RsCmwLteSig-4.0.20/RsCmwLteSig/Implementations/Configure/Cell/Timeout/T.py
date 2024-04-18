from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TCls:
	"""T commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("t", core, parent)

	def set(self, value: int or bool, text=repcap.Text.T3324) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:TOUT:T<nr> \n
		Snippet: driver.configure.cell.timeout.t.set(value = 1, text = repcap.Text.T3324) \n
			INTRO_CMD_HELP: Configures one of the following timers: \n
			- T3402, attach/TAU reattempts
			- T3412, periodic tracking area updates
		The information elements support the values 1 to 31 combined with the units 2 seconds, 1 minute and 6 minutes.
		This command configures the timer value in seconds. So there are three subranges with different increments. \n
			:param value: (integer or boolean) numeric | ON | OFF Range: 2 s to 11160 s ON | OFF enables or disables the timer.
			:param text: optional repeated capability selector. Default value: T3324
		"""
		param = Conversions.decimal_or_bool_value_to_str(value)
		text_cmd_val = self._cmd_group.get_repcap_cmd_value(text, repcap.Text)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:TOUT:T{text_cmd_val} {param}')

	def get(self, text=repcap.Text.T3324) -> int or bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:TOUT:T<nr> \n
		Snippet: value: int or bool = driver.configure.cell.timeout.t.get(text = repcap.Text.T3324) \n
			INTRO_CMD_HELP: Configures one of the following timers: \n
			- T3402, attach/TAU reattempts
			- T3412, periodic tracking area updates
		The information elements support the values 1 to 31 combined with the units 2 seconds, 1 minute and 6 minutes.
		This command configures the timer value in seconds. So there are three subranges with different increments. \n
			:param text: optional repeated capability selector. Default value: T3324
			:return: value: (integer or boolean) numeric | ON | OFF Range: 2 s to 11160 s ON | OFF enables or disables the timer."""
		text_cmd_val = self._cmd_group.get_repcap_cmd_value(text, repcap.Text)
		response = self._core.io.query_str(f'CONFigure:LTE:SIGNaling<Instance>:CELL:TOUT:T{text_cmd_val}?')
		return Conversions.str_to_int_or_bool(response)
