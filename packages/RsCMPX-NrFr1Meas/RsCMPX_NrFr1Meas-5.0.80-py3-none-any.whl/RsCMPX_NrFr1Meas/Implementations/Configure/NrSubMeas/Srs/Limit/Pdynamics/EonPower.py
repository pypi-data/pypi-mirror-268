from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EonPowerCls:
	"""EonPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: EonPowerScs, default value after init: EonPowerScs.Nr15"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eonPower", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_eonPowerScs_get', 'repcap_eonPowerScs_set', repcap.EonPowerScs.Nr15)

	def repcap_eonPowerScs_set(self, eonPowerScs: repcap.EonPowerScs) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to EonPowerScs.Default
		Default value after init: EonPowerScs.Nr15"""
		self._cmd_group.set_repcap_enum_value(eonPowerScs)

	def repcap_eonPowerScs_get(self) -> repcap.EonPowerScs:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, on_power: List[float], eonPowerScs=repcap.EonPowerScs.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:LIMit:PDYNamics:EONPower<scs> \n
		Snippet: driver.configure.nrSubMeas.srs.limit.pdynamics.eonPower.set(on_power = [1.1, 2.2, 3.3], eonPowerScs = repcap.EonPowerScs.Default) \n
		Defines limits for the ON power determined with the power dynamics measurement. There is one limit value per SCS and
		channel bandwidth. The effective limit is (<OnPower> - (9 dB + test tolerance) ) to (<OnPower> + (9 dB + test tolerance)
		). \n
			:param on_power: Comma-separated list of 15 values, for the channel bandwidths [MHz]: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100. For 15 kHz, the highest five channel bandwidths are not defined. For 60 kHz, the lowest channel bandwidth is not defined. Send KEEP for not defined values.
			:param eonPowerScs: optional repeated capability selector. Default value: Nr15 (settable in the interface 'EonPower')
		"""
		param = Conversions.list_to_csv_str(on_power)
		eonPowerScs_cmd_val = self._cmd_group.get_repcap_cmd_value(eonPowerScs, repcap.EonPowerScs)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:SRS:LIMit:PDYNamics:EONPower{eonPowerScs_cmd_val} {param}')

	def get(self, eonPowerScs=repcap.EonPowerScs.Default) -> List[float]:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:SRS:LIMit:PDYNamics:EONPower<scs> \n
		Snippet: value: List[float] = driver.configure.nrSubMeas.srs.limit.pdynamics.eonPower.get(eonPowerScs = repcap.EonPowerScs.Default) \n
		Defines limits for the ON power determined with the power dynamics measurement. There is one limit value per SCS and
		channel bandwidth. The effective limit is (<OnPower> - (9 dB + test tolerance) ) to (<OnPower> + (9 dB + test tolerance)
		). \n
			:param eonPowerScs: optional repeated capability selector. Default value: Nr15 (settable in the interface 'EonPower')
			:return: on_power: Comma-separated list of 15 values, for the channel bandwidths [MHz]: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100. For 15 kHz, the highest five channel bandwidths are not defined. For 60 kHz, the lowest channel bandwidth is not defined. Send KEEP for not defined values."""
		eonPowerScs_cmd_val = self._cmd_group.get_repcap_cmd_value(eonPowerScs, repcap.EonPowerScs)
		response = self._core.io.query_bin_or_ascii_float_list(f'CONFigure:NRSub:MEASurement<Instance>:SRS:LIMit:PDYNamics:EONPower{eonPowerScs_cmd_val}?')
		return response

	def clone(self) -> 'EonPowerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EonPowerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
