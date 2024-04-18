from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeIdentityCls:
	"""UeIdentity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ueIdentity", core, parent)

	def get_imsi(self) -> str:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:UEIDentity:IMSI \n
		Snippet: value: str = driver.configure.cell.ueIdentity.get_imsi() \n
		Specifies the default IMSI. \n
			:return: value: string 14 to 16 digits
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:UEIDentity:IMSI?')
		return trim_str_response(response)

	def set_imsi(self, value: str) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:UEIDentity:IMSI \n
		Snippet: driver.configure.cell.ueIdentity.set_imsi(value = 'abc') \n
		Specifies the default IMSI. \n
			:param value: string 14 to 16 digits
		"""
		param = Conversions.value_to_quoted_str(value)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:UEIDentity:IMSI {param}')
