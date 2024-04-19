from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PlossCls:
	"""Ploss commands group definition. 7 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ploss", core, parent)

	@property
	def tsTone(self):
		"""tsTone commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_tsTone'):
			from .TsTone import TsToneCls
			self._tsTone = TsToneCls(self._core, self._cmd_group)
		return self._tsTone

	@property
	def view(self):
		"""view commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_view'):
			from .View import ViewCls
			self._view = ViewCls(self._core, self._cmd_group)
		return self._view

	def get_trace(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:PLOSs:TRACe \n
		Snippet: value: bool = driver.configure.gprf.measurement.ploss.get_trace() \n
		Selects whether a result diagram is provided. \n
			:return: trace_mode: OFF: no result diagram, faster measurement ON: result diagram, slower measurement
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:PLOSs:TRACe?')
		return Conversions.str_to_bool(response)

	def set_trace(self, trace_mode: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:PLOSs:TRACe \n
		Snippet: driver.configure.gprf.measurement.ploss.set_trace(trace_mode = False) \n
		Selects whether a result diagram is provided. \n
			:param trace_mode: OFF: no result diagram, faster measurement ON: result diagram, slower measurement
		"""
		param = Conversions.bool_to_str(trace_mode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:PLOSs:TRACe {param}')

	# noinspection PyTypeChecker
	def get_mmode(self) -> enums.MeasMode:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:PLOSs:MMODe \n
		Snippet: value: enums.MeasMode = driver.configure.gprf.measurement.ploss.get_mmode() \n
		Selects the measurement mode. \n
			:return: meas_mode: OSHort: measurement with an 'open' and with a 'short' OOPen: measurement with an 'open'
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:PLOSs:MMODe?')
		return Conversions.str_to_scalar_enum(response, enums.MeasMode)

	def set_mmode(self, meas_mode: enums.MeasMode) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:PLOSs:MMODe \n
		Snippet: driver.configure.gprf.measurement.ploss.set_mmode(meas_mode = enums.MeasMode.CCALibration) \n
		Selects the measurement mode. \n
			:param meas_mode: OSHort: measurement with an 'open' and with a 'short' OOPen: measurement with an 'open'
		"""
		param = Conversions.enum_scalar_to_str(meas_mode, enums.MeasMode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:PLOSs:MMODe {param}')

	def clone(self) -> 'PlossCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PlossCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
