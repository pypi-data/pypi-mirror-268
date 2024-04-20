from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GhoppingCls:
	"""Ghopping commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ghopping", core, parent)

	@property
	def init(self):
		"""init commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_init'):
			from .Init import InitCls
			self._init = InitCls(self._core, self._cmd_group)
		return self._init

	@property
	def hid(self):
		"""hid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hid'):
			from .Hid import HidCls
			self._hid = HidCls(self._core, self._cmd_group)
		return self._hid

	def set(self, group_hopping: enums.GroupHopping, carrierComponentFour=repcap.CarrierComponentFour.Nr1, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUCCh:GHOPping \n
		Snippet: driver.configure.nrSubMeas.cc.allocation.pucch.ghopping.set(group_hopping = enums.GroupHopping.DISable, carrierComponentFour = repcap.CarrierComponentFour.Nr1, allocation = repcap.Allocation.Default) \n
		Specifies whether group hopping and/or sequence hopping are used for the PUCCH DMRS, for carrier <no>, allocation <a>. \n
			:param group_hopping: NEITher: no group hopping and no sequence hopping ENABle: group hopping DISable: sequence hopping
			:param carrierComponentFour: optional repeated capability selector. Default value: Nr1
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
		"""
		param = Conversions.enum_scalar_to_str(group_hopping, enums.GroupHopping)
		carrierComponentFour_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentFour, repcap.CarrierComponentFour)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponentFour_cmd_val}:ALLocation{allocation_cmd_val}:PUCCh:GHOPping {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponentFour=repcap.CarrierComponentFour.Nr1, allocation=repcap.Allocation.Default) -> enums.GroupHopping:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUCCh:GHOPping \n
		Snippet: value: enums.GroupHopping = driver.configure.nrSubMeas.cc.allocation.pucch.ghopping.get(carrierComponentFour = repcap.CarrierComponentFour.Nr1, allocation = repcap.Allocation.Default) \n
		Specifies whether group hopping and/or sequence hopping are used for the PUCCH DMRS, for carrier <no>, allocation <a>. \n
			:param carrierComponentFour: optional repeated capability selector. Default value: Nr1
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: group_hopping: NEITher: no group hopping and no sequence hopping ENABle: group hopping DISable: sequence hopping"""
		carrierComponentFour_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentFour, repcap.CarrierComponentFour)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		response = self._core.io.query_str(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponentFour_cmd_val}:ALLocation{allocation_cmd_val}:PUCCh:GHOPping?')
		return Conversions.str_to_scalar_enum(response, enums.GroupHopping)

	def clone(self) -> 'GhoppingCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = GhoppingCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
