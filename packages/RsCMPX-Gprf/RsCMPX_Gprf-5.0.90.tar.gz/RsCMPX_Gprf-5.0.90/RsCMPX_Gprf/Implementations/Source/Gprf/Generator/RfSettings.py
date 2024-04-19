from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettingsCls:
	"""RfSettings commands group definition. 7 total commands, 0 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfSettings", core, parent)

	def get_lo_frequency(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RFSettings:LOFRequency \n
		Snippet: value: float = driver.source.gprf.generator.rfSettings.get_lo_frequency() \n
		Queries the required external LO frequency resulting from the generator settings. The command also triggers a refresh of
		the information before the query. So no need for a separate refresh command. \n
			:return: lo_frequency: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:RFSettings:LOFRequency?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_lo_level(self) -> enums.LoLevel:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RFSettings:LOLevel \n
		Snippet: value: enums.LoLevel = driver.source.gprf.generator.rfSettings.get_lo_level() \n
		Queries whether the level of an external LO signal is correct. \n
			:return: lo_level: Level correct, too low, too high.
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:RFSettings:LOLevel?')
		return Conversions.str_to_scalar_enum(response, enums.LoLevel)

	def get_dgain(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RFSettings:DGAin \n
		Snippet: value: float = driver.source.gprf.generator.rfSettings.get_dgain() \n
		Defines the digital gain of the RF generator. \n
			:return: digital_gain: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:RFSettings:DGAin?')
		return Conversions.str_to_float(response)

	def set_dgain(self, digital_gain: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RFSettings:DGAin \n
		Snippet: driver.source.gprf.generator.rfSettings.set_dgain(digital_gain = 1.0) \n
		Defines the digital gain of the RF generator. \n
			:param digital_gain: No help available
		"""
		param = Conversions.decimal_value_to_str(digital_gain)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:RFSettings:DGAin {param}')

	def get_pe_power(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RFSettings:PEPower \n
		Snippet: value: float = driver.source.gprf.generator.rfSettings.get_pe_power() \n
		Queries the peak envelope power. \n
			:return: peak_envelope_pow: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:RFSettings:PEPower?')
		return Conversions.str_to_float(response)

	def get_eattenuation(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RFSettings:EATTenuation \n
		Snippet: value: float = driver.source.gprf.generator.rfSettings.get_eattenuation() \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the output connector. \n
			:return: ext_rf_out_att: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:RFSettings:EATTenuation?')
		return Conversions.str_to_float(response)

	def set_eattenuation(self, ext_rf_out_att: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RFSettings:EATTenuation \n
		Snippet: driver.source.gprf.generator.rfSettings.set_eattenuation(ext_rf_out_att = 1.0) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the output connector. \n
			:param ext_rf_out_att: No help available
		"""
		param = Conversions.decimal_value_to_str(ext_rf_out_att)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:RFSettings:EATTenuation {param}')

	def get_frequency(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RFSettings:FREQuency \n
		Snippet: value: float = driver.source.gprf.generator.rfSettings.get_frequency() \n
		Sets the frequency of the unmodulated RF carrier. For the supported frequency range, see 'Frequency ranges'. \n
			:return: frequency: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:RFSettings:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, frequency: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RFSettings:FREQuency \n
		Snippet: driver.source.gprf.generator.rfSettings.set_frequency(frequency = 1.0) \n
		Sets the frequency of the unmodulated RF carrier. For the supported frequency range, see 'Frequency ranges'. \n
			:param frequency: No help available
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:RFSettings:FREQuency {param}')

	def get_level(self) -> float:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RFSettings:LEVel \n
		Snippet: value: float = driver.source.gprf.generator.rfSettings.get_level() \n
		Sets the base RMS level of the RF generator. \n
			:return: level: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:RFSettings:LEVel?')
		return Conversions.str_to_float(response)

	def set_level(self, level: float) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:RFSettings:LEVel \n
		Snippet: driver.source.gprf.generator.rfSettings.set_level(level = 1.0) \n
		Sets the base RMS level of the RF generator. \n
			:param level: No help available
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:RFSettings:LEVel {param}')
