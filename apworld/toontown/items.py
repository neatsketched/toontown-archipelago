import random
import enum
from dataclasses import dataclass
from typing import Optional, List
from BaseClasses import ItemClassification
from . import consts


class ToontownItemName(enum.Enum):
    ### Laff Boost ###
    LAFF_BOOST_1 = "+1 Laff Boost"
    LAFF_BOOST_2 = "+2 Laff Boost"
    LAFF_BOOST_3 = "+3 Laff Boost"
    LAFF_BOOST_4 = "+4 Laff Boost"
    LAFF_BOOST_5 = "+5 Laff Boost"

    ### Jellybean Jar Capacity ###
    MONEY_CAP_750  = "+750 Jellybean Jar Capacity"
    MONEY_CAP_1000 = "+1000 Jellybean Jar Capacity"
    MONEY_CAP_1250 = "+1250 Jellybean Jar Capacity"
    MONEY_CAP_1500 = "+1500 Jellybean Jar Capacity"
    MONEY_CAP_2000 = "+2000 Jellybean Jar Capacity"
    MONEY_CAP_2500 = "+2500 Jellybean Jar Capacity"

    ### Fishing ###
    FISHING_ROD_UPGRADE = "Progressive Fishing Rod"

    ### Gag Training Frames ###
    TOONUP_FRAME = "Toon-Up Training Frame"
    TRAP_FRAME   = "Trap Training Frame"
    LURE_FRAME   = "Lure Training Frame"
    SOUND_FRAME  = "Sound Training Frame"
    THROW_FRAME  = "Throw Training Frame"
    SQUIRT_FRAME = "Squirt Training Frame"
    DROP_FRAME   = "Drop Training Frame"

    ### Gag Capacity ###
    GAG_CAPACITY_5  = "+5 Gag Capacity"
    GAG_CAPACITY_10 = "+10 Gag Capacity"
    GAG_CAPACITY_15 = "+15 Gag Capacity"

    ### Gag Multiplier ###
    GAG_MULTIPLIER_1 = "+1 Base Gag XP Multiplier"
    GAG_MULTIPLIER_2 = "+2 Base Gag XP Multiplier"

    ### Teleport Access ###
    TTC_TELEPORT  = "TTC Teleport Access"
    DD_TELEPORT   = "DD Teleport Access"
    DG_TELEPORT   = "DG Teleport Access"
    MML_TELEPORT  = "MML Teleport Access"
    TB_TELEPORT   = "TB Teleport Access"
    DDL_TELEPORT  = "DDL Teleport Access"
    SBHQ_TELEPORT = "SBHQ Teleport Access"
    CBHQ_TELEPORT = "CBHQ Teleport Access"
    LBHQ_TELEPORT = "LBHQ Teleport Access"
    BBHQ_TELEPORT = "BBHQ Teleport Access"

    ### HQ Access ###
    TTC_HQ_ACCESS = "Toontown Central HQ Access"
    DD_HQ_ACCESS  = "Donald's Dock HQ Access"
    DG_HQ_ACCESS  = "Daisy Gardens HQ Access"
    MML_HQ_ACCESS = "Minnie's Melodyland HQ Access"
    TB_HQ_ACCESS  = "The Brrrgh HQ Access"
    DDL_HQ_ACCESS = "Donald's Dreamland HQ Access"

    ### Facility Keys ###
    FRONT_FACTORY_ACCESS = "Front Factory Key"
    SIDE_FACTORY_ACCESS  = "Side Factory Key"

    COIN_MINT_ACCESS    = "Coin Mint Key"
    DOLLAR_MINT_ACCESS  = "Dollar Mint Key"
    BULLION_MINT_ACCESS = "Bullion Mint Key"

    A_OFFICE_ACCESS = "Office A Key"
    B_OFFICE_ACCESS = "Office B Key"
    C_OFFICE_ACCESS = "Office C Key"
    D_OFFICE_ACCESS = "Office D Key"

    FRONT_ONE_ACCESS  = "Front One Key"
    MIDDLE_TWO_ACCESS = "Middle Two Key"
    BACK_THREE_ACCESS = "Back Three Key"

    ### Cog Disguises ###
    SELLBOT_DISGUISE = "Sellbot Disguise"
    CASHBOT_DISGUISE = "Cashbot Disguise"
    LAWBOT_DISGUISE  = "Lawbot Disguise"
    BOSSBOT_DISGUISE = "Bossbot Disguise"

    ### Jellybean Bundles ###
    MONEY_250  = "250 Jellybeans"
    MONEY_500  = "500 Jellybeans"
    MONEY_1000 = "1000 Jellybeans"
    MONEY_2000 = "2000 Jellybeans"

    ### Gag XP Bundles ###
    XP_500  = "500 Gag XP Bundle"
    XP_1000 = "1000 Gag XP Bundle"
    XP_1500 = "1500 Gag XP Bundle"
    XP_2000 = "2000 Gag XP Bundle"
    XP_2500 = "2500 Gag XP Bundle"

    ### Reward Bundles ###
    SOS_REWARD       = "Random SOS Card"
    UNITE_REWARD     = "Random Unite"
    PINK_SLIP_REWARD = "Pink Slip Bundle"

    ### Traps ###
    UBER_TRAP = "Uber Trap"
    DRIP_TRAP = "Drip Trap"


@dataclass
class ToontownItemDefinition:
    name: ToontownItemName
    classification: ItemClassification
    quantity: int = 0  # 0 implies manually/dynamically generated in World
    description: Optional[str] = None
    unique_id: int = 0


ITEM_DEFINITIONS: List[ToontownItemDefinition] = [
    # region Laff Boosts
    ToontownItemDefinition(ToontownItemName.LAFF_BOOST_1, ItemClassification.useful),
    ToontownItemDefinition(ToontownItemName.LAFF_BOOST_2, ItemClassification.useful),
    ToontownItemDefinition(ToontownItemName.LAFF_BOOST_3, ItemClassification.useful),
    ToontownItemDefinition(ToontownItemName.LAFF_BOOST_4, ItemClassification.useful),
    ToontownItemDefinition(ToontownItemName.LAFF_BOOST_5, ItemClassification.useful),
    # endregion
    # region Gag Capacity
    ToontownItemDefinition(ToontownItemName.GAG_CAPACITY_5, ItemClassification.useful,  quantity=9),
    ToontownItemDefinition(ToontownItemName.GAG_CAPACITY_10, ItemClassification.useful, quantity=2),
    ToontownItemDefinition(ToontownItemName.GAG_CAPACITY_15, ItemClassification.useful, quantity=1),
    # endregion
    # region Jellybean Capacity
    ToontownItemDefinition(ToontownItemName.MONEY_CAP_750,  ItemClassification.useful, quantity=1),
    ToontownItemDefinition(ToontownItemName.MONEY_CAP_1000, ItemClassification.useful, quantity=1),
    ToontownItemDefinition(ToontownItemName.MONEY_CAP_1250, ItemClassification.useful, quantity=1),
    ToontownItemDefinition(ToontownItemName.MONEY_CAP_1500, ItemClassification.useful, quantity=1),
    ToontownItemDefinition(ToontownItemName.MONEY_CAP_2000, ItemClassification.useful, quantity=1),
    ToontownItemDefinition(ToontownItemName.MONEY_CAP_2500, ItemClassification.useful, quantity=1),
    # endregion
    # region Gag Training Frames
    ToontownItemDefinition(ToontownItemName.TOONUP_FRAME, ItemClassification.progression),
    ToontownItemDefinition(ToontownItemName.TRAP_FRAME,   ItemClassification.progression),
    ToontownItemDefinition(ToontownItemName.LURE_FRAME,   ItemClassification.progression),
    ToontownItemDefinition(ToontownItemName.SOUND_FRAME,  ItemClassification.progression),
    ToontownItemDefinition(ToontownItemName.THROW_FRAME,  ItemClassification.progression),
    ToontownItemDefinition(ToontownItemName.SQUIRT_FRAME, ItemClassification.progression),
    ToontownItemDefinition(ToontownItemName.DROP_FRAME,   ItemClassification.progression),
    # endregion
    # region Gag Training Multipliers
    ToontownItemDefinition(ToontownItemName.GAG_MULTIPLIER_1, ItemClassification.progression),
    ToontownItemDefinition(ToontownItemName.GAG_MULTIPLIER_2, ItemClassification.progression),
    # endregion
    # region Fishing Rod Upgrades
    ToontownItemDefinition(ToontownItemName.FISHING_ROD_UPGRADE, ItemClassification.progression, quantity=4),
    # endregion
    # region Teleport Access
    ToontownItemDefinition(ToontownItemName.TTC_TELEPORT, ItemClassification.useful, quantity=1),
    ToontownItemDefinition(ToontownItemName.DD_TELEPORT, ItemClassification.useful, quantity=1),
    ToontownItemDefinition(ToontownItemName.DG_TELEPORT, ItemClassification.useful, quantity=1),
    ToontownItemDefinition(ToontownItemName.MML_TELEPORT, ItemClassification.useful, quantity=1),
    ToontownItemDefinition(ToontownItemName.TB_TELEPORT, ItemClassification.useful, quantity=1),
    ToontownItemDefinition(ToontownItemName.DDL_TELEPORT, ItemClassification.useful, quantity=1),
    ToontownItemDefinition(ToontownItemName.SBHQ_TELEPORT, ItemClassification.useful, quantity=1),
    ToontownItemDefinition(ToontownItemName.CBHQ_TELEPORT, ItemClassification.useful, quantity=1),
    ToontownItemDefinition(ToontownItemName.LBHQ_TELEPORT, ItemClassification.useful, quantity=1),
    ToontownItemDefinition(ToontownItemName.BBHQ_TELEPORT, ItemClassification.useful, quantity=1),
    # endregion
    # region Tasking Access (Playground HQ entry access)
    ToontownItemDefinition(ToontownItemName.TTC_HQ_ACCESS, ItemClassification.progression),  # Given as a starting item ATM
    ToontownItemDefinition(ToontownItemName.DD_HQ_ACCESS,  ItemClassification.progression, quantity=1),
    ToontownItemDefinition(ToontownItemName.DG_HQ_ACCESS,  ItemClassification.progression, quantity=1),
    ToontownItemDefinition(ToontownItemName.MML_HQ_ACCESS, ItemClassification.progression, quantity=1),
    ToontownItemDefinition(ToontownItemName.TB_HQ_ACCESS,  ItemClassification.progression, quantity=1),
    ToontownItemDefinition(ToontownItemName.DDL_HQ_ACCESS, ItemClassification.progression, quantity=1),
    # endregion
    # region Facility Access
    ToontownItemDefinition(ToontownItemName.FRONT_FACTORY_ACCESS, ItemClassification.progression, quantity=1),
    ToontownItemDefinition(ToontownItemName.SIDE_FACTORY_ACCESS,  ItemClassification.progression, quantity=1),
    ToontownItemDefinition(ToontownItemName.COIN_MINT_ACCESS,     ItemClassification.progression, quantity=1),
    ToontownItemDefinition(ToontownItemName.DOLLAR_MINT_ACCESS,   ItemClassification.progression, quantity=1),
    ToontownItemDefinition(ToontownItemName.BULLION_MINT_ACCESS,  ItemClassification.progression, quantity=1),
    ToontownItemDefinition(ToontownItemName.A_OFFICE_ACCESS,      ItemClassification.progression, quantity=1),
    ToontownItemDefinition(ToontownItemName.B_OFFICE_ACCESS,      ItemClassification.progression, quantity=1),
    ToontownItemDefinition(ToontownItemName.C_OFFICE_ACCESS,      ItemClassification.progression, quantity=1),
    ToontownItemDefinition(ToontownItemName.D_OFFICE_ACCESS,      ItemClassification.progression, quantity=1),
    ToontownItemDefinition(ToontownItemName.FRONT_ONE_ACCESS,   ItemClassification.progression, quantity=1),
    ToontownItemDefinition(ToontownItemName.MIDDLE_TWO_ACCESS,  ItemClassification.progression, quantity=1),
    ToontownItemDefinition(ToontownItemName.BACK_THREE_ACCESS,    ItemClassification.progression, quantity=1),
    # endregion
    # region Boss Disguises
    ToontownItemDefinition(ToontownItemName.SELLBOT_DISGUISE, ItemClassification.progression, quantity=1),
    ToontownItemDefinition(ToontownItemName.CASHBOT_DISGUISE, ItemClassification.progression, quantity=1),
    ToontownItemDefinition(ToontownItemName.LAWBOT_DISGUISE,  ItemClassification.progression, quantity=1),
    ToontownItemDefinition(ToontownItemName.BOSSBOT_DISGUISE, ItemClassification.progression, quantity=1),
    # endregion
    # region Filler Items
    ToontownItemDefinition(ToontownItemName.MONEY_250,        ItemClassification.filler),
    ToontownItemDefinition(ToontownItemName.MONEY_500,        ItemClassification.filler),
    ToontownItemDefinition(ToontownItemName.MONEY_1000,       ItemClassification.filler),
    ToontownItemDefinition(ToontownItemName.MONEY_2000,       ItemClassification.filler),
    ToontownItemDefinition(ToontownItemName.XP_500,           ItemClassification.filler),
    ToontownItemDefinition(ToontownItemName.XP_1000,          ItemClassification.filler),
    ToontownItemDefinition(ToontownItemName.XP_1500,          ItemClassification.filler),
    ToontownItemDefinition(ToontownItemName.XP_2000,          ItemClassification.filler),
    ToontownItemDefinition(ToontownItemName.XP_2500,          ItemClassification.filler),
    ToontownItemDefinition(ToontownItemName.SOS_REWARD,       ItemClassification.filler),
    ToontownItemDefinition(ToontownItemName.UNITE_REWARD,     ItemClassification.filler),
    ToontownItemDefinition(ToontownItemName.PINK_SLIP_REWARD, ItemClassification.filler),
    # endregion
    # region Traps
    ToontownItemDefinition(ToontownItemName.UBER_TRAP, ItemClassification.trap),
    ToontownItemDefinition(ToontownItemName.DRIP_TRAP, ItemClassification.trap),
    # endregion
]

ITEM_DESCRIPTIONS = {
    ToontownItemName.SELLBOT_DISGUISE.value: "Grants access to fight the Sellbot VP",
    ToontownItemName.CASHBOT_DISGUISE.value: "Grants access to fight the Cashbot CFO",
    ToontownItemName.LAWBOT_DISGUISE.value:  "Grants access to fight the Lawbot CJ",
    ToontownItemName.BOSSBOT_DISGUISE.value: "Grants access to fight the Bossbot CEO",
}


for i in range(len(ITEM_DEFINITIONS)):
    ITEM_DEFINITIONS[i].unique_id = i + consts.BASE_ID

GAG_TRAINING_FRAMES = (
    ToontownItemName.TOONUP_FRAME,
    ToontownItemName.TRAP_FRAME,
    ToontownItemName.LURE_FRAME,
    ToontownItemName.SOUND_FRAME,
    ToontownItemName.THROW_FRAME,
    ToontownItemName.SQUIRT_FRAME,
    ToontownItemName.DROP_FRAME
)

# todo add quality/rarity to filler items
JUNK_ITEMS = [item for item in ITEM_DEFINITIONS if item.classification == ItemClassification.filler]
TRAP_ITEMS = [item for item in ITEM_DEFINITIONS if item.classification == ItemClassification.trap]


def get_item_def_from_id(_id: int) -> Optional[ToontownItemDefinition]:
    index = _id - consts.BASE_ID
    if 0 <= index < len(ITEM_DEFINITIONS):
        return ITEM_DEFINITIONS[index]
    return None


def random_junk() -> ToontownItemDefinition:
    return random.choice(JUNK_ITEMS)


def random_trap() -> ToontownItemDefinition:
    return random.choice(TRAP_ITEMS)


ITEM_NAME_TO_ID = {item.name.value: i + consts.BASE_ID for i, item in enumerate(ITEM_DEFINITIONS)}
