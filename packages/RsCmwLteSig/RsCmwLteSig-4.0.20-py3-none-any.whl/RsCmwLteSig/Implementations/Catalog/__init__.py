from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CatalogCls:
	"""Catalog commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	@property
	def connection(self):
		"""connection commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_connection'):
			from .Connection import ConnectionCls
			self._connection = ConnectionCls(self._core, self._cmd_group)
		return self._connection

	# noinspection PyTypeChecker
	def get_scenario(self) -> List[enums.Scenario]:
		"""SCPI: CATalog:LTE:SIGNaling<instance>:SCENario \n
		Snippet: value: List[enums.Scenario] = driver.catalog.get_scenario() \n
		Queries a list of all supported scenarios, depending on the available hardware and licenses. \n
			:return: scenarios: NAV | SCEL | TRO | AD | SCF | TROF | ADF | CATR | CAFR | BF | BFSM4 | BH | CATF | CAFF | BFF | BHF | CC | CCMP | CCMS1 | CF | CH | CHSM4 | CJ | CJSM4 | CL | CFF | CHF | CJF | CJFS4 | DD | DH | DJ | DJSM4 | DL | DLSM4 | DN | DNSM4 | DP | DHF | DPF | EE | EJ | EL | ELSM4 | EN | ENSM4 | EP | EPSM4 | ER | ERSM4 | ET | EJF | EPF | EPFS4 | FF | FL | FN | FNSM4 | FP | FPSM4 | FR | FRSM4 | FT | FTSM4 | FV | FVSM4 | FX | FLF | FPF | FPFS4 | GG | GN | GP | GPSM4 | GR | GRSM4 | GT | GTSM4 | GV | GVSM4 | GX | GXSM4 | GYA | GYAS4 | GYC | GNF | GPF | GPFS4 | HH | HP | HR | HRSM4 | HT | HTSM4 | HV | HVSM4 | HX | HXSM4 | HYA | HYAS4 | HYC | HYCS4 | HYE | HYES4 | HYG | HPF Comma-separated list of all supported scenarios For mapping of the values to scenario names, see method RsCmwLteSig.Route.Scenario.value.
		"""
		response = self._core.io.query_str('CATalog:LTE:SIGNaling<Instance>:SCENario?')
		return Conversions.str_to_list_enum(response, enums.Scenario)

	def clone(self) -> 'CatalogCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CatalogCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
