from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardCls:
	"""Standard commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("standard", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:STANdard:ENABle \n
		Snippet: value: bool = driver.configure.fading.pcc.fadingSimulator.standard.get_enable() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:STANdard:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:STANdard:ENABle \n
		Snippet: driver.configure.fading.pcc.fadingSimulator.standard.set_enable(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:STANdard:ENABle {param}')

	# noinspection PyTypeChecker
	def get_profile(self) -> enums.FadingProfile:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:STANdard:PROFile \n
		Snippet: value: enums.FadingProfile = driver.configure.fading.pcc.fadingSimulator.standard.get_profile() \n
		No command help available \n
			:return: profile: No help available
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:STANdard:PROFile?')
		return Conversions.str_to_scalar_enum(response, enums.FadingProfile)

	def set_profile(self, profile: enums.FadingProfile) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:FADing[:PCC]:FSIMulator:STANdard:PROFile \n
		Snippet: driver.configure.fading.pcc.fadingSimulator.standard.set_profile(profile = enums.FadingProfile.CTESt) \n
		No command help available \n
			:param profile: No help available
		"""
		param = Conversions.enum_scalar_to_str(profile, enums.FadingProfile)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:FADing:PCC:FSIMulator:STANdard:PROFile {param}')
