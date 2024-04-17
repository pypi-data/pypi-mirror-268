from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EattenuationCls:
	"""Eattenuation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eattenuation", core, parent)

	def get_output(self) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:EATTenuation:OUTPut \n
		Snippet: value: float = driver.configure.rxQuality.eattenuation.get_output() \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the output connector. \n
			:return: atten: numeric Range: -50 dB to 90 dB
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:EATTenuation:OUTPut?')
		return Conversions.str_to_float(response)

	def set_output(self, atten: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:EATTenuation:OUTPut \n
		Snippet: driver.configure.rxQuality.eattenuation.set_output(atten = 1.0) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the output connector. \n
			:param atten: numeric Range: -50 dB to 90 dB
		"""
		param = Conversions.decimal_value_to_str(atten)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RXQuality:EATTenuation:OUTPut {param}')
