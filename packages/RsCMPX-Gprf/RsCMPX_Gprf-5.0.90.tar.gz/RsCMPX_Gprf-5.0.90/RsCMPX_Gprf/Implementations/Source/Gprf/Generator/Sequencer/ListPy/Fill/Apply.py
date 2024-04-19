from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ApplyCls:
	"""Apply commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("apply", core, parent)

	def set(self) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FILL:APPLy \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.fill.apply.set() \n
		Fills the sequencer list with a sequence of entries, as configured by the other SOURce:GPRF:GEN<i>:SEQuencer:LIST:FILL:...
		commands. \n
		"""
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FILL:APPLy')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FILL:APPLy \n
		Snippet: driver.source.gprf.generator.sequencer.listPy.fill.apply.set_with_opc() \n
		Fills the sequencer list with a sequence of entries, as configured by the other SOURce:GPRF:GEN<i>:SEQuencer:LIST:FILL:...
		commands. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCMPX_Gprf.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:LIST:FILL:APPLy', opc_timeout_ms)
