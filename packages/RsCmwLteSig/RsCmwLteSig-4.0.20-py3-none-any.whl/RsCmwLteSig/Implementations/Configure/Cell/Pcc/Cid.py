from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CidCls:
	"""Cid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cid", core, parent)

	def get_eutran(self) -> str:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:CID:EUTRan \n
		Snippet: value: str = driver.configure.cell.pcc.cid.get_eutran() \n
		Specifies the E-UTRAN cell identifier (28-digit binary number) . If you use carrier aggregation, configure different
		values for the component carriers. \n
			:return: cid: binary Range: #B0 to #B1111111111111111111111111111
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:CID:EUTRan?')
		return trim_str_response(response)

	def set_eutran(self, cid: str) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:CID:EUTRan \n
		Snippet: driver.configure.cell.pcc.cid.set_eutran(cid = rawAbc) \n
		Specifies the E-UTRAN cell identifier (28-digit binary number) . If you use carrier aggregation, configure different
		values for the component carriers. \n
			:param cid: binary Range: #B0 to #B1111111111111111111111111111
		"""
		param = Conversions.value_to_str(cid)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:CID:EUTRan {param}')
