from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPyCls:
	"""FilterPy commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("filterPy", core, parent)

	@property
	def bandpass(self):
		"""bandpass commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandpass'):
			from .Bandpass import BandpassCls
			self._bandpass = BandpassCls(self._core, self._cmd_group)
		return self._bandpass

	@property
	def gauss(self):
		"""gauss commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gauss'):
			from .Gauss import GaussCls
			self._gauss = GaussCls(self._core, self._cmd_group)
		return self._gauss

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.DigitalFilterType:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:FILTer:TYPE \n
		Snippet: value: enums.DigitalFilterType = driver.configure.gprf.measurement.power.filterPy.get_type_py() \n
		Selects the IF filter type. \n
			:return: filter_type: RF unit: BANDpass | GAUSs IF unit: BANDpass | GAUSs R&S CMW: BANDpass | GAUSs | WCDMa | CDMA | TDSCdma BANDpass: bandpass filter GAUSs: Gaussian filter WCDMA: 3.84-MHz RRC filter for WCDMA TX tests CDMA: 1.2288-MHz channel filter for CDMA 2000 TX tests TDSCdma: 1.28-MHz RRC filter for TD-SCDMA TX tests
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:FILTer:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.DigitalFilterType)

	def set_type_py(self, filter_type: enums.DigitalFilterType) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:FILTer:TYPE \n
		Snippet: driver.configure.gprf.measurement.power.filterPy.set_type_py(filter_type = enums.DigitalFilterType.BANDpass) \n
		Selects the IF filter type. \n
			:param filter_type: RF unit: BANDpass | GAUSs IF unit: BANDpass | GAUSs R&S CMW: BANDpass | GAUSs | WCDMa | CDMA | TDSCdma BANDpass: bandpass filter GAUSs: Gaussian filter WCDMA: 3.84-MHz RRC filter for WCDMA TX tests CDMA: 1.2288-MHz channel filter for CDMA 2000 TX tests TDSCdma: 1.28-MHz RRC filter for TD-SCDMA TX tests
		"""
		param = Conversions.enum_scalar_to_str(filter_type, enums.DigitalFilterType)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:FILTer:TYPE {param}')

	def clone(self) -> 'FilterPyCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FilterPyCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
