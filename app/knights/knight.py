class Knight:

    def __init__(self, config: dict) -> None:

        self.name = config["name"]
        self.power = config["power"]
        self.hp = config["hp"]
        self.protection = 0

        if len(config["armour"]) > 0:
            for item in config["armour"]:
                self.protection += item["protection"]

        self.power += config["weapon"]["power"]

        if config["potion"] is not None:
            if "power" in config["potion"]["effect"]:
                self.power += config["potion"]["effect"]["power"]

            if "hp" in config["potion"]["effect"]:
                self.hp += config["potion"]["effect"]["hp"]

            if "protection" in config["potion"]["effect"]:
                self.protection += config["potion"]["effect"]["protection"]
