from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SrsCls:
	"""Srs commands group definition. 10 total commands, 2 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("srs", core, parent)

	@property
	def scIndex(self):
		"""scIndex commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_scIndex'):
			from .ScIndex import ScIndexCls
			self._scIndex = ScIndexCls(self._core, self._cmd_group)
		return self._scIndex

	@property
	def poffset(self):
		"""poffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_poffset'):
			from .Poffset import PoffsetCls
			self._poffset = PoffsetCls(self._core, self._cmd_group)
		return self._poffset

	def get_hbandwidth(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:CELL[:PCC]:SRS:HBANdwidth \n
		Snippet: value: int = driver.configure.cell.pcc.srs.get_hbandwidth() \n
		Specifies the 'srs-HoppingBandwidth' value. The setting is only used if manual configuration is enabled, see method
		RsCmwLteSig.Configure.Cell.Pcc.Srs.mcEnable. \n
			:return: hopping_bw: numeric Range: 0 to 3
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SRS:HBANdwidth?')
		return Conversions.str_to_int(response)

	def set_hbandwidth(self, hopping_bw: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:CELL[:PCC]:SRS:HBANdwidth \n
		Snippet: driver.configure.cell.pcc.srs.set_hbandwidth(hopping_bw = 1) \n
		Specifies the 'srs-HoppingBandwidth' value. The setting is only used if manual configuration is enabled, see method
		RsCmwLteSig.Configure.Cell.Pcc.Srs.mcEnable. \n
			:param hopping_bw: numeric Range: 0 to 3
		"""
		param = Conversions.decimal_value_to_str(hopping_bw)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SRS:HBANdwidth {param}')

	def get_dbandwidth(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:CELL[:PCC]:SRS:DBANdwidth \n
		Snippet: value: int = driver.configure.cell.pcc.srs.get_dbandwidth() \n
		Specifies the 'srs-Bandwidth' value. The setting is only used if manual configuration is enabled, see method RsCmwLteSig.
		Configure.Cell.Pcc.Srs.mcEnable. \n
			:return: dedicated_bw: numeric Range: 0 to 3
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SRS:DBANdwidth?')
		return Conversions.str_to_int(response)

	def set_dbandwidth(self, dedicated_bw: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:CELL[:PCC]:SRS:DBANdwidth \n
		Snippet: driver.configure.cell.pcc.srs.set_dbandwidth(dedicated_bw = 1) \n
		Specifies the 'srs-Bandwidth' value. The setting is only used if manual configuration is enabled, see method RsCmwLteSig.
		Configure.Cell.Pcc.Srs.mcEnable. \n
			:param dedicated_bw: numeric Range: 0 to 3
		"""
		param = Conversions.decimal_value_to_str(dedicated_bw)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SRS:DBANdwidth {param}')

	def get_bw_config(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:CELL[:PCC]:SRS:BWConfig \n
		Snippet: value: int = driver.configure.cell.pcc.srs.get_bw_config() \n
		Specifies the 'srs-BandwidthConfig' value. The setting is only used if manual configuration is enabled, see method
		RsCmwLteSig.Configure.Cell.Pcc.Srs.mcEnable. \n
			:return: bw_configuration: numeric Range: 0 to 7
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SRS:BWConfig?')
		return Conversions.str_to_int(response)

	def set_bw_config(self, bw_configuration: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:CELL[:PCC]:SRS:BWConfig \n
		Snippet: driver.configure.cell.pcc.srs.set_bw_config(bw_configuration = 1) \n
		Specifies the 'srs-BandwidthConfig' value. The setting is only used if manual configuration is enabled, see method
		RsCmwLteSig.Configure.Cell.Pcc.Srs.mcEnable. \n
			:param bw_configuration: numeric Range: 0 to 7
		"""
		param = Conversions.decimal_value_to_str(bw_configuration)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SRS:BWConfig {param}')

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:SRS:ENABle \n
		Snippet: value: bool = driver.configure.cell.pcc.srs.get_enable() \n
		Enables support of SRS. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SRS:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:SRS:ENABle \n
		Snippet: driver.configure.cell.pcc.srs.set_enable(enable = False) \n
		Enables support of SRS. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SRS:ENABle {param}')

	def get_mc_enable(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:CELL[:PCC]:SRS:MCENable \n
		Snippet: value: bool = driver.configure.cell.pcc.srs.get_mc_enable() \n
		Enables or disables the manual configuration of signaled values for SRS configuration. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SRS:MCENable?')
		return Conversions.str_to_bool(response)

	def set_mc_enable(self, enable: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:CELL[:PCC]:SRS:MCENable \n
		Snippet: driver.configure.cell.pcc.srs.set_mc_enable(enable = False) \n
		Enables or disables the manual configuration of signaled values for SRS configuration. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SRS:MCENable {param}')

	def get_sf_config(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:CELL[:PCC]:SRS:SFConfig \n
		Snippet: value: int = driver.configure.cell.pcc.srs.get_sf_config() \n
		Specifies the 'srs-SubframeConfig' value. The setting is only used if manual configuration is enabled, see method
		RsCmwLteSig.Configure.Cell.Pcc.Srs.mcEnable. \n
			:return: subframe: decimal Range: 0 to 15
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SRS:SFConfig?')
		return Conversions.str_to_int(response)

	def set_sf_config(self, subframe: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<Instance>:CELL[:PCC]:SRS:SFConfig \n
		Snippet: driver.configure.cell.pcc.srs.set_sf_config(subframe = 1) \n
		Specifies the 'srs-SubframeConfig' value. The setting is only used if manual configuration is enabled, see method
		RsCmwLteSig.Configure.Cell.Pcc.Srs.mcEnable. \n
			:param subframe: decimal Range: 0 to 15
		"""
		param = Conversions.decimal_value_to_str(subframe)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SRS:SFConfig {param}')

	def get_dconfig(self) -> bool:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:SRS:DCONfig \n
		Snippet: value: bool = driver.configure.cell.pcc.srs.get_dconfig() \n
		Selects whether the UE-specific SRS parameters are signaled to the UE or not. The setting is only used if manual
		configuration is enabled, see method RsCmwLteSig.Configure.Cell.Pcc.Srs.mcEnable. \n
			:return: dconfiguration: OFF | ON OFF: send only cell-specific SRS parameters ON: send also UE-specific SRS parameters
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SRS:DCONfig?')
		return Conversions.str_to_bool(response)

	def set_dconfig(self, dconfiguration: bool) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL[:PCC]:SRS:DCONfig \n
		Snippet: driver.configure.cell.pcc.srs.set_dconfig(dconfiguration = False) \n
		Selects whether the UE-specific SRS parameters are signaled to the UE or not. The setting is only used if manual
		configuration is enabled, see method RsCmwLteSig.Configure.Cell.Pcc.Srs.mcEnable. \n
			:param dconfiguration: OFF | ON OFF: send only cell-specific SRS parameters ON: send also UE-specific SRS parameters
		"""
		param = Conversions.bool_to_str(dconfiguration)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PCC:SRS:DCONfig {param}')

	def clone(self) -> 'SrsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SrsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
