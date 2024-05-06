from app.services.achievement import AchievementService
from app.services.changes import ChangesService
from app.services.character import CharacterService
from app.services.collection import CollectionService
from app.services.craft import CraftService
from app.services.daily_offer import DailyOfferService
from app.services.item import ItemService
from app.services.market import MarketService
from app.services.missile import MissileService
from app.services.pixyship import PixyShipService
from app.services.player import PlayerService
from app.services.prestige import PrestigeService
from app.services.reasearch import ResearchService
from app.services.record import RecordService
from app.services.record_details import RecordDetailsService
from app.services.room import RoomService
from app.services.ship import ShipService
from app.services.skin import SkinService
from app.services.sprite import SpriteService
from app.services.training import TrainingService


class ServiceFactory:
    def __init__(self):
        self._record_service = None
        self._sprite_service: SpriteService | None = None
        self._market_service: MarketService | None = None
        self._training_service: TrainingService | None = None
        self._skin_service: SkinService | None = None
        self._collection_service: CollectionService | None = None
        self._character_service: CharacterService | None = None
        self._item_service: ItemService | None = None
        self._research_service: ResearchService | None = None
        self._room_service: RoomService | None = None
        self._ship_service: ShipService | None = None
        self._achievement_service: AchievementService | None = None
        self._craft_service: CraftService | None = None
        self._pixyship_service: PixyShipService | None = None
        self._missile_service: MissileService | None = None
        self._prestige_service: PrestigeService | None = None
        self._changes_service: ChangesService | None = None
        self._record_details_service: RecordDetailsService | None = None
        self._daily_offer_service: DailyOfferService | None = None
        self._player_service: PlayerService | None = None

    @property
    def record_service(self) -> RecordService:
        if self._record_service is None:
            self._record_service = RecordService()

        return self._record_service

    @property
    def sprite_service(self) -> SpriteService:
        if self._sprite_service is None:
            self._sprite_service = SpriteService()
            self._sprite_service.record_service = self.record_service

        return self._sprite_service

    @property
    def market_service(self) -> MarketService:
        if self._market_service is None:
            self._market_service = MarketService()

        return self._market_service

    @property
    def training_service(self) -> TrainingService:
        if self._training_service is None:
            self._training_service = TrainingService()
            self._training_service.record_service = self.record_service
            self._training_service.sprite_service = self.sprite_service

        return self._training_service

    @property
    def skin_service(self) -> SkinService:
        if self._skin_service is None:
            self._skin_service = SkinService()
            self._skin_service.record_service = self.record_service
            self._skin_service.sprite_service = self.sprite_service

        return self._skin_service

    @property
    def collection_service(self) -> CollectionService:
        if self._collection_service is None:
            self._collection_service = CollectionService()
            self._collection_service.record_service = self.record_service
            self._collection_service.sprite_service = self.sprite_service

        return self._collection_service

    @property
    def character_service(self) -> CharacterService:
        if self._character_service is None:
            self._character_service = CharacterService()
            self._character_service.record_service = self.record_service
            self._character_service.sprite_service = self.sprite_service
            self._character_service.collection_service = self.collection_service

        return self._character_service

    @property
    def item_service(self) -> ItemService:
        if self._item_service is None:
            self._item_service = ItemService()
            self._item_service.record_service = self.record_service
            self._item_service.sprite_service = self.sprite_service
            self._item_service.market_service = self.market_service
            self._item_service.training_service = self.training_service
            self._item_service.skin_service = self.skin_service
            self._item_service.character_service = self.character_service

        return self._item_service

    @property
    def research_service(self) -> ResearchService:
        if self._research_service is None:
            self._research_service = ResearchService()
            self._research_service.record_service = self.record_service
            self._research_service.sprite_service = self.sprite_service
            self._research_service.room_service = self.room_service

        return self._research_service

    @property
    def room_service(self) -> RoomService:
        if self._room_service is None:
            self._room_service = RoomService()
            self._room_service.record_service = self.record_service
            self._room_service.sprite_service = self.sprite_service
            self._room_service.item_service = self.item_service
            self._room_service.research_service = self.research_service

        return self._room_service

    @property
    def ship_service(self) -> ShipService:
        if self._ship_service is None:
            self._ship_service = ShipService()
            self._ship_service.record_service = self.record_service
            self._ship_service.sprite_service = self.sprite_service
            self._ship_service.item_service = self.item_service
            self._ship_service.room_service = self.room_service

        return self._ship_service

    @property
    def achievement_service(self) -> AchievementService:
        if self._achievement_service is None:
            self._achievement_service = AchievementService()
            self._achievement_service.record_service = self.record_service
            self._achievement_service.sprite_service = self.sprite_service

        return self._achievement_service

    @property
    def craft_service(self) -> CraftService:
        if self._craft_service is None:
            self._craft_service = CraftService()
            self._craft_service.record_service = self.record_service
            self._craft_service.sprite_service = self.sprite_service

        return self._craft_service

    @property
    def pixyship_service(self) -> PixyShipService:
        if self._pixyship_service is None:
            self._pixyship_service = PixyShipService()
            self._pixyship_service.room_service = self.room_service
            self._pixyship_service.skin_service = self.skin_service
            self._pixyship_service.item_service = self.item_service
            self._pixyship_service.character_service = self.character_service

        return self._pixyship_service

    @property
    def missile_service(self) -> MissileService:
        if self._missile_service is None:
            self._missile_service = MissileService()
            self._missile_service.pixyship_service = self.pixyship_service
            self._missile_service.record_service = self.record_service
            self._missile_service.sprite_service = self.sprite_service

        return self._missile_service

    @property
    def prestige_service(self) -> PrestigeService:
        if self._prestige_service is None:
            self._prestige_service = PrestigeService()
            self._prestige_service.record_service = self.record_service
            self._prestige_service.character_service = self.character_service

        return self._prestige_service

    @property
    def changes_service(self) -> ChangesService:
        if self._changes_service is None:
            self._changes_service = ChangesService()
            self._changes_service.record_service = self.record_service
            self._changes_service.sprite_service = self.sprite_service
            self._changes_service.character_service = self.character_service
            self._changes_service.item_service = self.item_service

        return self._changes_service

    @property
    def record_details_service(self) -> RecordDetailsService:
        if self._record_details_service is None:
            self._record_details_service = RecordDetailsService()
            self._record_details_service.record_service = self.record_service
            self._record_details_service.item_service = self.item_service
            self._record_details_service.ship_service = self.ship_service
            self._record_details_service.character_service = self.character_service
            self._record_details_service.skin_service = self.skin_service
            self._record_details_service.achievement_service = self.achievement_service
            self._record_details_service.collection_service = self.collection_service
            self._record_details_service.craft_service = self.craft_service
            self._record_details_service.missile_service = self.missile_service
            self._record_details_service.prestige_service = self.prestige_service
            self._record_details_service.research_service = self.research_service
            self._record_details_service.room_service = self.room_service
            self._record_details_service.sprite_service = self.sprite_service
            self._record_details_service.training_service = self.training_service

        return self._record_details_service

    @property
    def daily_offer_service(self) -> DailyOfferService:
        if self._daily_offer_service is None:
            self._daily_offer_service = DailyOfferService()
            self._daily_offer_service.pixyship_service = self.pixyship_service
            self._daily_offer_service.record_service = self.record_service
            self._daily_offer_service.sprite_service = self.sprite_service
            self._daily_offer_service.item_service = self.item_service
            self._daily_offer_service.character_service = self.character_service
            self._daily_offer_service.record_details_service = self.record_details_service

        return self._daily_offer_service

    @property
    def player_service(self) -> PlayerService:
        if self._player_service is None:
            self._player_service = PlayerService()
            self._player_service.sprite_service = self.sprite_service
            self._player_service.item_service = self.item_service
            self._player_service.ship_service = self.ship_service
            self._player_service.room_service = self.room_service
            self._player_service.skin_service = self.skin_service

        return self._player_service
