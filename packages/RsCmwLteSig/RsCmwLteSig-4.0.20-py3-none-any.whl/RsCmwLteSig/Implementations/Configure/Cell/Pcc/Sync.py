from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SyncCls:
	"""Sync commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sync", core, parent)

	# noinspection PyTypeChecker
	def get_zone(self) -> enums.SyncZone:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:SYNC:ZONE \n
		Snippet: value: enums.SyncZone = driver.configure.cell.pcc.sync.get_zone() \n
		Selects the synchronization zone for the signaling application. \n
			:return: zone: NONE | Z1 NONE: no synchronization Z1: synchronization to zone 1
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SYNC:ZONE?')
		return Conversions.str_to_scalar_enum(response, enums.SyncZone)

	def set_zone(self, zone: enums.SyncZone) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:SYNC:ZONE \n
		Snippet: driver.configure.cell.pcc.sync.set_zone(zone = enums.SyncZone.NONE) \n
		Selects the synchronization zone for the signaling application. \n
			:param zone: NONE | Z1 NONE: no synchronization Z1: synchronization to zone 1
		"""
		param = Conversions.enum_scalar_to_str(zone, enums.SyncZone)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SYNC:ZONE {param}')

	def get_offset(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:SYNC:OFFSet \n
		Snippet: value: float = driver.configure.cell.pcc.sync.get_offset() \n
		Configures the timing offset relative to the time zone. \n
			:return: offset: numeric Range: 0 s to 1E-3 s, Unit: s
		"""
		response = self._core.io.query_str_with_opc('CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SYNC:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, offset: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:SYNC:OFFSet \n
		Snippet: driver.configure.cell.pcc.sync.set_offset(offset = 1.0) \n
		Configures the timing offset relative to the time zone. \n
			:param offset: numeric Range: 0 s to 1E-3 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write_with_opc(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SYNC:OFFSet {param}')
