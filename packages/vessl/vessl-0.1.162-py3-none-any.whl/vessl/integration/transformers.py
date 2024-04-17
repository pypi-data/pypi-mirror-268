from transformers import (
    TrainerCallback,
    TrainerControl,
    TrainerState,
    TrainingArguments,
)

from vessl.internal import api, finish
from vessl.internal import hyperparameters as hp
from vessl.internal import init, log

# keys which are in summary logs
SUMMARY_KEYS = {
    "train_runtime",
    "train_samples_per_second",
    "train_steps_per_second",
    "train_loss",
    "total_flos",
}


class VesslCallback(TrainerCallback):
    """
    A [`TrainerCallback`] that logs metrics, media, model checkpoints to [VESSL AI](https://vessl.ai/).

    Args:
        access_token(str): Access token to override. Defaults to
                `access_token` from `~/.vessl/config`.
        organization_name(str): Organization name to override. Defaults to
                `organization_name` from `~/.vessl/config`.
        project_name(str): Project name to override. Defaults to
            `project name` from `~/.vessl/config`.
        credentials_file(str): Defaults to None.
        force_update_access_token(bool): True if force update access token,
            False otherwise. Defaults to False.
        upload_model(bool): True if upload model after training finishes. Defaults to False.
        repository_name(str): Repository name to upload model. If it is None but upload_model is True,
            raise an exception. Defaults to None.
    """

    def __init__(
        self,
        access_token: str = None,
        organization_name: str = None,
        project_name: str = None,
        credentials_file: str = None,
        force_update_access_token: bool = False,
    ) -> None:
        api.configure(
            access_token=access_token,
            organization_name=organization_name,
            project_name=project_name,
            credentials_file=credentials_file,
            force_update_access_token=force_update_access_token,
        )
        self._initialized = False

    def setup(self, args: "TrainingArguments", state: "TrainerState", **kwargs):
        """
        Setup the optional VESSL integration.

        If training is performed in VESSL Run, do nothing.
        Otherwise, such as in case of local experiments, initialize the new VESSL Experiment and connect to it.
        """
        self._initialized = True
        if state.is_world_process_zero:
            init()

    def on_train_begin(
        self, args: "TrainingArguments", state: "TrainerState", control: "TrainerControl", **kwargs
    ):
        """Setup VESSL when training begins"""
        if not self._initialized:
            self.setup(args, state)

    def on_log(
        self,
        args: "TrainingArguments",
        state: "TrainerState",
        control: "TrainerControl",
        logs: dict[str, float] = None,
        **kwargs,
    ) -> None:
        if not self._initialized:
            self.setup(args, state)

        # log metrics in the main process only
        if state.is_world_process_zero:
            # if the current step is the max step, and the summary keys are subset of log keys, just skip logging.
            # It is summary log and it will be handled in on_train_end logs
            log_keys = set(logs.keys())
            if state.max_steps != state.global_step or not SUMMARY_KEYS.issubset(log_keys):
                log(payload=logs, step=state.global_step)

    def on_train_end(
        self, args: "TrainingArguments", state: "TrainerState", control: "TrainerControl", **kwargs
    ):
        """Clean up experiment and upload final model when training ends"""
        if self._initialized and state.is_world_process_zero:
            finish()

            # get the last log and if it contains train stats such as train_runtime, train_steps_per_seconds, etc,
            # log to hyperparameter section
            summary_log = state.log_history[-1]
            hp.update(summary_log)

