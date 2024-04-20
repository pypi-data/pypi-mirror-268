from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MerrorCls:
	"""Merror commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("merror", core, parent)

	def fetch(self, xvalue: int, trace_select: enums.TraceSelect, carrierComponent=repcap.CarrierComponent.Default, layer=repcap.Layer.Default, deltaMarker=repcap.DeltaMarker.Default) -> float:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:MEValuation[:CC<no>][:LAYer<layer>]:DMARker<Nr>:MERRor \n
		Snippet: value: float = driver.nrSubMeas.multiEval.cc.layer.dmarker.merror.fetch(xvalue = 1, trace_select = enums.TraceSelect.AVERage, carrierComponent = repcap.CarrierComponent.Default, layer = repcap.Layer.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		Uses the markers 1 and 2 with relative values on the diagrams: EVM RMS, EVM peak, magnitude error and phase error vs OFDM
		symbol. \n
		Suppressed linked return values: reliability \n
			:param xvalue: X-value of the marker position relative to the x-value of the reference marker There are two x-values per OFDM symbol on the x-axis (symbol 0 low, symbol 0 high, ..., symbol 14 low, symbol 14 high) .
			:param trace_select: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param layer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Layer')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Dmarker')
			:return: yvalue: Y-value of the marker position relative to the y-value of the reference marker"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('xvalue', xvalue, DataType.Integer), ArgSingle('trace_select', trace_select, DataType.Enum, enums.TraceSelect))
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		layer_cmd_val = self._cmd_group.get_repcap_cmd_value(layer, repcap.Layer)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:NRSub:MEASurement<Instance>:MEValuation:CC{carrierComponent_cmd_val}:LAYer{layer_cmd_val}:DMARker{deltaMarker_cmd_val}:MERRor? {param}'.rstrip(), suppressed)
		return Conversions.str_to_float(response)
