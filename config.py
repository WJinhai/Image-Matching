import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  # sets device for model and PyTorch tensors
print('device: ' + str(device))

# Model parameters
im_size = 224
channel = 3

# Training parameters
num_workers = 1  # for data-loading; right now, only 1 works with h5py
grad_clip = 5.  # clip gradients at an absolute value of
print_freq = 100  # print training/validation stats  every __ batches
checkpoint = None  # path to checkpoint, None if none

# Data parameters
num_classes = 9935
num_samples = 357646  # before filtering: 373471
num_tests = 10000
DATA_DIR = 'data'
IMG_DIR = 'data/cron20190326_resized/'
pickle_file = 'data/cron20190326.pickle'
