from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PvSymbolCls:
	"""PvSymbol commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pvSymbol", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:NRSub:MEASurement<Instance>:SRS:TRACe:PVSYmbol \n
		Snippet: value: List[float] = driver.nrSubMeas.srs.trace.pvSymbol.read() \n
		Return the values of the power vs symbol trace. See also 'Square Power vs Symbol'. \n
		Suppressed linked return values: reliability \n
			:return: power: Comma-separated list of power values, one value per symbol. The number of symbols depends on the SCS and on the configured number of subframes."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:NRSub:MEASurement<Instance>:SRS:TRACe:PVSYmbol?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:SRS:TRACe:PVSYmbol \n
		Snippet: value: List[float] = driver.nrSubMeas.srs.trace.pvSymbol.fetch() \n
		Return the values of the power vs symbol trace. See also 'Square Power vs Symbol'. \n
		Suppressed linked return values: reliability \n
			:return: power: Comma-separated list of power values, one value per symbol. The number of symbols depends on the SCS and on the configured number of subframes."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NRSub:MEASurement<Instance>:SRS:TRACe:PVSYmbol?', suppressed)
		return response
