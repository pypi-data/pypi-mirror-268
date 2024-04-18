from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PuschCls:
	"""Pusch commands group definition. 8 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pusch", core, parent)

	@property
	def tpc(self):
		"""tpc commands group. 2 Sub-classes, 5 commands."""
		if not hasattr(self, '_tpc'):
			from .Tpc import TpcCls
			self._tpc = TpcCls(self._core, self._cmd_group)
		return self._tpc

	def get_oln_power(self) -> float:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL[:PCC]:PUSCh:OLNPower \n
		Snippet: value: float = driver.configure.uplink.pcc.pusch.get_oln_power() \n
		Defines a cell-specific nominal power value for full resource block allocation in the UL (entire cell bandwidth used) .
		From this value, the cell-specific nominal power value PO_NOMINAL_PUSCH related to one resource block is determined and
		sent to all UEs via broadcast. This command is only relevant for basic configuration and rejected if advanced
		configuration is active. \n
			:return: power: numeric Range: -50 dBm to 23 dBm, Unit: dBm
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:UL:PCC:PUSCh:OLNPower?')
		return Conversions.str_to_float(response)

	def set_oln_power(self, power: float) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:UL[:PCC]:PUSCh:OLNPower \n
		Snippet: driver.configure.uplink.pcc.pusch.set_oln_power(power = 1.0) \n
		Defines a cell-specific nominal power value for full resource block allocation in the UL (entire cell bandwidth used) .
		From this value, the cell-specific nominal power value PO_NOMINAL_PUSCH related to one resource block is determined and
		sent to all UEs via broadcast. This command is only relevant for basic configuration and rejected if advanced
		configuration is active. \n
			:param power: numeric Range: -50 dBm to 23 dBm, Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:UL:PCC:PUSCh:OLNPower {param}')

	def clone(self) -> 'PuschCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PuschCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
