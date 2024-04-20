from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EvMagnitudeCls:
	"""EvMagnitude commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("evMagnitude", core, parent)

	@property
	def peak(self):
		"""peak commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_peak'):
			from .Peak import PeakCls
			self._peak = PeakCls(self._core, self._cmd_group)
		return self._peak

	def fetch(self, xvalue: int, trace_select: enums.TraceSelect, carrierComponent=repcap.CarrierComponent.Default, layer=repcap.Layer.Default, absoluteMarker=repcap.AbsoluteMarker.Default) -> float:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:MEValuation[:CC<no>][:LAYer<layer>]:AMARker<Nr>:EVMagnitude \n
		Snippet: value: float = driver.nrSubMeas.multiEval.cc.layer.amarker.evMagnitude.fetch(xvalue = 1, trace_select = enums.TraceSelect.AVERage, carrierComponent = repcap.CarrierComponent.Default, layer = repcap.Layer.Default, absoluteMarker = repcap.AbsoluteMarker.Default) \n
		Uses the markers 1 and 2 with absolute values on the diagrams: EVM RMS, EVM peak, magnitude error and phase error vs OFDM
		symbol. \n
		Suppressed linked return values: reliability \n
			:param xvalue: Absolute x-value of the marker position There are two x-values per OFDM symbol on the x-axis (symbol 0 low, symbol 0 high, ..., symbol 14 low, symbol 14 high) .
			:param trace_select: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param layer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Layer')
			:param absoluteMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Amarker')
			:return: yvalue: Absolute y-value of the marker position"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('xvalue', xvalue, DataType.Integer), ArgSingle('trace_select', trace_select, DataType.Enum, enums.TraceSelect))
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		layer_cmd_val = self._cmd_group.get_repcap_cmd_value(layer, repcap.Layer)
		absoluteMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(absoluteMarker, repcap.AbsoluteMarker)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:NRSub:MEASurement<Instance>:MEValuation:CC{carrierComponent_cmd_val}:LAYer{layer_cmd_val}:AMARker{absoluteMarker_cmd_val}:EVMagnitude? {param}'.rstrip(), suppressed)
		return Conversions.str_to_float(response)

	def clone(self) -> 'EvMagnitudeCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EvMagnitudeCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
