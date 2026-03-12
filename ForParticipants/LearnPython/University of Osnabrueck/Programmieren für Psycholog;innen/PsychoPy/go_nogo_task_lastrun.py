#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on Juni 24, 2025, at 14:13
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
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
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
expName = 'go_nogo_task'  # from the Builder filename that created this script
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
        originPath='C:\\Users\\sebas\\Documents\\PsychoPy\\go_nogo_task_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='priority'
    )
    thisExp.setPriority('type', priority.HIGH)
    thisExp.setPriority('imageFile', priority.HIGH)
    thisExp.setPriority('corrAns', priority.HIGH)
    thisExp.setPriority('TrialResp.keys', priority.HIGH)
    thisExp.setPriority('TrialResp.corr', priority.HIGH)
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
        logging.console.setLevel('debug')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('warning')
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
            winType='pyglet', allowGUI=True, allowStencil=False,
            monitor='testMonitor', color='darkgrey', colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = 'darkgrey'
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
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
    if deviceManager.getDevice('IntroResp') is None:
        # initialise IntroResp
        IntroResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='IntroResp',
        )
    if deviceManager.getDevice('TrialResp') is None:
        # initialise TrialResp
        TrialResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='TrialResp',
        )
    if deviceManager.getDevice('OutroResp') is None:
        # initialise OutroResp
        OutroResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='OutroResp',
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
    
    # --- Initialize components for Routine "TrialIntro" ---
    IntroText = visual.TextStim(win=win, name='IntroText',
        text='BlaBlaBla\n\n(Text neu eingeben)',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    IntroResp = keyboard.Keyboard(deviceName='IntroResp')
    
    # --- Initialize components for Routine "Delay" ---
    text = visual.TextStim(win=win, name='text',
        text='Get Ready!',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "TrialRoutine" ---
    TrialImage = visual.ImageStim(
        win=win,
        name='TrialImage', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    TrialResp = keyboard.Keyboard(deviceName='TrialResp')
    
    # --- Initialize components for Routine "TrialOutro" ---
    OutroText = visual.TextStim(win=win, name='OutroText',
        text='BlaBlaBla \n\n(Text neu eingeben)',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    OutroResp = keyboard.Keyboard(deviceName='OutroResp')
    
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
    
    # --- Prepare to start Routine "TrialIntro" ---
    # create an object to store info about Routine TrialIntro
    TrialIntro = data.Routine(
        name='TrialIntro',
        components=[IntroText, IntroResp],
    )
    TrialIntro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for IntroResp
    IntroResp.keys = []
    IntroResp.rt = []
    _IntroResp_allKeys = []
    # store start times for TrialIntro
    TrialIntro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    TrialIntro.tStart = globalClock.getTime(format='float')
    TrialIntro.status = STARTED
    thisExp.addData('TrialIntro.started', TrialIntro.tStart)
    TrialIntro.maxDuration = None
    # keep track of which components have finished
    TrialIntroComponents = TrialIntro.components
    for thisComponent in TrialIntro.components:
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
    
    # --- Run Routine "TrialIntro" ---
    TrialIntro.forceEnded = routineForceEnded = not continueRoutine
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
        
        # *IntroResp* updates
        waitOnFlip = False
        
        # if IntroResp is starting this frame...
        if IntroResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            IntroResp.frameNStart = frameN  # exact frame index
            IntroResp.tStart = t  # local t and not account for scr refresh
            IntroResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(IntroResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'IntroResp.started')
            # update status
            IntroResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(IntroResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(IntroResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if IntroResp.status == STARTED and not waitOnFlip:
            theseKeys = IntroResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _IntroResp_allKeys.extend(theseKeys)
            if len(_IntroResp_allKeys):
                IntroResp.keys = _IntroResp_allKeys[-1].name  # just the last key pressed
                IntroResp.rt = _IntroResp_allKeys[-1].rt
                IntroResp.duration = _IntroResp_allKeys[-1].duration
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
            TrialIntro.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialIntro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "TrialIntro" ---
    for thisComponent in TrialIntro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for TrialIntro
    TrialIntro.tStop = globalClock.getTime(format='float')
    TrialIntro.tStopRefresh = tThisFlipGlobal
    thisExp.addData('TrialIntro.stopped', TrialIntro.tStop)
    # check responses
    if IntroResp.keys in ['', [], None]:  # No response was made
        IntroResp.keys = None
    thisExp.addData('IntroResp.keys',IntroResp.keys)
    if IntroResp.keys != None:  # we had a response
        thisExp.addData('IntroResp.rt', IntroResp.rt)
        thisExp.addData('IntroResp.duration', IntroResp.duration)
    thisExp.nextEntry()
    # the Routine "TrialIntro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Delay" ---
    # create an object to store info about Routine Delay
    Delay = data.Routine(
        name='Delay',
        components=[text],
    )
    Delay.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for Delay
    Delay.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    Delay.tStart = globalClock.getTime(format='float')
    Delay.status = STARTED
    thisExp.addData('Delay.started', Delay.tStart)
    Delay.maxDuration = None
    # keep track of which components have finished
    DelayComponents = Delay.components
    for thisComponent in Delay.components:
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
    
    # --- Run Routine "Delay" ---
    Delay.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
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
            if tThisFlipGlobal > text.tStartRefresh + 2.0-frameTolerance:
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
            Delay.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Delay.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Delay" ---
    for thisComponent in Delay.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for Delay
    Delay.tStop = globalClock.getTime(format='float')
    Delay.tStopRefresh = tThisFlipGlobal
    thisExp.addData('Delay.stopped', Delay.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if Delay.maxDurationReached:
        routineTimer.addTime(-Delay.maxDuration)
    elif Delay.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    TrialLoop = data.TrialHandler2(
        name='TrialLoop',
        nReps=5.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('conditions.xlsx'), 
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
        
        # --- Prepare to start Routine "TrialRoutine" ---
        # create an object to store info about Routine TrialRoutine
        TrialRoutine = data.Routine(
            name='TrialRoutine',
            components=[TrialImage, TrialResp],
        )
        TrialRoutine.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        TrialImage.setImage(imageFile)
        # create starting attributes for TrialResp
        TrialResp.keys = []
        TrialResp.rt = []
        _TrialResp_allKeys = []
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
            
            # *TrialResp* updates
            waitOnFlip = False
            
            # if TrialResp is starting this frame...
            if TrialResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TrialResp.frameNStart = frameN  # exact frame index
                TrialResp.tStart = t  # local t and not account for scr refresh
                TrialResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TrialResp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TrialResp.started')
                # update status
                TrialResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(TrialResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(TrialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if TrialResp is stopping this frame...
            if TrialResp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > TrialResp.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    TrialResp.tStop = t  # not accounting for scr refresh
                    TrialResp.tStopRefresh = tThisFlipGlobal  # on global time
                    TrialResp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'TrialResp.stopped')
                    # update status
                    TrialResp.status = FINISHED
                    TrialResp.status = FINISHED
            if TrialResp.status == STARTED and not waitOnFlip:
                theseKeys = TrialResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _TrialResp_allKeys.extend(theseKeys)
                if len(_TrialResp_allKeys):
                    TrialResp.keys = _TrialResp_allKeys[-1].name  # just the last key pressed
                    TrialResp.rt = _TrialResp_allKeys[-1].rt
                    TrialResp.duration = _TrialResp_allKeys[-1].duration
                    # was this correct?
                    if (TrialResp.keys == str(corrAns)) or (TrialResp.keys == corrAns):
                        TrialResp.corr = 1
                    else:
                        TrialResp.corr = 0
            
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
        # check responses
        if TrialResp.keys in ['', [], None]:  # No response was made
            TrialResp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               TrialResp.corr = 1;  # correct non-response
            else:
               TrialResp.corr = 0;  # failed to respond (incorrectly)
        # store data for TrialLoop (TrialHandler)
        TrialLoop.addData('TrialResp.keys',TrialResp.keys)
        TrialLoop.addData('TrialResp.corr', TrialResp.corr)
        if TrialResp.keys != None:  # we had a response
            TrialLoop.addData('TrialResp.rt', TrialResp.rt)
            TrialLoop.addData('TrialResp.duration', TrialResp.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if TrialRoutine.maxDurationReached:
            routineTimer.addTime(-TrialRoutine.maxDuration)
        elif TrialRoutine.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        thisExp.nextEntry()
        
    # completed 5.0 repeats of 'TrialLoop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "TrialOutro" ---
    # create an object to store info about Routine TrialOutro
    TrialOutro = data.Routine(
        name='TrialOutro',
        components=[OutroText, OutroResp],
    )
    TrialOutro.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for OutroResp
    OutroResp.keys = []
    OutroResp.rt = []
    _OutroResp_allKeys = []
    # store start times for TrialOutro
    TrialOutro.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    TrialOutro.tStart = globalClock.getTime(format='float')
    TrialOutro.status = STARTED
    thisExp.addData('TrialOutro.started', TrialOutro.tStart)
    TrialOutro.maxDuration = None
    # keep track of which components have finished
    TrialOutroComponents = TrialOutro.components
    for thisComponent in TrialOutro.components:
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
    
    # --- Run Routine "TrialOutro" ---
    TrialOutro.forceEnded = routineForceEnded = not continueRoutine
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
        
        # *OutroResp* updates
        waitOnFlip = False
        
        # if OutroResp is starting this frame...
        if OutroResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            OutroResp.frameNStart = frameN  # exact frame index
            OutroResp.tStart = t  # local t and not account for scr refresh
            OutroResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(OutroResp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'OutroResp.started')
            # update status
            OutroResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(OutroResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(OutroResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if OutroResp.status == STARTED and not waitOnFlip:
            theseKeys = OutroResp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _OutroResp_allKeys.extend(theseKeys)
            if len(_OutroResp_allKeys):
                OutroResp.keys = _OutroResp_allKeys[-1].name  # just the last key pressed
                OutroResp.rt = _OutroResp_allKeys[-1].rt
                OutroResp.duration = _OutroResp_allKeys[-1].duration
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
            TrialOutro.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialOutro.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "TrialOutro" ---
    for thisComponent in TrialOutro.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for TrialOutro
    TrialOutro.tStop = globalClock.getTime(format='float')
    TrialOutro.tStopRefresh = tThisFlipGlobal
    thisExp.addData('TrialOutro.stopped', TrialOutro.tStop)
    # check responses
    if OutroResp.keys in ['', [], None]:  # No response was made
        OutroResp.keys = None
    thisExp.addData('OutroResp.keys',OutroResp.keys)
    if OutroResp.keys != None:  # we had a response
        thisExp.addData('OutroResp.rt', OutroResp.rt)
        thisExp.addData('OutroResp.duration', OutroResp.duration)
    thisExp.nextEntry()
    # the Routine "TrialOutro" was not non-slip safe, so reset the non-slip timer
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
