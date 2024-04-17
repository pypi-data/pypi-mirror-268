import nni
import numpy as np
import time
import torch


params = {
    "features": 512,
    "lr": 0.001,
    "momentum": 0,
}


optimized_params = nni.get_next_parameter()
params.update(optimized_params)


torch.ones([4000, 128], dtype=torch.float64, device="cuda")
time.sleep(10)


nni.report_final_result({
    "default": np.random.randint(10),
    "experiment_id": nni.get_experiment_id(),
    "trial_id": nni.get_trial_id(),
    "params": params,
    "cuda": (torch.cuda.is_available(), torch.cuda.device_count()),
})
