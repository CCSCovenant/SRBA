class GameManager:

    def __int__(self, Character_List, Enemy_List, Spec_Event_List):
        self.Spec_Event_List = Spec_Event_List
        self.Character_List = Character_List
        self.Enemy_List = Enemy_List

        pass

    def next_event(self):
        for spec_event in self.Spec_Event_List:
            self.event_check(spec_event)

        for character in self.Character_List:
            for character_event in character.eventList:
                self.event_check(character_event)

        for enemy in self.Enemy_List:
            for enemy_event in enemy.eventList:
                self.event_check(enemy_event)

    def event_check(self, event):
        if event.is_event_active(GameManager=self):
            if event.event_end_check(GameManager=self):
                event.on_event_end(GameManager=self)
            else:
                event.on_event_run(GameManager=self)
        else:
            if event.event_start_check(GameManager=self):
                event.on_event_start(GameManager=self)

    def summon_enemy(self):
        pass

    def remove_enemy(self):
        pass
