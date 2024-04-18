from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdcchCls:
	"""Pdcch commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdcch", core, parent)

	def get_poffset(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL[:PCC]:PDCCh:POFFset \n
		Snippet: value: float = driver.configure.downlink.pcc.pdcch.get_poffset() \n
		Defines the power level of a physical downlink control channel (PDCCH) resource element. \n
			:return: offset: numeric PDCCH power relative to RS EPRE Range: -30 dB to 0 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:DL:PCC:PDCCh:POFFset?')
		return Conversions.str_to_float(response)

	def set_poffset(self, offset: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:DL[:PCC]:PDCCh:POFFset \n
		Snippet: driver.configure.downlink.pcc.pdcch.set_poffset(offset = 1.0) \n
		Defines the power level of a physical downlink control channel (PDCCH) resource element. \n
			:param offset: numeric PDCCH power relative to RS EPRE Range: -30 dB to 0 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:DL:PCC:PDCCh:POFFset {param}')
