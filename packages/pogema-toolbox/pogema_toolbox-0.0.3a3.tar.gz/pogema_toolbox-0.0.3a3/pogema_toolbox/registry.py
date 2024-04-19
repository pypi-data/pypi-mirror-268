from pathlib import Path
import yaml
from loguru import logger

from pogema_toolbox.algorithm_config import AlgoBase


class ToolboxRegistry:
    _instances = {}

    _maps = None
    _algorithms = {}
    _envs = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(ToolboxRegistry, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]

    @classmethod
    def get_state(cls):
        return {
            'maps': cls._maps,
            'algorithms': cls._algorithms,
            'envs': cls._envs,
        }

    @classmethod
    def recreate_from_state(cls, state):
        cls._maps = state.get('maps', {})
        cls._algorithms = state.get('algorithms', {})
        cls._envs = state.get('envs', {})
        logger.debug(f'Registry is recreated from state')

    # ----- Algorithms section -----
    @classmethod
    def register_algorithm(cls, name, make_func, config_make_func=None, preprocessing_make_func=None):
        if name in cls._algorithms:
            logger.warning(f'Registering existing algorithm with name {name}')
        cls._algorithms[name] = make_func, config_make_func, preprocessing_make_func
        logger.debug(f'Registered algorithm with name {name}')

    @classmethod
    def create_algorithm(cls, algo_name, **kwargs):
        algo_make_func, config_make_func, _ = cls._algorithms[algo_name]
        logger.debug(f'Creating {algo_name} algorithm')
        if config_make_func:
            config = cls.create_algorithm_config(algo_name, **kwargs)
            return algo_make_func(config)
        return algo_make_func()

    @classmethod
    def create_algorithm_config(cls, algo_name, **kwargs):
        _, config_make_func, _ = cls._algorithms[algo_name]
        if config_make_func is None:
            logger.debug('Using default config - AlgoBase')
            return AlgoBase(**kwargs)
        logger.debug(f'Creating {algo_name} config')
        return config_make_func(**kwargs)

    @classmethod
    def create_algorithm_preprocessing(cls, env_to_wrap, algo_name, **kwargs):
        _, config_make_func, preprocessing_make_func = cls._algorithms[algo_name]
        if config_make_func is not None:
            algo_cfg = cls.create_algorithm_config(algo_name, **kwargs)
            logger.debug(f'Creating {algo_name} preprocessing')
            return preprocessing_make_func(env_to_wrap, algo_cfg)
        return preprocessing_make_func(env_to_wrap)

    # ----- Environments section -----
    @classmethod
    def register_env(cls, name, make_func, config_make_func=None):
        if name in cls._envs:
            logger.warning(f'Registering existing environment with name {name}')
        cls._envs[name] = make_func, config_make_func
        logger.debug(f'Registered environment with name {name}')

    @classmethod
    def create_env(cls, env_name, **kwargs):
        env_make_func, config_make_func = cls._envs[env_name]

        if config_make_func:
            logger.debug(f'Creating {env_name} env using config')
            config = config_make_func(**kwargs)
            return env_make_func(config)
        logger.debug(f'Creating {env_name} env')
        return env_make_func()

    # ----- Maps section -----
    @classmethod
    def get_maps(cls):
        if cls._maps is None:
            cls._initialize_maps()
        return cls._maps

    @classmethod
    def register_maps(cls, maps):
        for map_name, map_grid in maps.items():
            if map_name in cls.get_maps():
                logger.warning(f'Registering existing map with name {map_name}')
            cls._maps[map_name] = map_grid
            logger.debug(f'Registered map with name {map_name}')

    @classmethod
    def _initialize_maps(cls):
        maps_folder_path = Path(__file__).parent / "maps"
        cls._maps = {}

        for yaml_file_path in maps_folder_path.glob("*.yaml"):
            with open(yaml_file_path, "r") as f:
                try:
                    grids_content = yaml.safe_load(f)
                    if grids_content:  # Check if the YAML file is not empty
                        cls._maps.update(grids_content)
                except yaml.YAMLError as exc:
                    logger.error(f'Error loading YAML file {yaml_file_path}: {exc}')
        logger.debug(f'Registered {len(cls._maps)} maps')
