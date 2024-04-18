from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhichCls:
	"""Phich commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phich", core, parent)

	def get_poffset(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL[:PCC]:PHICh:POFFset \n
		Snippet: value: float = driver.configure.downlink.pcc.phich.get_poffset() \n
		Defines the power level of a physical hybrid ARQ indicator channel (PHICH) resource element. \n
			:return: offset: numeric PHICH power relative to RS EPRE Range: -30 dB to 0 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:DL:PCC:PHICh:POFFset?')
		return Conversions.str_to_float(response)

	def set_poffset(self, offset: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL[:PCC]:PHICh:POFFset \n
		Snippet: driver.configure.downlink.pcc.phich.set_poffset(offset = 1.0) \n
		Defines the power level of a physical hybrid ARQ indicator channel (PHICH) resource element. \n
			:param offset: numeric PHICH power relative to RS EPRE Range: -30 dB to 0 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:DL:PCC:PHICh:POFFset {param}')
