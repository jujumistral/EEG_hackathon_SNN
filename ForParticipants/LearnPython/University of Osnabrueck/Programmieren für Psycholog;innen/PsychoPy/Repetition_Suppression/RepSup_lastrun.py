#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on August 04, 2025, at 12:55
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware, parallel
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'RepSup'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1536, 960]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s' % (expInfo['participant'], expName)
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\sebas\\Documents\\PsychoPy\\Repetition_Suppression\\RepSup_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('IntroResponse') is None:
        # initialise IntroResponse
        IntroResponse = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='IntroResponse',
        )
    if deviceManager.getDevice('OutroResponse') is None:
        # initialise OutroResponse
        OutroResponse = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='OutroResponse',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Fragen" ---
    FragenSagehorn = visual.TextStim(win=win, name='FragenSagehorn',
        text='Sehr geehrte Frau Sagehorn,\nich habe ein paar Fragen dazu - insbesondere danach ob meine Umsetzung korrekt ist - bei mir bricht das Programm mit der unten stehenden Meldung ab - nach meinem Verständnis fehlt hier nur der EEG-Port - somit kann ich aber auch nicht weiter prüfen.\nMeine Zusammenstellung:\n- der Ordner wie beschrieben \n- in "lists" das .py Dokument was wir zusammen in der Einheit erarbeitet hatten\n- in "stimuli" die 240 Bilddateien\n- "data" ist leer\n\nZudem wird jedes Mal wenn ich das Experiment starte, eine randomisierte VP-Nummer angezeigt. Ich kann diese immer ändern, also es ist kein Problem, aber ich frage mich ob das so sein soll?\n\nIch habe auch den folgenden Teil aus den Conditions beim Trial Loop entfernt "+ expInfo[\'participant\'] + \'.csv\'" - erst danach wurde bei mir der Pfad erkannt. Passt das so, oder muss ich etwas anpassen?\n\n\n6.4725     WARNING     psychopy.parallel has been imported but no parallel port driver found. Install either inpout32, inpoutx64 or dlportio\nTraceback (most recent call last):\n17.3870     WARNING     launchHubServer: If using the iohub mouse or eyetracker devices, fullScr should be True.\n  File "C:\\Users\\sebas\\Documents\\PsychoPy\\Repetition_Suppression\\RepSup_lastrun.py", line 1248, in <module>\n    run(\n  File "C:\\Users\\sebas\\Documents\\PsychoPy\\Repetition_Suppression\\RepSup_lastrun.py", line 404, in run\n    p_port = parallel.ParallelPort(address=\'0x0378\')\nTypeError: \'NoneType\' object is not callable\n2.2332     WARNING     Monitor specification not found. Creating a temporary one...\nioHub Server Process Completed With Code:  0\n################ Experiment ended with exit code 1 [pid:35932] #################',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "IntroRoutine" ---
    IntroText = visual.TextStim(win=win, name='IntroText',
        text='BlaBlaBla\n(spare ich mir, da nicht durchgeführt)',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    IntroResponse = keyboard.Keyboard(deviceName='IntroResponse')
    
    # --- Initialize components for Routine "TrialFixation" ---
    TrialFixationPoint = visual.ShapeStim(
        win=win, name='TrialFixationPoint',
        size=(0.5, 0.5), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "TrialRoutine" ---
    TrialImage = visual.ImageStim(
        win=win,
        name='TrialImage', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    p_port = parallel.ParallelPort(address='0x0378')
    
    # --- Initialize components for Routine "InterStimulusInterval" ---
    text = visual.TextStim(win=win, name='text',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "OutroRoutine" ---
    OutroText = visual.TextStim(win=win, name='OutroText',
        text="BlaBlaBla\n\nPress 'space' to exit the experiment.",
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    OutroResponse = keyboard.Keyboard(deviceName='OutroResponse')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "Fragen" ---
    # create an object to store info about Routine Fragen
    Fragen = data.Routine(
        name='Fragen',
        components=[FragenSagehorn],
    )
    Fragen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for Fragen
    Fragen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Fragen.tStart = globalClock.getTime(format='float')
    Fragen.status = STARTED
    thisExp.addData('Fragen.started', Fragen.tStart)
    Fragen.maxDuration = None
    # keep track of which components have finished
    FragenComponents = Fragen.components
    for thisComponent in Fragen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Fragen" ---
    Fragen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FragenSagehorn* updates
        
        # if FragenSagehorn is starting this frame...
        if FragenSagehorn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FragenSagehorn.frameNStart = frameN  # exact frame index
            FragenSagehorn.tStart = t  # local t and not account for scr refresh
            FragenSagehorn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FragenSagehorn, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'FragenSagehorn.started')
            # update status
            FragenSagehorn.status = STARTED
            FragenSagehorn.setAutoDraw(True)
        
        # if FragenSagehorn is active this frame...
        if FragenSagehorn.status == STARTED:
            # update params
            pass
        
        # if FragenSagehorn is stopping this frame...
        if FragenSagehorn.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FragenSagehorn.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                FragenSagehorn.tStop = t  # not accounting for scr refresh
                FragenSagehorn.tStopRefresh = tThisFlipGlobal  # on global time
                FragenSagehorn.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'FragenSagehorn.stopped')
                # update status
                FragenSagehorn.status = FINISHED
                FragenSagehorn.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            Fragen.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Fragen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Fragen" ---
    for thisComponent in Fragen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Fragen
    Fragen.tStop = globalClock.getTime(format='float')
    Fragen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Fragen.stopped', Fragen.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Fragen.maxDurationReached:
        routineTimer.addTime(-Fragen.maxDuration)
    elif Fragen.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "IntroRoutine" ---
    # create an object to store info about Routine IntroRoutine
    IntroRoutine = data.Routine(
        name='IntroRoutine',
        components=[IntroText, IntroResponse],
    )
    IntroRoutine.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for IntroResponse
    IntroResponse.keys = []
    IntroResponse.rt = []
    _IntroResponse_allKeys = []
    # store start times for IntroRoutine
    IntroRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    IntroRoutine.tStart = globalClock.getTime(format='float')
    IntroRoutine.status = STARTED
    thisExp.addData('IntroRoutine.started', IntroRoutine.tStart)
    IntroRoutine.maxDuration = None
    # keep track of which components have finished
    IntroRoutineComponents = IntroRoutine.components
    for thisComponent in IntroRoutine.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "IntroRoutine" ---
    IntroRoutine.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *IntroText* updates
        
        # if IntroText is starting this frame...
        if IntroText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IntroText.frameNStart = frameN  # exact frame index
            IntroText.tStart = t  # local t and not account for scr refresh
            IntroText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IntroText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IntroText.started')
            # update status
            IntroText.status = STARTED
            IntroText.setAutoDraw(True)
        
        # if IntroText is active this frame...
        if IntroText.status == STARTED:
            # update params
            pass
        
        # *IntroResponse* updates
        waitOnFlip = False
        
        # if IntroResponse is starting this frame...
        if IntroResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IntroResponse.frameNStart = frameN  # exact frame index
            IntroResponse.tStart = t  # local t and not account for scr refresh
            IntroResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IntroResponse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IntroResponse.started')
            # update status
            IntroResponse.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(IntroResponse.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(IntroResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if IntroResponse.status == STARTED and not waitOnFlip:
            theseKeys = IntroResponse.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _IntroResponse_allKeys.extend(theseKeys)
            if len(_IntroResponse_allKeys):
                IntroResponse.keys = _IntroResponse_allKeys[-1].name  # just the last key pressed
                IntroResponse.rt = _IntroResponse_allKeys[-1].rt
                IntroResponse.duration = _IntroResponse_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            IntroRoutine.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IntroRoutine.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "IntroRoutine" ---
    for thisComponent in IntroRoutine.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for IntroRoutine
    IntroRoutine.tStop = globalClock.getTime(format='float')
    IntroRoutine.tStopRefresh = tThisFlipGlobal
    thisExp.addData('IntroRoutine.stopped', IntroRoutine.tStop)
    # check responses
    if IntroResponse.keys in ['', [], None]:  # No response was made
        IntroResponse.keys = None
    thisExp.addData('IntroResponse.keys',IntroResponse.keys)
    if IntroResponse.keys != None:  # we had a response
        thisExp.addData('IntroResponse.rt', IntroResponse.rt)
        thisExp.addData('IntroResponse.duration', IntroResponse.duration)
    thisExp.nextEntry()
    # the Routine "IntroRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    TrialLoop = data.TrialHandler2(
        name='TrialLoop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('/Users/sebas/Documents/PsychoPy/Repetition_Suppression/lists/08_RS_Lists'), 
        seed=None, 
    )
    thisExp.addLoop(TrialLoop)  # add the loop to the experiment
    thisTrialLoop = TrialLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop.rgb)
    if thisTrialLoop != None:
        for paramName in thisTrialLoop:
            globals()[paramName] = thisTrialLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrialLoop in TrialLoop:
        currentLoop = TrialLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop.rgb)
        if thisTrialLoop != None:
            for paramName in thisTrialLoop:
                globals()[paramName] = thisTrialLoop[paramName]
        
        # --- Prepare to start Routine "TrialFixation" ---
        # create an object to store info about Routine TrialFixation
        TrialFixation = data.Routine(
            name='TrialFixation',
            components=[TrialFixationPoint],
        )
        TrialFixation.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for TrialFixation
        TrialFixation.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        TrialFixation.tStart = globalClock.getTime(format='float')
        TrialFixation.status = STARTED
        thisExp.addData('TrialFixation.started', TrialFixation.tStart)
        TrialFixation.maxDuration = None
        # keep track of which components have finished
        TrialFixationComponents = TrialFixation.components
        for thisComponent in TrialFixation.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TrialFixation" ---
        # if trial has changed, end Routine now
        if isinstance(TrialLoop, data.TrialHandler2) and thisTrialLoop.thisN != TrialLoop.thisTrial.thisN:
            continueRoutine = False
        TrialFixation.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TrialFixationPoint* updates
            
            # if TrialFixationPoint is starting this frame...
            if TrialFixationPoint.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialFixationPoint.frameNStart = frameN  # exact frame index
                TrialFixationPoint.tStart = t  # local t and not account for scr refresh
                TrialFixationPoint.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialFixationPoint, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TrialFixationPoint.started')
                # update status
                TrialFixationPoint.status = STARTED
                TrialFixationPoint.setAutoDraw(True)
            
            # if TrialFixationPoint is active this frame...
            if TrialFixationPoint.status == STARTED:
                # update params
                pass
            
            # if TrialFixationPoint is stopping this frame...
            if TrialFixationPoint.status == STARTED:
                if bool(fix_duration):
                    # keep track of stop time/frame for later
                    TrialFixationPoint.tStop = t  # not accounting for scr refresh
                    TrialFixationPoint.tStopRefresh = tThisFlipGlobal  # on global time
                    TrialFixationPoint.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'TrialFixationPoint.stopped')
                    # update status
                    TrialFixationPoint.status = FINISHED
                    TrialFixationPoint.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                TrialFixation.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TrialFixation.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TrialFixation" ---
        for thisComponent in TrialFixation.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for TrialFixation
        TrialFixation.tStop = globalClock.getTime(format='float')
        TrialFixation.tStopRefresh = tThisFlipGlobal
        thisExp.addData('TrialFixation.stopped', TrialFixation.tStop)
        # the Routine "TrialFixation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "TrialRoutine" ---
        # create an object to store info about Routine TrialRoutine
        TrialRoutine = data.Routine(
            name='TrialRoutine',
            components=[TrialImage, p_port],
        )
        TrialRoutine.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        TrialImage.setImage(imageFile)
        # store start times for TrialRoutine
        TrialRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        TrialRoutine.tStart = globalClock.getTime(format='float')
        TrialRoutine.status = STARTED
        thisExp.addData('TrialRoutine.started', TrialRoutine.tStart)
        TrialRoutine.maxDuration = None
        # keep track of which components have finished
        TrialRoutineComponents = TrialRoutine.components
        for thisComponent in TrialRoutine.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TrialRoutine" ---
        # if trial has changed, end Routine now
        if isinstance(TrialLoop, data.TrialHandler2) and thisTrialLoop.thisN != TrialLoop.thisTrial.thisN:
            continueRoutine = False
        TrialRoutine.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TrialImage* updates
            
            # if TrialImage is starting this frame...
            if TrialImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialImage.frameNStart = frameN  # exact frame index
                TrialImage.tStart = t  # local t and not account for scr refresh
                TrialImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialImage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TrialImage.started')
                # update status
                TrialImage.status = STARTED
                TrialImage.setAutoDraw(True)
            
            # if TrialImage is active this frame...
            if TrialImage.status == STARTED:
                # update params
                pass
            
            # if TrialImage is stopping this frame...
            if TrialImage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > TrialImage.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    TrialImage.tStop = t  # not accounting for scr refresh
                    TrialImage.tStopRefresh = tThisFlipGlobal  # on global time
                    TrialImage.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'TrialImage.stopped')
                    # update status
                    TrialImage.status = FINISHED
                    TrialImage.setAutoDraw(False)
            # *p_port* updates
            
            # if p_port is starting this frame...
            if p_port.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                p_port.frameNStart = frameN  # exact frame index
                p_port.tStart = t  # local t and not account for scr refresh
                p_port.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(p_port, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('p_port.started', t)
                # update status
                p_port.status = STARTED
                p_port.status = STARTED
                win.callOnFlip(p_port.setData, int(1))
            
            # if p_port is stopping this frame...
            if p_port.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > p_port.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    p_port.tStop = t  # not accounting for scr refresh
                    p_port.tStopRefresh = tThisFlipGlobal  # on global time
                    p_port.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('p_port.stopped', t)
                    # update status
                    p_port.status = FINISHED
                    win.callOnFlip(p_port.setData, int(0))
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                TrialRoutine.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TrialRoutine.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TrialRoutine" ---
        for thisComponent in TrialRoutine.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for TrialRoutine
        TrialRoutine.tStop = globalClock.getTime(format='float')
        TrialRoutine.tStopRefresh = tThisFlipGlobal
        thisExp.addData('TrialRoutine.stopped', TrialRoutine.tStop)
        if p_port.status == STARTED:
            win.callOnFlip(p_port.setData, int(0))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if TrialRoutine.maxDurationReached:
            routineTimer.addTime(-TrialRoutine.maxDuration)
        elif TrialRoutine.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # --- Prepare to start Routine "InterStimulusInterval" ---
        # create an object to store info about Routine InterStimulusInterval
        InterStimulusInterval = data.Routine(
            name='InterStimulusInterval',
            components=[text],
        )
        InterStimulusInterval.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for InterStimulusInterval
        InterStimulusInterval.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        InterStimulusInterval.tStart = globalClock.getTime(format='float')
        InterStimulusInterval.status = STARTED
        thisExp.addData('InterStimulusInterval.started', InterStimulusInterval.tStart)
        InterStimulusInterval.maxDuration = None
        # keep track of which components have finished
        InterStimulusIntervalComponents = InterStimulusInterval.components
        for thisComponent in InterStimulusInterval.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "InterStimulusInterval" ---
        # if trial has changed, end Routine now
        if isinstance(TrialLoop, data.TrialHandler2) and thisTrialLoop.thisN != TrialLoop.thisTrial.thisN:
            continueRoutine = False
        InterStimulusInterval.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # if text is stopping this frame...
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.tStopRefresh = tThisFlipGlobal  # on global time
                    text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.stopped')
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                InterStimulusInterval.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in InterStimulusInterval.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "InterStimulusInterval" ---
        for thisComponent in InterStimulusInterval.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for InterStimulusInterval
        InterStimulusInterval.tStop = globalClock.getTime(format='float')
        InterStimulusInterval.tStopRefresh = tThisFlipGlobal
        thisExp.addData('InterStimulusInterval.stopped', InterStimulusInterval.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if InterStimulusInterval.maxDurationReached:
            routineTimer.addTime(-InterStimulusInterval.maxDuration)
        elif InterStimulusInterval.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'TrialLoop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "OutroRoutine" ---
    # create an object to store info about Routine OutroRoutine
    OutroRoutine = data.Routine(
        name='OutroRoutine',
        components=[OutroText, OutroResponse],
    )
    OutroRoutine.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for OutroResponse
    OutroResponse.keys = []
    OutroResponse.rt = []
    _OutroResponse_allKeys = []
    # store start times for OutroRoutine
    OutroRoutine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    OutroRoutine.tStart = globalClock.getTime(format='float')
    OutroRoutine.status = STARTED
    thisExp.addData('OutroRoutine.started', OutroRoutine.tStart)
    OutroRoutine.maxDuration = None
    # keep track of which components have finished
    OutroRoutineComponents = OutroRoutine.components
    for thisComponent in OutroRoutine.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "OutroRoutine" ---
    OutroRoutine.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *OutroText* updates
        
        # if OutroText is starting this frame...
        if OutroText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            OutroText.frameNStart = frameN  # exact frame index
            OutroText.tStart = t  # local t and not account for scr refresh
            OutroText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(OutroText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'OutroText.started')
            # update status
            OutroText.status = STARTED
            OutroText.setAutoDraw(True)
        
        # if OutroText is active this frame...
        if OutroText.status == STARTED:
            # update params
            pass
        
        # *OutroResponse* updates
        waitOnFlip = False
        
        # if OutroResponse is starting this frame...
        if OutroResponse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            OutroResponse.frameNStart = frameN  # exact frame index
            OutroResponse.tStart = t  # local t and not account for scr refresh
            OutroResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(OutroResponse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'OutroResponse.started')
            # update status
            OutroResponse.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(OutroResponse.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(OutroResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if OutroResponse.status == STARTED and not waitOnFlip:
            theseKeys = OutroResponse.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _OutroResponse_allKeys.extend(theseKeys)
            if len(_OutroResponse_allKeys):
                OutroResponse.keys = _OutroResponse_allKeys[-1].name  # just the last key pressed
                OutroResponse.rt = _OutroResponse_allKeys[-1].rt
                OutroResponse.duration = _OutroResponse_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            OutroRoutine.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in OutroRoutine.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "OutroRoutine" ---
    for thisComponent in OutroRoutine.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for OutroRoutine
    OutroRoutine.tStop = globalClock.getTime(format='float')
    OutroRoutine.tStopRefresh = tThisFlipGlobal
    thisExp.addData('OutroRoutine.stopped', OutroRoutine.tStop)
    # check responses
    if OutroResponse.keys in ['', [], None]:  # No response was made
        OutroResponse.keys = None
    thisExp.addData('OutroResponse.keys',OutroResponse.keys)
    if OutroResponse.keys != None:  # we had a response
        thisExp.addData('OutroResponse.rt', OutroResponse.rt)
        thisExp.addData('OutroResponse.duration', OutroResponse.duration)
    thisExp.nextEntry()
    # the Routine "OutroRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
