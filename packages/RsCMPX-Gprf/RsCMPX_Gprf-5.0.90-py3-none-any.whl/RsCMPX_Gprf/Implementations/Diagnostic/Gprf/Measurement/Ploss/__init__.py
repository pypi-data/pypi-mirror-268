from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PlossCls:
	"""Ploss commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ploss", core, parent)

	@property
	def rnames(self):
		"""rnames commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rnames'):
			from .Rnames import RnamesCls
			self._rnames = RnamesCls(self._core, self._cmd_group)
		return self._rnames

	def get_ccalibration(self) -> bool:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:PLOSs:CCALibration \n
		Snippet: value: bool = driver.diagnostic.gprf.measurement.ploss.get_ccalibration() \n
		No command help available \n
			:return: calibration: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:GPRF:MEASurement<Instance>:PLOSs:CCALibration?')
		return Conversions.str_to_bool(response)

	def set_ccalibration(self, calibration: bool) -> None:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:PLOSs:CCALibration \n
		Snippet: driver.diagnostic.gprf.measurement.ploss.set_ccalibration(calibration = False) \n
		No command help available \n
			:param calibration: No help available
		"""
		param = Conversions.bool_to_str(calibration)
		self._core.io.write(f'DIAGnostic:GPRF:MEASurement<Instance>:PLOSs:CCALibration {param}')

	# noinspection PyTypeChecker
	def get_smode(self) -> enums.SelectMode:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:PLOSs:SMODe \n
		Snippet: value: enums.SelectMode = driver.diagnostic.gprf.measurement.ploss.get_smode() \n
		No command help available \n
			:return: select_mode: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:GPRF:MEASurement<Instance>:PLOSs:SMODe?')
		return Conversions.str_to_scalar_enum(response, enums.SelectMode)

	def clone(self) -> 'PlossCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PlossCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
