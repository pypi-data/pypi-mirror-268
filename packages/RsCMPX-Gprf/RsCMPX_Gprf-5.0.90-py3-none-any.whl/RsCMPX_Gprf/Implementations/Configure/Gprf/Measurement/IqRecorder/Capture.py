from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CaptureCls:
	"""Capture commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("capture", core, parent)

	def set(self, capt_samp_bef_trig: int, capt_samp_aft_trig: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:CAPTure \n
		Snippet: driver.configure.gprf.measurement.iqRecorder.capture.set(capt_samp_bef_trig = 1, capt_samp_aft_trig = 1) \n
		Selects the number of samples to be recorded before and after the trigger event. Configure the two settings so that their
		sum does not exceed the maximum number of samples. \n
			:param capt_samp_bef_trig: Samples before trigger event
			:param capt_samp_aft_trig: Samples after trigger event
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('capt_samp_bef_trig', capt_samp_bef_trig, DataType.Integer), ArgSingle('capt_samp_aft_trig', capt_samp_aft_trig, DataType.Integer))
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:CAPTure {param}'.rstrip())

	# noinspection PyTypeChecker
	class CaptureStruct(StructBase):
		"""Response structure. Fields: \n
			- Capt_Samp_Bef_Trig: int: Samples before trigger event
			- Capt_Samp_Aft_Trig: int: Samples after trigger event"""
		__meta_args_list = [
			ArgStruct.scalar_int('Capt_Samp_Bef_Trig'),
			ArgStruct.scalar_int('Capt_Samp_Aft_Trig')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Capt_Samp_Bef_Trig: int = None
			self.Capt_Samp_Aft_Trig: int = None

	def get(self) -> CaptureStruct:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:CAPTure \n
		Snippet: value: CaptureStruct = driver.configure.gprf.measurement.iqRecorder.capture.get() \n
		Selects the number of samples to be recorded before and after the trigger event. Configure the two settings so that their
		sum does not exceed the maximum number of samples. \n
			:return: structure: for return value, see the help for CaptureStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:CAPTure?', self.__class__.CaptureStruct())
