from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LayerCls:
	"""Layer commands group definition. 20 total commands, 5 Subgroups, 0 group commands
	Repeated Capability: Layer, default value after init: Layer.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("layer", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_layer_get', 'repcap_layer_set', repcap.Layer.Nr1)

	def repcap_layer_set(self, layer: repcap.Layer) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Layer.Default
		Default value after init: Layer.Nr1"""
		self._cmd_group.set_repcap_enum_value(layer)

	def repcap_layer_get(self) -> repcap.Layer:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def iq(self):
		"""iq commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_iq'):
			from .Iq import IqCls
			self._iq = IqCls(self._core, self._cmd_group)
		return self._iq

	@property
	def iemissions(self):
		"""iemissions commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_iemissions'):
			from .Iemissions import IemissionsCls
			self._iemissions = IemissionsCls(self._core, self._cmd_group)
		return self._iemissions

	@property
	def evmc(self):
		"""evmc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_evmc'):
			from .Evmc import EvmcCls
			self._evmc = EvmcCls(self._core, self._cmd_group)
		return self._evmc

	@property
	def evmSymbol(self):
		"""evmSymbol commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_evmSymbol'):
			from .EvmSymbol import EvmSymbolCls
			self._evmSymbol = EvmSymbolCls(self._core, self._cmd_group)
		return self._evmSymbol

	@property
	def esFlatness(self):
		"""esFlatness commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_esFlatness'):
			from .EsFlatness import EsFlatnessCls
			self._esFlatness = EsFlatnessCls(self._core, self._cmd_group)
		return self._esFlatness

	def clone(self) -> 'LayerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LayerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
