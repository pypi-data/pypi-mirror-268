from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CanalyzerCls:
	"""Canalyzer commands group definition. 6 total commands, 2 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("canalyzer", core, parent)

	@property
	def iqFile(self):
		"""iqFile commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqFile'):
			from .IqFile import IqFileCls
			self._iqFile = IqFileCls(self._core, self._cmd_group)
		return self._iqFile

	@property
	def sall(self):
		"""sall commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sall'):
			from .Sall import SallCls
			self._sall = SallCls(self._core, self._cmd_group)
		return self._sall

	def get_mname(self) -> str:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:CANalyzer:MNAMe \n
		Snippet: value: str = driver.configure.gprf.measurement.canalyzer.get_mname() \n
		Queries which firmware application has captured the data. \n
			:return: meas_name: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:CANalyzer:MNAMe?')
		return trim_str_response(response)

	def get_segment(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:CANalyzer:SEGMent \n
		Snippet: value: int = driver.configure.gprf.measurement.canalyzer.get_segment() \n
		Selects a segment of a list mode measurement for result analysis. The selection affects the GUI contents and the contents
		stored by the command method RsCMPX_Gprf.Configure.Gprf.Measurement.Canalyzer.IqFile.set. \n
			:return: segment: Segment number
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:CANalyzer:SEGMent?')
		return Conversions.str_to_int(response)

	def set_segment(self, segment: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:CANalyzer:SEGMent \n
		Snippet: driver.configure.gprf.measurement.canalyzer.set_segment(segment = 1) \n
		Selects a segment of a list mode measurement for result analysis. The selection affects the GUI contents and the contents
		stored by the command method RsCMPX_Gprf.Configure.Gprf.Measurement.Canalyzer.IqFile.set. \n
			:param segment: Segment number
		"""
		param = Conversions.decimal_value_to_str(segment)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:CANalyzer:SEGMent {param}')

	def get_step(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:CANalyzer:STEP \n
		Snippet: value: int = driver.configure.gprf.measurement.canalyzer.get_step() \n
		Selects a step of a list mode measurement for result analysis. The selection affects the GUI contents and the contents
		stored by the command method RsCMPX_Gprf.Configure.Gprf.Measurement.Canalyzer.IqFile.set. \n
			:return: step: Step number
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:CANalyzer:STEP?')
		return Conversions.str_to_int(response)

	def set_step(self, step: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:CANalyzer:STEP \n
		Snippet: driver.configure.gprf.measurement.canalyzer.set_step(step = 1) \n
		Selects a step of a list mode measurement for result analysis. The selection affects the GUI contents and the contents
		stored by the command method RsCMPX_Gprf.Configure.Gprf.Measurement.Canalyzer.IqFile.set. \n
			:param step: Step number
		"""
		param = Conversions.decimal_value_to_str(step)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:CANalyzer:STEP {param}')

	def clone(self) -> 'CanalyzerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CanalyzerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
