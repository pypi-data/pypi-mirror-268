from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CheckCls:
	"""Check commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("check", core, parent)

	def set(self, index: int, check: bool) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:CHECk \n
		Snippet: driver.source.gprf.generator.sequencer.apool.check.set(index = 1, check = False) \n
		No command help available \n
			:param index: No help available
			:param check: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('check', check, DataType.Boolean))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:CHECk {param}'.rstrip())

	def get(self, index: int) -> bool:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:CHECk \n
		Snippet: value: bool = driver.source.gprf.generator.sequencer.apool.check.get(index = 1) \n
		No command help available \n
			:param index: No help available
			:return: check: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:CHECk? {param}')
		return Conversions.str_to_bool(response)
