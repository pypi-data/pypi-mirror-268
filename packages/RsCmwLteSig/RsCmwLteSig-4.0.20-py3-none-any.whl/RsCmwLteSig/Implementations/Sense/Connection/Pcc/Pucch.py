from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PucchCls:
	"""Pucch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pucch", core, parent)

	# noinspection PyTypeChecker
	def get_ffca(self) -> enums.PucchFormat:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:CONNection[:PCC]:PUCCh:FFCA \n
		Snippet: value: enums.PucchFormat = driver.sense.connection.pcc.pucch.get_ffca() \n
		Queries the PUCCH format used for carrier aggregation scenarios. \n
			:return: format_py: F1BCs | F3 | F4 | F5 F1BCs: PUCCH format 1b with channel selection F3: PUCCH format 3 F4: PUCCH format 4 F5: PUCCH format 5
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:CONNection:PCC:PUCCh:FFCA?')
		return Conversions.str_to_scalar_enum(response, enums.PucchFormat)
