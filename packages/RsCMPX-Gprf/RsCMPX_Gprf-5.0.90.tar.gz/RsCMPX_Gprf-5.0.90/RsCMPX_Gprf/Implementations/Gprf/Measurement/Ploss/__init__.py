from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PlossCls:
	"""Ploss commands group definition. 9 total commands, 3 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ploss", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	@property
	def clear(self):
		"""clear commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_clear'):
			from .Clear import ClearCls
			self._clear = ClearCls(self._core, self._cmd_group)
		return self._clear

	@property
	def eeprom(self):
		"""eeprom commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_eeprom'):
			from .Eeprom import EepromCls
			self._eeprom = EepromCls(self._core, self._cmd_group)
		return self._eeprom

	def stop(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: STOP:GPRF:MEASurement<Instance>:PLOSs \n
		Snippet: driver.gprf.measurement.ploss.stop() \n
			INTRO_CMD_HELP: Stops or aborts the measurement: \n
			- STOP...: The measurement enters the 'RDY' state. The resources remain allocated to the measurement.
			- ABORt...: The measurement enters the 'OFF' state. Allocated resources are released.  \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'STOP:GPRF:MEASurement<Instance>:PLOSs', opc_timeout_ms)

	def abort(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: ABORt:GPRF:MEASurement<Instance>:PLOSs \n
		Snippet: driver.gprf.measurement.ploss.abort() \n
			INTRO_CMD_HELP: Stops or aborts the measurement: \n
			- STOP...: The measurement enters the 'RDY' state. The resources remain allocated to the measurement.
			- ABORt...: The measurement enters the 'OFF' state. Allocated resources are released.  \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'ABORt:GPRF:MEASurement<Instance>:PLOSs', opc_timeout_ms)

	def clone(self) -> 'PlossCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PlossCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
