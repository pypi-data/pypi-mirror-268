from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettingsCls:
	"""RfSettings commands group definition. 16 total commands, 4 Subgroups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfSettings", core, parent)

	@property
	def dtx(self):
		"""dtx commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_dtx'):
			from .Dtx import DtxCls
			self._dtx = DtxCls(self._core, self._cmd_group)
		return self._dtx

	@property
	def cte(self):
		"""cte commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cte'):
			from .Cte import CteCls
			self._cte = CteCls(self._core, self._cmd_group)
		return self._cte

	@property
	def mmode(self):
		"""mmode commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mmode'):
			from .Mmode import MmodeCls
			self._mmode = MmodeCls(self._core, self._cmd_group)
		return self._mmode

	@property
	def mchannel(self):
		"""mchannel commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_mchannel'):
			from .Mchannel import MchannelCls
			self._mchannel = MchannelCls(self._core, self._cmd_group)
		return self._mchannel

	def get_eattenuation(self) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:EATTenuation \n
		Snippet: value: float = driver.configure.rfSettings.get_eattenuation() \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector.
		For the combined signal path scenario, use CONFigure:BLUetooth:SIGN<i>:RFSettings:EATTenuation:INPut. \n
			:return: external_att: numeric Range: -50 dB to 90 dB
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:EATTenuation?')
		return Conversions.str_to_float(response)

	def set_eattenuation(self, external_att: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:EATTenuation \n
		Snippet: driver.configure.rfSettings.set_eattenuation(external_att = 1.0) \n
		Defines an external attenuation (or gain, if the value is negative) , to be applied to the input connector.
		For the combined signal path scenario, use CONFigure:BLUetooth:SIGN<i>:RFSettings:EATTenuation:INPut. \n
			:param external_att: numeric Range: -50 dB to 90 dB
		"""
		param = Conversions.decimal_value_to_str(external_att)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:EATTenuation {param}')

	def get_umargin(self) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:UMARgin \n
		Snippet: value: float = driver.configure.rfSettings.get_umargin() \n
		Sets the margin that the R&S CMW adds to the expected nominal power to determine the reference level. The reference level
		minus the external input attenuation must be within the power range of the selected input connector; refer to the data
		sheet. For the combined signal path scenario, use CONFigure:BLUetooth:SIGN<i>:RFSettings:UMARgin. \n
			:return: user_margin: numeric Range: 0 dB to (55 dB + external attenuation - expected nominal power)
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:UMARgin?')
		return Conversions.str_to_float(response)

	def set_umargin(self, user_margin: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:UMARgin \n
		Snippet: driver.configure.rfSettings.set_umargin(user_margin = 1.0) \n
		Sets the margin that the R&S CMW adds to the expected nominal power to determine the reference level. The reference level
		minus the external input attenuation must be within the power range of the selected input connector; refer to the data
		sheet. For the combined signal path scenario, use CONFigure:BLUetooth:SIGN<i>:RFSettings:UMARgin. \n
			:param user_margin: numeric Range: 0 dB to (55 dB + external attenuation - expected nominal power)
		"""
		param = Conversions.decimal_value_to_str(user_margin)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:UMARgin {param}')

	def get_envelope_power(self) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:ENPower \n
		Snippet: value: float = driver.configure.rfSettings.get_envelope_power() \n
		Sets the expected nominal power of the measured RF signal. For the combined signal path scenario,
		use CONFigure:BLUetooth:SIGN<i>:RFSettings:ENPower. \n
			:return: exp_nominal_power: numeric The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the data sheet.
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:ENPower?')
		return Conversions.str_to_float(response)

	def set_envelope_power(self, exp_nominal_power: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:ENPower \n
		Snippet: driver.configure.rfSettings.set_envelope_power(exp_nominal_power = 1.0) \n
		Sets the expected nominal power of the measured RF signal. For the combined signal path scenario,
		use CONFigure:BLUetooth:SIGN<i>:RFSettings:ENPower. \n
			:param exp_nominal_power: numeric The range of the expected nominal power can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the data sheet.
		"""
		param = Conversions.decimal_value_to_str(exp_nominal_power)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:ENPower {param}')

	def get_frequency(self) -> float:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:FREQuency \n
		Snippet: value: float = driver.configure.rfSettings.get_frequency() \n
		Selects the center frequency of the RF analyzer.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:BLUetooth:SIGN<i>:RFSettings:CHANnel:LOOPback
			- CONFigure:BLUetooth:SIGN<i>:RFSettings:CHANnel:TXTest
			- CONFigure:BLUetooth:SIGN<i>:RFSettings:FREQuency:LOOPback?
			- CONFigure:BLUetooth:SIGN<i>:RFSettings:FREQuency:TXTest?
			- CONFigure:BLUetooth:SIGN<i>:RFSettings:HOPPing
			- method RsCmwBluetoothMeas.Configure.RfSettings.Mmode.value
			- method RsCmwBluetoothMeas.Configure.RfSettings.Mchannel.classic \n
			:return: analyzer_freq: numeric Range: 100 MHz to 6 GHz, Unit: Hz
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, analyzer_freq: float) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:FREQuency \n
		Snippet: driver.configure.rfSettings.set_frequency(analyzer_freq = 1.0) \n
		Selects the center frequency of the RF analyzer.
			INTRO_CMD_HELP: For the combined signal path scenario, use: \n
			- CONFigure:BLUetooth:SIGN<i>:RFSettings:CHANnel:LOOPback
			- CONFigure:BLUetooth:SIGN<i>:RFSettings:CHANnel:TXTest
			- CONFigure:BLUetooth:SIGN<i>:RFSettings:FREQuency:LOOPback?
			- CONFigure:BLUetooth:SIGN<i>:RFSettings:FREQuency:TXTest?
			- CONFigure:BLUetooth:SIGN<i>:RFSettings:HOPPing
			- method RsCmwBluetoothMeas.Configure.RfSettings.Mmode.value
			- method RsCmwBluetoothMeas.Configure.RfSettings.Mchannel.classic \n
			:param analyzer_freq: numeric Range: 100 MHz to 6 GHz, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(analyzer_freq)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:FREQuency {param}')

	def get_rlevel(self) -> int:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:RLEVel \n
		Snippet: value: int = driver.configure.rfSettings.get_rlevel() \n
		No command help available \n
			:return: reference_level: No help available
		"""
		response = self._core.io.query_str('CONFigure:BLUetooth:MEASurement<Instance>:RFSettings:RLEVel?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'RfSettingsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfSettingsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
