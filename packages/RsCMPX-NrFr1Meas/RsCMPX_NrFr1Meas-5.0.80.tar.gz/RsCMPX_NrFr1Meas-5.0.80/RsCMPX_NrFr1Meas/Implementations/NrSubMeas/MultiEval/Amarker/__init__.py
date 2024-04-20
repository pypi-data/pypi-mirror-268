from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AmarkerCls:
	"""Amarker commands group definition. 2 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: AbsoluteMarker, default value after init: AbsoluteMarker.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("amarker", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_absoluteMarker_get', 'repcap_absoluteMarker_set', repcap.AbsoluteMarker.Nr1)

	def repcap_absoluteMarker_set(self, absoluteMarker: repcap.AbsoluteMarker) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to AbsoluteMarker.Default
		Default value after init: AbsoluteMarker.Nr1"""
		self._cmd_group.set_repcap_enum_value(absoluteMarker)

	def repcap_absoluteMarker_get(self) -> repcap.AbsoluteMarker:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def pdynamics(self):
		"""pdynamics commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pdynamics'):
			from .Pdynamics import PdynamicsCls
			self._pdynamics = PdynamicsCls(self._core, self._cmd_group)
		return self._pdynamics

	@property
	def pmonitor(self):
		"""pmonitor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmonitor'):
			from .Pmonitor import PmonitorCls
			self._pmonitor = PmonitorCls(self._core, self._cmd_group)
		return self._pmonitor

	def clone(self) -> 'AmarkerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AmarkerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
