from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BoxCls:
	"""Box commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("box", core, parent)

	def get(self, serial_number: str) -> str:
		"""SCPI: CATalog:SYSTem:RF42:BOX \n
		Snippet: value: str = driver.catalog.system.rf42.box.get(serial_number = 'abc') \n
		No command help available \n
			:param serial_number: No help available
			:return: result: No help available"""
		param = Conversions.value_to_quoted_str(serial_number)
		response = self._core.io.query_str(f'CATalog:SYSTem:RF42:BOX? {param}')
		return trim_str_response(response)
