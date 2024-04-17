from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VbwCls:
	"""Vbw commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vbw", core, parent)

	def get_auto(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW:AUTO \n
		Snippet: value: bool = driver.configure.spectrum.freqSweep.vbw.get_auto() \n
		Enables or disables the automatic mode for the VBW in frequency sweep mode. \n
			:return: vbw_auto: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW:AUTO?')
		return Conversions.str_to_bool(response)

	def set_auto(self, vbw_auto: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW:AUTO \n
		Snippet: driver.configure.spectrum.freqSweep.vbw.set_auto(vbw_auto = False) \n
		Enables or disables the automatic mode for the VBW in frequency sweep mode. \n
			:param vbw_auto: OFF | ON
		"""
		param = Conversions.bool_to_str(vbw_auto)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW:AUTO {param}')

	def get_value(self) -> float or bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW \n
		Snippet: value: float or bool = driver.configure.spectrum.freqSweep.vbw.get_value() \n
		Configures the video bandwidth (VBW) for the frequency sweep mode. Setting this value is only possible if the automatic
		mode is off. \n
			:return: vbw: (float or boolean) numeric | OFF Only certain values can be configured, see Table 'Supported values'. Other values are rounded to the next allowed value. Range: 10 Hz to 10 MHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW?')
		return Conversions.str_to_float_or_bool(response)

	def set_value(self, vbw: float or bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW \n
		Snippet: driver.configure.spectrum.freqSweep.vbw.set_value(vbw = 1.0) \n
		Configures the video bandwidth (VBW) for the frequency sweep mode. Setting this value is only possible if the automatic
		mode is off. \n
			:param vbw: (float or boolean) numeric | OFF Only certain values can be configured, see Table 'Supported values'. Other values are rounded to the next allowed value. Range: 10 Hz to 10 MHz, Unit: Hz
		"""
		param = Conversions.decimal_or_bool_value_to_str(vbw)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FSWeep:VBW {param}')
