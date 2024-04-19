from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ItransitionCls:
	"""Itransition commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("itransition", core, parent)

	def set(self, index: int, inc_transition: enums.IncTransition) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:ITRansition \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.itransition.set(index = 1, inc_transition = enums.IncTransition.IMMediate) \n
		Defines or queries a condition for the transition to the next list entry, for the sequencer list entry with the selected
		<Index>. \n
			:param index: No help available
			:param inc_transition: IMMediate: immediately RMARker: restart marker WMA1 to WMA4: waveform markers 1 to 4
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('index', index, DataType.Integer), ArgSingle('inc_transition', inc_transition, DataType.Enum, enums.IncTransition))
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:ITRansition {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, index: int) -> enums.IncTransition:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:ITRansition \n
		Snippet: value: enums.IncTransition = driver.source.gprf.generator.sequencer.listPy.itransition.get(index = 1) \n
		Defines or queries a condition for the transition to the next list entry, for the sequencer list entry with the selected
		<Index>. \n
			:param index: No help available
			:return: inc_transition: IMMediate: immediately RMARker: restart marker WMA1 to WMA4: waveform markers 1 to 4"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:ITRansition? {param}')
		return Conversions.str_to_scalar_enum(response, enums.IncTransition)

	# noinspection PyTypeChecker
	def get_all(self) -> List[enums.IncTransition]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:ITRansition:ALL \n
		Snippet: value: List[enums.IncTransition] = driver.source.gprf.generator.sequencer.listPy.itransition.get_all() \n
		Defines or queries a condition for the transition to the next list entry, for all sequencer list entries. \n
			:return: inc_transition: Comma-separated list of values, one value per list entry. Immediate, restart marker, waveform marker 1 to 4.
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:ITRansition:ALL?')
		return Conversions.str_to_list_enum(response, enums.IncTransition)

	def set_all(self, inc_transition: List[enums.IncTransition]) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:ITRansition:ALL \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.itransition.set_all(inc_transition = [IncTransition.IMMediate, IncTransition.WMA4]) \n
		Defines or queries a condition for the transition to the next list entry, for all sequencer list entries. \n
			:param inc_transition: Comma-separated list of values, one value per list entry. Immediate, restart marker, waveform marker 1 to 4.
		"""
		param = Conversions.enum_list_to_str(inc_transition, enums.IncTransition)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:ITRansition:ALL {param}')
