from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PccCls:
	"""Pcc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pcc", core, parent)

	# noinspection PyTypeChecker
	def get_downlink(self) -> enums.Bandwidth:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:BANDwidth[:PCC]:DL \n
		Snippet: value: enums.Bandwidth = driver.configure.cell.bandwidth.pcc.get_downlink() \n
		Defines the DL cell bandwidth. The PCC DL bandwidth is also used for the UL. \n
			:return: bandwidth: B014 | B030 | B050 | B100 | B150 | B200 B014: 1.4 MHz B030: 3 MHz B050: 5 MHz B100: 10 MHz B150: 15 MHz B200: 20 MHz
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:BANDwidth:PCC:DL?')
		return Conversions.str_to_scalar_enum(response, enums.Bandwidth)

	def set_downlink(self, bandwidth: enums.Bandwidth) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:BANDwidth[:PCC]:DL \n
		Snippet: driver.configure.cell.bandwidth.pcc.set_downlink(bandwidth = enums.Bandwidth.B014) \n
		Defines the DL cell bandwidth. The PCC DL bandwidth is also used for the UL. \n
			:param bandwidth: B014 | B030 | B050 | B100 | B150 | B200 B014: 1.4 MHz B030: 3 MHz B050: 5 MHz B100: 10 MHz B150: 15 MHz B200: 20 MHz
		"""
		param = Conversions.enum_scalar_to_str(bandwidth, enums.Bandwidth)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:BANDwidth:PCC:DL {param}')
