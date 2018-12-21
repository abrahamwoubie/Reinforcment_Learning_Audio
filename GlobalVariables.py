class GlobalVariables :

    #options for running different experiments
    use_samples = 1
    use_pitch = 0
    use_spectrogram = 0
    use_raw_data = 0

    #Grid Size
    nRow = 3
    nCol = 3

    #parameters
    sample_state_size = 100
    pitch_state_size= 87
    spectrogram_state_size= 57788
    raw_data_state_size= 100
    action_size = 4
    batch_size = 32
    Number_of_episodes=100
    timesteps=(nRow+nCol+nRow)
    how_many_times = 1 #How many times to run the same experiment

