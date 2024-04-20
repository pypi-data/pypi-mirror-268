from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentCls:
	"""Current commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:NRSub:MEASurement<Instance>:SRS:TRACe:PERRor:CURRent \n
		Snippet: value: List[float] = driver.nrSubMeas.srs.trace.perror.current.read() \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:return: results: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:NRSub:MEASurement<Instance>:SRS:TRACe:PERRor:CURRent?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:SRS:TRACe:PERRor:CURRent \n
		Snippet: value: List[float] = driver.nrSubMeas.srs.trace.perror.current.fetch() \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:return: results: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NRSub:MEASurement<Instance>:SRS:TRACe:PERRor:CURRent?', suppressed)
		return response
