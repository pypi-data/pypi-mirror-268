from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PmonitorCls:
	"""Pmonitor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmonitor", core, parent)

	def fetch(self, xvalue: int) -> float:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:MEValuation:REFMarker:PMONitor \n
		Snippet: value: float = driver.nrSubMeas.multiEval.referenceMarker.pmonitor.fetch(xvalue = 1) \n
		Uses the reference marker on the power monitor trace. \n
		Suppressed linked return values: reliability \n
			:param xvalue: Absolute x-value of the marker position (slot number)
			:return: yvalue: Absolute y-value of the marker position"""
		param = Conversions.decimal_value_to_str(xvalue)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:NRSub:MEASurement<Instance>:MEValuation:REFMarker:PMONitor? {param}', suppressed)
		return Conversions.str_to_float(response)
