from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SensitivityCls:
	"""Sensitivity commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sensitivity", core, parent)

	def get_start_level(self) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SENSitivity:STARtlevel \n
		Snippet: value: float = driver.configure.rxQuality.sensitivity.get_start_level() \n
		Sets Tx start level of R&S CMW for sensitivity search measurement. The allowed value range can be calculated as follows:
		Range (Start Level) = Range (Output Power) - External Attenuation Range (Output Power) = -130 dBm to 0 dBm (RFx COM) or
		-120 dBm to 8 dBm (RFx OUT) ; please also notice the ranges quoted in the data sheet. \n
			:return: start_level: numeric Range: see above
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SENSitivity:STARtlevel?')
		return Conversions.str_to_float(response)

	def set_start_level(self, start_level: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SENSitivity:STARtlevel \n
		Snippet: driver.configure.rxQuality.sensitivity.set_start_level(start_level = 1.0) \n
		Sets Tx start level of R&S CMW for sensitivity search measurement. The allowed value range can be calculated as follows:
		Range (Start Level) = Range (Output Power) - External Attenuation Range (Output Power) = -130 dBm to 0 dBm (RFx COM) or
		-120 dBm to 8 dBm (RFx OUT) ; please also notice the ranges quoted in the data sheet. \n
			:param start_level: numeric Range: see above
		"""
		param = Conversions.decimal_value_to_str(start_level)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SENSitivity:STARtlevel {param}')

	def get_stepsize(self) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SENSitivity:STEPsize \n
		Snippet: value: float = driver.configure.rxQuality.sensitivity.get_stepsize() \n
		Sets the step size for decreasing Tx level of R&S CMW for sensitivity search measurement. \n
			:return: stepsize: numeric Range: 0.01 dB to 5 dB
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SENSitivity:STEPsize?')
		return Conversions.str_to_float(response)

	def set_stepsize(self, stepsize: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SENSitivity:STEPsize \n
		Snippet: driver.configure.rxQuality.sensitivity.set_stepsize(stepsize = 1.0) \n
		Sets the step size for decreasing Tx level of R&S CMW for sensitivity search measurement. \n
			:param stepsize: numeric Range: 0.01 dB to 5 dB
		"""
		param = Conversions.decimal_value_to_str(stepsize)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SENSitivity:STEPsize {param}')

	def get_retry(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SENSitivity:RETRy \n
		Snippet: value: int = driver.configure.rxQuality.sensitivity.get_retry() \n
		Specify the number of retry attempts per step for sensitivity search measurement. \n
			:return: retry_count: numeric Range: 0 to 7
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SENSitivity:RETRy?')
		return Conversions.str_to_int(response)

	def set_retry(self, retry_count: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SENSitivity:RETRy \n
		Snippet: driver.configure.rxQuality.sensitivity.set_retry(retry_count = 1) \n
		Specify the number of retry attempts per step for sensitivity search measurement. \n
			:param retry_count: numeric Range: 0 to 7
		"""
		param = Conversions.decimal_value_to_str(retry_count)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:SENSitivity:RETRy {param}')
