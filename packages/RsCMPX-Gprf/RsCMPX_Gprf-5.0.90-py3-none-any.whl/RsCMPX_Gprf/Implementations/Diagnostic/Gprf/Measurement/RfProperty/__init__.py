from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfPropertyCls:
	"""RfProperty commands group definition. 13 total commands, 10 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfProperty", core, parent)

	@property
	def franges(self):
		"""franges commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_franges'):
			from .Franges import FrangesCls
			self._franges = FrangesCls(self._core, self._cmd_group)
		return self._franges

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRateCls
			self._symbolRate = SymbolRateCls(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def nbLevel(self):
		"""nbLevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nbLevel'):
			from .NbLevel import NbLevelCls
			self._nbLevel = NbLevelCls(self._core, self._cmd_group)
		return self._nbLevel

	@property
	def bandpass(self):
		"""bandpass commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bandpass'):
			from .Bandpass import BandpassCls
			self._bandpass = BandpassCls(self._core, self._cmd_group)
		return self._bandpass

	@property
	def gauss(self):
		"""gauss commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_gauss'):
			from .Gauss import GaussCls
			self._gauss = GaussCls(self._core, self._cmd_group)
		return self._gauss

	@property
	def fspan(self):
		"""fspan commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fspan'):
			from .Fspan import FspanCls
			self._fspan = FspanCls(self._core, self._cmd_group)
		return self._fspan

	@property
	def listPy(self):
		"""listPy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPyCls
			self._listPy = ListPyCls(self._core, self._cmd_group)
		return self._listPy

	@property
	def iqRecorder(self):
		"""iqRecorder commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqRecorder'):
			from .IqRecorder import IqRecorderCls
			self._iqRecorder = IqRecorderCls(self._core, self._cmd_group)
		return self._iqRecorder

	@property
	def loFrequency(self):
		"""loFrequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_loFrequency'):
			from .LoFrequency import LoFrequencyCls
			self._loFrequency = LoFrequencyCls(self._core, self._cmd_group)
		return self._loFrequency

	def get_tfilter(self) -> bool:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:RFPRoperty:TFILter \n
		Snippet: value: bool = driver.diagnostic.gprf.measurement.rfProperty.get_tfilter() \n
		No command help available \n
			:return: def: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:GPRF:MEASurement<Instance>:RFPRoperty:TFILter?')
		return Conversions.str_to_bool(response)

	def set_tfilter(self, def: bool) -> None:
		"""SCPI: DIAGnostic:GPRF:MEASurement<Instance>:RFPRoperty:TFILter \n
		Snippet: driver.diagnostic.gprf.measurement.rfProperty.set_tfilter(def = False) \n
		No command help available \n
			:param def: No help available
		"""
		param = Conversions.bool_to_str(def)
		self._core.io.write(f'DIAGnostic:GPRF:MEASurement<Instance>:RFPRoperty:TFILter {param}')

	def clone(self) -> 'RfPropertyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfPropertyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
