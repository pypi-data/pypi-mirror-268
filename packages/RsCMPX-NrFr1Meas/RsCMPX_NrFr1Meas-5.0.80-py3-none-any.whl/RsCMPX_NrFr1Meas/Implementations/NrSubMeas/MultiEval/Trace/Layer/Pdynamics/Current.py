from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def read(self, layer=repcap.Layer.Default) -> List[float]:
		"""SCPI: READ:NRSub:MEASurement<Instance>:MEValuation:TRACe[:LAYer<layer>]:PDYNamics:CURRent \n
		Snippet: value: List[float] = driver.nrSubMeas.multiEval.trace.layer.pdynamics.current.read(layer = repcap.Layer.Default) \n
		Return the values of the power dynamics traces. Each value is sampled with 48 Ts, corresponding to 1.5625 µs. The results
		of the current, average and maximum traces can be retrieved. The OFF power sections refer to antenna <l>. The ON power
		section refers to the sum of both antenna signals. See also 'Square Power Dynamics'. \n
		Suppressed linked return values: reliability \n
			:param layer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Layer')
			:return: power: 2048 power values, from -1100 µs to +2098.4375 µs relative to the start of the measured active slot. The values have a spacing of 1.5625 µs. The 705th value is at the start of the slot (0 µs) ."""
		layer_cmd_val = self._cmd_group.get_repcap_cmd_value(layer, repcap.Layer)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:NRSub:MEASurement<Instance>:MEValuation:TRACe:LAYer{layer_cmd_val}:PDYNamics:CURRent?', suppressed)
		return response

	def fetch(self, layer=repcap.Layer.Default) -> List[float]:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:MEValuation:TRACe[:LAYer<layer>]:PDYNamics:CURRent \n
		Snippet: value: List[float] = driver.nrSubMeas.multiEval.trace.layer.pdynamics.current.fetch(layer = repcap.Layer.Default) \n
		Return the values of the power dynamics traces. Each value is sampled with 48 Ts, corresponding to 1.5625 µs. The results
		of the current, average and maximum traces can be retrieved. The OFF power sections refer to antenna <l>. The ON power
		section refers to the sum of both antenna signals. See also 'Square Power Dynamics'. \n
		Suppressed linked return values: reliability \n
			:param layer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Layer')
			:return: power: 2048 power values, from -1100 µs to +2098.4375 µs relative to the start of the measured active slot. The values have a spacing of 1.5625 µs. The 705th value is at the start of the slot (0 µs) ."""
		layer_cmd_val = self._cmd_group.get_repcap_cmd_value(layer, repcap.Layer)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NRSub:MEASurement<Instance>:MEValuation:TRACe:LAYer{layer_cmd_val}:PDYNamics:CURRent?', suppressed)
		return response
