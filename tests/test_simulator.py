import os
import torch
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from src.data.train_utils import load_data
from src.map_api.lanelet import MapReader
from src.data.ego_dataset import EgoDataset
from src.simulation.simulator import InteractionSimulator
from src.visualization.animation import animate, save_animation

from src.map_api.frenet import FrenetPath
from src.map_api.frenet_utils import compute_acceleration_vector
from src.data.geometry import angle_to_vector, wrap_angles

import warnings
warnings.filterwarnings("ignore")

lanelet_path = "../exp/lanelet"
data_path = "../interaction-dataset-master"
scenario1 = "DR_CHN_Merging_ZS"
scenario2 = "DR_DEU_Merging_MT"
scenario = scenario1
filename = "vehicle_tracks_007.csv"

# load map
map_data = MapReader(cell_len=10)
map_data.parse(os.path.join(data_path, "maps", scenario + ".osm"))

def test_simulator_from_data():
    """ Use preprocessed frenet actions to control the simulator """
    df_track = load_data(data_path, scenario, filename)
    ego_dataset = EgoDataset(df_track)
    
    env = InteractionSimulator(ego_dataset, map_data)
    
    obs_env = env.reset(0)
    
    eps_id = env._track_data["meta"][1]
    df_eps = df_track.loc[df_track["eps_id"] == eps_id].reset_index(drop=True)
    
    lane_id = df_eps["lane_id"].values[0]
    ref_path = FrenetPath(np.array(map_data.lanes[lane_id].centerline.linestring.coords))
    for t in range(env.T):
        # get true agent control
        ctl_env = env.get_action()        
        
        # get acceleration from frenet state in dataset
        vx = df_eps["vx"].values
        vy = df_eps["vy"].values
        v = np.sqrt(vx**2 + vy**2)

        ax = df_eps["ax"].values
        ay = df_eps["ay"].values
        a = np.sqrt(ax**2 + ay**2)
        
        theta = df_eps["psi_rad"].values
        norm = df_eps["norm"].values
        kappa = df_eps["kappa"].values
        
        acc_vec = np.arctan2(ay, ax)
        delta_vec = wrap_angles(acc_vec - theta)
        sign = np.ones_like(theta)
        sign[delta_vec > 0.5 * np.pi] = -1
        sign[delta_vec < 0.5 * -np.pi] = -1
        a *= sign

        tan_vec = angle_to_vector(theta)
        norm_vec = angle_to_vector(norm)
        ctl_env = compute_acceleration_vector(a, v, kappa, tan_vec, norm_vec)
        ctl_env = ctl_env[t].reshape(-1)

        obs_env, r, done, info = env.step(ctl_env)
        
        if done:
            break

    ani = animate(map_data, env._sim_states, env._track_data, title="test", annot=True)
    save_animation(ani, "/Users/rw422/Documents/render_ani.mp4")

def test_observer():
    from src.simulation.observers import Observer
    from src.simulation.observers import FEATURE_SET
    
    observer = Observer(
        map_data, ego_features=FEATURE_SET["ego"],
        relative_features=FEATURE_SET["relative"]
    )
    
    # create synthetic data
    # ego_state = np.array([1065.303, 958.918, -10, -0.01, np.pi, 0])
    ego_state = np.array([1091.742, 950.918, -10, -0.01, np.pi, 0])
    agent_state = np.array([[1060.303, 960.918, -10, -0.01, np.pi]])
    state = {"ego": ego_state, "agents": agent_state}
    obs = observer.observe(state)
    assert list(obs.shape) == [1, len(observer.feature_set)]
    print("test_pbserver_new passed")

if __name__ == "__main__":
    test_simulator_from_data()
    # test_observer()