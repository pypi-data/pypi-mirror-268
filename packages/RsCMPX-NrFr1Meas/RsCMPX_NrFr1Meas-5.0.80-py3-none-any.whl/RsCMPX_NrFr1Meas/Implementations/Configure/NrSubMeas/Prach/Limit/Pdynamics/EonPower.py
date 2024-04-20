from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EonPowerCls:
	"""EonPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: EonPower, default value after init: EonPower.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eonPower", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_eonPower_get', 'repcap_eonPower_set', repcap.EonPower.Nr1)

	def repcap_eonPower_set(self, eonPower: repcap.EonPower) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to EonPower.Default
		Default value after init: EonPower.Nr1"""
		self._cmd_group.set_repcap_enum_value(eonPower)

	def repcap_eonPower_get(self) -> repcap.EonPower:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, on_power: List[float], eonPower=repcap.EonPower.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:PRACh:LIMit:PDYNamics:EONPower<e> \n
		Snippet: driver.configure.nrSubMeas.prach.limit.pdynamics.eonPower.set(on_power = [1.1, 2.2, 3.3], eonPower = repcap.EonPower.Default) \n
		Defines limits for the ON power determined with the power dynamics measurement. There are two limit values per channel
		bandwidth. \n
			:param on_power: Comma-separated list of 15 values, for the channel bandwidths [MHz]: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100. The effective limit is (OnPower - (9 dB + test tolerance) ) to (OnPower + (9 dB + test tolerance) ).
			:param eonPower: optional repeated capability selector. Default value: Nr1 (settable in the interface 'EonPower')
		"""
		param = Conversions.list_to_csv_str(on_power)
		eonPower_cmd_val = self._cmd_group.get_repcap_cmd_value(eonPower, repcap.EonPower)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:PRACh:LIMit:PDYNamics:EONPower{eonPower_cmd_val} {param}')

	def get(self, eonPower=repcap.EonPower.Default) -> List[float]:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:PRACh:LIMit:PDYNamics:EONPower<e> \n
		Snippet: value: List[float] = driver.configure.nrSubMeas.prach.limit.pdynamics.eonPower.get(eonPower = repcap.EonPower.Default) \n
		Defines limits for the ON power determined with the power dynamics measurement. There are two limit values per channel
		bandwidth. \n
			:param eonPower: optional repeated capability selector. Default value: Nr1 (settable in the interface 'EonPower')
			:return: on_power: Comma-separated list of 15 values, for the channel bandwidths [MHz]: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100. The effective limit is (OnPower - (9 dB + test tolerance) ) to (OnPower + (9 dB + test tolerance) )."""
		eonPower_cmd_val = self._cmd_group.get_repcap_cmd_value(eonPower, repcap.EonPower)
		response = self._core.io.query_bin_or_ascii_float_list(f'CONFigure:NRSub:MEASurement<Instance>:PRACh:LIMit:PDYNamics:EONPower{eonPower_cmd_val}?')
		return response

	def clone(self) -> 'EonPowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EonPowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
