from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DtoneCls:
	"""Dtone commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dtone", core, parent)

	@property
	def ofrequency(self):
		"""ofrequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ofrequency'):
			from .Ofrequency import OfrequencyCls
			self._ofrequency = OfrequencyCls(self._core, self._cmd_group)
		return self._ofrequency

	@property
	def level(self):
		"""level commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_level'):
			from .Level import LevelCls
			self._level = LevelCls(self._core, self._cmd_group)
		return self._level

	def get_ratio(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:DTONe:RATio \n
		Snippet: value: float = driver.source.gprf.generator.dtone.get_ratio() \n
		Specifies the ratio in dB between the RMS levels of the two signals. \n
			:return: ratio: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:DTONe:RATio?')
		return Conversions.str_to_float(response)

	def set_ratio(self, ratio: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:DTONe:RATio \n
		Snippet: driver.source.gprf.generator.dtone.set_ratio(ratio = 1.0) \n
		Specifies the ratio in dB between the RMS levels of the two signals. \n
			:param ratio: No help available
		"""
		param = Conversions.decimal_value_to_str(ratio)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:DTONe:RATio {param}')

	def clone(self) -> 'DtoneCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DtoneCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
