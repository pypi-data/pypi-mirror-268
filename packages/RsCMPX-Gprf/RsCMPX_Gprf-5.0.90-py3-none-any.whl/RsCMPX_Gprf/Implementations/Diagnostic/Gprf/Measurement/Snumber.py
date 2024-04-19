from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SnumberCls:
	"""Snumber commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("snumber", core, parent)

	def get_bb_meas(self) -> int:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:SNUMber:BBMeas \n
		Snippet: value: int = driver.diagnostic.gprf.measurement.snumber.get_bb_meas() \n
		No command help available \n
			:return: slot_number: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:GPRF:MEASurement<Instance>:SNUMber:BBMeas?')
		return Conversions.str_to_int(response)

	def set_bb_meas(self, slot_number: int) -> None:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:SNUMber:BBMeas \n
		Snippet: driver.diagnostic.gprf.measurement.snumber.set_bb_meas(slot_number = 1) \n
		No command help available \n
			:param slot_number: No help available
		"""
		param = Conversions.decimal_value_to_str(slot_number)
		self._core.io.write(f'DIAGnostic:GPRF:MEASurement<Instance>:SNUMber:BBMeas {param}')

	def get_value(self) -> int:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:SNUMber \n
		Snippet: value: int = driver.diagnostic.gprf.measurement.snumber.get_value() \n
		No command help available \n
			:return: slot_number: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:GPRF:MEASurement<Instance>:SNUMber?')
		return Conversions.str_to_int(response)

	def set_value(self, slot_number: int) -> None:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:SNUMber \n
		Snippet: driver.diagnostic.gprf.measurement.snumber.set_value(slot_number = 1) \n
		No command help available \n
			:param slot_number: No help available
		"""
		param = Conversions.decimal_value_to_str(slot_number)
		self._core.io.write(f'DIAGnostic:GPRF:MEASurement<Instance>:SNUMber {param}')
