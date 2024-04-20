from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PmonitorCls:
	"""Pmonitor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmonitor", core, parent)

	def fetch(self, xvalue: int, deltaMarker=repcap.DeltaMarker.Default) -> float:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:MEValuation:DMARker<No>:PMONitor \n
		Snippet: value: float = driver.nrSubMeas.multiEval.dmarker.pmonitor.fetch(xvalue = 1, deltaMarker = repcap.DeltaMarker.Default) \n
		Uses the markers 1 and 2 with relative values on the power monitor trace. \n
		Suppressed linked return values: reliability \n
			:param xvalue: X-value of the marker position relative to the x-value of the reference marker (in slots)
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Dmarker')
			:return: yvalue: Y-value of the marker position relative to the y-value of the reference marker"""
		param = Conversions.decimal_value_to_str(xvalue)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:NRSub:MEASurement<Instance>:MEValuation:DMARker{deltaMarker_cmd_val}:PMONitor? {param}', suppressed)
		return Conversions.str_to_float(response)
