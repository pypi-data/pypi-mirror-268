from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEvalCls:
	"""MultiEval commands group definition. 7 total commands, 0 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiEval", core, parent)

	def get_threshold(self) -> float or bool:
		"""SCPI: TRIGger:NRSub:MEASurement<Instance>:MEValuation:THReshold \n
		Snippet: value: float or bool = driver.trigger.nrSubMeas.multiEval.get_threshold() \n
		Defines the trigger threshold for power trigger sources. \n
			:return: trig_threshold: (float or boolean) No help available
		"""
		response = self._core.io.query_str('TRIGger:NRSub:MEASurement<Instance>:MEValuation:THReshold?')
		return Conversions.str_to_float_or_bool(response)

	def set_threshold(self, trig_threshold: float or bool) -> None:
		"""SCPI: TRIGger:NRSub:MEASurement<Instance>:MEValuation:THReshold \n
		Snippet: driver.trigger.nrSubMeas.multiEval.set_threshold(trig_threshold = 1.0) \n
		Defines the trigger threshold for power trigger sources. \n
			:param trig_threshold: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(trig_threshold)
		self._core.io.write(f'TRIGger:NRSub:MEASurement<Instance>:MEValuation:THReshold {param}')

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.SignalSlope:
		"""SCPI: TRIGger:NRSub:MEASurement<Instance>:MEValuation:SLOPe \n
		Snippet: value: enums.SignalSlope = driver.trigger.nrSubMeas.multiEval.get_slope() \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:return: slope: REDGe: Rising edge FEDGe: Falling edge
		"""
		response = self._core.io.query_str('TRIGger:NRSub:MEASurement<Instance>:MEValuation:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SignalSlope)

	def set_slope(self, slope: enums.SignalSlope) -> None:
		"""SCPI: TRIGger:NRSub:MEASurement<Instance>:MEValuation:SLOPe \n
		Snippet: driver.trigger.nrSubMeas.multiEval.set_slope(slope = enums.SignalSlope.FEDGe) \n
		Qualifies whether the trigger event is generated at the rising or at the falling edge of the trigger pulse (valid for
		external and power trigger sources) . \n
			:param slope: REDGe: Rising edge FEDGe: Falling edge
		"""
		param = Conversions.enum_scalar_to_str(slope, enums.SignalSlope)
		self._core.io.write(f'TRIGger:NRSub:MEASurement<Instance>:MEValuation:SLOPe {param}')

	def get_delay(self) -> float:
		"""SCPI: TRIGger:NRSub:MEASurement<Instance>:MEValuation:DELay \n
		Snippet: value: float = driver.trigger.nrSubMeas.multiEval.get_delay() \n
		Defines a time delaying the start of the measurement relative to the trigger event. This setting has no influence on free
		run measurements. \n
			:return: delay: No help available
		"""
		response = self._core.io.query_str('TRIGger:NRSub:MEASurement<Instance>:MEValuation:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: TRIGger:NRSub:MEASurement<Instance>:MEValuation:DELay \n
		Snippet: driver.trigger.nrSubMeas.multiEval.set_delay(delay = 1.0) \n
		Defines a time delaying the start of the measurement relative to the trigger event. This setting has no influence on free
		run measurements. \n
			:param delay: No help available
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'TRIGger:NRSub:MEASurement<Instance>:MEValuation:DELay {param}')

	def get_timeout(self) -> float or bool:
		"""SCPI: TRIGger:NRSub:MEASurement<Instance>:MEValuation:TOUT \n
		Snippet: value: float or bool = driver.trigger.nrSubMeas.multiEval.get_timeout() \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on Free Run measurements. \n
			:return: trigger_timeout: (float or boolean) No help available
		"""
		response = self._core.io.query_str('TRIGger:NRSub:MEASurement<Instance>:MEValuation:TOUT?')
		return Conversions.str_to_float_or_bool(response)

	def set_timeout(self, trigger_timeout: float or bool) -> None:
		"""SCPI: TRIGger:NRSub:MEASurement<Instance>:MEValuation:TOUT \n
		Snippet: driver.trigger.nrSubMeas.multiEval.set_timeout(trigger_timeout = 1.0) \n
		Selects the maximum time that the measurement waits for a trigger event before it stops in remote control mode or
		indicates a trigger timeout in manual operation mode. This setting has no influence on Free Run measurements. \n
			:param trigger_timeout: (float or boolean) No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(trigger_timeout)
		self._core.io.write(f'TRIGger:NRSub:MEASurement<Instance>:MEValuation:TOUT {param}')

	def get_mgap(self) -> float:
		"""SCPI: TRIGger:NRSub:MEASurement<Instance>:MEValuation:MGAP \n
		Snippet: value: float = driver.trigger.nrSubMeas.multiEval.get_mgap() \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:return: min_trig_gap: No help available
		"""
		response = self._core.io.query_str('TRIGger:NRSub:MEASurement<Instance>:MEValuation:MGAP?')
		return Conversions.str_to_float(response)

	def set_mgap(self, min_trig_gap: float) -> None:
		"""SCPI: TRIGger:NRSub:MEASurement<Instance>:MEValuation:MGAP \n
		Snippet: driver.trigger.nrSubMeas.multiEval.set_mgap(min_trig_gap = 1.0) \n
		Sets a minimum time during which the IF signal must be below the trigger threshold before the trigger is armed so that an
		IF power trigger event can be generated. \n
			:param min_trig_gap: No help available
		"""
		param = Conversions.decimal_value_to_str(min_trig_gap)
		self._core.io.write(f'TRIGger:NRSub:MEASurement<Instance>:MEValuation:MGAP {param}')

	# noinspection PyTypeChecker
	def get_smode(self) -> enums.SyncMode:
		"""SCPI: TRIGger:NRSub:MEASurement<Instance>:MEValuation:SMODe \n
		Snippet: value: enums.SyncMode = driver.trigger.nrSubMeas.multiEval.get_smode() \n
		Selects the size of the search window for synchronization. \n
			:return: sync_mode: Normal, enhanced, normal single slot, enhanced single slot
		"""
		response = self._core.io.query_str('TRIGger:NRSub:MEASurement<Instance>:MEValuation:SMODe?')
		return Conversions.str_to_scalar_enum(response, enums.SyncMode)

	def set_smode(self, sync_mode: enums.SyncMode) -> None:
		"""SCPI: TRIGger:NRSub:MEASurement<Instance>:MEValuation:SMODe \n
		Snippet: driver.trigger.nrSubMeas.multiEval.set_smode(sync_mode = enums.SyncMode.ENHanced) \n
		Selects the size of the search window for synchronization. \n
			:param sync_mode: Normal, enhanced, normal single slot, enhanced single slot
		"""
		param = Conversions.enum_scalar_to_str(sync_mode, enums.SyncMode)
		self._core.io.write(f'TRIGger:NRSub:MEASurement<Instance>:MEValuation:SMODe {param}')

	def get_fsync(self) -> bool:
		"""SCPI: TRIGger:NRSub:MEASurement<Instance>:MEValuation:FSYNc \n
		Snippet: value: bool = driver.trigger.nrSubMeas.multiEval.get_fsync() \n
		Enables frame synchronization for 'Free Run (Fast Sync) ' and 'IF Power'. \n
			:return: frame_sync: OFF: slot synchronization ON: frame synchronization
		"""
		response = self._core.io.query_str('TRIGger:NRSub:MEASurement<Instance>:MEValuation:FSYNc?')
		return Conversions.str_to_bool(response)

	def set_fsync(self, frame_sync: bool) -> None:
		"""SCPI: TRIGger:NRSub:MEASurement<Instance>:MEValuation:FSYNc \n
		Snippet: driver.trigger.nrSubMeas.multiEval.set_fsync(frame_sync = False) \n
		Enables frame synchronization for 'Free Run (Fast Sync) ' and 'IF Power'. \n
			:param frame_sync: OFF: slot synchronization ON: frame synchronization
		"""
		param = Conversions.bool_to_str(frame_sync)
		self._core.io.write(f'TRIGger:NRSub:MEASurement<Instance>:MEValuation:FSYNc {param}')
