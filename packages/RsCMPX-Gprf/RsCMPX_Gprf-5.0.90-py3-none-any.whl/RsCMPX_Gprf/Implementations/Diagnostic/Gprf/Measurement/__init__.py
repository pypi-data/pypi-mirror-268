from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MeasurementCls:
	"""Measurement commands group definition. 20 total commands, 3 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	@property
	def rfProperty(self):
		"""rfProperty commands group. 10 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfProperty'):
			from .RfProperty import RfPropertyCls
			self._rfProperty = RfPropertyCls(self._core, self._cmd_group)
		return self._rfProperty

	@property
	def snumber(self):
		"""snumber commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_snumber'):
			from .Snumber import SnumberCls
			self._snumber = SnumberCls(self._core, self._cmd_group)
		return self._snumber

	@property
	def ploss(self):
		"""ploss commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_ploss'):
			from .Ploss import PlossCls
			self._ploss = PlossCls(self._core, self._cmd_group)
		return self._ploss

	def get_rlevel(self) -> float:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:RLEVel \n
		Snippet: value: float = driver.diagnostic.gprf.measurement.get_rlevel() \n
		No command help available \n
			:return: reference_level: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:GPRF:MEASurement<Instance>:RLEVel?')
		return Conversions.str_to_float(response)

	def set_rlevel(self, reference_level: float) -> None:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:RLEVel \n
		Snippet: driver.diagnostic.gprf.measurement.set_rlevel(reference_level = 1.0) \n
		No command help available \n
			:param reference_level: No help available
		"""
		param = Conversions.decimal_value_to_str(reference_level)
		self._core.io.write(f'DIAGnostic:GPRF:MEASurement<Instance>:RLEVel {param}')

	def get_debug(self) -> bool:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:DEBug \n
		Snippet: value: bool = driver.diagnostic.gprf.measurement.get_debug() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:GPRF:MEASurement<Instance>:DEBug?')
		return Conversions.str_to_bool(response)

	def set_debug(self, enable: bool) -> None:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:DEBug \n
		Snippet: driver.diagnostic.gprf.measurement.set_debug(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'DIAGnostic:GPRF:MEASurement<Instance>:DEBug {param}')

	def clone(self) -> 'MeasurementCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MeasurementCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
