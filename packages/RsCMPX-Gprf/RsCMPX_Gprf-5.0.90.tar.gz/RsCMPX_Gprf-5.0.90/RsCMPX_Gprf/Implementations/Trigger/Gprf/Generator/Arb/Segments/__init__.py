from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SegmentsCls:
	"""Segments commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("segments", core, parent)

	@property
	def manual(self):
		"""manual commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_manual'):
			from .Manual import ManualCls
			self._manual = ManualCls(self._core, self._cmd_group)
		return self._manual

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ArbSegmentsMode:
		"""SCPI: TRIGger:GPRF:GENerator<Instance>:ARB:SEGMents:MODE \n
		Snippet: value: enums.ArbSegmentsMode = driver.trigger.gprf.generator.arb.segments.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:GENerator<Instance>:ARB:SEGMents:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ArbSegmentsMode)

	def set_mode(self, mode: enums.ArbSegmentsMode) -> None:
		"""SCPI: TRIGger:GPRF:GENerator<Instance>:ARB:SEGMents:MODE \n
		Snippet: driver.trigger.gprf.generator.arb.segments.set_mode(mode = enums.ArbSegmentsMode.AUTO) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ArbSegmentsMode)
		self._core.io.write(f'TRIGger:GPRF:GENerator<Instance>:ARB:SEGMents:MODE {param}')

	def clone(self) -> 'SegmentsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SegmentsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
