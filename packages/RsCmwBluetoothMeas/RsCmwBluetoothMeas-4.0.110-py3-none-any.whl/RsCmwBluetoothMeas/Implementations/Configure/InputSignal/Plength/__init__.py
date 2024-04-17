from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PlengthCls:
	"""Plength commands group definition. 10 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plength", core, parent)

	@property
	def qhsl(self):
		"""qhsl commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_qhsl'):
			from .Qhsl import QhslCls
			self._qhsl = QhslCls(self._core, self._cmd_group)
		return self._qhsl

	@property
	def lowEnergy(self):
		"""lowEnergy commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_lowEnergy'):
			from .LowEnergy import LowEnergyCls
			self._lowEnergy = LowEnergyCls(self._core, self._cmd_group)
		return self._lowEnergy

	def get_brate(self) -> List[int]:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:BRATe \n
		Snippet: value: List[int] = driver.configure.inputSignal.plength.get_brate() \n
		Specifies the number of bytes (octets) in the payload data of the measured BR signal. The range of values depends on the
		packet type (method RsCmwBluetoothMeas.Configure.InputSignal.Ptype.brate) . The command requires 3 comma-separated
		parameters, one for each BR packet type (order: DH1, DH3, DH5) . For the combined signal path scenario,
		use CONFigure:BLUetooth:SIGN<i>:CONNection:PACKets:PLENgth:BRATe. \n
			:return: payload_length: numeric 3 payload lengths for BR packets Range: 0 to 27 (DH1) , 0 to 183 (DH3) , 0 to 339 (DH5)
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:BRATe?')
		return response

	def set_brate(self, payload_length: List[int]) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:BRATe \n
		Snippet: driver.configure.inputSignal.plength.set_brate(payload_length = [1, 2, 3]) \n
		Specifies the number of bytes (octets) in the payload data of the measured BR signal. The range of values depends on the
		packet type (method RsCmwBluetoothMeas.Configure.InputSignal.Ptype.brate) . The command requires 3 comma-separated
		parameters, one for each BR packet type (order: DH1, DH3, DH5) . For the combined signal path scenario,
		use CONFigure:BLUetooth:SIGN<i>:CONNection:PACKets:PLENgth:BRATe. \n
			:param payload_length: numeric 3 payload lengths for BR packets Range: 0 to 27 (DH1) , 0 to 183 (DH3) , 0 to 339 (DH5)
		"""
		param = Conversions.list_to_csv_str(payload_length)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:BRATe {param}')

	def get_edrate(self) -> List[int]:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:EDRate \n
		Snippet: value: List[int] = driver.configure.inputSignal.plength.get_edrate() \n
		Specifies the number of bytes (octets) in the payload data of the measured EDR signal. The range of values depends on the
		packet type (method RsCmwBluetoothMeas.Configure.InputSignal.Ptype.edrate) . The command requires 6 comma-separated
		parameters, one for each EDR packet type (order: 2-DH1, 2-DH3, 2-DH5, 3-DH1, 3-DH3, 3-DH5) . For the combined signal path
		scenario, use CONFigure:BLUetooth:SIGN<i>:CONNection:PACKets:PLENgth:EDRate. \n
			:return: payload_length: numeric 6 payload lengths for EDR packets Range: 0 to 54 (2-DH1) , 0 to 367 (2-DH3) , 0 to 679 (2-DH5) , 0 to 83 (3-DH1) , 0 to 552 (3-DH3) , 0 to 1021 (3-DH5)
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:EDRate?')
		return response

	def set_edrate(self, payload_length: List[int]) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:EDRate \n
		Snippet: driver.configure.inputSignal.plength.set_edrate(payload_length = [1, 2, 3]) \n
		Specifies the number of bytes (octets) in the payload data of the measured EDR signal. The range of values depends on the
		packet type (method RsCmwBluetoothMeas.Configure.InputSignal.Ptype.edrate) . The command requires 6 comma-separated
		parameters, one for each EDR packet type (order: 2-DH1, 2-DH3, 2-DH5, 3-DH1, 3-DH3, 3-DH5) . For the combined signal path
		scenario, use CONFigure:BLUetooth:SIGN<i>:CONNection:PACKets:PLENgth:EDRate. \n
			:param payload_length: numeric 6 payload lengths for EDR packets Range: 0 to 54 (2-DH1) , 0 to 367 (2-DH3) , 0 to 679 (2-DH5) , 0 to 83 (3-DH1) , 0 to 552 (3-DH3) , 0 to 1021 (3-DH5)
		"""
		param = Conversions.list_to_csv_str(payload_length)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:PLENgth:EDRate {param}')

	def clone(self) -> 'PlengthCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PlengthCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
