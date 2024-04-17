from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbwCls:
	"""Rbw commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbw", core, parent)

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.RbwFilterType:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:RBW:TYPE \n
		Snippet: value: enums.RbwFilterType = driver.configure.spectrum.zeroSpan.rbw.get_type_py() \n
		Configures the type of the resolution filter to be used in zero span mode. \n
			:return: rbw_type: GAUSs | BANDpass
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:RBW:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.RbwFilterType)

	def set_type_py(self, rbw_type: enums.RbwFilterType) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:RBW:TYPE \n
		Snippet: driver.configure.spectrum.zeroSpan.rbw.set_type_py(rbw_type = enums.RbwFilterType.BANDpass) \n
		Configures the type of the resolution filter to be used in zero span mode. \n
			:param rbw_type: GAUSs | BANDpass
		"""
		param = Conversions.enum_scalar_to_str(rbw_type, enums.RbwFilterType)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:RBW:TYPE {param}')

	def get_bandpass(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:RBW:BANDpass \n
		Snippet: value: float = driver.configure.spectrum.zeroSpan.rbw.get_bandpass() \n
		Configures the bandwidth of the bandpass resolution filter. In the current software version, the value is fixed. \n
			:return: rbw_bandpass: numeric Range: 40 MHz to 40 MHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:RBW:BANDpass?')
		return Conversions.str_to_float(response)

	def set_bandpass(self, rbw_bandpass: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:RBW:BANDpass \n
		Snippet: driver.configure.spectrum.zeroSpan.rbw.set_bandpass(rbw_bandpass = 1.0) \n
		Configures the bandwidth of the bandpass resolution filter. In the current software version, the value is fixed. \n
			:param rbw_bandpass: numeric Range: 40 MHz to 40 MHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(rbw_bandpass)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:RBW:BANDpass {param}')

	def get_gauss(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:RBW:GAUSs \n
		Snippet: value: float = driver.configure.spectrum.zeroSpan.rbw.get_gauss() \n
		Configures the bandwidth of the Gaussian resolution filter. \n
			:return: rbw: numeric Only certain values can be configured, see Table 'Supported values'. Other values are rounded to the next allowed value. Range: 100 Hz to 10 MHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:RBW:GAUSs?')
		return Conversions.str_to_float(response)

	def set_gauss(self, rbw: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:RBW:GAUSs \n
		Snippet: driver.configure.spectrum.zeroSpan.rbw.set_gauss(rbw = 1.0) \n
		Configures the bandwidth of the Gaussian resolution filter. \n
			:param rbw: numeric Only certain values can be configured, see Table 'Supported values'. Other values are rounded to the next allowed value. Range: 100 Hz to 10 MHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(rbw)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:SPECtrum:ZSPan:RBW:GAUSs {param}')
