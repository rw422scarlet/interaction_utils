
class CarfollowingReward:
    """
    Reward features:
    0 lane deviation: -(d - d_target)^2, d_target = 0 m
    1 relative distance: 0 * (s_rel >= min_s_rel) - s_rel_penalty * (s_rel < min_s_rel)
    2 looming: -(loom - loom_target)^2, loom_target = 0 
    """
    def __init__(self, feature_names):
        self.feature_names = feature_names
        self.idx_d = feature_names.index("ego_d")
        self.idx_s_rel = feature_names.index("lv_s_rel")
        self.idx_loom = feature_names.index("lv_inv_tau")

        self.d_target = 0.
        self.min_s_rel = 3.
        self.s_rel_penalty = 10.
        self.loom_target = 0.

    def __call__(self, obs, ctl):
        obs = obs.flatten().clone()
        d = obs[self.idx_d]
        s_rel = obs[self.idx_s_rel]
        loom_s = obs[self.idx_loom]

        f1 = -(d - self.d_target) ** 2
        f2 = (s_rel >= self.min_s_rel) * 0 - self.s_rel_penalty * (s_rel < self.min_s_rel)
        f3 = -(loom_s - self.loom_target) ** 2
        r = f1 + f2 + 10 * f3
        return r