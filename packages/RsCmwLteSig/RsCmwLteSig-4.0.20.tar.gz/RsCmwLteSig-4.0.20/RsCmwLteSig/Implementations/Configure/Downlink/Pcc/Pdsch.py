from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdschCls:
	"""Pdsch commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdsch", core, parent)

	# noinspection PyTypeChecker
	def get_pa(self) -> enums.PowerOffset:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL[:PCC]:PDSCh:PA \n
		Snippet: value: enums.PowerOffset = driver.configure.downlink.pcc.pdsch.get_pa() \n
		Defines the power offset PA. \n
			:return: pa: ZERO | N3DB | N6DB Power offset of 0 dB | -3 dB | -6 dB
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:DL:PCC:PDSCh:PA?')
		return Conversions.str_to_scalar_enum(response, enums.PowerOffset)

	def set_pa(self, pa: enums.PowerOffset) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL[:PCC]:PDSCh:PA \n
		Snippet: driver.configure.downlink.pcc.pdsch.set_pa(pa = enums.PowerOffset.N3DB) \n
		Defines the power offset PA. \n
			:param pa: ZERO | N3DB | N6DB Power offset of 0 dB | -3 dB | -6 dB
		"""
		param = Conversions.enum_scalar_to_str(pa, enums.PowerOffset)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:DL:PCC:PDSCh:PA {param}')

	def get_rindex(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL[:PCC]:PDSCh:RINDex \n
		Snippet: value: int = driver.configure.downlink.pcc.pdsch.get_rindex() \n
		Defines the power ratio index PB. The index is required for calculation of the power level of a PDSCH resource element. \n
			:return: ratio_index: numeric Range: 0 to 3
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:DL:PCC:PDSCh:RINDex?')
		return Conversions.str_to_int(response)

	def set_rindex(self, ratio_index: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL[:PCC]:PDSCh:RINDex \n
		Snippet: driver.configure.downlink.pcc.pdsch.set_rindex(ratio_index = 1) \n
		Defines the power ratio index PB. The index is required for calculation of the power level of a PDSCH resource element. \n
			:param ratio_index: numeric Range: 0 to 3
		"""
		param = Conversions.decimal_value_to_str(ratio_index)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:DL:PCC:PDSCh:RINDex {param}')
