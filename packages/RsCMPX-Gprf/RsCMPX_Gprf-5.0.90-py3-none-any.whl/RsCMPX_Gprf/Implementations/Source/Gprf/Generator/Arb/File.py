from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.Utilities import trim_str_response
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FileCls:
	"""File commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("file", core, parent)

	def set(self, arb_file: enums.ArbFile = None) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:FILE \n
		Snippet: driver.source.gprf.generator.arb.file.set(arb_file = enums.ArbFile.ABSPath) \n
		Selects a waveform file for the ARB baseband mode. This command supports path aliases (e.g. @WAVEFORM) .
		Use MMEMory:ALIases? to query the available path aliases. If the selected file does not exist or no file has been
		selected, a query returns 'No File Selected'.
			INTRO_CMD_HELP: If the selected file does exist, a query returns: \n
			- Without <PathType>: The string used to select the file. If an alias has been used, the alias is not substituted.
			- With <PathType>: The absolute path of the file. If an alias has been used, the alias is substituted.  \n
			:param arb_file: (enum or string) Name of the waveform file to be used (.wv) .
		"""
		param = ''
		if arb_file:
			param = Conversions.enum_ext_scalar_to_str(arb_file, enums.ArbFile)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:ARB:FILE {param}'.strip())

	def get(self, arb_file: enums.ArbFile = None) -> str:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:FILE \n
		Snippet: value: str = driver.source.gprf.generator.arb.file.get(arb_file = enums.ArbFile.ABSPath) \n
		Selects a waveform file for the ARB baseband mode. This command supports path aliases (e.g. @WAVEFORM) .
		Use MMEMory:ALIases? to query the available path aliases. If the selected file does not exist or no file has been
		selected, a query returns 'No File Selected'.
			INTRO_CMD_HELP: If the selected file does exist, a query returns: \n
			- Without <PathType>: The string used to select the file. If an alias has been used, the alias is not substituted.
			- With <PathType>: The absolute path of the file. If an alias has been used, the alias is substituted.  \n
			:param arb_file: (enum or string) Name of the waveform file to be used (.wv) .
			:return: arb_file_retrun: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('arb_file', arb_file, DataType.EnumExt, enums.ArbFile, is_optional=True))
		response = self._core.io.query_str(f'SOURce:GPRF:GENerator<Instance>:ARB:FILE? {param}'.rstrip())
		return trim_str_response(response)

	def get_date(self) -> str:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:FILE:DATE \n
		Snippet: value: str = driver.source.gprf.generator.arb.file.get_date() \n
		Queries the date of the loaded waveform file. \n
			:return: date: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:ARB:FILE:DATE?')
		return trim_str_response(response)

	def get_version(self) -> str:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:FILE:VERSion \n
		Snippet: value: str = driver.source.gprf.generator.arb.file.get_version() \n
		Queries the version of the loaded waveform file. \n
			:return: version: The version or an empty string, if no file version is defined.
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:ARB:FILE:VERSion?')
		return trim_str_response(response)

	def get_option(self) -> str:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:ARB:FILE:OPTion \n
		Snippet: value: str = driver.source.gprf.generator.arb.file.get_option() \n
		Returns the options that are required to play the loaded ARB file. \n
			:return: options: A comma-separated list of options.
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:ARB:FILE:OPTion?')
		return trim_str_response(response)
