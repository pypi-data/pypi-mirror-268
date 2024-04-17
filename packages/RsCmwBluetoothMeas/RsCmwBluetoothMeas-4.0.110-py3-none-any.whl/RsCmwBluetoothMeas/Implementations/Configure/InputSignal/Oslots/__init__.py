from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OslotsCls:
	"""Oslots commands group definition. 5 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("oslots", core, parent)

	@property
	def lowEnergy(self):
		"""lowEnergy commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_lowEnergy'):
			from .LowEnergy import LowEnergyCls
			self._lowEnergy = LowEnergyCls(self._core, self._cmd_group)
		return self._lowEnergy

	def get_edrate(self) -> List[int]:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:OSLots:EDRate \n
		Snippet: value: List[int] = driver.configure.inputSignal.oslots.get_edrate() \n
		Specifies the number of unused slots between any two occupied slots or slot sequences. \n
			:return: no_of_off_slots: numeric Number of off slots for the different packet types: 3 values for BR packets (DH1, DH3, DH5) 6 values for EDR packets (2-DH1, 2-DH3, 2-DH5, 3-DH1, 3-DH3, 3-DH5) Range: 1 to 9
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:OSLots:EDRate?')
		return response

	def set_edrate(self, no_of_off_slots: List[int]) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:OSLots:EDRate \n
		Snippet: driver.configure.inputSignal.oslots.set_edrate(no_of_off_slots = [1, 2, 3]) \n
		Specifies the number of unused slots between any two occupied slots or slot sequences. \n
			:param no_of_off_slots: numeric Number of off slots for the different packet types: 3 values for BR packets (DH1, DH3, DH5) 6 values for EDR packets (2-DH1, 2-DH3, 2-DH5, 3-DH1, 3-DH3, 3-DH5) Range: 1 to 9
		"""
		param = Conversions.list_to_csv_str(no_of_off_slots)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:OSLots:EDRate {param}')

	def get_brate(self) -> List[int]:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:OSLots:BRATe \n
		Snippet: value: List[int] = driver.configure.inputSignal.oslots.get_brate() \n
		Specifies the number of unused slots between any two occupied slots or slot sequences. \n
			:return: no_of_off_slots: numeric Number of off slots for the different packet types: 3 values for BR packets (DH1, DH3, DH5) 6 values for EDR packets (2-DH1, 2-DH3, 2-DH5, 3-DH1, 3-DH3, 3-DH5) Range: 1 to 9
		"""
		response = self._core.io.query_bin_or_ascii_int_list('CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:OSLots:BRATe?')
		return response

	def set_brate(self, no_of_off_slots: List[int]) -> None:
		"""SCPI: CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:OSLots:BRATe \n
		Snippet: driver.configure.inputSignal.oslots.set_brate(no_of_off_slots = [1, 2, 3]) \n
		Specifies the number of unused slots between any two occupied slots or slot sequences. \n
			:param no_of_off_slots: numeric Number of off slots for the different packet types: 3 values for BR packets (DH1, DH3, DH5) 6 values for EDR packets (2-DH1, 2-DH3, 2-DH5, 3-DH1, 3-DH3, 3-DH5) Range: 1 to 9
		"""
		param = Conversions.list_to_csv_str(no_of_off_slots)
		self._core.io.write(f'CONFigure:BLUetooth:MEASurement<Instance>:ISIGnal:OSLots:BRATe {param}')

	def clone(self) -> 'OslotsCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = OslotsCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
