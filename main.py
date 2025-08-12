import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)
    for data_player in players:
        user = players[data_player]
        skills = user["race"]["skills"]
        guild = Guild.objects.get_or_create(
            name=user["guild"]["name"],
            description=user["guild"]["description"])
        race = Race.objects.get_or_create(
            name=user["race"]["name"],
            description=user["race"]["description"])

        player = Player.objects.create(
            nickname=data_player,
            email=user["email"],
            bio=user["bio"],
            race=race,
            guild=guild
        )
        for skill in skills:
            Skill.objects.get_or_create(
                name=skill["name"],
                bonus=skill["bonus"],
                race=player.race)


if __name__ == "__main__":
    main()
