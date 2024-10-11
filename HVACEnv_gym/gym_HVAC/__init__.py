from gym.envs.registration import register

register(
    id='HVACEnv-v0',
    entry_point='gym_HVAC.envs:HVACEnv',
	max_episode_steps=200,
)