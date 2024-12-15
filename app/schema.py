import datetime
from typing import Self, Union

from pydantic import BaseModel, Field, model_validator


class DateRange(BaseModel):
    start_date: datetime.date = Field(examples=[datetime.date(2023, 1, 1)])
    end_date: datetime.date = Field(examples=[datetime.date.today()])

    @model_validator(mode="after")
    def verify_start_date_le_end_date(self) -> Self:
        if self.start_date > self.end_date:
            raise ValueError("'start_date' should be less than or equal to 'end_date'")
        return self


class Filters(BaseModel):
    date_range: DateRange | None = None
    category: list[str] = Field(default_factory=list) # noqa
    product_ids: list[int] = Field(default_factory=list) # noqa


class GetSummary(BaseModel):
    columns: list[str] = Field(default=["quantity_sold", "price_per_unit"]) # noqa
    filters: Filters | None = Field(default=None)


class Metrics(BaseModel):
    mean: float
    median: float
    mode: float
    std_dev: float
    percentile_25: float
    percentile_75: float


Summary = Union[dict[str, Metrics], dict]
