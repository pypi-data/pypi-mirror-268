from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SearchCls:
	"""Search commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("search", core, parent)

	def get_intrasearch(self) -> float or bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:RESelection:SEARch:INTRasearch \n
		Snippet: value: float or bool = driver.configure.cell.reSelection.search.get_intrasearch() \n
		Defines the threshold SIntraSearch. The value divided by 2 is broadcasted to the UE in SIB3. \n
			:return: sintra_search: (float or boolean) numeric | ON | OFF Range: 0 dB to 62 dB, Unit: dB ON | OFF enables or disables transmission of the information element.
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:RESelection:SEARch:INTRasearch?')
		return Conversions.str_to_float_or_bool(response)

	def set_intrasearch(self, sintra_search: float or bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:RESelection:SEARch:INTRasearch \n
		Snippet: driver.configure.cell.reSelection.search.set_intrasearch(sintra_search = 1.0) \n
		Defines the threshold SIntraSearch. The value divided by 2 is broadcasted to the UE in SIB3. \n
			:param sintra_search: (float or boolean) numeric | ON | OFF Range: 0 dB to 62 dB, Unit: dB ON | OFF enables or disables transmission of the information element.
		"""
		param = Conversions.decimal_or_bool_value_to_str(sintra_search)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:RESelection:SEARch:INTRasearch {param}')

	def get_nintrasearch(self) -> float or bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:RESelection:SEARch:NINTrasearch \n
		Snippet: value: float or bool = driver.configure.cell.reSelection.search.get_nintrasearch() \n
		Defines the threshold SnonIntraSearch. The value divided by 2 is broadcasted to the UE in SIB3. \n
			:return: snonintra_search: (float or boolean) numeric | ON | OFF Range: 0 dB to 62 dB, Unit: dB ON | OFF enables or disables transmission of the information element.
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:RESelection:SEARch:NINTrasearch?')
		return Conversions.str_to_float_or_bool(response)

	def set_nintrasearch(self, snonintra_search: float or bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:RESelection:SEARch:NINTrasearch \n
		Snippet: driver.configure.cell.reSelection.search.set_nintrasearch(snonintra_search = 1.0) \n
		Defines the threshold SnonIntraSearch. The value divided by 2 is broadcasted to the UE in SIB3. \n
			:param snonintra_search: (float or boolean) numeric | ON | OFF Range: 0 dB to 62 dB, Unit: dB ON | OFF enables or disables transmission of the information element.
		"""
		param = Conversions.decimal_or_bool_value_to_str(snonintra_search)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:RESelection:SEARch:NINTrasearch {param}')
