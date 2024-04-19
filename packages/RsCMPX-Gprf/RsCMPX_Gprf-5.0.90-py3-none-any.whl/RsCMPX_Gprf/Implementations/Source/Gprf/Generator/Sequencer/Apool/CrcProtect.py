from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CrcProtectCls:
	"""CrcProtect commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("crcProtect", core, parent)

	# noinspection PyTypeChecker
	def get_all(self) -> List[enums.YesNoStatus]:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:CRCProtect:ALL \n
		Snippet: value: List[enums.YesNoStatus] = driver.source.gprf.generator.sequencer.apool.crcProtect.get_all() \n
		Queries whether the ARB files in the file pool contain CRC checksums. \n
			:return: crc_protection: Comma-separated list of values, one value per file
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:CRCProtect:ALL?')
		return Conversions.str_to_list_enum(response, enums.YesNoStatus)

	# noinspection PyTypeChecker
	def get(self, index: int) -> enums.YesNoStatus:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:CRCProtect \n
		Snippet: value: enums.YesNoStatus = driver.source.gprf.generator.sequencer.apool.crcProtect.get(index = 1) \n
		Queries whether the ARB file with the specified <Index> contains a CRC checksum. \n
			:param index: No help available
			:return: crc_protection: No help available"""
		param = Conversions.decimal_value_to_str(index)
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:APOol:CRCProtect? {param}')
		return Conversions.str_to_scalar_enum(response, enums.YesNoStatus)
