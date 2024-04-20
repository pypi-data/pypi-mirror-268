from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LayerCls:
	"""Layer commands group definition. 14 total commands, 1 Subgroups, 0 group commands
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
	def pdynamics(self):
		"""pdynamics commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdynamics'):
			from .Pdynamics import PdynamicsCls
			self._pdynamics = PdynamicsCls(self._core, self._cmd_group)
		return self._pdynamics

	def clone(self) -> 'LayerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = LayerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
