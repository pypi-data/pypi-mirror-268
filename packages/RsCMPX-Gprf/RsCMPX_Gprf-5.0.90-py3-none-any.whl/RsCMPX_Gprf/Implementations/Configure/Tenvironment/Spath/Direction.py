from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DirectionCls:
	"""Direction commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("direction", core, parent)

	def set(self, name_signal_path: str, signal_direction: enums.SignalDirection) -> None:
		"""SCPI: [CONFigure]:TENVironment:SPATh:DIRection \n
		Snippet: driver.configure.tenvironment.spath.direction.set(name_signal_path = 'abc', signal_direction = enums.SignalDirection.RX) \n
		No command help available \n
			:param name_signal_path: No help available
			:param signal_direction: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_signal_path', name_signal_path, DataType.String), ArgSingle('signal_direction', signal_direction, DataType.Enum, enums.SignalDirection))
		self._core.io.write(f'CONFigure:TENVironment:SPATh:DIRection {param}'.rstrip())

	# noinspection PyTypeChecker
	def get(self, name_signal_path: str) -> enums.SignalDirection:
		"""SCPI: [CONFigure]:TENVironment:SPATh:DIRection \n
		Snippet: value: enums.SignalDirection = driver.configure.tenvironment.spath.direction.get(name_signal_path = 'abc') \n
		No command help available \n
			:param name_signal_path: No help available
			:return: signal_direction: No help available"""
		param = Conversions.value_to_quoted_str(name_signal_path)
		response = self._core.io.query_str(f'CONFigure:TENVironment:SPATh:DIRection? {param}')
		return Conversions.str_to_scalar_enum(response, enums.SignalDirection)
