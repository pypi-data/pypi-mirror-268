from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PzeroCls:
	"""Pzero commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pzero", core, parent)

	# noinspection PyTypeChecker
	def get_mapping(self) -> enums.PortsMapping:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:PZERo:MAPPing \n
		Snippet: value: enums.PortsMapping = driver.configure.connection.pcc.pzero.get_mapping() \n
		Selects the mapping of antenna port 0 to the RF output paths. Only for TM 7 in scenarios with two RF output paths,
		without fading. \n
			:return: port: R1 | R1R2 R1: Map port 0 to the first RF output path. R1R2: Map port 0 to both RF output paths.
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:PZERo:MAPPing?')
		return Conversions.str_to_scalar_enum(response, enums.PortsMapping)

	def set_mapping(self, port: enums.PortsMapping) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CONNection[:PCC]:PZERo:MAPPing \n
		Snippet: driver.configure.connection.pcc.pzero.set_mapping(port = enums.PortsMapping.R1) \n
		Selects the mapping of antenna port 0 to the RF output paths. Only for TM 7 in scenarios with two RF output paths,
		without fading. \n
			:param port: R1 | R1R2 R1: Map port 0 to the first RF output path. R1R2: Map port 0 to both RF output paths.
		"""
		param = Conversions.enum_scalar_to_str(port, enums.PortsMapping)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CONNection:PCC:PZERo:MAPPing {param}')
