from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ManualCls:
	"""Manual commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("manual", core, parent)

	def get_enhanced(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UECategory:MANual:ENHanced \n
		Snippet: value: float = driver.configure.connection.ueCategory.manual.get_enhanced() \n
		Configures the UE category to be used by the R&S CMW if no reported value is available or usage of the reported value is
		disabled, see method RsCmwLteSig.Configure.Connection.UeCategory.Reported.Enhanced.set. \n
			:return: ue_cat_manual: M1 | M2 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:UECategory:MANual:ENHanced?')
		return Conversions.str_to_float(response)

	def set_enhanced(self, ue_cat_manual: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UECategory:MANual:ENHanced \n
		Snippet: driver.configure.connection.ueCategory.manual.set_enhanced(ue_cat_manual = 1.0) \n
		Configures the UE category to be used by the R&S CMW if no reported value is available or usage of the reported value is
		disabled, see method RsCmwLteSig.Configure.Connection.UeCategory.Reported.Enhanced.set. \n
			:param ue_cat_manual: M1 | M2 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12
		"""
		param = Conversions.decimal_value_to_str(ue_cat_manual)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:UECategory:MANual:ENHanced {param}')

	def get_value(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UECategory:MANual \n
		Snippet: value: int = driver.configure.connection.ueCategory.manual.get_value() \n
		No command help available \n
			:return: ue_cat_manual: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:UECategory:MANual?')
		return Conversions.str_to_int(response)

	def set_value(self, ue_cat_manual: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection:UECategory:MANual \n
		Snippet: driver.configure.connection.ueCategory.manual.set_value(ue_cat_manual = 1) \n
		No command help available \n
			:param ue_cat_manual: No help available
		"""
		param = Conversions.decimal_value_to_str(ue_cat_manual)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:UECategory:MANual {param}')
