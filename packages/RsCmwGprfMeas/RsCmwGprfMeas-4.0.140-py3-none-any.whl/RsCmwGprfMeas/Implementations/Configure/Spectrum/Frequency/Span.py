from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SpanCls:
	"""Span commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("span", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.SpanMode:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:SPAN:MODE \n
		Snippet: value: enums.SpanMode = driver.configure.spectrum.frequency.span.get_mode() \n
		Configures the operating mode of the spectrum analyzer. FSWeep is not supported for combined signal path measurements. \n
			:return: span_mode: FSWeep | ZSPan FSWeep: frequency sweep mode ZSPan: zero span (time sweep) mode
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:SPAN:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SpanMode)

	def set_mode(self, span_mode: enums.SpanMode) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:SPAN:MODE \n
		Snippet: driver.configure.spectrum.frequency.span.set_mode(span_mode = enums.SpanMode.FSWeep) \n
		Configures the operating mode of the spectrum analyzer. FSWeep is not supported for combined signal path measurements. \n
			:param span_mode: FSWeep | ZSPan FSWeep: frequency sweep mode ZSPan: zero span (time sweep) mode
		"""
		param = Conversions.enum_scalar_to_str(span_mode, enums.SpanMode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:SPAN:MODE {param}')

	def get_value(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:SPAN \n
		Snippet: value: float = driver.configure.spectrum.frequency.span.get_value() \n
		Configures the frequency span for frequency sweep mode. The supported frequency range depends on the instrument model and
		the available options. The supported range can be smaller than stated here. Refer to the preface of your model-specific
		base unit manual. \n
			:return: frequency_span: numeric Range: 1.0 kHz to 5.93 GHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:SPAN?')
		return Conversions.str_to_float(response)

	def set_value(self, frequency_span: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:SPAN \n
		Snippet: driver.configure.spectrum.frequency.span.set_value(frequency_span = 1.0) \n
		Configures the frequency span for frequency sweep mode. The supported frequency range depends on the instrument model and
		the available options. The supported range can be smaller than stated here. Refer to the preface of your model-specific
		base unit manual. \n
			:param frequency_span: numeric Range: 1.0 kHz to 5.93 GHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency_span)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:FREQuency:SPAN {param}')
