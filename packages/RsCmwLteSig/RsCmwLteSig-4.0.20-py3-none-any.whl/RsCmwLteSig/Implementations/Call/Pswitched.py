from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PswitchedCls:
	"""Pswitched commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pswitched", core, parent)

	def set_action(self, ps_action: enums.PswAction) -> None:
		"""SCPI: CALL:LTE:SIGNaling<instance>:PSWitched:ACTion \n
		Snippet: driver.call.pswitched.set_action(ps_action = enums.PswAction.CONNect) \n
		Controls the PS connection state. As a prerequisite, the DL signal must be switched on, see method RsCmwLteSig.Source.
		Cell.State.value. \n
			:param ps_action: CONNect | DISConnect | SMS | DETach | HANDover CONNect: Initiate a mobile-terminated connection setup DISConnect: Release the connection SMS: Send an SMS DETach: Detach the UE HANDover: Initiate a handover (within the LTE signaling application or to another signaling application)
		"""
		param = Conversions.enum_scalar_to_str(ps_action, enums.PswAction)
		self._core.io.write_with_opc(f'CALL:LTE:SIGNaling<Instance>:PSWitched:ACTion {param}')
