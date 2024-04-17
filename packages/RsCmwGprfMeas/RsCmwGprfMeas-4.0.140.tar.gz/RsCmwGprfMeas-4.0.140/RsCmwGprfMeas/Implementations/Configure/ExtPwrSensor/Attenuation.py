from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AttenuationCls:
	"""Attenuation commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attenuation", core, parent)

	def get_state(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:ATTenuation:STATe \n
		Snippet: value: bool = driver.configure.extPwrSensor.attenuation.get_state() \n
		Enables or disables the result correction for an external input attenuation. \n
			:return: attenuator_state: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:EPSensor:ATTenuation:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, attenuator_state: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:ATTenuation:STATe \n
		Snippet: driver.configure.extPwrSensor.attenuation.set_state(attenuator_state = False) \n
		Enables or disables the result correction for an external input attenuation. \n
			:param attenuator_state: OFF | ON
		"""
		param = Conversions.bool_to_str(attenuator_state)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:EPSensor:ATTenuation:STATe {param}')

	def get_value(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:ATTenuation \n
		Snippet: value: float = driver.configure.extPwrSensor.attenuation.get_value() \n
		Specifies an external input attenuation factor for correction of the power results. \n
			:return: attenuation: numeric Range: -50 dB to 50 dB, Unit: dB
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:EPSensor:ATTenuation?')
		return Conversions.str_to_float(response)

	def set_value(self, attenuation: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:EPSensor:ATTenuation \n
		Snippet: driver.configure.extPwrSensor.attenuation.set_value(attenuation = 1.0) \n
		Specifies an external input attenuation factor for correction of the power results. \n
			:param attenuation: numeric Range: -50 dB to 50 dB, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(attenuation)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:EPSensor:ATTenuation {param}')
