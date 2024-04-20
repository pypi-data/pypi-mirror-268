from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PdynamicsCls:
	"""Pdynamics commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdynamics", core, parent)

	def fetch(self, xvalue: float, trace_select: enums.TraceSelect, absoluteMarker=repcap.AbsoluteMarker.Default) -> float:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:MEValuation:AMARker<No>:PDYNamics \n
		Snippet: value: float = driver.nrSubMeas.multiEval.amarker.pdynamics.fetch(xvalue = 1.0, trace_select = enums.TraceSelect.AVERage, absoluteMarker = repcap.AbsoluteMarker.Default) \n
		Uses the markers 1 and 2 with absolute values on the power dynamics trace. \n
		Suppressed linked return values: reliability \n
			:param xvalue: Absolute x-value of the marker position
			:param trace_select: No help available
			:param absoluteMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Amarker')
			:return: yvalue: Absolute y-value of the marker position"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('xvalue', xvalue, DataType.Float), ArgSingle('trace_select', trace_select, DataType.Enum, enums.TraceSelect))
		absoluteMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(absoluteMarker, repcap.AbsoluteMarker)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:NRSub:MEASurement<Instance>:MEValuation:AMARker{absoluteMarker_cmd_val}:PDYNamics? {param}'.rstrip(), suppressed)
		return Conversions.str_to_float(response)
