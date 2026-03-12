# Repetition Supression - Lists

import random
import os

######################################################################

# Helper function to generate a random fixation duration
def random_fixation_duration():
    return round(random.uniform(0.5, 0.8), 2)

######################################################################


# Lists for repeated and not repeated objects
# 240 objects 
# -> object numbers 1-120 will be repeated
# -> object numbers 121-240 will not be repeated
all_objects =list(range(1,241,1))


# How many lists do we need?
num_subjects = 100


# Loop für alle Versuchspersonen
for subject in range(1, num_subjects + 1):

    ##################################################################
    ###################### RANDOMIZE #################################
    # Randomize the objects
    rand_objects = all_objects
    random.shuffle(rand_objects)
    
    
    # Devide objects into repeats and non-repeats
    rep_objects   = rand_objects[0:120]
    norep_objects = rand_objects[120:240]
    
    
    # Devide into PC and VR
    rep_objects_PC   = rep_objects[0:60]
    rep_objects_VR   = rep_objects[60:120]
    norep_objects_PC = norep_objects[0:60]
    norep_objects_VR = norep_objects[60:120]
    
    
    
    ##################################################################
    #################### TRIAL LOGIC #################################
    # Gaps in between repeats (1, 2 or 3 Objects in between)
    
    trials_PC = [None] * 180
    trials_VR = [None] * 180
    
    triggers_PC = [None] * 180
    triggers_VR = [None] * 180
    
    fixation_durations_PC = [None] * 180
    fixation_durations_VR = [None] * 180
    
    
    
    #################################################################
    # PC Condition
    # Insert repeated objects into trial list
    # Gaps: 20 objects will be repetaetd after 1 object in between, 20 with 2 objects in between & 20 with 3 objects inbetween
    gaps = [1] * 20 + [2] * 20 + [3] * 20
    random.shuffle(gaps)
    
    for stim in rep_objects_PC:
    # Loop over all stimuli to be presented twice
        while True:
        # Endless loop for finding a suitable position (only breaks if position for stim is found)
            first_pos = random.randint(0, 179) # pick random position 
    
            if trials_PC[first_pos] is None:  # position must be free
                gap = random.choice(gaps) # randomly choose from the gap-list
                second_pos = first_pos + gap + 1  # where to place the repeated object
            
                if second_pos < 180 and trials_PC[second_pos] is None: # second position cannot be outside the 180 trials and must still be free
                    trials_PC[first_pos] = stim
                    triggers_PC[first_pos] = 1  # Trigger for first presentation
                    fixation_durations_PC[first_pos] = random_fixation_duration()
                    trials_PC[second_pos] = stim
                    triggers_PC[second_pos] = 2  # Trigger for second presentation
                    fixation_durations_PC[second_pos] = random_fixation_duration()
                    gaps.remove(gap)  # remove gap from gap-list
                    break
    
    
    # Fill remaining positions with non-repeated objects
    for stim in norep_objects_PC:
    # Loop over all stimuli to be presented once
        while True:
        # Endless loop for finding a suitable position (only breaks if position for stim is found)
            pos = random.randint(0, 179)
            
            if trials_PC[pos] is None:
            # only if position is still free
                trials_PC[pos] = stim
                triggers_PC[pos] = 8  # Trigger for new stimulus
                fixation_durations_PC[pos] = random_fixation_duration()
                break
    
    
    
    #################################################################
    # VR Condition
    # Insert repeated objects into trial list
    gaps = [1] * 20 + [2] * 20 + [3] * 20
    random.shuffle(gaps)
    
    for stim in rep_objects_VR:
        while True:
            first_pos = random.randint(0, 179)
            if trials_VR[first_pos] is None:
                gap = random.choice(gaps)
                second_pos = first_pos + gap + 1
            
                if second_pos < 180 and trials_VR[second_pos] is None:
                    trials_VR[first_pos] = stim
                    triggers_VR[first_pos] = 1  # Trigger for first presentation
                    trials_VR[second_pos] = stim
                    fixation_durations_VR[first_pos] = random_fixation_duration()
                    triggers_VR[second_pos] = 2  # Trigger for second presentation
                    fixation_durations_VR[second_pos] = random_fixation_duration()
                    gaps.remove(gap)
                    break
    
    
    # Fill remaining positions with non-repeated objects
    for stim in norep_objects_VR:
        while True:
            pos = random.randint(0, 179)
            if trials_VR[pos] is None:
                trials_VR[pos] = stim
                triggers_VR[pos] = 8  # Trigger for new stimulus
                fixation_durations_VR[pos] = random_fixation_duration()
                break
    
    
    ##################################################################
    #################### WRITE LISTS #################################
    
    # Dateinamen basierend auf Versuchspersonennummer
    filename_PC = f'RS_PC_List_{subject}.csv'
    filename_VR = f'RS_VR_List_{subject}.csv'
    

    # Write PC List
    with open(filename_PC, 'w') as file:
        file.write("imagePath,eegTrig,fix_duration\n")
        for stim, trigger, fixation_duration in zip(trials_PC, triggers_PC, fixation_durations_PC):
            line = f"stimuli/{stim}.png,{trigger},{fixation_duration}\n"
            file.write(line)
    
    # Write VR List
    with open(filename_VR, 'w') as file:
        file.write("imagePath,eegTrig,fix_duration\n")
        for stim, trigger, fixation_duration in zip(trials_VR, triggers_VR, fixation_durations_VR):
            line = f"stimuli/{stim}.png,{trigger},{fixation_duration}\n"
            file.write(line)


















