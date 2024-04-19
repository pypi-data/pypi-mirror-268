from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GeneratorCls:
	"""Generator commands group definition. 10 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("generator", core, parent)

	@property
	def arb(self):
		"""arb commands group. 2 Sub-classes, 4 commands."""
		if not hasattr(self, '_arb'):
			from .Arb import ArbCls
			self._arb = ArbCls(self._core, self._cmd_group)
		return self._arb

	@property
	def sequencer(self):
		"""sequencer commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_sequencer'):
			from .Sequencer import SequencerCls
			self._sequencer = SequencerCls(self._core, self._cmd_group)
		return self._sequencer

	def get_timeout(self) -> float or bool:
		"""SCPI: TRIGger:GPRF:GENerator<Instance>:TOUT \n
		Snippet: value: float or bool = driver.trigger.gprf.generator.get_timeout() \n
		Sets a time after which the generator must have received a trigger event, after it has been started. \n
			:return: timeout: (float or boolean) No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:GENerator<Instance>:TOUT?')
		return Conversions.str_to_float_or_bool(response)

	def set_timeout(self, timeout: float or bool) -> None:
		"""SCPI: TRIGger:GPRF:GENerator<Instance>:TOUT \n
		Snippet: driver.trigger.gprf.generator.set_timeout(timeout = 1.0) \n
		Sets a time after which the generator must have received a trigger event, after it has been started. \n
			:param timeout: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(timeout)
		self._core.io.write(f'TRIGger:GPRF:GENerator<Instance>:TOUT {param}')

	def clone(self) -> 'GeneratorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = GeneratorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
