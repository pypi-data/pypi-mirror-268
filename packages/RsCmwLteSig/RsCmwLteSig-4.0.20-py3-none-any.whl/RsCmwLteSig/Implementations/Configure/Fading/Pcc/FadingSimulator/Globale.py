from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GlobaleCls:
	"""Globale commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("globale", core, parent)

	def get_seed(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:GLOBal:SEED \n
		Snippet: value: int = driver.configure.fading.pcc.fadingSimulator.globale.get_seed() \n
		Sets the start seed for the pseudo-random fading algorithm. \n
			:return: seed: numeric Range: 0 to 9
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:GLOBal:SEED?')
		return Conversions.str_to_int(response)

	def set_seed(self, seed: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:GLOBal:SEED \n
		Snippet: driver.configure.fading.pcc.fadingSimulator.globale.set_seed(seed = 1) \n
		Sets the start seed for the pseudo-random fading algorithm. \n
			:param seed: numeric Range: 0 to 9
		"""
		param = Conversions.decimal_value_to_str(seed)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:GLOBal:SEED {param}')
