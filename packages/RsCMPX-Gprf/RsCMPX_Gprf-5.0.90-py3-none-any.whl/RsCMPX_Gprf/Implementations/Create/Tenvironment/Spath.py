from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpathCls:
	"""Spath commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spath", core, parent)

	def set(self, name_signal_path: str, name_antenna: str, name_connector: str, overwrite: bool = None) -> None:
		"""SCPI: CREate:TENVironment:SPATh \n
		Snippet: driver.create.tenvironment.spath.set(name_signal_path = 'abc', name_antenna = 'abc', name_connector = 'abc', overwrite = False) \n
		No command help available \n
			:param name_signal_path: No help available
			:param name_antenna: No help available
			:param name_connector: No help available
			:param overwrite: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name_signal_path', name_signal_path, DataType.String), ArgSingle('name_antenna', name_antenna, DataType.String), ArgSingle('name_connector', name_connector, DataType.String), ArgSingle('overwrite', overwrite, DataType.Boolean, None, is_optional=True))
		self._core.io.write(f'CREate:TENVironment:SPATh {param}'.rstrip())
