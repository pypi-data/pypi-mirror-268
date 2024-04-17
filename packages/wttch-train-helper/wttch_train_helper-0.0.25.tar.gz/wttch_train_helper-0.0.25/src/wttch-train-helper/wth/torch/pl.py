from wth.utils.config import Config

try:
    # 可选模块 ~~~
    import pytorch_lightning as pl


    def _pl_config(config: Config) -> dict:
        return config['pl']


    def trainer(config: Config) -> pl.Trainer:
        pl_config = _pl_config(config)
        if pl_config is None:
            raise KeyError(f"请在{config.config_file}中定义 pl")
        devices = pl_config['devices']

        return pl.Trainer()

except ImportError:
    print("Please install pytorch-lightning")
