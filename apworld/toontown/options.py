from dataclasses import dataclass

from Options import PerGameCommonOptions, StartInventoryPool, Range, Choice, Toggle


class StartLaffOption(Range):
    """
    The starting amount of max Laff Points to have when starting a new game.
    """
    display_name = "Starting Laff"
    range_start = 1
    range_end = 80
    default = 20


class MaxLaffOption(Range):
    """
    The max laff you can get from items throughout the run.
    Must be above or equal to the starting_laff.
    """
    display_name = "Max Laff"
    range_start = 1
    range_end = 150
    default = 150


class BaseGlobalGagXPRange(Range):
    """
    The base global gag experience multiplier when starting a new game.
    This multiplier is globally multiplicative on top of in-game boosts.
    """
    display_name = "Base Global Gag XP"
    range_start = 1
    range_end = 10
    default = 2


class MaxGlobalGagXPRange(Range):
    """
    Additional global gag experience that can be obtained from items.
    Stacks additively onto the base value above.
    Must be above or equal to the base_global_gag_xp.
    """
    display_name = "Max Global Gag XP"
    range_start = 0
    range_end = 30
    default = 15


class StartMoneyOption(Range):
    """
    The starting amount of jellybeans to have when starting a new game.
    """
    display_name = "Starting Jellybeans"
    range_start = 0
    range_end = 9999
    default = 50


class CogBossesRequired(Range):
    """
    How many cog bosses must be defeated before being able to talk to Flippy to complete the game.
    """
    display_name = "Cog Bosses Required"
    range_start = 0
    range_end = 4
    default = 4


class LogicalTasksPerPlayground(Range):
    """
    Determines the amount of tasks per playground that are in logic.
    """
    display_name = "Logical Tasks Per Playground"
    range_start = 0
    range_end = 12
    default = 12


class LogicalMaxedCogGallery(Toggle):
    """
    Enable to make Cog Gallery Maxed checks be in logic.
    """
    display_name = "Logical Maxed Cog Gallery"
    default = True


class ForcePlaygroundVisitTeleportAccessUnlocksOption(Toggle):
    """
    Enable to force your playground teleport access to be on its corresponding "Visit Location" check
    """
    display_name = "Force Visit Playground Teleport Access Unlocks"
    default = True


class ForceCogHQVisitTeleportAccessUnlocksOption(Toggle):
    """
    Enable to force your Cog HQ teleport access to be on its corresponding "Visit Location" check
    """
    display_name = "Force Visit Cog HQ Teleport Access Unlocks"


class SeedGenerationTypeOption(Choice):
    """
    Type of seeding to use when RNG checks happen in game.

    Global: RNG elements are determined solely by the AP seed
    Per Slot: RNG elements are determined by AP seed and Slot Name
    Per Toon: RNG elements are determined by AP seed and internal toon ID
    Wild: RNG elements are completely random and will shuffle upon relogging
    """
    option_global = 0
    option_slot_name = 1
    option_unique = 2
    option_wild = 3

    display_name = "Seed Generation Type"


class TrapPercentOption(Range):
    """
    Percentage of junk items to be replaced with traps
    """

    display_name = "Trap Percentage"
    range_start = 1
    range_end = 100
    default = 20


@dataclass
class ToontownOptions(PerGameCommonOptions):
    max_laff: MaxLaffOption
    starting_laff: StartLaffOption
    base_global_gag_xp: BaseGlobalGagXPRange
    max_global_gag_xp: MaxGlobalGagXPRange
    starting_money: StartMoneyOption
    cog_bosses_required: CogBossesRequired
    logical_tasks_per_playground: LogicalTasksPerPlayground
    logical_maxed_cog_gallery: LogicalMaxedCogGallery
    force_playground_visit_teleport_access_unlocks: ForcePlaygroundVisitTeleportAccessUnlocksOption
    force_coghq_visit_teleport_access_unlocks: ForceCogHQVisitTeleportAccessUnlocksOption
    seed_generation_type: SeedGenerationTypeOption
    trap_percent: TrapPercentOption
