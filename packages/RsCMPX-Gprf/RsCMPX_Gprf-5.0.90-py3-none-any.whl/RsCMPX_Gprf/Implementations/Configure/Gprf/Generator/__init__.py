from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GeneratorCls:
	"""Generator commands group definition. 5 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("generator", core, parent)

	@property
	def spath(self):
		"""spath commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_spath'):
			from .Spath import SpathCls
			self._spath = SpathCls(self._core, self._cmd_group)
		return self._spath

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.InstrumentType:
		"""SCPI: CONFigure:GPRF:GENerator<Instance>:TYPE \n
		Snippet: value: enums.InstrumentType = driver.configure.gprf.generator.get_type_py() \n
		No command help available \n
			:return: instrument_type: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:GENerator<Instance>:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.InstrumentType)

	def set_type_py(self, instrument_type: enums.InstrumentType) -> None:
		"""SCPI: CONFigure:GPRF:GENerator<Instance>:TYPE \n
		Snippet: driver.configure.gprf.generator.set_type_py(instrument_type = enums.InstrumentType.PROTocol) \n
		No command help available \n
			:param instrument_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(instrument_type, enums.InstrumentType)
		self._core.io.write(f'CONFigure:GPRF:GENerator<Instance>:TYPE {param}')

	def clone(self) -> 'GeneratorCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = GeneratorCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
