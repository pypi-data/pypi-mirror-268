from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AllocationCls:
	"""Allocation commands group definition. 16 total commands, 2 Subgroups, 1 group commands
	Repeated Capability: Allocation, default value after init: Allocation.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("allocation", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_allocation_get', 'repcap_allocation_set', repcap.Allocation.Nr1)

	def repcap_allocation_set(self, allocation: repcap.Allocation) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Allocation.Default
		Default value after init: Allocation.Nr1"""
		self._cmd_group.set_repcap_enum_value(allocation)

	def repcap_allocation_get(self) -> repcap.Allocation:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def pusch(self):
		"""pusch commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_pusch'):
			from .Pusch import PuschCls
			self._pusch = PuschCls(self._core, self._cmd_group)
		return self._pusch

	@property
	def pucch(self):
		"""pucch commands group. 7 Sub-classes, 1 commands."""
		if not hasattr(self, '_pucch'):
			from .Pucch import PucchCls
			self._pucch = PucchCls(self._core, self._cmd_group)
		return self._pucch

	def set(self, bandwidth_part: enums.BandwidthPart, slot_format: int, content: enums.ChannelTypeA, allocated_slots: enums.AllocatedSlots, carrierComponent=repcap.CarrierComponent.Nr1, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation> \n
		Snippet: driver.configure.nrSubMeas.cc.allocation.set(bandwidth_part = enums.BandwidthPart.BWP0, slot_format = 1, content = enums.ChannelTypeA.PUCCh, allocated_slots = enums.AllocatedSlots.ALL, carrierComponent = repcap.CarrierComponent.Nr1, allocation = repcap.Allocation.Default) \n
		Selects the type of channel to be measured, for carrier <no>, allocation <a>. The other parameters in this command are
		fixed in the current software version. \n
			:param bandwidth_part: The current software version uses only one bandwidth part.
			:param slot_format: The current software version supports only slot format 1.
			:param content: Type of channel to be measured
			:param allocated_slots: In the current software version, all UL slots must be scheduled and use the same allocation.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('bandwidth_part', bandwidth_part, DataType.Enum, enums.BandwidthPart), ArgSingle('slot_format', slot_format, DataType.Integer), ArgSingle('content', content, DataType.Enum, enums.ChannelTypeA), ArgSingle('allocated_slots', allocated_slots, DataType.Enum, enums.AllocatedSlots))
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocation_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class AllocationStruct(StructBase):
		"""Response structure. Fields: \n
			- Bandwidth_Part: enums.BandwidthPart: The current software version uses only one bandwidth part.
			- Slot_Format: int: The current software version supports only slot format 1.
			- Content: enums.ChannelTypeA: Type of channel to be measured
			- Allocated_Slots: enums.AllocatedSlots: In the current software version, all UL slots must be scheduled and use the same allocation."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Bandwidth_Part', enums.BandwidthPart),
			ArgStruct.scalar_int('Slot_Format'),
			ArgStruct.scalar_enum('Content', enums.ChannelTypeA),
			ArgStruct.scalar_enum('Allocated_Slots', enums.AllocatedSlots)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Bandwidth_Part: enums.BandwidthPart = None
			self.Slot_Format: int = None
			self.Content: enums.ChannelTypeA = None
			self.Allocated_Slots: enums.AllocatedSlots = None

	def get(self, carrierComponent=repcap.CarrierComponent.Nr1, allocation=repcap.Allocation.Default) -> AllocationStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation> \n
		Snippet: value: AllocationStruct = driver.configure.nrSubMeas.cc.allocation.get(carrierComponent = repcap.CarrierComponent.Nr1, allocation = repcap.Allocation.Default) \n
		Selects the type of channel to be measured, for carrier <no>, allocation <a>. The other parameters in this command are
		fixed in the current software version. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: structure: for return value, see the help for AllocationStruct structure arguments."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocation_cmd_val}?', self.__class__.AllocationStruct())

	def clone(self) -> 'AllocationCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AllocationCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
