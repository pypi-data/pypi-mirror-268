import os

import torch
CUDA_NUM = '1'

device = 'cuda:'+CUDA_NUM if torch.cuda.is_available() else 'cpu'
print(device)
print(torch.cuda.get_device_name(0))
print(torch.cuda.is_available())
print(torch.__version__)

num_gpus = torch.cuda.device_count()

print("Number of available GPUs:", num_gpus)
print("Selected device:", device)

if device == 'cuda:'+CUDA_NUM:
    print("GPU device name:", torch.cuda.get_device_name(0))
print("CUDA is available:", torch.cuda.is_available())
print("PyTorch version:", torch.__version__)

with open('run_tests.txt', 'r') as f:
    script_filenames = f.read().splitlines()

for script_filename in script_filenames:
    if script_filename.strip():
        print(f"Running {script_filename}")
        os.system(f"python {script_filename}")
