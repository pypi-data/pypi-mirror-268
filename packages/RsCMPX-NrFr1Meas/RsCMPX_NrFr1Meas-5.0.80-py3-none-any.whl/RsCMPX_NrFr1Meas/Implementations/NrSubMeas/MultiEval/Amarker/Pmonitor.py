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

	def fetch(self, xvalue: int, absoluteMarker=repcap.AbsoluteMarker.Default) -> float:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:MEValuation:AMARker<No>:PMONitor \n
		Snippet: value: float = driver.nrSubMeas.multiEval.amarker.pmonitor.fetch(xvalue = 1, absoluteMarker = repcap.AbsoluteMarker.Default) \n
		Uses the markers 1 and 2 with absolute values on the power monitor trace. \n
		Suppressed linked return values: reliability \n
			:param xvalue: Absolute x-value of the marker position (slot number)
			:param absoluteMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Amarker')
			:return: yvalue: Absolute y-value of the marker position"""
		param = Conversions.decimal_value_to_str(xvalue)
		absoluteMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(absoluteMarker, repcap.AbsoluteMarker)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:NRSub:MEASurement<Instance>:MEValuation:AMARker{absoluteMarker_cmd_val}:PMONitor? {param}', suppressed)
		return Conversions.str_to_float(response)
