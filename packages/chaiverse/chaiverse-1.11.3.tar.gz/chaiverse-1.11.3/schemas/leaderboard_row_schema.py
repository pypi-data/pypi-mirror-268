from datetime import datetime
from typing import List, Literal, Optional, Union

from pydantic import BaseModel, Extra, Field

from chaiverse import config
from chaiverse.lib.pydantic_tools import get_fields_in_schema
from chaiverse.lib.date_tools import convert_to_us_pacific_date


class BaseLeaderboardRow(BaseModel, extra=Extra.allow):
    developer_uid: str
    submission_id: str
    model_name: Optional[str]
    status: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    double_thumbs_up: int = 0
    thumbs_up: int = 0
    thumbs_down: int = 0

    num_battles: int = 0
    num_wins: int = 0

    celo_rating: Optional[float] = None
    entertaining: Optional[float] = None
    stay_in_character: Optional[float] = None
    user_preference: Optional[float] = None
    safety_score: Optional[float] = None

    @property
    def display_name(self):
        name = self.model_name if self.model_name else self.submission_id
        return name

    @property
    def win_ratio(self):
        return self.num_wins / self.num_battles if self.num_battles > 0 else float('nan')

    @property
    def feedback_count(self):
        return self.double_thumbs_up + self.thumbs_up + self.thumbs_down

    @property
    def double_thumbs_up_ratio(self):
        return self.double_thumbs_up / self.feedback_count if self.feedback_count > 0 else float('nan')

    @property
    def thumbs_up_ratio(self):
        return (self.double_thumbs_up + self.thumbs_up) / self.feedback_count if self.feedback_count > 0 else float('nan')

    @property
    def single_thumbs_up_ratio(self):
        return self.thumbs_up / self.feedback_count if self.feedback_count > 0 else float('nan')

    @property
    def thumbs_down_ratio(self):
        return self.thumbs_down / self.feedback_count if self.feedback_count > 0 else float('nan')

    @property
    def model_score(self):
        model_score = None
        if self.entertaining and self.stay_in_character and self.user_preference:
            model_score = (self.entertaining + self.stay_in_character + self.user_preference) / 3
        return model_score

    @property
    def us_pacific_date(self):
        us_pacific_date = convert_to_us_pacific_date(self.timestamp).date()
        return us_pacific_date

    def can_auto_deactivate(self):
        can_auto_deactivate = self.num_battles >= config.AUTO_DEACTIVATION_MIN_NUM_BATTLES and self.status == 'deployed'
        return can_auto_deactivate

    def all_fields_dict(self):
        fields = get_fields_in_schema(self.__class__)
        fields = {key: getattr(self, key) for key in fields}
        return fields


class BasicLeaderboardRow(BaseLeaderboardRow):
    submission_type: Literal['basic'] = Field(default='basic')
    model_repo: str
    reward_repo: str = None
    model_num_parameters: float = None
    best_of: int = 1
    max_input_tokens: int

    @property
    def language_model(self):
        return self.model_repo

    @property
    def reward_model(self):
        return self.reward_repo

    @property
    def model_size(self):
        size_gb = round(self.model_num_parameters / 1e9) if self.model_num_parameters else None
        size_gb = f'{size_gb}B'
        return size_gb


class BlendLeaderboardRow(BaseLeaderboardRow):
    submission_type: Literal['blend'] = Field(default='blend')
    submissions: List[str]

    @property
    def language_model(self):
        return ','.join(self.submissions)

    @property
    def reward_model(self):
        return 'random'

    @property
    def model_size(self):
        return 'n/a'

    def can_auto_deactivate(self):
        return False


class RewardBlendLeaderboardRow(BaseLeaderboardRow):
    submission_type: Literal['reward_blend'] = Field(default='reward_blend')
    reward_repo: str

    submissions: List[str]
    num_samples: int

    @property
    def language_model(self):
        pseudo_language_model = ','.join(self.submissions)
        return pseudo_language_model

    @property
    def reward_model(self):
        return self.reward_repo

    @property
    def model_size(self):
        return 'n/a'

    def can_auto_deactivate(self):
        return False


class TaggedSubmissionID(BaseModel):
    submission_id: str
    tags: Optional[List[str]] = None


class RoutedBlendLeaderboardRow(BaseLeaderboardRow):
    submission_type: Literal['routed_blend'] = Field(default='routed_blend')
    router: str
    tagged_submissions: List[TaggedSubmissionID]

    @property
    def language_model(self):
        tagged_submissions = []
        for tagged_submission in self.tagged_submissions:
            tags = '|'.join(tagged_submission.tags)
            tagged_submissions.append(f'{tagged_submission.submission_id}:{tags}')
        pseudo_language_model = ','.join(tagged_submissions)
        return pseudo_language_model

    @property
    def reward_model(self):
        return self.router

    @property
    def model_size(self):
        return 'n/a'

    def can_auto_deactivate(self):
        return False


LeaderboardRow = Union[
    BlendLeaderboardRow,
    RewardBlendLeaderboardRow,
    RoutedBlendLeaderboardRow,
    BasicLeaderboardRow,
]
