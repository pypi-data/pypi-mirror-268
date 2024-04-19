from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AmbientCls:
	"""Ambient commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ambient", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Temperature: float: No parameter help available
			- Timestamp: str: No parameter help available
			- Box: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Temperature'),
			ArgStruct.scalar_str('Timestamp'),
			ArgStruct.scalar_str('Box')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Temperature: float = None
			self.Timestamp: str = None
			self.Box: str = None

	def get(self, all_py: enums.All = None) -> GetStruct:
		"""SCPI: SENSe:BASE:TEMPerature:OPERating:AMBient \n
		Snippet: value: GetStruct = driver.sense.base.temperature.operating.ambient.get(all_py = enums.All.ALL) \n
		No command help available \n
			:param all_py: No help available
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('all_py', all_py, DataType.Enum, enums.All, is_optional=True))
		return self._core.io.query_struct(f'SENSe:BASE:TEMPerature:OPERating:AMBient? {param}'.rstrip(), self.__class__.GetStruct())
