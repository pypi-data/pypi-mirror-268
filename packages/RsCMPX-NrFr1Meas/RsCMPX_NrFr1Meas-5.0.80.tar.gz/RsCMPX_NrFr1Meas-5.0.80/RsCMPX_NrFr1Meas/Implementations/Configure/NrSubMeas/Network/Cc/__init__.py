from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CcCls:
	"""Cc commands group definition. 2 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: CarrierComponentOne, default value after init: CarrierComponentOne.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cc", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_carrierComponentOne_get', 'repcap_carrierComponentOne_set', repcap.CarrierComponentOne.Nr1)

	def repcap_carrierComponentOne_set(self, carrierComponentOne: repcap.CarrierComponentOne) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CarrierComponentOne.Default
		Default value after init: CarrierComponentOne.Nr1"""
		self._cmd_group.set_repcap_enum_value(carrierComponentOne)

	def repcap_carrierComponentOne_get(self) -> repcap.CarrierComponentOne:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def plcId(self):
		"""plcId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plcId'):
			from .PlcId import PlcIdCls
			self._plcId = PlcIdCls(self._core, self._cmd_group)
		return self._plcId

	@property
	def cbandwidth(self):
		"""cbandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbandwidth'):
			from .Cbandwidth import CbandwidthCls
			self._cbandwidth = CbandwidthCls(self._core, self._cmd_group)
		return self._cbandwidth

	def clone(self) -> 'CcCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CcCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
