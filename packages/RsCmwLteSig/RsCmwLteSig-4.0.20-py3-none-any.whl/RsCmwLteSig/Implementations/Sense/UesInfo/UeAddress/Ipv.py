from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpvCls:
	"""Ipv commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: IPversion, default value after init: IPversion.IPv4"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ipv", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_iPversion_get', 'repcap_iPversion_set', repcap.IPversion.IPv4)

	def repcap_iPversion_set(self, iPversion: repcap.IPversion) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to IPversion.Default
		Default value after init: IPversion.IPv4"""
		self._cmd_group.set_repcap_enum_value(iPversion)

	def repcap_iPversion_get(self) -> repcap.IPversion:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def get(self, iPversion=repcap.IPversion.Default) -> List[str]:
		"""SCPI: SENSe:LTE:SIGNaling<instance>:UESinfo:UEADdress:IPV<n> \n
		Snippet: value: List[str] = driver.sense.uesInfo.ueAddress.ipv.get(iPversion = repcap.IPversion.Default) \n
		Returns the IPv4 addresses (<n> = 4) or the IPv6 prefixes (<n> = 6) assigned to the UE by the R&S CMW. \n
			:param iPversion: optional repeated capability selector. Default value: IPv4 (settable in the interface 'Ipv')
			:return: ip_addresses: string Comma-separated list of IP address/prefix strings"""
		iPversion_cmd_val = self._cmd_group.get_repcap_cmd_value(iPversion, repcap.IPversion)
		response = self._core.io.query_str(f'SENSe:LTE:SIGNaling<Instance>:UESinfo:UEADdress:IPV{iPversion_cmd_val}?')
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'IpvCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpvCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
