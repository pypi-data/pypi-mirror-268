from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RmsCls:
	"""Rms commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rms", core, parent)

	def get_offset(self) -> float:
		"""SCPI: DIAGnostic:GPRF:GENerator<Instance>:RMS:OFFSet \n
		Snippet: value: float = driver.diagnostic.gprf.generator.rms.get_offset() \n
		No command help available \n
			:return: rms_offset: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:GPRF:GENerator<Instance>:RMS:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, rms_offset: float) -> None:
		"""SCPI: DIAGnostic:GPRF:GENerator<Instance>:RMS:OFFSet \n
		Snippet: driver.diagnostic.gprf.generator.rms.set_offset(rms_offset = 1.0) \n
		No command help available \n
			:param rms_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(rms_offset)
		self._core.io.write(f'DIAGnostic:GPRF:GENerator<Instance>:RMS:OFFSet {param}')
