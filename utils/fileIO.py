import numpy as np

def save_preprocessed_data(data, file_path):
    # Extract and reshape the data from each Raw object
    data_list = [raw.get_data().reshape(1, -1) for raw in data]

    # Concatenate the data from all Raw objects into a single 2D array
    data_array = np.concatenate(data_list, axis=0)

    # Get the channel names
    channel_names = data[0].ch_names

    # Create column names with the format 'channel_name + sample_number'
    column_names = [f'{channel}_{i}' for i in range(data_array.shape[1] // len(channel_names)) for channel in channel_names]
    
    # Save the 2D array into a CSV file with column names
    np.savetxt(file_path, data_array, delimiter=',', header=','.join(column_names), comments='')


def load_preprocessed_data(file_path, n_channels):
    loaded_data = np.loadtxt(file_path, delimiter=',',dtype='object')

    
    data_array_flattened = loaded_data[1:,:]

    num_trials = data_array_flattened.shape[0]
    num_channels = n_channels
    num_samples_per_channel = data_array_flattened.shape[1] // num_channels  

    # Reshape the flattened data back to the original shape
    data_array_original_shape = data_array_flattened.reshape((num_trials, num_channels, num_samples_per_channel))

    processed_data = np.array(data_array_original_shape, dtype='float')

    return processed_data