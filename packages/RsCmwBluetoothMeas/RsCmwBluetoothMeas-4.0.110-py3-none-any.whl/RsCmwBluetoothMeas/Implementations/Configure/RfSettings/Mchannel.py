from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MchannelCls:
	"""Mchannel commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mchannel", core, parent)

	def get_classic(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:MCHannel[:CLASsic] \n
		Snippet: value: int = driver.configure.rfSettings.mchannel.get_classic() \n
		Specifies the channel to be measured in CSP single channel mode for classic, see method RsCmwBluetoothMeas.Configure.
		RfSettings.Mmode.value \n
			:return: measured_channel: numeric Range: 0 to 78
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:MCHannel:CLASsic?')
		return Conversions.str_to_int(response)

	def set_classic(self, measured_channel: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:MCHannel[:CLASsic] \n
		Snippet: driver.configure.rfSettings.mchannel.set_classic(measured_channel = 1) \n
		Specifies the channel to be measured in CSP single channel mode for classic, see method RsCmwBluetoothMeas.Configure.
		RfSettings.Mmode.value \n
			:param measured_channel: numeric Range: 0 to 78
		"""
		param = Conversions.decimal_value_to_str(measured_channel)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:MCHannel:CLASsic {param}')

	def get_low_energy(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:MCHannel:LENergy \n
		Snippet: value: int = driver.configure.rfSettings.mchannel.get_low_energy() \n
		Specifies the channel to be measured in CSP single channel mode with LE connection tests, see method RsCmwBluetoothMeas.
		Configure.RfSettings.Mmode.Nmode.lowEnergy \n
			:return: measured_channel: numeric Channel number Range: 1 to 11, 13 to 38
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:MCHannel:LENergy?')
		return Conversions.str_to_int(response)

	def set_low_energy(self, measured_channel: int) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:MCHannel:LENergy \n
		Snippet: driver.configure.rfSettings.mchannel.set_low_energy(measured_channel = 1) \n
		Specifies the channel to be measured in CSP single channel mode with LE connection tests, see method RsCmwBluetoothMeas.
		Configure.RfSettings.Mmode.Nmode.lowEnergy \n
			:param measured_channel: numeric Channel number Range: 1 to 11, 13 to 38
		"""
		param = Conversions.decimal_value_to_str(measured_channel)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:MCHannel:LENergy {param}')
