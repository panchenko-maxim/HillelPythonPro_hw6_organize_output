import random
from dataclasses import dataclass, field
from typing import TypedDict

from faker import Faker

type T_GROUP_NAME = str
type T_GROUP_NAMES = list[T_GROUP_NAME]

type T_USER_NAME = str


class Human(TypedDict):
    name: T_USER_NAME
    group: T_GROUP_NAME


type T_HUMANS = list[Human]


@dataclass
class DataProvider:
    _faker: Faker = field(default_factory=Faker)

    def _generate_group_names(
        self,
        amount: int = 10,
    ) -> T_GROUP_NAMES:
        return [self._faker.unique.company() for _ in range(amount)]

    def _generate_human(self, group_name: T_GROUP_NAME) -> Human:
        return Human(
            name=self._faker.unique.first_name(),
            group=group_name,
        )

    def _generate_humans(
        self,
        groups: T_GROUP_NAMES,
        amount_of_humans: int,
    ) -> T_HUMANS:
        members = []
        for _ in range(amount_of_humans):
            group_name = random.choice(groups)  # noqa: S311
            group_member = self._generate_human(group_name=group_name)
            members.append(group_member)

        return members

    def generate_group_members(
        self,
        amount_of_groups: None | int = None,
        amount_of_humans: None | int = None,
    ) -> T_HUMANS:
        amount_of_groups = amount_of_groups or random.randint(5, 10)  # noqa: S311
        amount_of_humans = amount_of_humans or random.randint(3, 30)  # noqa: S311

        _groups = self._generate_group_names(amount=amount_of_groups)
        return self._generate_humans(
            groups=_groups,
            amount_of_humans=amount_of_humans,
        )
