from redis import Redis
from ...typings.ai import AiModel, AiModelTokenManager
from datetime import datetime
from typing import Optional, Tuple
import time


class RedisTokenManager(AiModelTokenManager):

    def __init__(self, *, redis: Redis, tpm_namespace: Optional[str | property] = None, tpm: Optional[int] = None,
                 tpm_percentage: Optional[float] = None):
        self.__redis = redis
        if tpm is not None or tpm_percentage is not None:
            assert tpm_namespace is not None, "Missing tpm namespace"
        self.__tpm = tpm
        self.__tpm_percentage = tpm_percentage
        self.__tpm_namespace = tpm_namespace

    def get_namespace_tpm(self, *, ai_model: AiModel) -> int:
        """get TPM that this token manager should use"""
        if self.__tpm is not None:
            assert self.__tpm <= ai_model.tpm, "Custom tpm exceed maximum TPM allowance of ai model"
            return self.__tpm
        elif self.__tpm_percentage is not None:
            return min(max(int(self.__tpm_percentage * ai_model.tpm), ai_model.max_token), ai_model.tpm)
        return ai_model.tpm

    def wait_for_allow(self, require_token: int, *, ai_model: AiModel):
        locked = self._lock_for_tokens(self.__redis, require_token, ai_model)
        tried = 0
        max_tried = 500
        each_try_wait_secs = 2
        assert each_try_wait_secs * max_tried < 60 * 60  # should not be wait too long
        while not locked and tried < max_tried:
            # wait for lock success
            time.sleep(each_try_wait_secs)
            locked = self._lock_for_tokens(self.__redis, require_token, ai_model)
            tried += 1
            if tried >= max_tried:
                raise ValueError(
                    f"Fail to lock for token resource after {max_tried * each_try_wait_secs} secs of waiting")
            if tried % 10 == 0:
                print("Waiting to able to lock for token resource")
            time.sleep(each_try_wait_secs)

    def _lock_for_tokens(self, r, require_token: int, ai_model: AiModel) -> bool:
        """Lock for tokens"""
        if ai_model.tpm is None:
            # no need to lock, default True
            return True
        assert require_token < ai_model.max_token

        ai_model_key, namespace_key = self.get_usage_key_for_minute(ai_model, tpm_namespace=self.__tpm_namespace)

        # Cache1
        ai_model_h = r.get(ai_model_key)

        if ai_model_h is None:
            ai_model_h = 0
        else:
            ai_model_h = int(ai_model_h)

        # Cache 2
        if namespace_key is not None:
            namespace_h = r.get(namespace_key)
            if namespace_h is None:
                namespace_h = 0
            else:
                namespace_h = int(namespace_h)
            namespace_tpm = self.get_namespace_tpm(ai_model=ai_model)
            assert require_token <= namespace_tpm, "Require token exceeded namespace tpm"
        else:
            namespace_tpm = None
            namespace_h = None

        if ai_model_h + require_token < ai_model.tpm and (
                namespace_h is None or namespace_h + require_token <= namespace_tpm
        ):
            # allow to lock
            r.incr(ai_model_h, require_token)
            r.expire(ai_model_h, 60)  # always expire after 60s

            if namespace_h is not None:
                r.incr(namespace_h, require_token)
                r.expire(namespace_h, 60)  # always expire after 60s
            return True
        return False

    @classmethod
    def get_usage_key_for_minute(cls, ai_model: AiModel, tpm_namespace: Optional[str]) -> Tuple[str, Optional[str]]:
        """Return 2 redis key, Ai Model TPM key + Namespace Key"""
        now = datetime.utcnow()
        base_key = f"tm:{ai_model.endpoint}:{ai_model.deployment}"
        base_key = f"{base_key}-{now.year}-{now.month}-{now.day}-{now.hour}-{now.minute}"
        if tpm_namespace is not None: return base_key, f"{base_key}:{tpm_namespace}"
        return base_key, None
