#!python3
import irsdk
import json
import logging
from logging.handlers import RotatingFileHandler
import os
import requests
import time

#create logging rates for each category in seconds
#camera_sleep = 30
#compute_sleep = 10
#environment_sleep = 10
#race_sleep = 5
#track_sleep = 1
#vehicle_sleep = 1


if not os.path.exists('C:/iracing_telemetry'):
    os.mkdir('C:/iracing_telemetry')
if not os.path.exists('C:/iracing_telemetry/app'):
    os.mkdir('C:/iracing_telemetry/app')
if not os.path.exists('C:/iracing_telemetry/data'):
    os.mkdir('C:/iracing_telemetry/data')


#set path to store log files
data_path = 'C:/iracing_telemetry/data/json.log'
app_path = 'C:/iracing_telemetry/app/json.log'

# create dict for values of txt from github pyirsdk repo
mydict = {
    'AirDensity': '',
    'AirPressure': '',
    'AirTemp': '',
    'Brake': '',
    'BrakeRaw': '',
    'CamCameraNumber': '',
    'CamCameraState': '',
    'CamCarIdx': '',
    'CamGroupNumber': '',
    'CarIdxBestLapNum': '',
    'CarIdxBestLapTime': '',
    'CarIdxClassPosition': '',
    'CarIdxEstTime': '',
    'CarIdxF2Time': '',
    'CarIdxGear': '',
    'CarIdxLap': '',
    'CarIdxLapCompleted': '',
    'CarIdxLapDistPct': '',
    'CarIdxLastLapTime': '',
    'CarIdxOnPitRoad': '',
    'CarIdxP2P_Count': '',
    'CarIdxP2P_Status': '',
    'CarIdxPaceFlags': '',
    'CarIdxPaceLine': '',
    'CarIdxPaceRow': '',
    'CarIdxPosition': '',
    'CarIdxRPM': '',
    'CarIdxSteer': '',
    'CarIdxTrackSurface': '',
    'CarIdxTrackSurfaceMaterial': '',
    'CarLeftRight': '',
    'Clutch': '',
    'CpuUsageBG': '',
    'DCDriversSoFar': '',
    'DCLapStatus': '',
    'dcStarter': '',
    'DisplayUnits': '',
    'dpFastRepair': '',
    'dpFuelAddKg': '',
    'dpFuelFill': '',
    'dpLFTireChange': '',
    'dpLFTireColdPress': '',
    'dpLRTireChange': '',
    'dpLRTireColdPress': '',
    'dpRFTireChange': '',
    'dpRFTireColdPress': '',
    'dpRRTireChange': '',
    'dpRRTireColdPress': '',
    'dpWindshieldTearoff': '',
    'DriverMarker': '',
    'EngineWarnings': '',
    'EnterExitReset': '',
    'FastRepairAvailable': '',
    'FastRepairUsed': '',
    'FogLevel': '',
    'FrameRate': '',
    'FrontTireSetsAvailable': '',
    'FrontTireSetsUsed': '',
    'FuelLevel': '',
    'FuelLevelPct': '',
    'FuelPress': '',
    'FuelUsePerHour': '',
    'Gear': '',
    'HandbrakeRaw': '',
    'IsDiskLoggingActive': '',
    'IsDiskLoggingEnabled': '',
    'IsInGarage': '',
    'IsOnTrack': '',
    'IsOnTrackCar': '',
    'IsReplayPlaying': '',
    'Lap': '',
    'LapBestLap': '',
    'LapBestLapTime': '',
    'LapBestNLapLap': '',
    'LapBestNLapTime': '',
    'LapCompleted': '',
    'LapCurrentLapTime': '',
    'LapDeltaToBestLap': '',
    'LapDeltaToBestLap_DD': '',
    'LapDeltaToBestLap_OK': '',
    'LapDeltaToOptimalLap': '',
    'LapDeltaToOptimalLap_DD': '',
    'LapDeltaToOptimalLap_OK': '',
    'LapDeltaToSessionBestLap': '',
    'LapDeltaToSessionBestLap_DD': '',
    'LapDeltaToSessionBestLap_OK': '',
    'LapDeltaToSessionLastlLap': '',
    'LapDeltaToSessionLastlLap_DD': '',
    'LapDeltaToSessionLastlLap_OK': '',
    'LapDeltaToSessionOptimalLap': '',
    'LapDeltaToSessionOptimalLap_DD': '',
    'LapDeltaToSessionOptimalLap_OK': '',
    'LapDist': '',
    'LapDistPct': '',
    'LapLasNLapSeq': '',
    'LapLastLapTime': '',
    'LapLastNLapTime': '',
    'LatAccel': '',
    'LatAccel_ST': '',
    'LeftTireSetsAvailable': '',
    'LeftTireSetsUsed': '',
    'LFbrakeLinePress': '',
    'LFcoldPressure': '',
    'LFshockDefl': '',
    'LFshockDefl_ST': '',
    'LFshockVel': '',
    'LFshockVel_ST': '',
    'LFtempCL': '',
    'LFtempCM': '',
    'LFtempCR': '',
    'LFTiresAvailable': '',
    'LFTiresUsed': '',
    'LFwearL': '',
    'LFwearM': '',
    'LFwearR': '',
    'LoadNumTextures': '',
    'LongAccel': '',
    'LongAccel_ST': '',
    'LRbrakeLinePress': '',
    'LRcoldPressure': '',
    'LRshockDefl': '',
    'LRshockDefl_ST': '',
    'LRshockVel': '',
    'LRshockVel_ST': '',
    'LRtempCL': '',
    'LRtempCM': '',
    'LRtempCR': '',
    'LRTiresAvailable': '',
    'LRTiresUsed': '',
    'LRwearL': '',
    'LRwearM': '',
    'LRwearR': '',
    'ManifoldPress': '',
    'ManualBoost': '',
    'ManualNoBoost': '',
    'OilLevel': '',
    'OilPress': '',
    'OilTemp': '',
    'OkToReloadTextures': '',
    'OnPitRoad': '',
    'PaceMode': '',
    'Pitch': '',
    'PitchRate': '',
    'PitchRate_ST': '',
    'PitOptRepairLeft': '',
    'PitRepairLeft': '',
    'PitsOpen': '',
    'PitstopActive': '',
    'PitSvFlags': '',
    'PitSvFuel': '',
    'PitSvLFP': '',
    'PitSvLRP': '',
    'PitSvRFP': '',
    'PitSvRRP': '',
    'PlayerCarClassPosition': '',
    'PlayerCarDriverIncidentCount': '',
    'PlayerCarDryTireSetLimit': '',
    'PlayerCarIdx': '',
    'PlayerCarInPitStall': '',
    'PlayerCarMyIncidentCount': '',
    'PlayerCarPitSvStatus': '',
    'PlayerCarPosition': '',
    'PlayerCarPowerAdjust': '',
    'PlayerCarTeamIncidentCount': '',
    'PlayerCarTowTime': '',
    'PlayerCarWeightPenalty': '',
    'PlayerTrackSurface': '',
    'PlayerTrackSurfaceMaterial': '',
    'PushToPass': '',
    'RaceLaps': '',
    'RadioTransmitCarIdx': '',
    'RadioTransmitFrequencyIdx': '',
    'RadioTransmitRadioIdx': '',
    'RearTireSetsAvailable': '',
    'RearTireSetsUsed': '',
    'RelativeHumidity': '',
    'ReplayFrameNum': '',
    'ReplayFrameNumEnd': '',
    'ReplayPlaySlowMotion': '',
    'ReplayPlaySpeed': '',
    'ReplaySessionNum': '',
    'ReplaySessionTime': '',
    'RFbrakeLinePress': '',
    'RFcoldPressure': '',
    'RFshockDefl': '',
    'RFshockDefl_ST': '',
    'RFshockVel': '',
    'RFshockVel_ST': '',
    'RFtempCL': '',
    'RFtempCM': '',
    'RFtempCR': '',
    'RFTiresAvailable': '',
    'RFTiresUsed': '',
    'RFwearL': '',
    'RFwearM': '',
    'RFwearR': '',
    'RightTireSetsAvailable': '',
    'RightTireSetsUsed': '',
    'Roll': '',
    'RollRate': '',
    'RollRate_ST': '',
    'RPM': '',
    'RRbrakeLinePress': '',
    'RRcoldPressure': '',
    'RRshockDefl': '',
    'RRshockDefl_ST': '',
    'RRshockVel': '',
    'RRshockVel_ST': '',
    'RRtempCL': '',
    'RRtempCM': '',
    'RRtempCR': '',
    'RRTiresAvailable': '',
    'RRTiresUsed': '',
    'RRwearL': '',
    'RRwearM': '',
    'RRwearR': '',
    'SessionFlags': '',
    'SessionLapsRemain': '',
    'SessionLapsRemainEx': '',
    'SessionNum': '',
    'SessionState': '',
    'SessionTick': '',
    'SessionTime': '',
    'SessionTimeOfDay': '',
    'SessionTimeRemain': '',
    'SessionUniqueID': '',
    'ShiftGrindRPM': '',
    'ShiftIndicatorPct': '',
    'ShiftPowerPct': '',
    'Skies': '',
    'Speed': '',
    'SteeringWheelAngle': '',
    'SteeringWheelAngleMax': '',
    'SteeringWheelPctDamper': '',
    'SteeringWheelPctTorque': '',
    'SteeringWheelPctTorqueSign': '',
    'SteeringWheelPctTorqueSignStops': '',
    'SteeringWheelPeakForceNm': '',
    'SteeringWheelTorque': '',
    'SteeringWheelTorque_ST': '',
    'Throttle': '',
    'ThrottleRaw': '',
    'TireLF_RumblePitch': '',
    'TireLR_RumblePitch': '',
    'TireRF_RumblePitch': '',
    'TireRR_RumblePitch': '',
    'TireSetsAvailable': '',
    'TireSetsUsed': '',
    'TrackTemp': '',
    'TrackTempCrew': '',
    'VelocityX': '',
    'VelocityX_ST': '',
    'VelocityY': '',
    'VelocityY_ST': '',
    'VelocityZ': '',
    'VelocityZ_ST': '',
    'VertAccel': '',
    'VertAccel_ST': '',
    'Voltage': '',
    'WaterLevel': '',
    'WaterTemp': '',
    'WeatherType': '',
    'WindDir': '',
    'WindVel': '',
    'Yaw': '',
    'YawNorth': '',
    'YawRate': '',
    'YawRate_ST': '',
}

camera_dict = {
    'CamCameraNumber': '',
    'CamCameraState': '',
    'CamCarIdx': '',
    'CamGroupNumber': '',
    'ReplayFrameNum': '',
    'ReplayFrameNumEnd': '',
    'ReplayPlaySlowMotion': '',
    'ReplayPlaySpeed': '',
    'ReplaySessionNum': '',
    'ReplaySessionTime': '',
}

compute_dict = {
    'CpuUsageBG': '',
    'FrameRate': '',
    'IsDiskLoggingActive': '',
    'IsDiskLoggingEnabled': '',
    'IsReplayPlaying': '',
    'LoadNumTextures': '',
    'OkToReloadTextures': '',
    'SessionNum': '',
    'SessionState': '',
    'SessionTick': '',
    'SessionTime': '',
    'SessionUniqueID': '',
}

environment_dict = {
    'AirDensity': '',
    'AirPressure': '',
    'AirTemp': '',
    'FogLevel': '',
    'PlayerTrackSurface': '',
    'PlayerTrackSurfaceMaterial': '',
    'RelativeHumidity': '',
    'SessionTimeOfDay': '',
    'Skies': '',
    'TrackTempCrew': '',
    'WeatherType': '',
    'WindDir': '',
    'WindVel': '',
}

race_dict = {
    'CarIdxBestLapNum': '',
    'CarIdxBestLapTime': '',
    'CarIdxClassPosition': '',
    'CarIdxEstTime': '',
    'CarIdxF2Time': '',
    'CarIdxLap': '',
    'CarIdxLapCompleted': '',
    'CarIdxLapDistPct': '',
    'CarIdxLastLapTime': '',
    'CarIdxOnPitRoad': '',
    'CarIdxP2P_Count': '',
    'CarIdxP2P_Status': '',
    'CarIdxPaceFlags': '',
    'CarIdxPaceLine': '',
    'CarIdxPaceRow': '',
    'CarIdxPosition': '',
    'CarLeftRight': '',
    'DCDriversSoFar': '',
    'DCLapStatus': '',
    'DisplayUnits': '',
    'dpFastRepair': '',
    'dpFuelAddKg': '',
    'dpFuelFill': '',
    'dpLFTireChange': '',
    'dpLFTireColdPress': '',
    'dpLRTireChange': '',
    'dpLRTireColdPress': '',
    'dpRFTireChange': '',
    'dpRFTireColdPress': '',
    'dpRRTireChange': '',
    'dpRRTireColdPress': '',
    'dpWindshieldTearoff': '',
    'DriverMarker': '',
    'EnterExitReset': '',
    'FastRepairAvailable': '',
    'FastRepairUsed': '',
    'FrontTireSetsAvailable': '',
    'FrontTireSetsUsed': '',
    'IsInGarage': '',
    'IsOnTrack': '',
    'IsOnTrackCar': '',
    'Lap': '',
    'LapBestLap': '',
    'LapBestLapTime': '',
    'LapBestNLapLap': '',
    'LapBestNLapTime': '',
    'LapCompleted': '',
    'LapCurrentLapTime': '',
    'LapDeltaToBestLap': '',
    'LapDeltaToBestLap_DD': '',
    'LapDeltaToBestLap_OK': '',
    'LapDeltaToOptimalLap': '',
    'LapDeltaToOptimalLap_DD': '',
    'LapDeltaToOptimalLap_OK': '',
    'LapDeltaToSessionBestLap': '',
    'LapDeltaToSessionBestLap_DD': '',
    'LapDeltaToSessionBestLap_OK': '',
    'LapDeltaToSessionLastlLap': '',
    'LapDeltaToSessionLastlLap_DD': '',
    'LapDeltaToSessionLastlLap_OK': '',
    'LapDeltaToSessionOptimalLap': '',
    'LapDeltaToSessionOptimalLap_DD': '',
    'LapDeltaToSessionOptimalLap_OK': '',
    'LapDist': '',
    'LapDistPct': '',
    'LapLasNLapSeq': '',
    'LapLastLapTime': '',
    'LapLastNLapTime': '',
    'LeftTireSetsAvailable': '',
    'LeftTireSetsUsed': '',
    'LFTiresAvailable': '',
    'LFTiresUsed': '',
    'LRTiresAvailable': '',
    'LRTiresUsed': '',
    'OnPitRoad': '',
    'PaceMode': '',
    'PitOptRepairLeft': '',
    'PitRepairLeft': '',
    'PitsOpen': '',
    'PitstopActive': '',
    'PitSvFlags': '',
    'PitSvFuel': '',
    'PitSvLFP': '',
    'PitSvLRP': '',
    'PitSvRFP': '',
    'PitSvRRP': '',
    'PlayerCarClassPosition': '',
    'PlayerCarDriverIncidentCount': '',
    'PlayerCarIdx': '',
    'PlayerCarInPitStall': '',
    'PlayerCarMyIncidentCount': '',
    'PlayerCarPitSvStatus': '',
    'PlayerCarPosition': '',
    'PlayerCarTeamIncidentCount': '',
    'PlayerCarTowTime': '',
    'PlayerCarWeightPenalty': '',
    'PushToPass': '',
    'RaceLaps': '',
    'RadioTransmitCarIdx': '',
    'RadioTransmitFrequencyIdx': '',
    'RadioTransmitRadioIdx': '',
    'RearTireSetsAvailable': '',
    'RearTireSetsUsed': '',
    'RFTiresAvailable': '',
    'RFTiresUsed': '',
    'RightTireSetsAvailable': '',
    'RightTireSetsUsed': '',
    'RRTiresAvailable': '',
    'RRTiresUsed': '',
    'SessionFlags': '',
    'SessionLapsRemain': '',
    'SessionLapsRemainEx': '',
    'SessionTimeRemain': '',
    'TireSetsAvailable': '',
    'TireSetsUsed': '',
}

track_dict = {
    'CarIdxTrackSurface': '',
    'CarIdxTrackSurfaceMaterial': '',
}

vehicle_dict = {
    'Brake': '',
    'BrakeRaw': '',
    'CarIdxGear': '',
    'CarIdxRPM': '',
    'CarIdxSteer': '',
    'Clutch': '',
    'dcStarter': '',
    'EngineWarnings': '',
    'FuelLevel': '',
    'FuelLevelPct': '',
    'FuelPress': '',
    'FuelUsePerHour': '',
    'Gear': '',
    'HandbrakeRaw': '',
    'LatAccel': '',
    'LatAccel_ST': '',
    'LFbrakeLinePress': '',
    'LFcoldPressure': '',
    'LFshockDefl': '',
    'LFshockDefl_ST': '',
    'LFshockVel': '',
    'LFshockVel_ST': '',
    'LFtempCL': '',
    'LFtempCM': '',
    'LFtempCR': '',
    'LFwearL': '',
    'LFwearM': '',
    'LFwearR': '',
    'LongAccel': '',
    'LongAccel_ST': '',
    'LRbrakeLinePress': '',
    'LRcoldPressure': '',
    'LRshockDefl': '',
    'LRshockDefl_ST': '',
    'LRshockVel': '',
    'LRshockVel_ST': '',
    'LRtempCL': '',
    'LRtempCM': '',
    'LRtempCR': '',
    'LRwearL': '',
    'LRwearM': '',
    'LRwearR': '',
    'ManifoldPress': '',
    'ManualBoost': '',
    'ManualNoBoost': '',
    'OilLevel': '',
    'OilPress': '',
    'OilTemp': '',
    'Pitch': '',
    'PitchRate': '',
    'PitchRate_ST': '',
    'PlayerCarDryTireSetLimit': '',
    'PlayerCarPowerAdjust': '',
    'RFbrakeLinePress': '',
    'RFcoldPressure': '',
    'RFshockDefl': '',
    'RFshockDefl_ST': '',
    'RFshockVel': '',
    'RFshockVel_ST': '',
    'RFtempCL': '',
    'RFtempCM': '',
    'RFtempCR': '',
    'RFwearL': '',
    'RFwearM': '',
    'RFwearR': '',
    'Roll': '',
    'RollRate': '',
    'RollRate_ST': '',
    'RPM': '',
    'RRbrakeLinePress': '',
    'RRcoldPressure': '',
    'RRshockDefl': '',
    'RRshockDefl_ST': '',
    'RRshockVel': '',
    'RRshockVel_ST': '',
    'RRtempCL': '',
    'RRtempCM': '',
    'RRtempCR': '',
    'RRwearL': '',
    'RRwearM': '',
    'RRwearR': '',
    'ShiftGrindRPM': '',
    'ShiftPowerPct': '',
    'Speed': '',
    'SteeringWheelAngle': '',
    'SteeringWheelAngleMax': '',
    'SteeringWheelPctDamper': '',
    'SteeringWheelPctTorque': '',
    'SteeringWheelPctTorqueSign': '',
    'SteeringWheelPctTorqueSignStops': '',
    'SteeringWheelPeakForceNm': '',
    'SteeringWheelTorque': '',
    'SteeringWheelTorque_ST': '',
    'Throttle': '',
    'ThrottleRaw': '',
    'TireLF_RumblePitch': '',
    'TireLR_RumblePitch': '',
    'TireRF_RumblePitch': '',
    'TireRR_RumblePitch': '',
    'VelocityX': '',
    'VelocityX_ST': '',
    'VelocityY': '',
    'VelocityY_ST': '',
    'VelocityZ': '',
    'VelocityZ_ST': '',
    'VertAccel': '',
    'VertAccel_ST': '',
    'Voltage': '',
    'WaterLevel': '',
    'WaterTemp': '',
    'Yaw': '',
    'YawNorth': '',
    'YawRate': '',
    'YawRate_ST': '',
}

#configure logging rotation
data_logger = logging.getLogger("Rotating Data Log")
data_logger.setLevel(logging.INFO)
data_handler = RotatingFileHandler(data_path, maxBytes=15500, backupCount=10)
data_logger.addHandler(data_handler)

app_logger = logging.getLogger("Rotating App Log")
app_logger.setLevel(logging.INFO)
app_handler = RotatingFileHandler(app_path, maxBytes=15500, backupCount=10)
app_logger.addHandler(app_handler)

# this is our State class, with some helpful variables
class State:
    ir_connected = False
    last_car_setup_tick = -1

# here we check if we are connected to iracing
# so we can retrieve some data
def check_iracing():
    if state.ir_connected and not (ir.is_initialized and ir.is_connected):
        state.ir_connected = False
        # don't forget to reset your State variables
        state.last_car_setup_tick = -1
        # we are shutting down ir library (clearing all internal variables)
        ir.shutdown()
        app_logger.info(time.ctime() + ' irsdk disconnected')
    elif not state.ir_connected and ir.startup() and ir.is_initialized and ir.is_connected:
        state.ir_connected = True
        app_logger.info(time.ctime() + ' irsdk connected')

#build loop to poll through dictionary of key value pairs & dump to json payload
# def loop():
#     for key, value in mydict.items():
#         value = ir[key]
#         mydict.update({key: value})
#     data_logger.info(json.dumps(mydict))
#     print("logged")
#     # add sleep timer from variable we put at top

def camera_loop():
    for key, value in camera_dict.items():
        value = ir[key]
        camera_dict.update({key: value})
    data_logger.info(json.dumps(camera_dict))
    app_logger.info(time.ctime() + " camera_dict: logged")
    #time.sleep(camera_sleep)

def compute_loop():
    for key, value in compute_dict.items():
        value = ir[key]
        compute_dict.update({key: value})
    data_logger.info(json.dumps(compute_dict))
    app_logger.info(time.ctime() + " compute_dict: logged")
    #time.sleep(compute_sleep)

def environment_loop():
    for key, value in environment_dict.items():
        value = ir[key]
        environment_dict.update({key: value})
    data_logger.info(json.dumps(environment_dict))
    app_logger.info(time.ctime() + " environment_dict: logged")
    #time.sleep(environment_sleep)

def race_loop():
    for key, value in race_dict.items():
        value = ir[key]
        race_dict.update({key: value})
    data_logger.info(json.dumps(race_dict))
    app_logger.info(time.ctime() + " race_dict: logged")
    #time.sleep(race_sleep)

def track_loop():
    for key, value in track_dict.items():
        value = ir[key]
        track_dict.update({key: value})
    data_logger.info(json.dumps(track_dict))
    app_logger.info(time.ctime() + " track_dict: logged")
    #time.sleep(track_sleep)

def vehicle_loop():
    for key, value in vehicle_dict.items():
        value = ir[key]
        vehicle_dict.update({key: value})
    data_logger.info(json.dumps(vehicle_dict))
    app_logger.info(time.ctime() + " vehicle_dict: logged")
    #time.sleep(vehicle_sleep)

if __name__ == '__main__':
    # initializing ir and state
    ir = irsdk.IRSDK()
    state = State()

    try:
        # infinite loop
        while True:
            # check if we are connected to iracing
            check_iracing()
            # if we are, then process data
            if state.ir_connected:
                # loop()
                camera_loop()
                compute_loop()
                environment_loop()
                race_loop()
                track_loop()
                vehicle_loop()
                #vehicle_loop(), etc
            # sleep for 1 second
            # maximum you can use is 1/60
            # cause iracing updates data with 60 fps
            time.sleep(1)
    except KeyboardInterrupt:
        # press ctrl+c to exit
        pass
    
