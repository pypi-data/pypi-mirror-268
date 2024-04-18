from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EasyCls:
	"""Easy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("easy", core, parent)

	def get_bfbw(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:EASY:BFBW \n
		Snippet: value: bool = driver.configure.connection.easy.get_bfbw() \n
		Specifies whether the easy mode is used if the band or the frequency or the cell bandwidth is changed. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:EASY:BFBW?')
		return Conversions.str_to_bool(response)

	def set_bfbw(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:EASY:BFBW \n
		Snippet: driver.configure.connection.easy.set_bfbw(enable = False) \n
		Specifies whether the easy mode is used if the band or the frequency or the cell bandwidth is changed. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:EASY:BFBW {param}')
