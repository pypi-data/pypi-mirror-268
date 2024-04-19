from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NpeakCls:
	"""Npeak commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("npeak", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Xvalue: float: No parameter help available
			- Yvalue: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_float('Xvalue'),
			ArgStruct.scalar_float('Yvalue')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Xvalue: float = None
			self.Yvalue: float = None

	def fetch(self, detector: enums.Detector, statistic: enums.Statistic, marker=repcap.Marker.Default) -> FetchStruct:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:SPECtrum:MARKer<MarkerNo>:NPEak \n
		Snippet: value: FetchStruct = driver.gprf.measurement.spectrum.marker.npeak.fetch(detector = enums.Detector.AUTopeak, statistic = enums.Statistic.AVERage, marker = repcap.Marker.Default) \n
		No command help available \n
			:param detector: No help available
			:param statistic: No help available
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		param = ArgSingleList().compose_cmd_string(ArgSingle('detector', detector, DataType.Enum, enums.Detector), ArgSingle('statistic', statistic, DataType.Enum, enums.Statistic))
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		return self._core.io.query_struct(f'FETCh:GPRF:MEASurement<Instance>:SPECtrum:MARKer{marker_cmd_val}:NPEak? {param}'.rstrip(), self.__class__.FetchStruct())
