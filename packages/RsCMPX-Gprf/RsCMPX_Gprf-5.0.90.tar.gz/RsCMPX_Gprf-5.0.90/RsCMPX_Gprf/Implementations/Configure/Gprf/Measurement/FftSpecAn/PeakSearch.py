from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PeakSearchCls:
	"""PeakSearch commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("peakSearch", core, parent)

	def get_noa_markers(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:PSEarch:NOAMarkers \n
		Snippet: value: int = driver.configure.gprf.measurement.fftSpecAn.peakSearch.get_noa_markers() \n
		Defines the number of active markers for the peak search. \n
			:return: no_active_markers: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:PSEarch:NOAMarkers?')
		return Conversions.str_to_int(response)

	def set_noa_markers(self, no_active_markers: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:PSEarch:NOAMarkers \n
		Snippet: driver.configure.gprf.measurement.fftSpecAn.peakSearch.set_noa_markers(no_active_markers = 1) \n
		Defines the number of active markers for the peak search. \n
			:param no_active_markers: No help available
		"""
		param = Conversions.decimal_value_to_str(no_active_markers)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:PSEarch:NOAMarkers {param}')

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):  # From WriteStructDefinition CmdPropertyTemplate.xml
		"""Structure for setting input parameters. Fields: \n
			- Full_Span_Enable_0: bool: Enable full-span search for marker 0. OFF: Search the configured range. ON: Search the full span and ignore the configured range.
			- Peak_Range_From_0: float: Lower end of the search range for marker 0.
			- Peak_Range_To_0: float: Upper end of the search range for marker 0.
			- Full_Span_Enable_1: bool: Enable full-span search for marker 1.
			- Peak_Range_From_1: float: Lower end of the search range for marker 1.
			- Peak_Range_To_1: float: Upper end of the search range for marker 1.
			- Full_Span_Enable_2: bool: Enable full-span search for marker 2.
			- Peak_Range_From_2: float: Lower end of the search range for marker 2.
			- Peak_Range_To_2: float: Upper end of the search range for marker 2.
			- Full_Span_Enable_3: bool: Enable full-span search for marker 3.
			- Peak_Range_From_3: float: Lower end of the search range for marker 3.
			- Peak_Range_To_3: float: Upper end of the search range for marker 3.
			- Full_Span_Enable_4: bool: Enable full-span search for marker 4.
			- Peak_Range_From_4: float: Lower end of the search range for marker 4.
			- Peak_Range_To_4: float: Upper end of the search range for marker 4."""
		__meta_args_list = [
			ArgStruct.scalar_bool('Full_Span_Enable_0'),
			ArgStruct.scalar_float('Peak_Range_From_0'),
			ArgStruct.scalar_float('Peak_Range_To_0'),
			ArgStruct.scalar_bool('Full_Span_Enable_1'),
			ArgStruct.scalar_float('Peak_Range_From_1'),
			ArgStruct.scalar_float('Peak_Range_To_1'),
			ArgStruct.scalar_bool('Full_Span_Enable_2'),
			ArgStruct.scalar_float('Peak_Range_From_2'),
			ArgStruct.scalar_float('Peak_Range_To_2'),
			ArgStruct.scalar_bool('Full_Span_Enable_3'),
			ArgStruct.scalar_float('Peak_Range_From_3'),
			ArgStruct.scalar_float('Peak_Range_To_3'),
			ArgStruct.scalar_bool('Full_Span_Enable_4'),
			ArgStruct.scalar_float('Peak_Range_From_4'),
			ArgStruct.scalar_float('Peak_Range_To_4')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Full_Span_Enable_0: bool = None
			self.Peak_Range_From_0: float = None
			self.Peak_Range_To_0: float = None
			self.Full_Span_Enable_1: bool = None
			self.Peak_Range_From_1: float = None
			self.Peak_Range_To_1: float = None
			self.Full_Span_Enable_2: bool = None
			self.Peak_Range_From_2: float = None
			self.Peak_Range_To_2: float = None
			self.Full_Span_Enable_3: bool = None
			self.Peak_Range_From_3: float = None
			self.Peak_Range_To_3: float = None
			self.Full_Span_Enable_4: bool = None
			self.Peak_Range_From_4: float = None
			self.Peak_Range_To_4: float = None

	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:PSEarch \n
		Snippet: value: ValueStruct = driver.configure.gprf.measurement.fftSpecAn.peakSearch.get_value() \n
		Defines the peak search ranges. The maximum allowed search ranges depend on the frequency span: –span/2 to span/2. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:PSEarch?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:PSEarch \n
		Snippet with structure: \n
		structure = driver.configure.gprf.measurement.fftSpecAn.peakSearch.ValueStruct() \n
		structure.Full_Span_Enable_0: bool = False \n
		structure.Peak_Range_From_0: float = 1.0 \n
		structure.Peak_Range_To_0: float = 1.0 \n
		structure.Full_Span_Enable_1: bool = False \n
		structure.Peak_Range_From_1: float = 1.0 \n
		structure.Peak_Range_To_1: float = 1.0 \n
		structure.Full_Span_Enable_2: bool = False \n
		structure.Peak_Range_From_2: float = 1.0 \n
		structure.Peak_Range_To_2: float = 1.0 \n
		structure.Full_Span_Enable_3: bool = False \n
		structure.Peak_Range_From_3: float = 1.0 \n
		structure.Peak_Range_To_3: float = 1.0 \n
		structure.Full_Span_Enable_4: bool = False \n
		structure.Peak_Range_From_4: float = 1.0 \n
		structure.Peak_Range_To_4: float = 1.0 \n
		driver.configure.gprf.measurement.fftSpecAn.peakSearch.set_value(value = structure) \n
		Defines the peak search ranges. The maximum allowed search ranges depend on the frequency span: –span/2 to span/2. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GPRF:MEASurement<Instance>:FFTSanalyzer:PSEarch', value)
