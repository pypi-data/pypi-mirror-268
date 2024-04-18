from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UfddCls:
	"""Ufdd commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ufdd", core, parent)

	@property
	def eredirection(self):
		"""eredirection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eredirection'):
			from .Eredirection import EredirectionCls
			self._eredirection = EredirectionCls(self._core, self._cmd_group)
		return self._eredirection

	def get_supported(self) -> List[bool]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UECapability:IRAT:UFDD:SUPPorted \n
		Snippet: value: List[bool] = driver.sense.ueCapability.interRat.ufdd.get_supported() \n
		Returns a list of values indicating the support of the individual UTRA FDD operating bands by the UE. \n
			:return: supported_band: OFF | ON 32 values: band 1, ..., band 32
		"""
		response = self._core.io.query_str('SENSe:LTE:SIGNaling<Instance>:UECapability:IRAT:UFDD:SUPPorted?')
		return Conversions.str_to_bool_list(response)

	def clone(self) -> 'UfddCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UfddCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
