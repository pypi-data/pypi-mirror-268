from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrachCls:
	"""Prach commands group definition. 8 total commands, 1 Subgroups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prach", core, parent)

	@property
	def pcIndex(self):
		"""pcIndex commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_pcIndex'):
			from .PcIndex import PcIndexCls
			self._pcIndex = PcIndexCls(self._core, self._cmd_group)
		return self._pcIndex

	# noinspection PyTypeChecker
	def get_nr_preambles(self) -> enums.EnablePreambles:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:PRACh:NRPReambles \n
		Snippet: value: enums.EnablePreambles = driver.configure.cell.prach.get_nr_preambles() \n
		Selects whether the application ignores received preambles or not. \n
			:return: enable: OFF | ON | NIPReambles OFF: respond to received preambles ON: ignore received preambles NIPReambles: ignore a configured number of preambles, then respond to subsequent preambles - for configuration see method RsCmwLteSig.Configure.Cell.Prach.niprach, only allowed for power ramping step size 0 dB
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PRACh:NRPReambles?')
		return Conversions.str_to_scalar_enum(response, enums.EnablePreambles)

	def set_nr_preambles(self, enable: enums.EnablePreambles) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:PRACh:NRPReambles \n
		Snippet: driver.configure.cell.prach.set_nr_preambles(enable = enums.EnablePreambles.NIPReambles) \n
		Selects whether the application ignores received preambles or not. \n
			:param enable: OFF | ON | NIPReambles OFF: respond to received preambles ON: ignore received preambles NIPReambles: ignore a configured number of preambles, then respond to subsequent preambles - for configuration see method RsCmwLteSig.Configure.Cell.Prach.niprach, only allowed for power ramping step size 0 dB
		"""
		param = Conversions.enum_scalar_to_str(enable, enums.EnablePreambles)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PRACh:NRPReambles {param}')

	def get_niprach(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:PRACh:NIPRach \n
		Snippet: value: int = driver.configure.cell.prach.get_niprach() \n
		Configures the number of preambles to be ignored if the mode NIPReambles is active, see method RsCmwLteSig.Configure.Cell.
		Prach.nrPreambles. \n
			:return: count: numeric Range: 1 to 250
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PRACh:NIPRach?')
		return Conversions.str_to_int(response)

	def set_niprach(self, count: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:PRACh:NIPRach \n
		Snippet: driver.configure.cell.prach.set_niprach(count = 1) \n
		Configures the number of preambles to be ignored if the mode NIPReambles is active, see method RsCmwLteSig.Configure.Cell.
		Prach.nrPreambles. \n
			:param count: numeric Range: 1 to 250
		"""
		param = Conversions.decimal_value_to_str(count)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PRACh:NIPRach {param}')

	# noinspection PyTypeChecker
	def get_pr_step(self) -> enums.PrStep:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:PRACh:PRSTep \n
		Snippet: value: enums.PrStep = driver.configure.cell.prach.get_pr_step() \n
		Specifies the transmit power difference between two consecutive preambles. \n
			:return: step: ZERO | P2DB | P4DB | P6DB 0 dB, 2 dB, 4 dB, 6 dB
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PRACh:PRSTep?')
		return Conversions.str_to_scalar_enum(response, enums.PrStep)

	def set_pr_step(self, step: enums.PrStep) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:PRACh:PRSTep \n
		Snippet: driver.configure.cell.prach.set_pr_step(step = enums.PrStep.P2DB) \n
		Specifies the transmit power difference between two consecutive preambles. \n
			:param step: ZERO | P2DB | P4DB | P6DB 0 dB, 2 dB, 4 dB, 6 dB
		"""
		param = Conversions.enum_scalar_to_str(step, enums.PrStep)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PRACh:PRSTep {param}')

	def get_pf_offset(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:PRACh:PFOFfset \n
		Snippet: value: int = driver.configure.cell.prach.get_pf_offset() \n
		Specifies the PRACH frequency offset. \n
			:return: prach_freq_offset: numeric Range: 0 to total RB - 6 depending on cell bandwidth, see table below
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PRACh:PFOFfset?')
		return Conversions.str_to_int(response)

	def set_pf_offset(self, prach_freq_offset: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:PRACh:PFOFfset \n
		Snippet: driver.configure.cell.prach.set_pf_offset(prach_freq_offset = 1) \n
		Specifies the PRACH frequency offset. \n
			:param prach_freq_offset: numeric Range: 0 to total RB - 6 depending on cell bandwidth, see table below
		"""
		param = Conversions.decimal_value_to_str(prach_freq_offset)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PRACh:PFOFfset {param}')

	def get_lrs_index(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:PRACh:LRSindex \n
		Snippet: value: int = driver.configure.cell.prach.get_lrs_index() \n
		Specifies the logical root sequence index to be used by the UE for generation of the preamble sequence. \n
			:return: log_root_seq_index: numeric Range: 0 to 837
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PRACh:LRSindex?')
		return Conversions.str_to_int(response)

	def set_lrs_index(self, log_root_seq_index: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:PRACh:LRSindex \n
		Snippet: driver.configure.cell.prach.set_lrs_index(log_root_seq_index = 1) \n
		Specifies the logical root sequence index to be used by the UE for generation of the preamble sequence. \n
			:param log_root_seq_index: numeric Range: 0 to 837
		"""
		param = Conversions.decimal_value_to_str(log_root_seq_index)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PRACh:LRSindex {param}')

	def get_zcz_config(self) -> int:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:PRACh:ZCZConfig \n
		Snippet: value: int = driver.configure.cell.prach.get_zcz_config() \n
		Specifies the zero correlation zone config. \n
			:return: zero_corr_zone_con: numeric Range: 0 to 15
		"""
		response = self._core.io.query_str('CONFigure:LTE:SIGNaling<Instance>:CELL:PRACh:ZCZConfig?')
		return Conversions.str_to_int(response)

	def set_zcz_config(self, zero_corr_zone_con: int) -> None:
		"""SCPI: CONFigure:LTE:SIGNaling<instance>:CELL:PRACh:ZCZConfig \n
		Snippet: driver.configure.cell.prach.set_zcz_config(zero_corr_zone_con = 1) \n
		Specifies the zero correlation zone config. \n
			:param zero_corr_zone_con: numeric Range: 0 to 15
		"""
		param = Conversions.decimal_value_to_str(zero_corr_zone_con)
		self._core.io.write(f'CONFigure:LTE:SIGNaling<Instance>:CELL:PRACh:ZCZConfig {param}')

	def clone(self) -> 'PrachCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PrachCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
