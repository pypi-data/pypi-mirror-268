from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqSettingsCls:
	"""IqSettings commands group definition. 5 total commands, 0 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqSettings", core, parent)

	def get_symbol_rate(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:IQSettings:SRATe \n
		Snippet: value: float = driver.source.gprf.generator.iqSettings.get_symbol_rate() \n
		No command help available \n
			:return: sample_rate: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:IQSettings:SRATe?')
		return Conversions.str_to_float(response)

	def set_symbol_rate(self, sample_rate: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:IQSettings:SRATe \n
		Snippet: driver.source.gprf.generator.iqSettings.set_symbol_rate(sample_rate = 1.0) \n
		No command help available \n
			:param sample_rate: No help available
		"""
		param = Conversions.decimal_value_to_str(sample_rate)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:IQSettings:SRATe {param}')

	# noinspection PyTypeChecker
	def get_tmode(self) -> enums.TransferMode:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:IQSettings:TMODe \n
		Snippet: value: enums.TransferMode = driver.source.gprf.generator.iqSettings.get_tmode() \n
		No command help available \n
			:return: transfer_mode: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:IQSettings:TMODe?')
		return Conversions.str_to_scalar_enum(response, enums.TransferMode)

	def set_tmode(self, transfer_mode: enums.TransferMode) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:IQSettings:TMODe \n
		Snippet: driver.source.gprf.generator.iqSettings.set_tmode(transfer_mode = enums.TransferMode.ENABlemode) \n
		No command help available \n
			:param transfer_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(transfer_mode, enums.TransferMode)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:IQSettings:TMODe {param}')

	def get_level(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:IQSettings:LEVel \n
		Snippet: value: float = driver.source.gprf.generator.iqSettings.get_level() \n
		No command help available \n
			:return: level: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:IQSettings:LEVel?')
		return Conversions.str_to_float(response)

	def get_pep(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:IQSettings:PEP \n
		Snippet: value: float = driver.source.gprf.generator.iqSettings.get_pep() \n
		No command help available \n
			:return: pep: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:IQSettings:PEP?')
		return Conversions.str_to_float(response)

	def get_crest(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:IQSettings:CRESt \n
		Snippet: value: float = driver.source.gprf.generator.iqSettings.get_crest() \n
		No command help available \n
			:return: crest: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:IQSettings:CRESt?')
		return Conversions.str_to_float(response)
