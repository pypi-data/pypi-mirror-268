from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CcCls:
	"""Cc commands group definition. 39 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cc", core, parent)
		
		self._cmd_group.multi_repcap_types = "CarrierComponent,CarrierComponentFour,CarrierComponentOne"

	@property
	def cbandwidth(self):
		"""cbandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbandwidth'):
			from .Cbandwidth import CbandwidthCls
			self._cbandwidth = CbandwidthCls(self._core, self._cmd_group)
		return self._cbandwidth

	@property
	def plcId(self):
		"""plcId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plcId'):
			from .PlcId import PlcIdCls
			self._plcId = PlcIdCls(self._core, self._cmd_group)
		return self._plcId

	@property
	def taPosition(self):
		"""taPosition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_taPosition'):
			from .TaPosition import TaPositionCls
			self._taPosition = TaPositionCls(self._core, self._cmd_group)
		return self._taPosition

	@property
	def txBwidth(self):
		"""txBwidth commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_txBwidth'):
			from .TxBwidth import TxBwidthCls
			self._txBwidth = TxBwidthCls(self._core, self._cmd_group)
		return self._txBwidth

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import FrequencyCls
			self._frequency = FrequencyCls(self._core, self._cmd_group)
		return self._frequency

	@property
	def nbwParts(self):
		"""nbwParts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nbwParts'):
			from .NbwParts import NbwPartsCls
			self._nbwParts = NbwPartsCls(self._core, self._cmd_group)
		return self._nbwParts

	@property
	def bwPart(self):
		"""bwPart commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_bwPart'):
			from .BwPart import BwPartCls
			self._bwPart = BwPartCls(self._core, self._cmd_group)
		return self._bwPart

	@property
	def nallocations(self):
		"""nallocations commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nallocations'):
			from .Nallocations import NallocationsCls
			self._nallocations = NallocationsCls(self._core, self._cmd_group)
		return self._nallocations

	@property
	def allocation(self):
		"""allocation commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_allocation'):
			from .Allocation import AllocationCls
			self._allocation = AllocationCls(self._core, self._cmd_group)
		return self._allocation

	@property
	def rpool(self):
		"""rpool commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_rpool'):
			from .Rpool import RpoolCls
			self._rpool = RpoolCls(self._core, self._cmd_group)
		return self._rpool

	def clone(self) -> 'CcCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CcCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
