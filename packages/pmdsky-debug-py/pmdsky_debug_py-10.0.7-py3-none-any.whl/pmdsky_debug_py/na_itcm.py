from .protocol import Symbol


class NaItcmArm7Functions:

    _start_arm7 = Symbol(
        None,
        None,
        None,
        "The entrypoint for the ARM7 CPU.\n\nHandles mapping the ARM7 binary into the various memory areas that the program will be using.\n\nOnce the memory mapping has been completed, a constant containing the address to NitroSpMain is loaded into a register (r1), and a `bx` branch will jump to NitroSpMain.\n\nNo params.",
    )

    do_autoload_arm7 = Symbol(None, None, None, "")

    StartAutoloadDoneCallbackArm7 = Symbol(None, None, None, "")

    NitroSpMain = Symbol(
        None,
        None,
        None,
        "This main function for the ARM7 subsystem. Contains the main event loop.\n\nNo params.",
    )

    HardwareInterrupt = Symbol(
        None,
        None,
        None,
        "Called whenever a hardware interrupt takes place.\n\nReturns immediately if the IME flag is 0 or if none of the devices that requested an interrupt has the corresponding Interrupt Enable flag set.\nIt searches for the first device that requested an interrupt, clears its Interrupt Request flag, then jumps to the start of the corresponding interrupt function. The return address is manually set to ReturnFromInterrupt.\nThis function does not return.\n\nNo params.",
    )

    ReturnFromInterrupt = Symbol(
        None,
        None,
        None,
        "The execution returns to this function after a hardware interrupt function is run.\n\nNo params.",
    )

    AudioInterrupt = Symbol(
        None,
        None,
        None,
        "Called when handling a hardware interrupt from the audio system.\n\nIts parameter is used to index a list of function pointers. The game then jumps to the read pointer.\n\nr0: Index of the function to jump to",
    )

    ClearImeFlag = Symbol(
        None,
        None,
        None,
        "Clears the Interrupt Master Enable flag, which disables all hardware interrupts.\n\nreturn: Previous IME value",
    )

    ClearIeFlag = Symbol(
        None,
        None,
        None,
        "Clears the specified Interrupt Enable flag, which disables interrupts for the specified hardware component.\n\nr0: Flag to clear\nreturn: Previous value of the Interrupt Enable flags",
    )

    GetCurrentPlaybackTime = Symbol(
        None,
        None,
        None,
        "Returns the time that the current song has been playing for. Might have a more generic purpose.\n\nThe time is obtained using a couple of RAM counters and the hardware timers for additional precision.\nThe game uses this value to know when a given note should stop being played. It doesn't seem to be used to keep track of the\ncurrent time instant within the song.\n\nreturn: Playback time. Units unknown.",
    )

    ClearIrqFlag = Symbol(
        None,
        None,
        None,
        "Copy of the ARM9 function. See arm9.yml for more information.\n\nreturn: Old value of cpsr & 0x80 (0x80 if interrupts were disabled, 0x0 if they were already enabled)",
    )

    EnableIrqFlag = Symbol(
        None,
        None,
        None,
        "Copy of the ARM9 function. See arm9.yml for more information.\n\nreturn: Old value of cpsr & 0x80 (0x80 if interrupts were already disabled, 0x0 if they were enabled)",
    )

    SetIrqFlag = Symbol(
        None,
        None,
        None,
        "Copy of the ARM9 function. See arm9.yml for more information.\n\nr0: Value to set the flag to (0x80 to set it, which disables interrupts; 0x0 to unset it, which enables interrupts)\nreturn: Old value of cpsr & 0x80 (0x80 if interrupts were disabled, 0x0 if they were enabled)",
    )

    EnableIrqFiqFlags = Symbol(
        None,
        None,
        None,
        "Copy of the ARM9 function. See arm9.yml for more information.\n\nreturn: Old value of cpsr & 0xC0 (contains the previous values of the i and f flags)",
    )

    SetIrqFiqFlags = Symbol(
        None,
        None,
        None,
        "Copy of the ARM9 function. See arm9.yml for more information.\n\nr0: Value to set the flags to (0xC0 to set both flags, 0x80 to set the i flag and clear the f flag, 0x40 to set the f flag and clear the i flag and 0x0 to clear both flags)\nreturn: Old value of cpsr & 0xC0 (contains the previous values of the i and f flags)",
    )

    GetProcessorMode = Symbol(
        None,
        None,
        None,
        "Copy of the ARM9 function. See arm9.yml for more information.\n\nreturn: cpsr & 0x1f (the cpsr mode bits M4-M0)",
    )

    _s32_div_f = Symbol(
        None,
        None,
        None,
        "Copy of the ARM9 function. See arm9.yml for more information.\n\nr0: dividend\nr1: divisor\nreturn: (quotient) | (remainder << 32)",
    )

    _u32_div_f = Symbol(
        None,
        None,
        None,
        "Copy of the ARM9 function. See arm9.yml for more information.\n\nr0: dividend\nr1: divisor\nreturn: (quotient) | (remainder << 32)",
    )

    _u32_div_not_0_f = Symbol(
        None,
        None,
        None,
        "Copy of the ARM9 function. See arm9.yml for more information.\n\nr0: dividend\nr1: divisor\nreturn: (quotient) | (remainder << 32)",
    )


class NaItcmArm7Data:

    pass


class NaItcmArm7Section:
    name = "arm7"
    description = "The ARM7 binary.\n\nThis is the secondary binary that gets loaded when the game is launched.\n\nSpeaking generally, this is the program run by the Nintendo DS's secondary ARM7TDMI CPU, which handles the audio I/O, the touch screen, Wi-Fi functions, cryptography, and more.\n\nMemory map: (binary is initially loaded at 0x2380000)\n0x2380000-0x23801E8 => Contains _start_arm7 and two more methods, all related to memory mapping.\n0x23801E8-0x238F7F0 => Mapped to 0x37F8000, contains NitroSpMain and functions crucial to execution.\n0x238F7F0-0x23A7068 => Mapped to 0x27E0000, contains everything else that won't fit in the fast WRAM.\n\nNote that while the length for the main EU/NA/JP block is defined as 0x27080 above, after memory mappings, the block located at that address is only a 0x1E8 long ENTRY block, containing 3 functions solely used for the initial memory mapping. The memory following this block is reused and its purpose is undocumented at the moment."
    loadaddress = None
    length = None
    functions = NaItcmArm7Functions
    data = NaItcmArm7Data


class NaItcmArm9Functions:

    Svc_SoftReset = Symbol(None, None, None, "Software interrupt.")

    Svc_WaitByLoop = Symbol(None, None, None, "Software interrupt.")

    Svc_CpuSet = Symbol(None, None, None, "Software interrupt.")

    _start = Symbol(
        None,
        None,
        None,
        "The entrypoint for the ARM9 CPU. This is like the 'main' function for the ARM9 subsystem.\n\nOnce the entry function reaches the end, a constant containing the address to NitroMain is loaded into a register (r1), and a `bx` branch will jump to NitroMain.\n\nNo params.",
    )

    InitI_CpuClear32 = Symbol(None, None, None, "")

    MIi_UncompressBackward = Symbol(
        None,
        None,
        None,
        "Startup routine in the program's crt0 (https://en.wikipedia.org/wiki/Crt0).",
    )

    do_autoload = Symbol(
        None,
        None,
        None,
        "Startup routine in the program's crt0 (https://en.wikipedia.org/wiki/Crt0).",
    )

    StartAutoloadDoneCallback = Symbol(
        None,
        None,
        None,
        "Startup routine in the program's crt0 (https://en.wikipedia.org/wiki/Crt0).",
    )

    init_cp15 = Symbol(None, None, None, "")

    OSi_ReferSymbol = Symbol(
        None,
        None,
        None,
        "Startup routine in the program's crt0 (https://en.wikipedia.org/wiki/Crt0).",
    )

    NitroMain = Symbol(
        None, None, None, "Entrypoint into NitroSDK, the DS devkit library."
    )

    InitMemAllocTable = Symbol(
        None,
        None,
        None,
        "Initializes MEMORY_ALLOCATION_TABLE.\n\nSets up the default memory arena, sets the default memory allocator parameters (calls SetMemAllocatorParams(0, 0)), and does some other stuff.\n\nNo params.",
    )

    SetMemAllocatorParams = Symbol(
        None,
        None,
        None,
        "Sets global parameters for the memory allocator.\n\nThis includes MEMORY_ALLOCATION_ARENA_GETTERS and some other stuff.\n\nDungeon mode uses the default arena getters. Ground mode uses its own arena getters that return custom arenas for some flag values, which are defined in overlay 11 and set (by calling this function) at the start of GroundMainLoop. Note that the sound memory arena is provided explicitly to MemLocateSet in the sound code, so doesn't go through this path.\n\nr0: GetAllocArena function pointer (GetAllocArenaDefault is used if null)\nr1: GetFreeArena function pointer (GetFreeArenaDefault is used if null)",
    )

    GetAllocArenaDefault = Symbol(
        None,
        None,
        None,
        "The default function for retrieving the arena for memory allocations. This function always just returns the initial arena pointer.\n\nr0: initial memory arena pointer, or null\nr1: flags (see MemAlloc)\nreturn: memory arena pointer, or null",
    )

    GetFreeArenaDefault = Symbol(
        None,
        None,
        None,
        "The default function for retrieving the arena for memory freeing. This function always just returns the initial arena pointer.\n\nr0: initial memory arena pointer, or null\nr1: pointer to free\nreturn: memory arena pointer, or null",
    )

    InitMemArena = Symbol(
        None,
        None,
        None,
        "Initializes a new memory arena with the given specifications, and records it in the global MEMORY_ALLOCATION_TABLE.\n\nr0: arena struct to be initialized\nr1: memory region to be owned by the arena, as {pointer, length}\nr2: pointer to block metadata array for the arena to use\nr3: maximum number of blocks that the arena can hold",
    )

    MemAllocFlagsToBlockType = Symbol(
        None,
        None,
        None,
        "Converts the internal alloc flags bitfield (struct mem_block field 0x4) to the block type bitfield (struct mem_block field 0x0).\n\nr0: internal alloc flags\nreturn: block type flags",
    )

    FindAvailableMemBlock = Symbol(
        None,
        None,
        None,
        "Searches through the given memory arena for a block with enough free space.\n\nBlocks are searched in reverse order. For object allocations (i.e., not arenas), the block with the smallest amount of free space that still suffices is returned. For arena allocations, the first satisfactory block found is returned.\n\nr0: memory arena to search\nr1: internal alloc flags\nr2: amount of space needed, in bytes\nreturn: index of the located block in the arena's block array, or -1 if nothing is available",
    )

    SplitMemBlock = Symbol(
        None,
        None,
        None,
        "Given a memory block at a given index, splits off another memory block of the specified size from the end.\n\nSince blocks are stored in an array on the memory arena struct, this is essentially an insertion operation, plus some processing on the block being split and its child.\n\nr0: memory arena\nr1: block index\nr2: internal alloc flags\nr3: number of bytes to split off\nstack[0]: user alloc flags (to assign to the new block)\nreturn: the newly split-off memory block",
    )

    MemAlloc = Symbol(
        None,
        None,
        None,
        "Allocates some memory on the heap, returning a pointer to the starting address.\n\nMemory allocation is done with region-based memory management. See MEMORY_ALLOCATION_TABLE for more information.\n\nThis function is just a wrapper around MemLocateSet.\n\nr0: length in bytes\nr1: flags (see the comment on struct mem_block::user_flags)\nreturn: pointer",
    )

    MemFree = Symbol(
        None,
        None,
        None,
        "Frees heap-allocated memory.\n\nThis function is just a wrapper around MemLocateUnset.\n\nr0: pointer",
    )

    MemArenaAlloc = Symbol(
        None,
        None,
        None,
        "Allocates some memory on the heap and creates a new global memory arena with it.\n\nThe actual allocation part works similarly to the normal MemAlloc.\n\nr0: desired parent memory arena, or null\nr1: length of the arena in bytes\nr2: maximum number of blocks that the arena can hold\nr3: flags (see MemAlloc)\nreturn: memory arena pointer",
    )

    CreateMemArena = Symbol(
        None,
        None,
        None,
        "Creates a new memory arena within a given block of memory.\n\nThis is essentially a wrapper around InitMemArena, accounting for the space needed by the arena metadata.\n\nr0: memory region in which to create the arena, as {pointer, length}\nr1: maximum number of blocks that the arena can hold\nreturn: memory arena pointer",
    )

    MemLocateSet = Symbol(
        None,
        None,
        None,
        "The implementation for MemAlloc.\n\nAt a high level, memory is allocated by choosing a memory arena, looking through blocks in the memory arena until a free one that's large enough is found, then splitting off a new memory block of the needed size.\n\nThis function is not fallible, i.e., it hangs the whole program on failure, so callers can assume it never fails.\n\nThe name for this function comes from the error message logged on failure, and it reflects what the function does: locate an available block of memory and set it up for the caller.\n\nr0: desired memory arena for allocation, or null (MemAlloc passes null)\nr1: length in bytes\nr2: flags (see MemAlloc)\nreturn: pointer to allocated memory",
    )

    MemLocateUnset = Symbol(
        None,
        None,
        None,
        "The implementation for MemFree.\n\nAt a high level, memory is freed by locating the pointer in its memory arena (searching block-by-block) and emptying the block so it's available for future allocations, and merging it with neighboring blocks if they're available.\n\nr0: desired memory arena for freeing, or null (MemFree passes null)\nr1: pointer to free",
    )

    RoundUpDiv256 = Symbol(
        None,
        None,
        None,
        "Divide a number by 256 and round up to the nearest integer.\n\nr0: number\nreturn: number // 256",
    )

    UFixedPoint64CmpLt = Symbol(
        None,
        None,
        None,
        "Compares two unsigned 64-bit fixed-point numbers (16 fraction bits) x and y.\n\nr0: upper 32 bits of x\nr1: lower 32 bits of x\nr2: upper 32 bits of y\nr3: lower 32 bits of y\nreturn: x < y",
    )

    MultiplyByFixedPoint = Symbol(
        None,
        None,
        None,
        "Multiply a signed integer x by a signed binary fixed-point multiplier (8 fraction bits).\n\nr0: x\nr1: multiplier\nreturn: x * multiplier",
    )

    UMultiplyByFixedPoint = Symbol(
        None,
        None,
        None,
        "Multiplies an unsigned integer x by an unsigned binary fixed-point multiplier (8 fraction bits).\n\nr0: x\nr1: multiplier\nreturn: x * multiplier",
    )

    IntToFixedPoint64 = Symbol(
        None,
        None,
        None,
        "Converts a signed integer to a 64-bit fixed-point number (16 fraction bits).\n\nNote that this function appears to be bugged: it appears to try to sign-extend if the input is negative, but in a nonsensical way, checking the sign bit for a 16-bit signed integer, but then doing the sign extension as if the input were a 32-bit signed integer.\n\nr0: [output] 64-bit fixed-point number\nr1: 32-bit signed int",
    )

    FixedPoint64ToInt = Symbol(
        None,
        None,
        None,
        "Converts a 64-bit fixed-point number (16 fraction bits) to a signed integer.\n\nr0: 64-bit fixed-point number\nreturn: 32-bit signed",
    )

    FixedPoint32To64 = Symbol(
        None,
        None,
        None,
        "Converts a 32-bit fixed-point number (8 fraction bits) to a 64-bit fixed point number (16 fraction bits). Sign-extends as necessary.\n\nr0: [output] 64-bit fixed-point number\nr1: 32-bit signed fixed-point number",
    )

    NegateFixedPoint64 = Symbol(
        None,
        None,
        None,
        "Negates a 64-bit fixed-point number (16 fraction bits) in-place.\n\nr0: 64-bit fixed-point number to negate",
    )

    FixedPoint64IsZero = Symbol(
        None,
        None,
        None,
        "Checks whether a 64-bit fixed-point number (16 fraction bits) is zero.\n\nr0: 64-bit fixed-point number\nreturn: bool",
    )

    FixedPoint64IsNegative = Symbol(
        None,
        None,
        None,
        "Checks whether a 64-bit fixed-point number (16 fraction bits) is negative.\n\nr0: 64-bit fixed-point number\nreturn: bool",
    )

    FixedPoint64CmpLt = Symbol(
        None,
        None,
        None,
        "Compares two signed 64-bit fixed-point numbers (16 fraction bits) x and y.\n\nr0: x\nr1: y\nreturn: x < y",
    )

    MultiplyFixedPoint64 = Symbol(
        None,
        None,
        None,
        "Multiplies two signed 64-bit fixed-point numbers (16 fraction bits) x and y.\n\nr0: [output] product (x * y)\nr1: x\nr2: y",
    )

    DivideFixedPoint64 = Symbol(
        None,
        None,
        None,
        "Divides two signed 64-bit fixed-point numbers (16 fraction bits).\n\nReturns the maximum positive value ((INT64_MAX >> 16) + (UINT16_MAX * 2^-16)) if the divisor is zero.\n\nr0: [output] quotient (dividend / divisor)\nr1: dividend\nr2: divisor",
    )

    UMultiplyFixedPoint64 = Symbol(
        None,
        None,
        None,
        "Multiplies two unsigned 64-bit fixed-point numbers (16 fraction bits) x and y.\n\nr0: [output] product (x * y)\nr1: x\nr2: y",
    )

    UDivideFixedPoint64 = Symbol(
        None,
        None,
        None,
        "Divides two unsigned 64-bit fixed-point numbers (16 fraction bits).\n\nReturns the maximum positive value for a signed fixed-point number ((INT64_MAX >> 16) + (UINT16_MAX * 2^-16)) if the divisor is zero.\n\nr0: [output] quotient (dividend / divisor)\nr1: dividend\nr2: divisor",
    )

    AddFixedPoint64 = Symbol(
        None,
        None,
        None,
        "Adds two 64-bit fixed-point numbers (16 fraction bits) x and y.\n\nr0: [output] sum (x + y)\nr1: x\nr2: y",
    )

    ClampedLn = Symbol(
        None,
        None,
        None,
        "The natural log function over the domain of [1, 2047]. The input is clamped to this domain.\n\nr0: [output] ln(x)\nr1: x",
    )

    GetRngSeed = Symbol(None, None, None, "Get the current value of PRNG_SEQUENCE_NUM.")

    SetRngSeed = Symbol(
        None, None, None, "Seed PRNG_SEQUENCE_NUM to a given value.\n\nr0: seed"
    )

    Rand16Bit = Symbol(
        None,
        None,
        None,
        "Computes a pseudorandom 16-bit integer using the general-purpose PRNG.\n\nNote that much of dungeon mode uses its own (slightly higher-quality) PRNG within overlay 29. See overlay29.yml for more information.\n\nRandom numbers are generated with a linear congruential generator (LCG), using a modulus of 2^16, a multiplier of 109, and an increment of 1021. I.e., the recurrence relation is `x = (109*x_prev + 1021) % 2^16`.\n\nThe LCG has a hard-coded seed of 13452 (0x348C), but can be seeded with a call to SetRngSeed.\n\nreturn: pseudorandom int on the interval [0, 65535]",
    )

    RandInt = Symbol(
        None,
        None,
        None,
        "Compute a pseudorandom integer under a given maximum value using the general-purpose PRNG.\n\nThis function relies on a single call to Rand16Bit. Even though it takes a 32-bit integer as input, the number of unique outcomes is capped at 2^16.\n\nr0: high\nreturn: pseudorandom integer on the interval [0, high - 1]",
    )

    RandRange = Symbol(
        None,
        None,
        None,
        "Compute a pseudorandom value between two integers using the general-purpose PRNG.\n\nThis function relies on a single call to Rand16Bit. Even though it takes 32-bit integers as input, the number of unique outcomes is capped at 2^16.\n\nr0: x\nr1: y\nreturn: pseudorandom integer on the interval [x, y - 1]",
    )

    Rand32Bit = Symbol(
        None,
        None,
        None,
        "Computes a random 32-bit integer using the general-purpose PRNG. The upper and lower 16 bits are each generated with a separate call to Rand16Bit (so this function advances the PRNG twice).\n\nreturn: pseudorandom int on the interval [0, 4294967295]",
    )

    RandIntSafe = Symbol(
        None,
        None,
        None,
        "Same as RandInt, except explicitly masking out the upper 16 bits of the output from Rand16Bit (which should be zero anyway).\n\nr0: high\nreturn: pseudorandom integer on the interval [0, high - 1]",
    )

    RandRangeSafe = Symbol(
        None,
        None,
        None,
        "Like RandRange, except reordering the inputs as needed, and explicitly masking out the upper 16 bits of the output from Rand16Bit (which should be zero anyway).\n\nr0: x\nr1: y\nreturn: pseudorandom integer on the interval [min(x, y), max(x, y) - 1]",
    )

    WaitForever = Symbol(
        None,
        None,
        None,
        "Sets some program state and calls WaitForInterrupt in an infinite loop.\n\nThis is called on fatal errors to hang the program indefinitely.\n\nNo params.",
    )

    InterruptMasterDisable = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nreturn: previous state",
    )

    InterruptMasterEnable = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nreturn: previous state",
    )

    InitMemAllocTableVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for InitMemAllocTable.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nNo params.",
    )

    ZInit8 = Symbol(None, None, None, "Zeroes an 8-byte buffer.\n\nr0: ptr")

    PointsToZero = Symbol(
        None,
        None,
        None,
        "Checks whether a pointer points to zero.\n\nr0: ptr\nreturn: bool",
    )

    MemZero = Symbol(None, None, None, "Zeroes a buffer.\n\nr0: ptr\nr1: len")

    MemZero16 = Symbol(
        None,
        None,
        None,
        "Zeros a buffer of 16-bit values.\n\nr0: ptr\nr1: len (# bytes)",
    )

    MemZero32 = Symbol(
        None,
        None,
        None,
        "Zeros a buffer of 32-bit values.\n\nr0: ptr\nr1: len (# bytes)",
    )

    MemsetSimple = Symbol(
        None,
        None,
        None,
        "A simple implementation of the memset(3) C library function.\n\nThis function was probably manually implemented by the developers. See memset for what's probably the real libc function.\n\nr0: ptr\nr1: value\nr2: len (# bytes)",
    )

    Memset32 = Symbol(
        None,
        None,
        None,
        "Fills a buffer of 32-bit values with a given value.\n\nr0: ptr\nr1: value\nr2: len (# bytes)",
    )

    MemcpySimple = Symbol(
        None,
        None,
        None,
        "A simple implementation of the memcpy(3) C library function.\n\nThis function was probably manually implemented by the developers. See memcpy for what's probably the real libc function.\n\nThis function copies from src to dst in backwards byte order, so this is safe to call for overlapping src and dst if src <= dst.\n\nr0: dest\nr1: src\nr2: n",
    )

    Memcpy16 = Symbol(
        None,
        None,
        None,
        "Copies 16-bit values from one buffer to another.\n\nr0: dest\nr1: src\nr2: n (# bytes)",
    )

    Memcpy32 = Symbol(
        None,
        None,
        None,
        "Copies 32-bit values from one buffer to another.\n\nr0: dest\nr1: src\nr2: n (# bytes)",
    )

    TaskProcBoot = Symbol(
        None,
        None,
        None,
        "Probably related to booting the game?\n\nThis function prints the debug message 'task proc boot'.\n\nNo params.",
    )

    EnableAllInterrupts = Symbol(
        None,
        None,
        None,
        "Sets the Interrupt Master Enable (IME) register to 1, which enables all CPU interrupts (if enabled in the Interrupt Enable (IE) register).\n\nSee https://problemkaputt.de/gbatek.htm#dsiomaps.\n\nreturn: old value in the IME register",
    )

    GetTime = Symbol(
        None,
        None,
        None,
        "Seems to get the current (system?) time as an IEEE 754 floating-point number.\n\nreturn: current time (maybe in seconds?)",
    )

    DisableAllInterrupts = Symbol(
        None,
        None,
        None,
        "Sets the Interrupt Master Enable (IME) register to 0, which disables all CPU interrupts (even if enabled in the Interrupt Enable (IE) register).\n\nSee https://problemkaputt.de/gbatek.htm#dsiomaps.\n\nreturn: old value in the IME register",
    )

    SoundResume = Symbol(
        None,
        None,
        None,
        "Probably resumes the sound player if paused?\n\nThis function prints the debug string 'sound resume'.",
    )

    CardPullOutWithStatus = Symbol(
        None,
        None,
        None,
        "Probably aborts the program with some status code? It seems to serve a similar purpose to the exit(3) function.\n\nThis function prints the debug string 'card pull out %d' with the status code.\n\nr0: status code",
    )

    CardPullOut = Symbol(
        None,
        None,
        None,
        "Sets some global flag that probably triggers system exit?\n\nThis function prints the debug string 'card pull out'.\n\nNo params.",
    )

    CardBackupError = Symbol(
        None,
        None,
        None,
        "Sets some global flag that maybe indicates a save error?\n\nThis function prints the debug string 'card backup error'.\n\nNo params.",
    )

    HaltProcessDisp = Symbol(
        None,
        None,
        None,
        "Maybe halts the process display?\n\nThis function prints the debug string 'halt process disp %d' with the status code.\n\nr0: status code",
    )

    OverlayIsLoaded = Symbol(
        None,
        None,
        None,
        "Checks if an overlay with a certain group ID is currently loaded.\n\nSee the LOADED_OVERLAY_GROUP_* data symbols or enum overlay_group_id in the C headers for a mapping between group ID and overlay number.\n\nr0: group ID of the overlay to check. A group ID of 0 denotes no overlay, and the return value will always be true in this case.\nreturn: bool",
    )

    LoadOverlay = Symbol(
        None,
        None,
        None,
        "Loads an overlay from ROM by its group ID.\n\nSee the LOADED_OVERLAY_GROUP_* data symbols or enum overlay_group_id in the C headers for a mapping between group ID and overlay number.\n\nr0: group ID of the overlay to load",
    )

    UnloadOverlay = Symbol(
        None,
        None,
        None,
        "Unloads an overlay from ROM by its group ID.\n\nSee the LOADED_OVERLAY_GROUP_* data symbols or enum overlay_group_id in the C headers for a mapping between group ID and overlay number.\n\nr0: group ID of the overlay to unload\nothers: ?",
    )

    Rgb8ToRgb5 = Symbol(
        None,
        None,
        None,
        "Transform the input rgb8 color to a rgb5 color\n\nr0: pointer to target rgb5 (2 bytes, aligned to LSB)\nr1: pointer to source rgb8",
    )

    EuclideanNorm = Symbol(
        None,
        None,
        None,
        "Computes the Euclidean norm of a two-component integer array, sort of like hypotf(3).\n\nr0: integer array [x, y]\nreturn: sqrt(x*x + y*y)",
    )

    ClampComponentAbs = Symbol(
        None,
        None,
        None,
        "Clamps the absolute values in a two-component integer array.\n\nGiven an integer array [x, y] and a maximum absolute value M, clamps each element of the array to M such that the output array is [min(max(x, -M), M), min(max(y, -M), M)].\n\nr0: 2-element integer array, will be mutated\nr1: max absolute value",
    )

    GetHeldButtons = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: controller\nr1: btn_ptr\nreturn: any_activated",
    )

    GetPressedButtons = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: controller\nr1: btn_ptr\nreturn: any_activated",
    )

    GetReleasedStylus = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: stylus_ptr\nreturn: any_activated",
    )

    KeyWaitInit = Symbol(
        None,
        None,
        None,
        "Implements (most of?) SPECIAL_PROC_KEY_WAIT_INIT (see ScriptSpecialProcessCall).\n\nNo params.",
    )

    DataTransferInit = Symbol(
        None,
        None,
        None,
        "Initializes data transfer mode to get data from the ROM cartridge.\n\nNo params.",
    )

    DataTransferStop = Symbol(
        None,
        None,
        None,
        "Finalizes data transfer from the ROM cartridge.\n\nThis function must always be called if DataTransferInit was called, or the game will crash.\n\nNo params.",
    )

    FileInitVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for FileInit.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nr0: file_stream pointer",
    )

    FileOpen = Symbol(
        None,
        None,
        None,
        "Opens a file from the ROM file system at the given path, sort of like C's fopen(3) library function.\n\nr0: file_stream pointer\nr1: file path string",
    )

    FileGetSize = Symbol(
        None,
        None,
        None,
        "Gets the size of an open file.\n\nr0: file_stream pointer\nreturn: file size",
    )

    FileRead = Symbol(
        None,
        None,
        None,
        "Reads the contents of a file into the given buffer, and moves the file cursor accordingly.\n\nData transfer mode must have been initialized (with DataTransferInit) prior to calling this function. This function looks like it's doing something akin to calling read(2) or fread(3) in a loop until all the bytes have been successfully read.\n\nNote: If code is running from IRQ mode, it appears that FileRead hangs the game. When the processor mode is forced into SYSTEM mode FileRead once again works, so it appears that ROM access only works in certain processor modes. Note that forcing the processor into a different mode is generally a bad idea and should be avoided as it will easily corrupt that processor mode's states.\n\nr0: file_stream pointer\nr1: [output] buffer\nr2: number of bytes to read\nreturn: number of bytes read",
    )

    FileSeek = Symbol(
        None,
        None,
        None,
        "Sets a file stream's position indicator.\n\nThis function has the a similar API to the fseek(3) library function from C, including using the same codes for the `whence` parameter:\n- SEEK_SET=0\n- SEEK_CUR=1\n- SEEK_END=2\n\nr0: file_stream pointer\nr1: offset\nr2: whence",
    )

    FileClose = Symbol(
        None,
        None,
        None,
        "Closes a file.\n\nData transfer mode must have been initialized (with DataTransferInit) prior to calling this function.\n\nNote: It is possible to keep a file stream open even if data transfer mode has been stopped, in which case the file stream can be used again if data transfer mode is reinitialized.\n\nr0: file_stream pointer",
    )

    UnloadFile = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: addr_ptr",
    )

    LoadFileFromRom = Symbol(
        None,
        None,
        None,
        "Loads a file from ROM by filepath into a heap-allocated buffer.\n\nr0: [output] pointer to an IO struct {ptr, len}\nr1: file path string pointer\nr2: flags",
    )

    UpdateFadeStatus = Symbol(
        None,
        None,
        None,
        "Updates the given screen_fade struct to initiate a fade for example.\n\nIn addition to initiating a fade this is called when a fade out is complete to set a flag for that in the struct.\n\nr0: screen_fade\nr1: probably the type of the fade\nr2: duration",
    )

    HandleFades = Symbol(
        None,
        None,
        None,
        "Handles updating the screen_fade struct in all modes except dungeon mode.\n\nGets called every frame for both screens, analyzes the fade_struct and does appropriate actions. If there's a fade in progress, it calculates the brightness on the next frame and updates the structure accordingly.\n\nr0: screen_fade\nreturn: bool",
    )

    GetFadeStatus = Symbol(
        None,
        None,
        None,
        "Returns 1 if fading to black, 2 if fading to white, 0 otherwise.\n\nr0: screen_fade\nreturn: int",
    )

    InitDebug = Symbol(
        None,
        None,
        None,
        "Would have initialized debugging-related things, if they were not removed.\nAs for the release version, does nothing but set DEBUG_IS_INITIALIZED to true.",
    )

    InitDebugFlag = Symbol(
        None,
        None,
        None,
        "Would have initialized the debug flags.\nDoes nothing in release binary.",
    )

    GetDebugFlag = Symbol(
        None,
        None,
        None,
        "Should return the value of the specified debug flag. Just returns 0 in the final binary.\n\nr0: flag ID\nreturn: flag value",
    )

    SetDebugFlag = Symbol(
        None,
        None,
        None,
        "Should set the value of a debug flag. A no-op in the final binary.\n\nr0: flag ID\nr1: flag value",
    )

    InitDebugStripped6 = Symbol(
        None,
        None,
        None,
        "Does nothing, only called in the debug initialization function.",
    )

    AppendProgPos = Symbol(
        None,
        None,
        None,
        "Write a base message into a string and append the file name and line number to the end in the format 'file = '%s'  line = %5d\n'.\n\nIf no program position info is given, 'ProgPos info NULL\n' is appended instead.\n\nr0: [output] str\nr1: program position info\nr2: base message\nreturn: number of characters printed, excluding the null-terminator",
    )

    InitDebugStripped5 = Symbol(
        None,
        None,
        None,
        "Does nothing, only called in the debug initialization function.",
    )

    DebugPrintTrace = Symbol(
        None,
        None,
        None,
        "Would log a printf format string tagged with the file name and line number in the debug binary.\n\nThis still constructs the string, but doesn't actually do anything with it in the final binary.\n\nIf message is a null pointer, the string '  Print  ' is used instead.\n\nr0: message\nr1: program position info (can be null)",
    )

    DebugDisplay = Symbol(
        None,
        None,
        None,
        "Would display a printf format string on the top screen in the debug binary.\n\nThis still constructs the string with vsprintf, but doesn't actually do anything with it in the final binary.\n\nIdentical to DebugPrint0 in release builds.\n\nr0: format\n...: variadic",
    )

    DebugPrint0 = Symbol(
        None,
        None,
        None,
        "Would log a printf format string in the debug binary.\n\nThis still constructs the string with vsprintf, but doesn't actually do anything with it in the final binary.\n\nIdentical to DebugDisplay in release builds.\n\nr0: format\n...: variadic",
    )

    InitDebugLogFlag = Symbol(
        None,
        None,
        None,
        "Would have initialized the debug log flags.\nDoes nothing in release binary.",
    )

    GetDebugLogFlag = Symbol(
        None,
        None,
        None,
        "Should return the value of the specified debug log flag. Just returns 0 in the final binary.\n\nr0: flag ID\nreturn: flag value",
    )

    SetDebugLogFlag = Symbol(
        None,
        None,
        None,
        "Should set the value of a debug log flag. A no-op in the final binary.\n\nr0: flag ID\nr1: flag value",
    )

    DebugPrint = Symbol(
        None,
        None,
        None,
        "Would log a printf format string in the debug binary. A no-op in the final binary.\n\nr0: log level\nr1: format\n...: variadic",
    )

    InitDebugStripped4 = Symbol(
        None,
        None,
        None,
        "Does nothing, only called in the debug initialization function.",
    )

    InitDebugStripped3 = Symbol(
        None,
        None,
        None,
        "Does nothing, only called in the debug initialization function.",
    )

    InitDebugStripped2 = Symbol(
        None,
        None,
        None,
        "Does nothing, only called in the debug initialization function.",
    )

    InitDebugStripped1 = Symbol(
        None,
        None,
        None,
        "Does nothing, only called in the debug initialization function.",
    )

    FatalError = Symbol(
        None,
        None,
        None,
        "Logs some debug messages, then hangs the process.\n\nThis function is called in lots of places to bail on a fatal error. Looking at the static data callers use to fill in the program position info is informative, as it tells you the original file name (probably from the standard __FILE__ macro) and line number (probably from the standard __LINE__ macro) in the source code.\n\nr0: program position info\nr1: format\n...: variadic",
    )

    OpenAllPackFiles = Symbol(
        None,
        None,
        None,
        "Open the 6 files at PACK_FILE_PATHS_TABLE into PACK_FILES_OPENED. Called during game initialization.\n\nNo params.",
    )

    GetFileLengthInPackWithPackNb = Symbol(
        None,
        None,
        None,
        "Call GetFileLengthInPack after looking up the global Pack archive by its number\n\nr0: pack file number\nr1: file number\nreturn: size of the file in bytes from the Pack Table of Content",
    )

    LoadFileInPackWithPackId = Symbol(
        None,
        None,
        None,
        "Call LoadFileInPack after looking up the global Pack archive by its identifier\n\nr0: pack file identifier\nr1: file index\nr2: [output] target buffer\nreturn: number of read bytes (identical to the length of the pack from the Table of Content)",
    )

    AllocAndLoadFileInPack = Symbol(
        None,
        None,
        None,
        "Allocate a file and load a file from the pack archive inside.\nThe data pointed by the pointer in the output need to be freed once is not needed anymore.\n\nr0: pack file identifier\nr1: file index\nr2: [output] result struct (will contain length and pointer)\nr3: allocation flags",
    )

    OpenPackFile = Symbol(
        None,
        None,
        None,
        "Open a Pack file, to be read later. Initialize the output structure.\n\nr0: [output] pack file struct\nr1: file name",
    )

    GetFileLengthInPack = Symbol(
        None,
        None,
        None,
        "Get the length of a file entry from a Pack archive\n\nr0: pack file struct\nr1: file index\nreturn: size of the file in bytes from the Pack Table of Content",
    )

    LoadFileInPack = Symbol(
        None,
        None,
        None,
        "Load the indexed file from the Pack archive, itself loaded from the ROM.\n\nr0: pack file struct\nr1: [output] target buffer\nr2: file index\nreturn: number of read bytes (identical to the length of the pack from the Table of Content)",
    )

    GetDungeonResultMsg = Symbol(
        None,
        None,
        None,
        "Gets the message that is shown on the dungeon results ('The Last Outing') screen, right after the leader's name.\n\nr0: Damage source value to use when displaying the cause of fainting or the result of the expedition\nr1: [output] Buffer where the resulting message will be stored\nr2: Buffer size\nr3: (?) Seems to point to a buffer",
    )

    GetDamageSource = Symbol(
        None,
        None,
        None,
        "Gets the damage source for a given move-item combination.\n\nIf there's no item, the source is the move ID. If the item is an orb, return DAMAGE_SOURCE_ORB_ITEM. Otherwise, return DAMAGE_SOURCE_NON_ORB_ITEM.\n\nr0: move ID\nr1: item ID\nreturn: damage source",
    )

    GetItemCategoryVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for GetItemCategory.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nr0: Item ID\nreturn: Category ID",
    )

    GetItemMoveId16 = Symbol(
        None,
        None,
        None,
        "Wraps GetItemMoveId, ensuring that the return value is 16-bit.\n\nr0: item ID\nreturn: move ID",
    )

    IsThrownItem = Symbol(
        None,
        None,
        None,
        "Checks if a given item ID is a thrown item (CATEGORY_THROWN_LINE or CATEGORY_THROWN_ARC).\n\nr0: item ID\nreturn: bool",
    )

    IsNotMoney = Symbol(
        None,
        None,
        None,
        "Checks if an item ID is not ITEM_POKE.\n\nr0: item ID\nreturn: bool",
    )

    IsEdible = Symbol(
        None,
        None,
        None,
        "Checks if an item has an item category of CATEGORY_BERRIES_SEEDS_VITAMINS or CATEGORY_FOOD_GUMMIES.\n\nr0: item ID\nreturn: bool",
    )

    IsHM = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item ID\nreturn: bool",
    )

    IsGummi = Symbol(
        None, None, None, "Checks if an item is a Gummi.\n\nr0: item ID\nreturn: bool"
    )

    IsAuraBow = Symbol(
        None,
        None,
        None,
        "Checks if an item is one of the aura bows received at the start of the game.\n\nr0: item ID\nreturn: bool",
    )

    IsLosableItem = Symbol(
        None,
        None,
        None,
        "Checks if an item can be lost after fainting in a dungeon. Specifically calls IsAuraBow and checks item::f_in_shop\nso that the player can't keep an aura bow they haven't paid for yet.\n\nr0: item pointer\nreturn: bool",
    )

    IsTreasureBox = Symbol(
        None,
        None,
        None,
        "Checks if the given item ID is a treasure box\n\nIn particular, it checks if the category of the item is CATEGORY_TREASURE_BOXES_1, CATEGORY_TREASURE_BOXES_2 or CATEGORY_TREASURE_BOXES_3.\n\nr0: item ID\nreturn: True if the item is a treasure box, false otherwise",
    )

    IsStorableItem = Symbol(
        None,
        None,
        None,
        "Checks if an item can be put into storage. Specifically checks for the Wonder Egg, Poke, and Used TMs. Used TMs\nlikely can't be stored because the move the TM teaches would be lost when sent to storage.\n\nr0: item_id\nreturn: bool",
    )

    IsShoppableItem = Symbol(
        None,
        None,
        None,
        "Checks if an item can be bought and sold from a Kecleon shop. Includes items like the Gold Thorn, Poke, Golden\nMask, Amber Tear, etc. Also has a special check to make sure an item's buy and sell price is more than 0.\n\nr0: item_id\nreturn: bool",
    )

    IsValidTargetItem = Symbol(
        None,
        None,
        None,
        "Checks if an item is a valid target item for missions. Returns true for any item less than ITEM_UNNAMED_0x16B.\nAppears to check a list for valid items above ITEM_UNNAMED_0x16B, but the list is empty?\n\nr0: item_id\nreturn: bool",
    )

    IsItemUsableNow = Symbol(
        None,
        None,
        None,
        "Checks if an item can be used right now. Returns true for all items that are not in a shop. If the item is in a\nshop, specifically checks for TMs/HMs and items that provide permanent buffs (Gummis, Sitrus Berry, Ginseng, etc).\n\nr0: item pointer\nreturn: bool",
    )

    IsTicketItem = Symbol(
        None,
        None,
        None,
        "Checks if an item is a ticket that can be used in the recycle shop (ITEM_PRIZE_TICKET, ITEM_SILVER_TICKET,\nITEM_GOLD_TICKET, and ITEM_PRISM_TICKET).\n\nr0: item_id\nreturn: bool",
    )

    InitItem = Symbol(
        None,
        None,
        None,
        "Initialize an item struct with the given information.\n\nThis will resolve the quantity based on the item type. For Poké, the quantity code will always be set to 1. For thrown items, the quantity code will be randomly generated on the range of valid quantities for that item type. For non-stackable items, the quantity code will always be set to 0. Otherwise, the quantity will be assigned from the quantity argument.\n\nr0: pointer to item to initialize\nr1: item ID\nr2: quantity\nr3: sticky flag",
    )

    InitStandardItem = Symbol(
        None,
        None,
        None,
        "Wrapper around InitItem with quantity set to 0.\n\nr0: pointer to item to initialize\nr1: item ID\nr2: sticky flag",
    )

    InitBulkItem = Symbol(
        None,
        None,
        None,
        "Initialize a struct bulk_item with the given information.\n\nThis will resolve the quantity based on the item type. For Poké, the quantity code will always be set to 1. For thrown items, the quantity code will be randomly generated on the range of valid quantities for that item type. For non-stackable items, the quantity code will always be set to 0.\n\nr0: pointer to bulk item to initialize\nr1: item ID",
    )

    BulkItemToItem = Symbol(
        None,
        None,
        None,
        "Convert a bulk_item into an equivalent item.\n\nr0: pointer to item to initialize\nr1: pointer to bulk_item",
    )

    ItemToBulkItem = Symbol(
        None,
        None,
        None,
        "Convert an item into an equivalent bulk_item.\n\nr0: pointer to bulk_item to initialize\nr1: pointer to item",
    )

    GetDisplayedBuyPrice = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item\nreturn: buy price",
    )

    GetDisplayedSellPrice = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item\nreturn: sell price",
    )

    GetActualBuyPrice = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item\nreturn: buy price",
    )

    GetActualSellPrice = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item\nreturn: sell price",
    )

    FindItemInInventory = Symbol(
        None,
        None,
        None,
        "Returns x if item_id is at position x in the bag\nReturns 0x8000+x if item_id is at position x in storage\nReturns -1 if item is not found\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: item_id\nreturn: inventory index",
    )

    SprintfStatic = Symbol(
        None,
        None,
        None,
        "Functionally the same as sprintf, just defined statically in many different places.\n\nSince this is essentially just a wrapper around vsprintf(3), this function was probably statically defined in a header somewhere and included in a bunch of different places. See the actual sprintf for the one in libc.\n\nr0: str\nr1: format\n...: variadic\nreturn: number of characters printed, excluding the null-terminator",
    )

    ItemZInit = Symbol(None, None, None, "Zero-initializes an item struct.\n\nr0: item")

    AreItemsEquivalent = Symbol(
        None,
        None,
        None,
        "Checks whether two items are equivalent and only checks the bitflags specified by the bitmask.\n\nr0: item\nr1: item\nr2: bitmask\nreturn: bool",
    )

    WriteItemsToSave = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: start_address\nr1: total_length\nreturn: ?",
    )

    ReadItemsFromSave = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: start_address\nr1: total_length\nreturn: ?",
    )

    IsItemAvailableInDungeonGroup = Symbol(
        None,
        None,
        None,
        "Checks one specific bit from AVAILABLE_ITEMS_IN_GROUP_TABLE?\n\nr0: dungeon ID\nr1: item ID\nreturn: bool",
    )

    GetItemIdFromList = Symbol(
        None,
        None,
        None,
        "category_num and item_num are numbers in range 0-10000\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: list_id\nr1: category_num\nr2: item_num\nreturn: item ID",
    )

    NormalizeTreasureBox = Symbol(
        None,
        None,
        None,
        "If the item is a treasure box return the first version of the treasure box in the item list.\nOtherwise, return the same item ID.\n\nr0: item ID\nreturn: normalized item ID",
    )

    SortItemList = Symbol(
        None,
        None,
        None,
        "Attempts to combine stacks of throwable items, sort the list, and then remove empty items.\nAppears to use selection sort to sort the list in place.\n\nr0: item array\nr1: number of items in array",
    )

    RemoveEmptyItems = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: list_pointer\nr1: size",
    )

    LoadItemPspi2n = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nNo params."
    )

    GetExclusiveItemType = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item ID\nreturn: ?",
    )

    GetExclusiveItemOffsetEnsureValid = Symbol(
        None,
        None,
        None,
        "Gets the exclusive item offset, which is the item ID relative to that of the first exclusive item, the Prism Ruff.\n\nIf the given item ID is not a valid item ID, ITEM_PLAIN_SEED (0x55) is returned. This is a bug, since 0x55 is the valid exclusive item offset for the Icy Globe.\n\nr0: item ID\nreturn: offset",
    )

    IsItemValid = Symbol(
        None,
        None,
        None,
        "Checks if an item is valid given its ID.\n\nIn particular, checks if the 'is valid' flag is set on its item_p.bin entry.\n\nr0: item ID\nreturn: bool",
    )

    GetExclusiveItemParameter = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item ID\nreturn: ?",
    )

    GetItemCategory = Symbol(
        None,
        None,
        None,
        "Returns the category of the specified item\n\nr0: Item ID\nreturn: Item category",
    )

    EnsureValidItem = Symbol(
        None,
        None,
        None,
        "Checks if the given item ID is valid (using IsItemValid). If so, return the given item ID. Otherwise, return ITEM_PLAIN_SEED.\n\nr0: item ID\nreturn: valid item ID",
    )

    GetItemName = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item ID\nreturn: item name",
    )

    GetItemNameFormatted = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: [output] name\nr1: item_id\nr2: flag\nr3: flag2",
    )

    GetItemBuyPrice = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item ID\nreturn: buy price",
    )

    GetItemSellPrice = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item ID\nreturn: sell price",
    )

    GetItemSpriteId = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item ID\nreturn: sprite ID",
    )

    GetItemPaletteId = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item ID\nreturn: palette ID",
    )

    GetItemActionName = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item ID\nreturn: action name ID",
    )

    GetThrownItemQuantityLimit = Symbol(
        None,
        None,
        None,
        "Get the minimum or maximum quantity for a given thrown item ID.\n\nr0: item ID\nr1: 0 for minimum, 1 for maximum\nreturn: minimum/maximum quantity for the given item ID",
    )

    GetItemMoveId = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item ID\nreturn: move ID",
    )

    TestItemAiFlag = Symbol(
        None,
        None,
        None,
        "Used to check the AI flags for an item. Tests bit 7 if r1 is 0, bit 6 if r1 is 1, bit\n5 otherwise.\n\nr0: item ID\nr1: bit_id\nreturn: bool",
    )

    IsItemInTimeDarkness = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item ID\nreturn: bool",
    )

    IsItemValidVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for IsItemValid.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nr0: item ID\nreturn: bool",
    )

    SetActiveInventoryToMain = Symbol(
        None,
        None,
        None,
        "Changes the currently active inventory to TEAM_MAIN.\n\nNo params.",
    )

    AllInventoriesZInit = Symbol(
        None,
        None,
        None,
        "Initializes all inventories (TEAM_MAIN, TEAM_SPECIAL_EPISODE, TEAM_RESCUE) to empty and sets the active inventory\nto TEAM_MAIN.\n\nNo params.",
    )

    SpecialEpisodeInventoryZInit = Symbol(
        None,
        None,
        None,
        "Initializes the TEAM_SPECIAL_EPISODE inventory to be empty.\n\nNo params.",
    )

    RescueInventoryZInit = Symbol(
        None,
        None,
        None,
        "Initializes the TEAM_RESCUE inventory to be empty.\n\nNo params.",
    )

    SetActiveInventory = Symbol(
        None,
        None,
        None,
        "Changes the currently active inventory. Has one for the main team, rescue team, and the special\nepisode team.\n\nr0: team ID",
    )

    GetMoneyCarried = Symbol(
        None,
        None,
        None,
        "Gets the amount of money the player is carrying.\n\nreturn: value",
    )

    SetMoneyCarried = Symbol(
        None,
        None,
        None,
        "Sets the amount of money the player is carrying, clamping the value to the range [0, MAX_MONEY_CARRIED].\n\nr0: new value",
    )

    AddMoneyCarried = Symbol(
        None,
        None,
        None,
        "Adds the amount of money to the player's current amount of money. Just calls\nSetMoneyCarried with the current money + money gained.\n\nr0: money gained (can be negative)",
    )

    GetCurrentBagCapacity = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nreturn: bag capacity",
    )

    IsBagFull = Symbol(
        None,
        None,
        None,
        "Implements SPECIAL_PROC_IS_BAG_FULL (see ScriptSpecialProcessCall).\n\nreturn: bool",
    )

    GetNbItemsInBag = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nreturn: # items",
    )

    CountNbItemsOfTypeInBag = Symbol(
        None,
        None,
        None,
        "Returns the number of items of the given kind in the bag\n\nr0: item ID\nreturn: count",
    )

    CountItemTypeInBag = Symbol(
        None,
        None,
        None,
        "Implements SPECIAL_PROC_COUNT_ITEM_TYPE_IN_BAG (see ScriptSpecialProcessCall).\n\nIrdkwia's notes: Count also stackable\n\nr0: item ID\nreturn: number of items of the specified ID in the bag",
    )

    IsItemInBag = Symbol(
        None,
        None,
        None,
        "Checks if an item is in the player's bag.\n\nr0: item ID\nreturn: bool",
    )

    IsItemWithFlagsInBag = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item ID\nr1: flags\nreturn: bool",
    )

    IsItemInTreasureBoxes = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item ID\nreturn: bool",
    )

    IsHeldItemInBag = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item\nreturn: bool",
    )

    IsItemForSpecialSpawnInBag = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nreturn: bool",
    )

    HasStorableItems = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nreturn: bool",
    )

    GetItemIndex = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item_ptr\nreturn: index",
    )

    GetEquivItemIndex = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item_ptr\nreturn: index",
    )

    GetEquippedThrowableItem = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nreturn: index",
    )

    GetFirstUnequippedItemOfType = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item ID\nreturn: index",
    )

    CopyItemAtIdx = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: index\nr1: [output] item_ptr\nreturn: exists",
    )

    GetItemAtIdx = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: index\nreturn: item pointer",
    )

    RemoveEmptyItemsInBag = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nNo params."
    )

    RemoveItemNoHole = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: index\nreturn: ?",
    )

    RemoveItem = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nr0: index"
    )

    RemoveHeldItemNoHole = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: held_index",
    )

    RemoveItemByIdAndStackNoHole = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item_ptr\nreturn: ?",
    )

    RemoveEquivItem = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item_ptr\nreturn: ?",
    )

    RemoveEquivItemNoHole = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item_ptr\nreturn: ?",
    )

    DecrementStackItem = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item_ptr\nreturn: ?",
    )

    RemoveItemNoHoleCheck = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: index\nreturn: ?",
    )

    RemoveFirstUnequippedItemOfType = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item ID\nreturn: ?",
    )

    RemoveAllItems = Symbol(
        None,
        None,
        None,
        "WARNING! Does not remove from party items\n\nNote: unverified, ported from Irdkwia's notes",
    )

    RemoveAllItemsStartingAt = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nr0: index"
    )

    SpecialProcAddItemToBag = Symbol(
        None,
        None,
        None,
        "Implements SPECIAL_PROC_ADD_ITEM_TO_BAG (see ScriptSpecialProcessCall).\n\nr0: pointer to an owned_item\nreturn: bool",
    )

    AddItemToBagNoHeld = Symbol(
        None,
        None,
        None,
        "A wrapper around AddItemToBag with held_by being 0 (no holder).\n\nr0: item_str\nreturn: bool item was successfully added to the bag",
    )

    AddItemToBag = Symbol(
        None,
        None,
        None,
        "Attempts to add an item to the bag.\n\nr0: item_str\nr1: held_by\nreturn: bool item was successfully added to the bag",
    )

    CleanStickyItemsInBag = Symbol(
        None,
        None,
        None,
        "Removes the sticky flag from all the items currently in the bag.\n\nNo params.",
    )

    CountStickyItemsInBag = Symbol(
        None,
        None,
        None,
        "Counts the number of sticky items currently in the bag.\n\nreturn: number of sticky items",
    )

    TransmuteHeldItemInBag = Symbol(
        None,
        None,
        None,
        "Looks for an item in the bag that has the same holder (held_by) as the transmute item and convert\ntheir equivalent item in the treasure bag into the transmute item. The monster's held item on\ntheir struct should be updated accordingly directly before or after calling this function.\n\nr0: transmute_item\nreturn: bool whether or not the item could be transmuted",
    )

    SetFlagsForHeldItemInBag = Symbol(
        None,
        None,
        None,
        "Looks for an item in the bag that has the holder (held_by) as the item and make their equivalent\nitem in the treasure bag sticky. The monster's held item on their struct should be updated\naccordingly directly before or after calling this function. Mostly used for making existing items\nsticky.\n\nr0: held_by\nr1: item bitflags",
    )

    RemoveHolderForItemInBag = Symbol(
        None,
        None,
        None,
        "Looks for an item in the bag that is equivalent and make the holder none. The monster's held item\non their struct should be updated accordingly directly before or after calling this function.\n\nr0: pointer to an item",
    )

    SetHolderForItemInBag = Symbol(
        None,
        None,
        None,
        "Modifies the item at the index to be held by the monster specified and updates the item with the\nholder as well. This only modifies the flags and held_by of the item.\n\nr0: item index\nr1: pointer to an item\nr2: held_by",
    )

    SortItemsInBag = Symbol(
        None,
        None,
        None,
        "Sorts the current items in the item bag but first checks if any Poke is in the bag to remove. If\nPoke is found, add it to money carried.\n\nNo params.",
    )

    RemovePokeItemsInBag = Symbol(
        None,
        None,
        None,
        "Checks the bag for any Poke and removes it after adding it to money carried.\n\nNo params.",
    )

    IsStorageFull = Symbol(
        None,
        None,
        None,
        "Checks if the storage is full accounting for the current rank of the team.\nImplements SPECIAL_PROC_0x39 (see ScriptSpecialProcessCall).\n\nreturn: bool",
    )

    CountNbOfItemsInStorage = Symbol(
        None,
        None,
        None,
        "Counts the number of items currently in storage (including invalid items).\n\nreturn: number of items in storage",
    )

    CountNbOfValidItemsInStorage = Symbol(
        None,
        None,
        None,
        "Counts the number of items currently in storage that are valid.\n\nreturn: number of valid items in storage",
    )

    CountNbOfValidItemsInTimeDarknessInStorage = Symbol(
        None,
        None,
        None,
        "Counts the number of items currently in storage that are valid and in time and darkness.\n\nreturn: number of valid items in storage",
    )

    CountNbItemsOfTypeInStorage = Symbol(
        None,
        None,
        None,
        "Counts the number of instances of an item in storage not accounting for the number of items\nin a stack.\n\nr0: item ID\nreturn: count",
    )

    CountItemTypeInStorage = Symbol(
        None,
        None,
        None,
        "Counts the number of a certain item in storage accounting for stackable items.\nImplements SPECIAL_PROC_COUNT_ITEM_TYPE_IN_STORAGE (see ScriptSpecialProcessCall).\n\nr0: pointer to an bulk_item\nreturn: number of items of the specified ID in storage",
    )

    GetEquivBulkItemIdxInStorage = Symbol(
        None,
        None,
        None,
        "Checks for a storage item equivalent to the bulk_item and returns the index of the item in storage.\nReturns -1 if unable to find an equivalent item.\n\nr0: pointer to a bulk_item\nreturn: index in storage",
    )

    ConvertStorageItemAtIdxToBulkItem = Symbol(
        None,
        None,
        None,
        "Get an item in storage and converts it into an equivalent bulk_item. This does not remove the\nitem from storage.\n\nr0: item index\nr1: [output] pointer to a bulk_item\nreturn: bool whether or not the item id is not 0",
    )

    ConvertStorageItemAtIdxToItem = Symbol(
        None,
        None,
        None,
        "Get an item in storage and converts it into an equivalent item. The item does NOT have the exists\nflag set to true. This does not remove the item from storage.\n\nr0: item index\nr1: [output] pointer to an item\nreturn: bool whether or not the item id is not 0",
    )

    RemoveItemAtIdxInStorage = Symbol(
        None,
        None,
        None,
        "Remove an item at the specified index from storage.\n\nr0: storage item idx\nreturn: bool whether or not the item was removed (fails if there is no storage item at the index)",
    )

    RemoveBulkItemInStorage = Symbol(
        None,
        None,
        None,
        "Removes a storage item equivalent to the bulk_item passed from storage.\nProbably? Implements SPECIAL_PROC_REMOVE_ITEM_TYPE_IN_STORAGE (see ScriptSpecialProcessCall).\n\nr0: pointer to a bulk_item\nreturn: bool whether an item was removed",
    )

    RemoveItemInStorage = Symbol(
        None,
        None,
        None,
        "Removes a storage item equivalent to the item passed from storage.\n\nr0: pointer to an item\nreturn: bool whether an item was removed",
    )

    StorageZInit = Symbol(
        None, None, None, "Initializes the storage to be empty.\n\nNo params."
    )

    AddBulkItemToStorage = Symbol(
        None,
        None,
        None,
        "Attempts to add the bulk_item to storage.\nImplements SPECIAL_PROC_ADD_ITEM_TO_STORAGE (see ScriptSpecialProcessCall).\n\nr0: pointer to a bulk_item\nreturn: bool whether an item was added",
    )

    AddItemToStorage = Symbol(
        None,
        None,
        None,
        "Attempts to add the item to storage.\n\nr0: pointer to an item\nreturn: bool whether an item was added",
    )

    SortItemsInStorage = Symbol(
        None,
        None,
        None,
        "Sorts the item in storage by making converting them into normal items in a temporary list and\nusing SortItemList on them. After, it puts the list of items back into storage. This may also have\nanother use or do something broader than just sorting because it outputs a bool array.\n\nr0: [output] bool array?\nr1: number of items to sort (usually just the current size of storage)",
    )

    AllKecleonShopsZInit = Symbol(
        None,
        None,
        None,
        "Empties the Kecleon shop for both TEAM_MAIN and TEAM_SPECIAL_EPISODE. TEAM_RESCUE does not appear to have its own\nKecleon shop.\n\nNo params.",
    )

    SpecialEpisodeKecleonShopZInit = Symbol(
        None, None, None, "Empties the special episode Kecleon shop.\n\nNo params."
    )

    SetActiveKecleonShop = Symbol(
        None,
        None,
        None,
        "Changes the currently active Kecleon shop. Has one for TEAM_MAIN and TEAM_SPECIAL_EPISODE. TEAM_RESCUE does not\nappear to have its own copy of the Kecleon shop it seems to use TEAM_MAIN intead of TEAM_RESCUE.\n\nr0: team ID",
    )

    GetMoneyStored = Symbol(
        None,
        None,
        None,
        "Gets the amount of money the player has stored in the Duskull Bank.\n\nreturn: amount of money stored",
    )

    SetMoneyStored = Symbol(
        None,
        None,
        None,
        "Sets the amount of money the player has stored in the Duskull Bank, clamping the value to the range [0, MAX_MONEY_STORED].\n\nr0: new value",
    )

    AddMoneyStored = Symbol(
        None,
        None,
        None,
        "Adds money to the amount of money the player has stored in the Duskull Bank. Just calls SetMoneyStored with the current money + money gained.\n\nr0: money gained (can be negative)",
    )

    SortKecleonItems1 = Symbol(
        None,
        None,
        None,
        "Sorts the items for the normal Kecleon Shop items in Treasure Town.\n\nNo params.",
    )

    GenerateKecleonItems1 = Symbol(
        None,
        None,
        None,
        "Generates the Kecleon Shop items for both shopkeepers in Treasure Town. This function also calls\nGenerateKecleonItems2 despite GenerateKecleonItems2 being called directly after. This means that\nany items generated for the Orb/TM shop will be overwritten by the subsequent call to\nGenerateKecleonItems2.\n\nr0: kecleon_shop_version to use",
    )

    SortKecleonItems2 = Symbol(
        None,
        None,
        None,
        "Sorts the items for the Orb/TM Kecleon Shop items in Treasure Town.\n\nNo params.",
    )

    GenerateKecleonItems2 = Symbol(
        None,
        None,
        None,
        "Generates the Kecleon Shop items for the TMs/Orbs shop in Treasure Town.\n\nr0: kecleon_shop_version to use",
    )

    GetExclusiveItemOffset = Symbol(
        None,
        None,
        None,
        "Gets the exclusive item offset, which is the item ID relative to that of the first exclusive item, the Prism Ruff.\n\nr0: item ID\nreturn: offset",
    )

    ApplyExclusiveItemStatBoosts = Symbol(
        None,
        None,
        None,
        "Applies stat boosts from an exclusive item.\n\nr0: item ID\nr1: pointer to attack stat to modify\nr2: pointer to special attack stat to modify\nr3: pointer to defense stat to modify\nstack[0]: pointer to special defense stat to modify",
    )

    SetExclusiveItemEffect = Symbol(
        None,
        None,
        None,
        "Sets the bit for an exclusive item effect.\n\nr0: pointer to the effects bitvector to modify\nr1: exclusive item effect ID",
    )

    ExclusiveItemEffectFlagTest = Symbol(
        None,
        None,
        None,
        "Tests the exclusive item bitvector for a specific exclusive item effect.\n\nr0: the effects bitvector to test\nr1: exclusive item effect ID\nreturn: bool",
    )

    IsExclusiveItemIdForMonster = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item ID\nr1: monster ID\nr2: type ID 1\nr3: type ID 2\nreturn: bool",
    )

    IsExclusiveItemForMonster = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item\nr1: monster ID\nr2: type ID 1\nr3: type ID 2\nreturn: bool",
    )

    BagHasExclusiveItemTypeForMonster = Symbol(
        None,
        None,
        None,
        "Checks the bag for any exclusive item that applies to the monster or type(s) and gets the item ID.\n\nr0: excl_type\nr1: monster ID\nr2: type ID 1\nr3: type ID 2\nreturn: exclusive item ID",
    )

    GetExclusiveItemForMonsterFromBag = Symbol(
        None,
        None,
        None,
        "Checks the bag for any exclusive item that applies to the monster or type(s) and copies that item\ninto the passed item struct.\n\nr0: [output] item_struct\nr1: excl_type\nr2: monster ID\nr3: type ID 1\nstack[0]: type ID 2\nreturn: bool whether an exclusive item was found",
    )

    GetHpBoostFromExclusiveItems = Symbol(
        None,
        None,
        None,
        "Calculates the current HP boost from exclusive items. If none are active, return 0.\n\nr0: some struct that has species ID in it?\nreturn: max HP boost from exclusive items",
    )

    ApplyGummiBoostsToGroundMonster = Symbol(
        None,
        None,
        None,
        "Applies the IQ boosts from eating a Gummi to the target monster. Basically a wrapper around\nApplyGummiBoostsGroundMode for struct ground_monster.\n\nr0: ground monster pointer\nr1: Item ID\nr2: bool to NOT increase stats\nr3: [output] pointer to a struct gummi_result to fill out",
    )

    ApplyGummiBoostsToTeamMember = Symbol(
        None,
        None,
        None,
        "Applies the IQ boosts from eating a Gummi to the target monster. Basically a wrapper around\nApplyGummiBoostsGroundMode for struct team_member.\n\nr0: team member pointer\nr1: Item ID\nr2: bool to NOT increase stats\nr3: [output] pointer to a struct gummi_result to fill out",
    )

    ApplySitrusBerryBoostToGroundMonster = Symbol(
        None,
        None,
        None,
        "Applies the hp boost from the Sitrus Berry to the target monster.\n\nr0: ground monster pointer\nr1: [output] pointer to attempted hp boost, if not NULL\nreturn: actual hp boost",
    )

    ApplyLifeSeedBoostToGroundMonster = Symbol(
        None,
        None,
        None,
        "Applies the hp boost from the Life Seed to the target monster.\n\nr0: ground monster pointer\nr1: [output] pointer to attempted hp boost, if not NULL\nreturn: actual hp boost",
    )

    ApplyGinsengToGroundMonster = Symbol(
        None,
        None,
        None,
        "Attempts to apply a ginseng boost to the highest valid move that the ground monster knows.\n\nr0: ground monster pointer\nr1: [output] move ID\nr2: [output] move boost\nreturn: actual move boost",
    )

    ApplyProteinBoostToGroundMonster = Symbol(
        None,
        None,
        None,
        "Applies the attack boost from Protein to the target monster.\n\nr0: ground monster pointer\nr1: [output] pointer to attempted attack boost, if not NULL\nreturn: actual attack boost",
    )

    ApplyCalciumBoostToGroundMonster = Symbol(
        None,
        None,
        None,
        "Applies the special attack boost from Calcium to the target monster.\n\nr0: ground monster pointer\nr1: [output] pointer to attempted special attack boost, if not NULL\nreturn: actual special attack boost",
    )

    ApplyIronBoostToGroundMonster = Symbol(
        None,
        None,
        None,
        "Applies the defense boost from Iron to the target monster.\n\nr0: ground monster pointer\nr1: [output] pointer to attempted defense boost, if not NULL\nreturn: actual defense boost",
    )

    ApplyZincBoostToGroundMonster = Symbol(
        None,
        None,
        None,
        "Applies the special defense boost from Zinc to the target monster.\n\nr0: ground monster pointer\nr1: [output] pointer to attempted special defense boost, if not NULL\nreturn: actual special defense boost",
    )

    ApplyNectarBoostToGroundMonster = Symbol(
        None,
        None,
        None,
        "Applies the iq boost from Nectar to the target monster.\n\nr0: ground monster pointer\nr1: [output] pointer to attempted iq boost, if not NULL\nreturn: actual iq boost",
    )

    IsMonsterAffectedByGravelyrockGroundMode = Symbol(
        None,
        None,
        None,
        "Checks if the monster is Bonsly or Sudowoodo.\n\nr0: ground monster pointer\nreturn: bool",
    )

    ApplyGravelyrockBoostToGroundMonster = Symbol(
        None,
        None,
        None,
        "Applies the iq boost from Gravelyrock to the target monster. Only Bonsly and Sudowoodo gain IQ from the Gravelyrock.\n\nr0: ground monster pointer\nr1: [output] pointer to attempted iq boost, if not NULL\nreturn: actual iq boost",
    )

    ApplyGummiBoostsGroundMode = Symbol(
        None,
        None,
        None,
        "Applies the IQ boosts from eating a Gummi to the monster's data. Generally called with not increasing stats true outside of the cafe.\n\nr0: Pointer to monster id\nr1: Pointer to monster iq\nr2: Pointer to monster offensive stats\nr3: Pointer to monster defensive stats\nstack[0]: Item ID\nstack[1]: bool to NOT increase stats\nstack[2]: [output] pointer to a struct gummi_result",
    )

    LoadSynthBin = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    CloseSynthBin = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    GetSynthItem = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    LoadWazaP = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    LoadWazaP2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    UnloadCurrentWazaP = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    GetMoveName = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: move ID\nreturn: move name",
    )

    FormatMoveString = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: string_buffer\nr1: move\nr2: type_print",
    )

    FormatMoveStringMore = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: ???\nr1: ???\nr2: move\nr3: type_print",
    )

    InitMove = Symbol(
        None,
        None,
        None,
        "Initializes a move info struct.\n\nThis sets f_exists and f_enabled_for_ai on the flags, the ID to the given ID, the PP to the max PP for the move ID, and the ginseng boost to 0.\n\nr0: pointer to move to initialize\nr1: move ID",
    )

    InitMoveCheckId = Symbol(
        None,
        None,
        None,
        "Same as InitMove, but the function ensures that the specified ID is not 0. If it is, the move is initialized as invalid and nothing else happens.\n\nr0: move\nr1: move ID",
    )

    GetInfoMoveGround = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: ground move\nr1: move ID",
    )

    GetMoveTargetAndRange = Symbol(
        None,
        None,
        None,
        "Gets the move target-and-range field. See struct move_target_and_range in the C headers.\n\nr0: move pointer\nr1: AI flag (every move has two target-and-range fields, one for players and one for AI)\nreturn: move target and range",
    )

    GetMoveType = Symbol(
        None,
        None,
        None,
        "Gets the type of a move\n\nr0: Pointer to move data\nreturn: Type of the move",
    )

    GetMovesetLevelUpPtr = Symbol(
        None,
        None,
        None,
        "Given the ID of a monster in the current dungeon, returns a pointer to the list of moves it learns by leveling up and the level in which each move is learnt.\n\nThe list contains pairs of <encoded move ID, level>. The move ID is encoded and can be 1 or 2 bytes long. GetEncodedHalfword must be used to decode it. The end of the list is marked by a null byte.\n\nr0: monster ID\nreturn: Pointer to encoded level-up move list",
    )

    IsInvalidMoveset = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: moveset_id\nreturn: bool",
    )

    GetMovesetHmTmPtr = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: monster ID\nreturn: ?",
    )

    GetMovesetEggPtr = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: monster ID\nreturn: ?",
    )

    GetMoveAiWeight = Symbol(
        None,
        None,
        None,
        "Gets the AI weight of a move\n\nr0: Pointer to move data\nreturn: AI weight of the move",
    )

    GetMoveNbStrikes = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: move\nreturn: # strikes",
    )

    GetMoveBasePower = Symbol(
        None,
        None,
        None,
        "Gets the base power of a move from the move data table.\n\nr0: move pointer\nreturn: base power",
    )

    GetMoveBasePowerGround = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: ground_move\nreturn: base power",
    )

    GetMoveAccuracyOrAiChance = Symbol(
        None,
        None,
        None,
        "Gets one of the two accuracy values of a move or its ai_condition_random_chance field.\n\nr0: Move pointer\nr1: 0 to get the move's first accuracy1 field, 1 to get its accuracy2, 2 to get its ai_condition_random_chance.\nreturn: Move's accuracy1, accuracy2 or ai_condition_random_chance",
    )

    GetMoveBasePp = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: move\nreturn: base PP",
    )

    GetMaxPp = Symbol(
        None,
        None,
        None,
        "Gets the maximum PP for a given move.\n\nIrkdwia's notes: GetMovePPWithBonus\n\nr0: move pointer\nreturn: max PP for the given move, capped at 99",
    )

    GetMoveMaxGinsengBoost = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: move\nreturn: max ginseng boost",
    )

    GetMoveMaxGinsengBoostGround = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: ground_move\nreturn: max ginseng boost",
    )

    GetMoveCritChance = Symbol(
        None,
        None,
        None,
        "Gets the critical hit chance of a move.\n\nr0: move pointer\nreturn: critical hit chance",
    )

    IsThawingMove = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: move\nreturn: bool",
    )

    IsAffectedByTaunt = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nBased on struct move_data, maybe this should be IsUsableWhileTaunted?\n\nr0: move\nreturn: bool",
    )

    GetMoveRangeId = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: move\nreturn: range ID",
    )

    GetMoveActualAccuracy = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: move ID\nreturn: accuracy",
    )

    GetMoveBasePowerFromId = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: move ID\nreturn: base power",
    )

    IsMoveRangeString19 = Symbol(
        None,
        None,
        None,
        "Returns whether a move's range string is 19 ('User').\n\nr0: Move pointer\nreturn: True if the move's range string field has a value of 19.",
    )

    GetMoveMessageFromId = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: move ID?\nreturn: string",
    )

    GetNbMoves = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: moveset_str\nreturn: # moves",
    )

    GetMovesetIdx = Symbol(
        None,
        None,
        None,
        "Returns the move position in the moveset if it is found, -1 otherwise\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: moveset_str\nr1: move ID\nreturn: ?",
    )

    IsReflectedByMagicCoat = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: move ID\nreturn: bool",
    )

    CanBeSnatched = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: move ID\nreturn: bool",
    )

    FailsWhileMuzzled = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nCalled IsMouthMove in Irdkwia's notes, which presumably is relevant to the Muzzled status.\n\nr0: move ID\nreturn: bool",
    )

    IsSoundMove = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: move\nreturn: bool",
    )

    IsRecoilMove = Symbol(
        None,
        None,
        None,
        "Checks if the given move is a recoil move (affected by Reckless).\n\nr0: move ID\nreturn: bool",
    )

    AllManip1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    AllManip2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    ManipMoves1v1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    ManipMoves1v2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    ManipMoves2v1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    ManipMoves2v2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DungeonMoveToGroundMove = Symbol(
        None,
        None,
        None,
        "Converts a struct move to a struct ground_move.\n\nr0: [output] ground_move\nr1: move",
    )

    GroundToDungeonMoveset = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: [output] moveset_dun_str\nr1: moveset_str",
    )

    DungeonToGroundMoveset = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: [output] moveset_str\nr1: moveset_dun_str",
    )

    GetInfoGroundMoveset = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: moveset_str\nr1: moves_id",
    )

    FindFirstFreeMovesetIdx = Symbol(
        None,
        None,
        None,
        "Returns the first position of an empty move in the moveset if it is found, -1 otherwise\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: moveset_str\nreturn: index",
    )

    LearnMoves = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: moveset_str\nr1: moves_id",
    )

    CopyMoveTo = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: write_info\nr1: buffer_write",
    )

    CopyMoveFrom = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: read_info\nr1: buffer_read",
    )

    CopyMovesetTo = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: write_info\nr1: buffer_write",
    )

    CopyMovesetFrom = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: read_info\nr1: buffer_read",
    )

    Is2TurnsMove = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: move ID\nreturn: bool",
    )

    IsRegularAttackOrProjectile = Symbol(
        None,
        None,
        None,
        "Checks if a move ID is MOVE_REGULAR_ATTACK or MOVE_PROJECTILE.\n\nr0: move ID\nreturn: bool",
    )

    IsPunchMove = Symbol(
        None,
        None,
        None,
        "Checks if the given move is a punch move (affected by Iron Fist).\n\nr0: move ID\nreturn: bool",
    )

    IsHealingWishOrLunarDance = Symbol(
        None,
        None,
        None,
        "Checks if a move ID is MOVE_HEALING_WISH or MOVE_LUNAR_DANCE.\n\nr0: move ID\nreturn: bool",
    )

    IsCopyingMove = Symbol(
        None,
        None,
        None,
        "Checks if a move ID is MOVE_MIMIC, MOVE_SKETCH, or MOVE_COPYCAT.\n\nr0: move ID\nreturn: bool",
    )

    IsTrappingMove = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: move ID\nreturn: bool",
    )

    IsOneHitKoMove = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: move ID\nreturn: bool",
    )

    IsNot2TurnsMoveOrSketch = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: move ID\nreturn: bool",
    )

    IsRealMove = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: move ID\nreturn: bool",
    )

    IsMovesetValid = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: moveset_str\nreturn: bool",
    )

    IsRealMoveInTimeDarkness = Symbol(
        None,
        None,
        None,
        "Seed Flare isn't a real move in Time/Darkness\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: move ID\nreturn: bool",
    )

    IsMovesetValidInTimeDarkness = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: moveset_str\nreturn: bool",
    )

    GetFirstNotRealMoveInTimeDarkness = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: moveset_str\nreturn: index",
    )

    IsSameMove = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: moveset_dun_str\nr1: move_data_dun_str\nreturn: bool",
    )

    GetMoveCategory = Symbol(
        None,
        None,
        None,
        "Gets a move's category (physical, special, status).\n\nr0: move ID\nreturn: move category enum",
    )

    GetPpIncrease = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: monster ID\nr1: IQ skills bitvector\nreturn: PP increase",
    )

    OpenWaza = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nr0: waza_id"
    )

    SelectWaza = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nr0: waza_id"
    )

    PlayBgmByIdVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for PlayBgmById.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nr0: Music ID",
    )

    PlayBgmByIdVolumeVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for PlayBgmByIdVolume.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nr0: Music ID\nr1: (?) Stored on byte 8 on the struct passed to SendAudioCommand\nr2: Volume (0-255)",
    )

    PlaySeVolumeWrapper = Symbol(
        None,
        None,
        None,
        "Wrapper for PlaySeVolume. Takes an index and uses it to determine the ID of the sound to play.\n\nr0: Index",
    )

    PlayBgmById = Symbol(
        None,
        None,
        None,
        "Initializes some values and then calls SendAudioCommand to play a BGM track.\n\nChecks for DEBUG_FLAG_BGM_OFF. The volume is set to either 0 or 255 depending on the flag before calling SendAudioCommand.\n\nr0: Music ID",
    )

    PlayBgmByIdVolume = Symbol(
        None,
        None,
        None,
        "Initializes some values and then calls SendAudioCommand to play a BGM track.\n\nChecks for DEBUG_FLAG_BGM_OFF. If 1, sets the volume to 0 before calling SendAudioCommand.\n\nr0: Music ID\nr1: (?) Stored on byte 8 on the struct passed to SendAudioCommand\nr2: Volume (0-255)",
    )

    StopBgmCommand = Symbol(
        None,
        None,
        None,
        "Stops the BGM that is being currently played by calling SendAudioCommand.\n\nNo params.",
    )

    PlaySeByIdVolume = Symbol(
        None,
        None,
        None,
        "Plays the specified sound effect with the specified volume.\n\nChecks for DEBUG_FLAG_SE_OFF and sets the volume to 0 if the flag is set. Calls SendAudioCommand2.\n\nr0: Sound effect ID\nr1: Volume (0-255)",
    )

    SendAudioCommand2 = Symbol(
        None,
        None,
        None,
        "Very similar to SendAudioCommand. Contains an additional function call.\n\nr0: Command to send",
    )

    AllocAudioCommand = Symbol(
        None,
        None,
        None,
        "Searches for an entry in AUDIO_COMMANDS_BUFFER that's not currently in use (audio_command::status == 0). Returns the first entry not in use, or null if none was found.\n\nAlso sets the status of the found entry to the value specified in r0.\n\nThe game doesn't bother checking if the result of the function is null, so the buffer is not supposed to ever get filled.\n\nr0: Status to set the found entry to\nreturn: The first unused entry, or null if none was found",
    )

    SendAudioCommand = Symbol(
        None,
        None,
        None,
        "Used to send commands to the audio engine (seems to be used mainly to play and stop music)\n\nThis function calls a stubbed-out one with the string 'audio command list'\n\nr0: Command to send",
    )

    InitSoundSystem = Symbol(
        None,
        None,
        None,
        "Initialize the DSE sound engine?\n\nThis function is called somewhere in the hierarchy under TaskProcBoot and appears to allocate a bunch of memory (including a dedicated memory arena, see SOUND_MEMORY_ARENA) for sound data, and reads a bunch of core sound files.\n\nFile paths referenced:\n- SOUND/SYSTEM/se_sys.swd\n- SOUND/SYSTEM/se_sys.sed\n- SOUND/SE/motion.swd\n- SOUND/SE/motion.sed\n- SOUND/BGM/bgm.swd (this is the main sample bank, see https://projectpokemon.org/home/docs/mystery-dungeon-nds/pok%C3%A9mon-mystery-dungeon-explorers-r78/)\n\nDebug strings:\n- entry system se swd %04x\n\n- entry system se sed %04x\n\n- entry motion se swd %04x\n\n- entry motion se sed %04x\n",
    )

    ManipBgmPlayback = Symbol(
        None,
        None,
        None,
        "Uncertain. More like bgm1&2 end\n\nNote: unverified, ported from Irdkwia's notes",
    )

    SoundDriverReset = Symbol(
        None, None, None, "Uncertain.\n\nNote: unverified, ported from Irdkwia's notes"
    )

    LoadDseFile = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: [output] iovec\nr1: filename\nreturn: bytes read",
    )

    PlaySeLoad = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    IsSongOver = Symbol(
        None,
        None,
        None,
        "True if the song that is currently being played has finished playing.\n\nreturn: True if the current song is over",
    )

    PlayBgm = Symbol(None, None, None, "Note: unverified, ported from Irdkwia's notes")

    StopBgm = Symbol(None, None, None, "Note: unverified, ported from Irdkwia's notes")

    ChangeBgm = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    PlayBgm2 = Symbol(None, None, None, "Note: unverified, ported from Irdkwia's notes")

    StopBgm2 = Symbol(None, None, None, "Note: unverified, ported from Irdkwia's notes")

    ChangeBgm2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    PlayME = Symbol(None, None, None, "Note: unverified, ported from Irdkwia's notes")

    StopME = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: fade_out",
    )

    PlaySe = Symbol(None, None, None, "Note: unverified, ported from Irdkwia's notes")

    PlaySeFullSpec = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SeChangeVolume = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SeChangePan = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    StopSe = Symbol(None, None, None, "Note: unverified, ported from Irdkwia's notes")

    InitAnimationControl = Symbol(
        None,
        None,
        None,
        "Initialize the animation_control structure\n\nr0: animation_control",
    )

    InitAnimationControlWithSet = Symbol(
        None,
        None,
        None,
        "Initialize the animation_control structure, and set a certain value in a bitflag to 1\n\nr0: animation_control",
    )

    SetSpriteIdForAnimationControl = Symbol(
        None,
        None,
        None,
        "Set the sprite id (from WAN_TABLE) in the given animation control\nAlso set field 0x72 to the sprite id if they differ\nIf they differ, it’ll also set field 0x43 to 0xFF\n\nr0: animation control\nr1: sprite id in WAN_TABLE",
    )

    SetAnimationForAnimationControlInternal = Symbol(
        None,
        None,
        None,
        "Set the wan animation (and other related settings) of an animation_control\nUsed by SetAnimationForAnimationControl\n\nr0: animation_control\nr1: wan_header\nr2: animation group id\nr3: animation id\nstack[0]: ?\nstack[1] (0x4): palette pos low (see the field on animation_control)\nstack[2] (0x8): ?\nstack[3] (0xC): ?\nstack[4] (0x10): palette_bank (directly set to the animation_control field with said name)",
    )

    SetAnimationForAnimationControl = Symbol(
        None,
        None,
        None,
        "Set the animation to play with this animation control, but do not start it.\n\n(args same as SetAndPlayAnimationForAnimationControl)\nr0: animation_control\nr1: animation key (either an animation or animation group depending on the type of sprite and if it does have animation group with this animation key as index)\nr2: direction_id (unsure) (the key to the wan_animation in itself, only used when animation key represent a wan_animation_group)\nr3: ?\nstack[0]: low_palette_pos\nstack[1] (0x4): ?\nstack[2] (0x8): ?\nstack[3] (0xC): ?",
    )

    GetWanForAnimationControl = Symbol(
        None,
        None,
        None,
        "Return the WAN to use for the given animation control\nReturn the override if it exists, otherwise look up the sprite id in WAN_TABLE\n\nr0: animation_control\nreturn: wan_header",
    )

    SetAndPlayAnimationForAnimationControl = Symbol(
        None,
        None,
        None,
        "Set the animation to play with the animation control, and start it.\n\nr0: animation_control\nr1: animation key (either an animation or animation group depending on the type of sprite and if it does have animation group with this animation key as index)\nr2: direction_id (unsure) (the key to the wan_animation in itself, only used when animation key represent a wan_animation_group)\nr3: ?\nstack[0]: low_palette_pos\nstack[1] (0x4): ?\nstack[2] (0x8): ?\nstack[3] (0xC): ?",
    )

    SwitchAnimationControlToNextFrame = Symbol(
        None,
        None,
        None,
        "Handle switching to the next frame of an animation control, including looping.\n\nr0: animation_control",
    )

    LoadAnimationFrameAndIncrementInAnimationControl = Symbol(
        None,
        None,
        None,
        "Read some value of the input animation frame, and update animation control with it.\nAlso switch next_animation_frame of animation_control to the next animation frame\nSeems to only be called on said next_animation_frame\nAlso set bit of some_bitfield at 0x0800 to 1\n\nr0: animation_control\nr1: animation_frame",
    )

    AnimationControlGetAllocForMaxFrame = Symbol(
        None,
        None,
        None,
        "Return the maximum allocation for a frame of this sprite, as stored in the WAN file\nReturn 0 if missing and takes sprite override into account\n\nr0: animation_control\nreturn: allocation for max frame",
    )

    DeleteWanTableEntry = Symbol(
        None,
        None,
        None,
        "Always delete an entry if the file is allocated externally (file_externally_allocated is set), otherwise, decrease the reference counter. If it reach 0, delete the sprite.\n\nr0: wan_table_ptr\nr1: wan_id",
    )

    AllocateWanTableEntry = Symbol(
        None,
        None,
        None,
        "Return the identifier to a free wan table entry (-1 if none are avalaible). The entry is zeroed.\n\nr0: wan_table_ptr\nreturn: the entry id in wan_table",
    )

    FindWanTableEntry = Symbol(
        None,
        None,
        None,
        "Search in the given table (in practice always seems to be WAN_TABLE) for an entry with the given file name.\n\nr0: table pointer\nr1: file name\nreturn: index of the found file, if found, or -1 if not found",
    )

    GetLoadedWanTableEntry = Symbol(
        None,
        None,
        None,
        "Look up a sprite with the provided pack_id and file_index in the wan table.\n\nr0: wan_table_ptr\nr1: pack_id\nr2: file_index\nreturn: sprite id in the wan table, -1 if not found",
    )

    InitWanTable = Symbol(
        None,
        None,
        None,
        "Initialize the input WAN table with 0x60 free entries (it needs a length of 0x1510 bytes)\n\nr0: wan_table_ptr",
    )

    LoadWanTableEntry = Symbol(
        None,
        None,
        None,
        "Appears to load data from the given file (in practice always seems to be animation data), using previously loaded data in the given table (see FindWanTableEntry) if possible.\n\nr0: table pointer\nr1: file name\nr2: flags\nreturn: table index of the loaded data",
    )

    LoadWanTableEntryFromPack = Symbol(
        None,
        None,
        None,
        "Return an already allocated entry for this sprite if it exists, otherwise allocate a new one and load the optionally compressed sprite.\n\nr0: wan_table_ptr\nr1: pack_id\nr2: file_index\nr3: allocation flags\nstack[0]: compressed\nreturn: the entry id in wan_table",
    )

    LoadWanTableEntryFromPackUseProvidedMemory = Symbol(
        None,
        None,
        None,
        "Return an already allocated entry for this sprite if it exists, otherwise allocate a new one and load the optionally compressed sprite into the provided memory area. Mark the sprite as externally allocated.\n\nr0: wan_table_ptr\nr1: pack_id\nr2: file_index\nr3: sprite_storage_ptr\nstack[0]: compressed\nreturn: the entry id in wan_table",
    )

    ReplaceWanFromBinFile = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: wan_table_ptr\nr1: wan_id\nr2: bin_file_id\nr3: file_id\nstack[0]: compressed",
    )

    DeleteWanTableEntryVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for DeleteWanTableEntry.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nr0: wan_table_ptr\nr1: wan_id",
    )

    WanHasAnimationGroup = Symbol(
        None,
        None,
        None,
        "Check if the input WAN file loaded in memory has an animation group with this ID\nValid means that the animation group is in the range of existing animation, and that it has at least one animation.\n\nr0: pointer to the header of the WAN\nr1: id of the animation group\nreturn: whether the WAN file has the given animation group",
    )

    WanTableSpriteHasAnimationGroup = Symbol(
        None,
        None,
        None,
        "Check if the sprite in the global WAN table has the given animation group\nsee WanHasAnimationGroup for more detail\n\nr0: sprite id in the WAN table\nr1: animation group id\nreturn: whether the associated sprite has the given animation group",
    )

    SpriteTypeInWanTable = Symbol(
        None,
        None,
        None,
        "Look up the sprite in the WAN table, and return its type\n\nr0: sprite id in the WAN table\nreturn: sprite type",
    )

    LoadWteFromRom = Symbol(
        None,
        None,
        None,
        "Loads a SIR0-wrapped WTE file from ROM, and returns a handle to it\n\nr0: [output] pointer to wte handle\nr1: file path string\nr2: load file flags",
    )

    LoadWteFromFileDirectory = Symbol(
        None,
        None,
        None,
        "Loads a SIR0-wrapped WTE file from a file directory, and returns a handle to it\n\nr0: [output] pointer to wte handle\nr1: file directory id\nr2: file index\nr3: malloc flags",
    )

    UnloadWte = Symbol(
        None,
        None,
        None,
        "Frees the buffer used to store the WTE data in the handle, and sets both pointers to null\n\nr0: pointer to wte handle",
    )

    LoadWtuFromBin = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: bin_file_id\nr1: file_id\nr2: load_type\nreturn: ?",
    )

    ProcessWte = Symbol(
        None,
        None,
        None,
        "Prepare a WTE data to be loaded into VRAM. Seems to need to be called with another undocumented function (at 0x0201e1d8 (EU))\nIt skips the texture and/or the palette if missing from the file. The texture VRAM has 128KiB of space, and palette has 16KiB.\nThe true palette VRAM offset will be upper_part*0x100+lower_part\n\nThis may or may not be the function that adds to the queue so it can be added during VBlank.\n\nr0: pointer to the WTE file header loaded in memory\nr1: where the WTE texture will be loaded in the VRAM (from 0 to 0x1FFFF)\nr2: upper part of the palette VRAM\nr3: lower part of the palette VRAM",
    )

    GeomSetTexImageParam = Symbol(
        None,
        None,
        None,
        "Send the TEXIMAGE_PARAM geometry engine command, that defines some parameters for the texture\nSee http://problemkaputt.de/gbatek.htm#ds3dtextureattributes for more information on the parameters\n\nr0: texture format\nr1: texture coordinates transformation modes\nr2: texture S-Size\nr3: texture T-Size\nstack[0] (0x0): repeat in S (bit 0) and/or T (bit 1) direction\nstack[1] (0x4): flip in S (bit 0) and/or T (bit 1) direction\nstack[2] (0x8): What to make of color 0 (bit 29)\nstack[3] (0xC): Texture VRAM offset divided by 8",
    )

    GeomSetVertexCoord16 = Symbol(
        None,
        None,
        None,
        "Send the 'VTX_16' geometry engine command, that defines the coordinate of a point of a polygon, using 16 bits.\nInputs are clamped over their 16 lower bits\n\nr0: x coordinate\nr1: y coordinate\nr2: z coordinate",
    )

    InitRender3dData = Symbol(
        None, None, None, "Initialize the global 'RENDER_3D' structure.\n\nNo params."
    )

    GeomSwapBuffers = Symbol(
        None,
        None,
        None,
        "Call the 'SWAP_BUFFERS' command. This will swap the geometry buffer. The parameter of 1 is provided, which enables manual Y-sorting of translucent polygons.\n\nNo params.",
    )

    InitRender3dElement64 = Symbol(
        None,
        None,
        None,
        "Initialize the render_3d_element_64 structure (without performing any drawing or external data access)\n\nr0: render_3d_element_64",
    )

    Render3d64Texture0x7 = Symbol(
        None,
        None,
        None,
        "RENDER_3D_FUNCTIONS_64[7]. Renders a render_3d_element_64 with type RENDER64_TEXTURE_0x7.\n\nConverts the render_3d_element_64 to a render_3d_element on the render queue of RENDER_3D, with type RENDER_TEXTURE.\n\nr0: render_3d_element_64",
    )

    Render3d64WindowFrame = Symbol(
        None,
        None,
        None,
        "Draw the frame for a window, using the 3D engine.\n\nThe render_3d_element_64 contains certain value that needs to be set to a correct value for it to work.\nThe element is not immediately sent to the geometry engine, but is converted to a render_3d_element and queued up in RENDER_3D.\n\nRENDER_3D_FUNCTIONS_64[6], corresponding to a type of RENDER64_WINDOW_FRAME.\n\nr0: render_3d_element_64",
    )

    EnqueueRender3d64Tiling = Symbol(
        None,
        None,
        None,
        "Converts a render_3d_element_64 with type RENDER64_TILING to a render_3d_element on the render queue of RENDER_3D, with type RENDER_TILING.\n\nr0: render_3d_element_64",
    )

    Render3d64Tiling = Symbol(
        None,
        None,
        None,
        "RENDER_3D_FUNCTIONS_64[5]. Renders a render_3d_element_64 with type RENDER64_TILING.\n\nConverts the render_3d_element_64 to a render_3d_element on the render queue of RENDER_3D, with type RENDER_TILING.\n\nr0: render_3d_element_64",
    )

    Render3d64Quadrilateral = Symbol(
        None,
        None,
        None,
        "RENDER_3D_FUNCTIONS_64[4]. Renders a render_3d_element_64 with type RENDER64_QUADRILATERAL.\n\nConverts the render_3d_element_64 to a render_3d_element on the render queue of RENDER_3D, with type RENDER_QUADRILATERAL.\n\nr0: render_3d_element_64",
    )

    Render3d64RectangleMulticolor = Symbol(
        None,
        None,
        None,
        "RENDER_3D_FUNCTIONS_64[3]. Renders a render_3d_element_64 with type RENDER64_RECTANGLE_MULTICOLOR.\n\nConverts the render_3d_element_64 to a render_3d_element on the render queue of RENDER_3D, with type RENDER_RECTANGLE.\n\nr0: render_3d_element_64",
    )

    Render3d64Rectangle = Symbol(
        None,
        None,
        None,
        "RENDER_3D_FUNCTIONS_64[2]. Renders a render_3d_element_64 with type RENDER64_RECTANGLE.\n\nConverts the render_3d_element_64 to a render_3d_element on the render queue of RENDER_3D, with type RENDER_RECTANGLE.\n\nr0: render_3d_element_64",
    )

    Render3d64Nothing = Symbol(
        None,
        None,
        None,
        "RENDER_3D_FUNCTIONS_64[1]. Renders a render_3d_element_64 with type RENDER64_NOTHING. This function is entirely empty.\n\nr0: render_3d_element_64",
    )

    Render3d64Texture = Symbol(
        None,
        None,
        None,
        "RENDER_3D_FUNCTIONS_64[0]. Renders a render_3d_element_64 with type RENDER64_TEXTURE.\n\nConverts the render_3d_element_64 to a render_3d_element on the render queue of RENDER_3D, with type RENDER_TEXTURE.\n\nr0: render_3d_element_64",
    )

    Render3dElement64 = Symbol(
        None,
        None,
        None,
        "Dispatches a render_3d_element_64 to the render function corresponding to its type.\n\nr0: render_3d_element_64",
    )

    HandleSir0Translation = Symbol(
        None,
        None,
        None,
        "Translates the offsets in a SIR0 file into NDS memory addresses, changes the magic number to SirO (opened), and returns a pointer to the first pointer specified in the SIR0 header (beginning of the data).\n\nIrkdiwa's notes:\n  ret_code = 0 if it wasn't a SIR0 file\n  ret_code = 1 if it has been transformed in SIRO file\n  ret_code = 2 if it was already a SIRO file\n  [output] contains a pointer to the header of the SIRO file if ret_code = 1 or 2\n  [output] contains a pointer which is exactly the same as the sir0_ptr if ret_code = 0\n\nr0: [output] double pointer to beginning of data\nr1: pointer to source file buffer\nreturn: return code",
    )

    ConvertPointersSir0 = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: sir0_ptr",
    )

    HandleSir0TranslationVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for HandleSir0Translation.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nr0: [output] double pointer to beginning of data\nr1: pointer to source file buffer\nreturn: return code",
    )

    DecompressAtNormalVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for DecompressAtNormal.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nr0: addr_decomp\nr1: expected_size\nr2: AT pointer\nreturn: ?",
    )

    DecompressAtNormal = Symbol(
        None,
        None,
        None,
        "Overwrites r3 probably passed to match DecompressAtHalf's definition.\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: addr_decomp\nr1: expected_size\nr2: AT pointer\nreturn: ?",
    )

    DecompressAtHalf = Symbol(
        None,
        None,
        None,
        "Same as DecompressAtNormal, except it stores each nibble as a byte\nand adds the high nibble (r3).\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: addr_decomp\nr1: expected_size\nr2: AT pointer\nr3: high_nibble\nreturn: ?",
    )

    DecompressAtFromMemoryPointerVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for DecompressAtFromMemoryPointer.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nr0: addr_decomp\nr1: expected_size\nr2: AT pointer\nreturn: ?",
    )

    DecompressAtFromMemoryPointer = Symbol(
        None,
        None,
        None,
        "Overwrites r3 probably passed to match DecompressAtHalf's definition.\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: addr_decomp\nr1: expected_size\nr2: AT pointer\nreturn: ?",
    )

    WriteByteFromMemoryPointer = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nr0: byte"
    )

    GetAtSize = Symbol(
        None,
        None,
        None,
        "Doesn't work for AT3PX and AT4PN\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: AT pointer\nr1: ?\nreturn: ?",
    )

    GetLanguageType = Symbol(
        None,
        None,
        None,
        "Gets the language type.\n\nThis is the value backing the special LANGUAGE_TYPE script variable.\n\nreturn: language type",
    )

    GetLanguage = Symbol(
        None,
        None,
        None,
        "Gets the single-byte language ID of the current program.\n\nThe language ID appears to be used to index some global tables.\n\nreturn: language ID",
    )

    StrcmpTag = Symbol(
        None,
        None,
        None,
        "Checks if a null-terminated string s1 either exactly equals a null-terminated string s2, or starts with s2 followed by a ':' or a ']'.\n\nr0: s1\nr1: s2\nreturn: bool",
    )

    AtoiTag = Symbol(
        None,
        None,
        None,
        "Parses a null-terminated string to a base-10 integer, reading digit characters between '0' and '9' until ':', ']', or the end of the string is encountered.\n\nAny characters that are not digits, ':', or ']' are ignored, and the string is converted as if those characters were removed from the string.\n\nr0: string to convert\nreturn: int",
    )

    AnalyzeText = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: buffer\nreturn: ?",
    )

    PreprocessString = Symbol(
        None,
        None,
        None,
        "An enhanced sprintf, which recognizes certain tags and replaces them with appropiate game values.\nThis function can also be used to simply insert values passed within the preprocessor args\n\nThe tags utilized for this function are lowercase, it might produce uppercase tags\nthat only are used when the text is being typewrited into a message box\n\nIrdkwia's notes: MenuCreateOptionString\n\nr0: [output] formatted string\nr1: maximum capacity of the output buffer\nr2: input format string\nr3: preprocessor flags\nstack[0]: pointer to preprocessor args",
    )

    PreprocessStringFromId = Symbol(
        None,
        None,
        None,
        "Calls PreprocessString after resolving the given string ID to a string.\n\nr0: [output] formatted string\nr1: maximum capacity of the output buffer\nr2: string ID\nr3: preprocessor flags\nstack[0]: pointer to preprocessor args",
    )

    StrcmpTagVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for StrcmpTag.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nr0: s1\nr1: s2\nreturn: bool",
    )

    AtoiTagVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for AtoiTag.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nr0: s\nreturn: int",
    )

    InitPreprocessorArgs = Symbol(
        None,
        None,
        None,
        "Initializes a struct preprocess_args.\n\nr0: preprocessor args pointer",
    )

    SetStringAccuracy = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SetStringPower = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    GetCurrentTeamNameString = Symbol(
        None,
        None,
        None,
        "Returns the current team name with a check for special episodes and story progression. If the story\nhas not progressed enough or the special episode is not for Team Charm, '???' will be displayed.\nDuring the Team Charm special episode, it will return 'Team Charm'.\n\nr0: [output] Pointer to the buffer where the string will be written\nr1: 0, 1 or 2???\nreturn: Pointer to the buffer where the string was written (in other words, the same value passed in r0)",
    )

    GetBagNameString = Symbol(
        None,
        None,
        None,
        "Returns 'One-Item Inventory' or 'Treasure Bag' depending on the size of the bag.\n\nr0: [output] Pointer to the buffer where the string will be written\nreturn: Pointer to the buffer where the string was written (in other words, the same value passed in r0)",
    )

    GetDungeonResultString = Symbol(
        None,
        None,
        None,
        "Returns a string containing some information to be used when displaying the dungeon results screen.\n\nThe exact string returned depends on the value of r0:\n0: Name of the move that fainted the leader. Empty string if the leader didn't faint.\n1-3: Seems to always result in an empty string.\n4: Name of the pokémon that fainted the leader, or name of the leader if the leader didn't faint.\n5: Name of the fainted leader. Empty string if the leader didn't faint.\n\nr0: String to return\nreturn: Pointer to resulting string",
    )

    SetQuestionMarks = Symbol(
        None,
        None,
        None,
        "Fills the buffer with the string '???'\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: buffer",
    )

    StrcpySimple = Symbol(
        None,
        None,
        None,
        "A simple implementation of the strcpy(3) C library function.\n\nThis function was probably manually implemented by the developers. See strcpy for what's probably the real libc function.\n\nr0: dest\nr1: src",
    )

    StrncpySimple = Symbol(
        None,
        None,
        None,
        "A simple implementation of the strncpy(3) C library function.\n\nThis function was probably manually implemented by the developers. See strncpy for what's probably the real libc function.\n\nr0: dest\nr1: src\nr2: n",
    )

    StrncpySimpleNoPad = Symbol(
        None,
        None,
        None,
        "Similar to StrncpySimple, but does not zero-pad the end of dest beyond the null-terminator.\n\nr0: dest\nr1: src\nr2: n",
    )

    StrncmpSimple = Symbol(
        None,
        None,
        None,
        "A simple implementation of the strncmp(3) C library function.\n\nThis function was probably manually implemented by the developers. See strncmp for what's probably the real libc function.\n\nr0: s1\nr1: s2\nr2: n\nreturn: comparison value",
    )

    StrncpySimpleNoPadSafe = Symbol(
        None,
        None,
        None,
        "Like StrncpySimpleNoPad, except there's a useless check on that each character is less than 0x100 (which is impossible for the result of a ldrb instruction).\n\nr0: dest\nr1: src\nr2: n",
    )

    StrcpyName = Symbol(
        None,
        None,
        None,
        "A special version of strcpy for handling names. Appears to use character 0x7E as some kind of\nformatting character in NA?\n\nr0: dst\nr1: src",
    )

    StrncpyName = Symbol(
        None,
        None,
        None,
        "A special version of strncpy for handling names. Appears to use character 0x7E as some kind of\nformatting character in NA? Copies at most n characters.\n\nr0: dst\nr1: src\nr2: n",
    )

    GetStringFromFile = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: Buffer\nr1: String ID",
    )

    LoadStringFile = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nNo params."
    )

    GetStringFromFileVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for GetStringFromFile.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nr0: Buffer\nr1: String ID",
    )

    StringFromId = Symbol(
        None,
        None,
        None,
        "Gets the string corresponding to a given string ID.\n\nr0: string ID\nreturn: string from the string files with the given string ID",
    )

    CopyStringFromId = Symbol(
        None,
        None,
        None,
        "Gets the string corresponding to a given string ID and copies it to the buffer specified in r0.\n\nr0: buffer\nr1: string ID",
    )

    CopyNStringFromId = Symbol(
        None,
        None,
        None,
        "Gets the string corresponding to a given string ID and copies it to the buffer specified in r0.\n\nThis function won't write more than <buffer length> bytes.\n\nr0: buffer\nr1: string ID\nr2: buffer length",
    )

    LoadTblTalk = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nNo params."
    )

    GetTalkLine = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: personality_index\nr1: group_id\nr2: restrictions\nreturn: ?",
    )

    IsAOrBPressed = Symbol(
        None, None, None, "Checks if A or B is currently being held.\n\nreturn: bool"
    )

    DrawTextInWindow = Symbol(
        None,
        None,
        None,
        "Seems to be responsible for drawing the text in a window.\n\nNeeds a call to UpdateWindow after to actually display the contents.\nUnclear if this is generic for windows or just text boxes.\n\nr0: window_id\nr1: x offset within window\nr2: y offset within window\nr3: text to draw",
    )

    GetWindow = Symbol(
        None,
        None,
        None,
        "Get the window with a given ID from WINDOW_LIST.\n\nr0: window_id\nreturn: window",
    )

    NewWindowScreenCheck = Symbol(
        None,
        None,
        None,
        "Calls NewWindow, with a pre-check for any valid existing windows in WINDOW_LIST on each screen.\n\nr0: window_params (see NewWindow)\nr1: ?\nreturn: window_id",
    )

    NewWindow = Symbol(
        None,
        None,
        None,
        "Seems to return the ID of a newly initialized window in the next available slot in WINDOW_LIST, given some starting information.\n\nIf WINDOW_LIST is full, it will be overflowed, with the slot with an ID of 20 being initialized and returned.\n\nr0: window_params pointer to be copied by value into window::hdr in the new window\nr1: ?\nreturn: window_id",
    )

    SetScreenWindowsColor = Symbol(
        None,
        None,
        None,
        "Sets the palette of the frames of windows in the specified screen\n\nr0: palette index\nr1: is upper screen",
    )

    SetBothScreensWindowsColor = Symbol(
        None,
        None,
        None,
        "Sets the palette of the frames of windows in both screens\n\nr0: palette index",
    )

    UpdateWindow = Symbol(
        None,
        None,
        None,
        "Seems to cause updated window contents to be displayed.\n   \nGets called for example at the end of a text box window update and seems to 'commit' the update, but in general also gets called with all kinds of window updates. \n\nr0: window_id",
    )

    ClearWindow = Symbol(
        None,
        None,
        None,
        "Clears the window, at least in the case of a text box.\n\nThe low number of XREFs makes it seem like there might be more such functions.\n\nr0: window_id",
    )

    DeleteWindow = Symbol(
        None,
        None,
        None,
        "Seems to uninitialize an active window in WINDOW_LIST with a given ID, freeing the slot for reuse by another window.\n\nr0: window_id",
    )

    GetWindowRectangle = Symbol(
        None,
        None,
        None,
        "Get the rectangle defined by a window.\n\nr0: window_id\nr1: [output] rectangle",
    )

    GetWindowContents = Symbol(
        None,
        None,
        None,
        "Gets the contents structure from the window with the given ID.\n\nr0: window_id\nreturn: contents",
    )

    LoadCursors = Symbol(
        None,
        None,
        None,
        "Load and initialize the cursor and cursor16 sprites, storing the result in CURSOR_ANIMATION_CONTROL and CURSOR_16_ANIMATION_CONTROL\n\nNo params.",
    )

    InitWindowTrailer = Symbol(
        None,
        None,
        None,
        "Seems to initialize a window_trailer within a new window.\n\nr0: window_trailer pointer",
    )

    Arm9LoadUnkFieldNa0x2029EC8 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nr0: id"
    )

    Arm9StoreUnkFieldNa0x2029ED8 = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nr1: value",
    )

    LoadAlert = Symbol(
        None,
        None,
        None,
        "Load and initialize the alert sprite, storing the result in ALERT_ANIMATION_CONTROL\n\nNo params.",
    )

    PrintClearMark = Symbol(
        None,
        None,
        None,
        "Prints the specified clear mark on the screen.\n\nClear marks are shown on the save file load screen. They are used to show which plot milestones have already been completed.\n\nr0: Clear mark ID\nr1: X pos (unknown units, usually ranges between 3 and 27)\nr2: Y pos (unknown units, normally 14)\nr3: ?",
    )

    CreateParentMenuFromStringIds = Symbol(
        None,
        None,
        None,
        "A wrapper around CreateParentMenuInternal, where the menu items can be defined by string ID instead of as strings.\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: simple_menu_id_item struct array, terminated with an item with string_id 0\nreturn: window_id",
    )

    IsEmptyString = Symbol(
        None,
        None,
        None,
        "Checks if a null-terminated string is empty. A NULL pointer counts as empty.\n\nr0: string\nreturn: whether the string is NULL or empty",
    )

    CreateParentMenu = Symbol(
        None,
        None,
        None,
        "A wrapper around CreateParentMenuInternal where ownership of the items array parameter won't be transferred to the menu.\n\nThe menu item array will be copied onto a new array on the heap. This means the argument doesn't need to remain valid after the function returns (e.g., it can be stack-allocated).\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: simple_menu_ptr_item struct array, terminated with an item with an NULL string pointer\nreturn: window_id",
    )

    CreateParentMenuWrapper = Symbol(
        None,
        None,
        None,
        "A wrapper around CreateParentMenu that sets field_0x1b0 to 1 if the returned window_id is not -2.\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: simple_menu_ptr_item struct array, terminated with an item with an NULL string pointer\nreturn: window_id",
    )

    CreateParentMenuInternal = Symbol(
        None,
        None,
        None,
        "Creates a window containing a simple textual menu with a list of options that might open submenus when selected. Also see struct simple_menu.\n\nMultiple levels of nesting is possible, i.e., a submenu could itself be a parent menu.\n\nThis is used in various menus that lead to submenus. For example, the top-level ground and dungeon mode menus.\n\nIf window_params is NULL, PARENT_MENU_DEFAULT_WINDOW_PARAMS will be used. Otherwise, it will be copied onto the window, ignoring the update and contents fields. If window_params::width and/or window_params::height are 0, they will be computed based on the contained text.\n\nIf window_extra_info is non-NULL, it will be copied onto the window. Note that window_extra_info can only be NULL if there are no window_flags set that require extra info.\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: heap-allocated simple_menu_items array, the menu takes ownership\nreturn: window_id",
    )

    ResumeParentMenu = Symbol(
        None,
        None,
        None,
        "Resumes input for a window created with CreateParentMenuInternal. Used for menus that do not close even after selecting an option.\n\nr0: window_id",
    )

    SetParentMenuState7 = Symbol(
        None, None, None, "Sets the state of a parent menu to 7.\n\nr0: window_id"
    )

    CloseParentMenu = Symbol(
        None,
        None,
        None,
        "Closes a window created with CreateParentMenu or CreateParentMenuFromStringIds.\n\nr0: window_id",
    )

    IsParentMenuActive = Symbol(
        None,
        None,
        None,
        "This is a guess.\n\nChecks if the state of a parent menu is something other than 8 or 9.\n\nr0: window_id\nreturn: bool",
    )

    CheckParentMenuField0x1A0 = Symbol(
        None,
        None,
        None,
        "Checks if a parent menu's field_0x1a0 is 0.\n\nr0: window_id\nreturn: bool",
    )

    UpdateParentMenu = Symbol(
        None,
        None,
        None,
        "Window update function for parent menus.\n\nr0: window pointer",
    )

    CreateSimpleMenuFromStringIds = Symbol(
        None,
        None,
        None,
        "A wrapper around CreateSimpleMenuInternal, where the menu items can be defined by string ID instead of as strings.\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: simple_menu_id_item struct array, terminated with an item with string_id 0\nstack[0]: number of items\nreturn: window_id",
    )

    CreateSimpleMenu = Symbol(
        None,
        None,
        None,
        "A wrapper around CreateSimpleMenuInternal where ownership of the simple_menu_items array parameter won't be transferred to the menu.\n\nThe menu item array will be copied onto a new array on the heap. This means the argument doesn't need to remain valid after the function returns (e.g., it can be stack-allocated).\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: simple_menu_items array\nstack[0]: number of items\nreturn: window_id",
    )

    CreateSimpleMenuInternal = Symbol(
        None,
        None,
        None,
        "Creates a window containing a simple textual menu with a list of options. Also see struct simple_menu.\n\nThis is used in lots of places. For example, some simple Yes/No prompts.\n\nIf window_params is NULL, SIMPLE_MENU_DEFAULT_WINDOW_PARAMS will be used. Otherwise, it will be copied onto the window, ignoring the update and contents fields. If window_params::width and/or window_params::height are 0, they will be computed based on the contained text.\n\nIf window_extra_info is non-NULL, it will be copied onto the window. Note that window_extra_info can only be NULL if there are no window_flags set that require extra info.\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: heap-allocated simple_menu_items array, the menu takes ownership\nstack[0]: number of items\nreturn: window_id",
    )

    ResumeSimpleMenu = Symbol(
        None,
        None,
        None,
        "Resumes input for a window created with CreateSimpleMenuInternal. Used for menus that do not close even after selecting an option.\n\nr0: window_id",
    )

    CloseSimpleMenu = Symbol(
        None,
        None,
        None,
        "Closes a window created with CreateSimpleMenu or CreateSimpleMenuFromStringIds.\n\nr0: window_id",
    )

    IsSimpleMenuActive = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nChecks if the menu state is anything other than 7 or 8.\n\nr0: window_id\nreturn: bool",
    )

    CheckSimpleMenuField0x1A0 = Symbol(
        None,
        None,
        None,
        "Checks if simple_menu::field_0x1a0 is 0.\n\nr0: window_id\nreturn: bool",
    )

    GetSimpleMenuField0x1A4 = Symbol(
        None,
        None,
        None,
        "Gets the value of simple_menu::field_0x1a4.\n\nr0: window_id\nreturn: field_0x1a4",
    )

    GetSimpleMenuResult = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: window_id\nreturn: ?",
    )

    UpdateSimpleMenu = Symbol(
        None,
        None,
        None,
        "Window update function for simple menus.\n\nr0: window pointer",
    )

    SetSimpleMenuField0x1AC = Symbol(
        None,
        None,
        None,
        "Sets simple_menu::field_0x1ac to the given value.\n\nr0: window_id\nr1: value",
    )

    CreateAdvancedMenu = Symbol(
        None,
        None,
        None,
        "Creates a window containing a textual menu with complex layout and functionality (e.g., paging through multiple pages). Also see struct advanced_menu.\n\nThis is used for menus like the IQ skills menu, and the dungeon selection menu from the overworld crossroads. Curiously, it's also used in some non-interactive contexts like the Adventure Log.\n\nIf window_params is NULL, ADVANCED_MENU_DEFAULT_WINDOW_PARAMS will be used. Otherwise, it will be copied onto the window, ignoring the update and contents fields. If window_params::width and/or window_params::height are 0, they will be computed based on the contained text.\n\nIf window_extra_info is non-NULL, it will be copied onto the window. Note that window_extra_info can only be NULL if there are no window_flags set that require extra info.\n\nThe entry function is used to get the strings for all currently available options, so when the page is flipped the entry function is used to get the strings for the entries on the other page?\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: entry_function\nstack[0]: total number of options\nstack[1]: number of options per page\nreturn: window_id",
    )

    ResumeAdvancedMenu = Symbol(
        None,
        None,
        None,
        "Resumes input for a window created with CreateAdvancedMenu. Used for menus that do not close even after selecting an option.\n\nr0: window_id",
    )

    CloseAdvancedMenu = Symbol(
        None,
        None,
        None,
        "Closes a window created with CreateAdvancedMenu.\n\nr0: window_id",
    )

    IsAdvancedMenuActive2 = Symbol(
        None,
        None,
        None,
        "This is a guess, by analogy to IsSimpleMenuActive, which does the same thing. Most of window types also have an analogous function that checks the state value. It's unclear how this relates to the other IsAdvancedMenuActive, or if this guess is completely wrong.\n\nChecks if the state of an advanced menu is something other than 7 or 8.\n\nr0: window_id\nreturn: bool",
    )

    IsAdvancedMenuActive = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nChecks if advanced_menu::field_0x1a0 is 0.\n\nThis seems to resemble the Check*Field* functions of some of the other menu types. It's unclear whether these are the real 'IsActive' functions, or whether the ones that check the state value are. It may be noteworthy that all menu types seem to have a variant of the 'state checking' function, but only some menu types seem to have a variant of the 'check field' function.\n\nr0: window_id\nreturn: bool",
    )

    GetAdvancedMenuCurrentOption = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: window_id\nreturn: ?",
    )

    GetAdvancedMenuResult = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: window_id\nreturn: ?",
    )

    UpdateAdvancedMenu = Symbol(
        None,
        None,
        None,
        "Window update function for advanced menus.\n\nr0: window pointer",
    )

    CreateCollectionMenu = Symbol(
        None,
        None,
        None,
        "Creates a window containing a menu for manipulating a collection of objects, with complex layout and functionality (e.g., paging). Also see struct collection_menu.\n\nCollection menus seem similar to advanced menus, but are used for certain menus involving item management (Kangaskhan Storage, Kecleon shop, Croagunk Swap Shop), missions (job selection, bulletin board), and possibly other things.\n\nIf window_params is NULL, COLLECTION_MENU_DEFAULT_WINDOW_PARAMS will be used. Otherwise, it will be copied onto the window, ignoring the update and contents fields. If window_params::width and/or window_params::height are 0, they will be computed based on the contained text.\n\nIf window_extra_info is non-NULL, it will be copied onto the window. Note that window_extra_info can only be NULL if there are no window_flags set that require extra info.\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: some function pointer?\nstack[0]: ?\nstack[1]: total number of options\nstack[2]: number of options per page\nreturn: window_id",
    )

    SetCollectionMenuField0x1BC = Symbol(
        None,
        None,
        None,
        "Sets collection_menu::field_0x1bc to the given value.\n\nr0: window_id\nr1: value",
    )

    SetCollectionMenuWidth = Symbol(
        None,
        None,
        None,
        "Sets collection_menu::width to a new value, clamped to be no greater than (window_params::width * 8 - 1) for the window.\n\nr0: window_id\nr1: width",
    )

    CloseCollectionMenu = Symbol(
        None,
        None,
        None,
        "Closes a window created with CreateCollectionMenu.\n\nr0: window_id",
    )

    IsCollectionMenuActive = Symbol(
        None,
        None,
        None,
        "This is a guess.\n\nChecks if the state of a collection menu is something other than 6 or 7.\n\nr0: window_id\nreturn: bool",
    )

    SetCollectionMenuField0x1C8 = Symbol(
        None,
        None,
        None,
        "Sets collection_menu::field_0x1c8 to the given value.\n\nr0: window_id\nr1: value",
    )

    SetCollectionMenuField0x1A0 = Symbol(
        None,
        None,
        None,
        "Sets collection_menu::field_0x1a0 to the given value.\n\nr0: window_id\nr1: value",
    )

    SetCollectionMenuField0x1A4 = Symbol(
        None,
        None,
        None,
        "Sets collection_menu::field_0x1a4 to the given value.\n\nr0: window_id\nr1: value",
    )

    SetCollectionMenuVoidFn = Symbol(
        None,
        None,
        None,
        "Sets collection_menu::field_0x1a8 to the given function pointer.\n\nr0: window_id\nr1: some function pointer?",
    )

    UpdateCollectionMenu = Symbol(
        None,
        None,
        None,
        "Window update function for collection menus.\n\nr0: window pointer",
    )

    SetCollectionMenuField0x1B2 = Symbol(
        None,
        None,
        None,
        "Sets collection_menu::field_0x1b2 to the given value.\n\nr0: window_id\nr1: value",
    )

    IsCollectionMenuState3 = Symbol(
        None,
        None,
        None,
        "Checks if a collection menu has a state value of 3.\n\nr0: window_id\nreturn: bool",
    )

    CreateOptionsMenu = Symbol(
        None,
        None,
        None,
        "Creates a window containing a menu controlling game options. Also see struct options_menu.\n\nThis is used for the options and window options menus, among other things.\n\nIf window_params is NULL, OPTIONS_MENU_DEFAULT_WINDOW_PARAMS will be used. Otherwise, it will be copied onto the window, ignoring the update and contents fields. If window_params::width and/or window_params::height are 0, they will be computed based on the contained text.\n\nIf window_extra_info is non-NULL, it will be copied onto the window. Note that window_extra_info can only be NULL if there are no window_flags set that require extra info.\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: options_menu_id_item struct array, terminated with an item with msg_id 0\nstack[0]: number of items\nstack[1]: ?\nreturn: window_id",
    )

    CloseOptionsMenu = Symbol(
        None,
        None,
        None,
        "Closes a window created with CreateOptionsMenu.\n\nr0: window_id",
    )

    IsOptionsMenuActive = Symbol(
        None,
        None,
        None,
        "This is a guess.\n\nChecks if the state of an options menu is something other than 6 or 7.\n\nr0: window_id\nreturn: bool",
    )

    CheckOptionsMenuField0x1A4 = Symbol(
        None,
        None,
        None,
        "Checks if options_menu::field_0x1a4 is 0.\n\nr0: window_id\nreturn: bool",
    )

    UpdateOptionsMenu = Symbol(
        None,
        None,
        None,
        "Window update function for options menus.\n\nr0: window pointer",
    )

    CreateDebugMenu = Symbol(
        None,
        None,
        None,
        "Creates a window containing the debug menu (probably). Also see struct debug_menu.\n\nThis is an educated guess, since this function references string IDs of debug menu strings.\n\nSee enum debug_flag and enum debug_log_flag.\n\nIf window_params is NULL, DEBUG_MENU_DEFAULT_WINDOW_PARAMS will be used. Otherwise, it will be copied onto the window, ignoring the update and contents fields. If window_params::width and/or window_params::height are 0, they will be computed based on the contained text.\n\nIf window_extra_info is non-NULL, it will be copied onto the window. Note that window_extra_info can only be NULL if there are no window_flags set that require extra info.\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: array of menu item string IDs\nstack[0]: number of menu items\nstack[1]: ?\nreturn: window_id",
    )

    CloseDebugMenu = Symbol(
        None,
        None,
        None,
        "Closes a window created with CreateDebugMenu.\n\nr0: window_id",
    )

    IsDebugMenuActive = Symbol(
        None,
        None,
        None,
        "This is a guess.\n\nChecks if the state of a debug menu is something other than 6 or 7.\n\nr0: window_id\nreturn: bool",
    )

    CheckDebugMenuField0x1A4 = Symbol(
        None,
        None,
        None,
        "Checks if debug_menu::field_0x1a4 is 0.\n\nr0: window_id\nreturn: bool",
    )

    UpdateDebugMenu = Symbol(
        None,
        None,
        None,
        "Window update function for debug menus.\n\nr0: window pointer",
    )

    CreateScrollBoxSingle = Symbol(
        None,
        None,
        None,
        "Creates window containing text that pages vertically on overflow, with a single pair of strings. Also see struct scroll_box.\n\nThis includes things like descriptions for items and moves.\n\nIf window_params is NULL, SCROLL_BOX_DEFAULT_WINDOW_PARAMS will be used. Otherwise, it will be copied onto the window, ignoring the update and contents fields.\n\nIf window_extra_info is non-NULL, it will be copied onto the window. Note that window_extra_info can only be NULL if there are no window_flags set that require extra info.\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: string ID 1\nstack[0]: preprocessor args 1\nstack[1]: string ID 2\nstack[2]: preprocessor args 2\nreturn: window_id",
    )

    CreateScrollBoxMulti = Symbol(
        None,
        None,
        None,
        "Creates window containing text that pages vertically on overflow, with an array of string pairs. Also see struct scroll_box.\n\nThis includes things like descriptions for items and moves.\n\nIf window_params is NULL, SCROLL_BOX_DEFAULT_WINDOW_PARAMS will be used. Otherwise, it will be copied onto the window, ignoring the update and contents fields.\n\nIf window_extra_info is non-NULL, it will be copied onto the window. Note that window_extra_info can only be NULL if there are no window_flags set that require extra info.\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: number of string pairs\nstack[0]: string ID 1 array\nstack[1]: preprocessor args 1 array\nstack[2]: string ID 2 array\nstack[3]: preprocessor args 2 array\nreturn: window_id",
    )

    SetScrollBoxState7 = Symbol(
        None, None, None, "Sets the state of a scroll box to 7.\n\nr0: window_id"
    )

    CloseScrollBox = Symbol(
        None,
        None,
        None,
        "Closes a window created with CreateScrollBoxSingle or CreateScrollBoxMulti.\n\nr0: window_id",
    )

    IsScrollBoxActive = Symbol(
        None,
        None,
        None,
        "This is a guess.\n\nChecks if the state of a scroll box is not 8.\n\nr0: window_id\nreturn: bool",
    )

    UpdateScrollBox = Symbol(
        None,
        None,
        None,
        "Window update function for scroll boxes.\n\nr0: window pointer",
    )

    CreateDialogueBox = Symbol(
        None,
        None,
        None,
        "Creates a window containing text that is gradually revealed via scrolling, and pages on overflow. Also see struct dialogue_box.\n\nThis is primarily used for character dialogue, hence the name. However, it can also be used for other types of messages. The defining feature of this window type is the scrolling/paging behavior.\n\nIf window_params is NULL, DIALOGUE_BOX_DEFAULT_WINDOW_PARAMS will be used. Otherwise, it will be copied onto the window, ignoring the update and contents fields.\n\nr0: window_params\nreturn: window_id",
    )

    CloseDialogueBox = Symbol(
        None,
        None,
        None,
        "Closes a window created with CreateDialogueBox.\n\nr0: window_id",
    )

    IsDialogueBoxActive = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: window_id\nreturn: bool",
    )

    ShowStringIdInDialogueBox = Symbol(
        None,
        None,
        None,
        "Preprocesses the corresponding string_id message in the text file and puts it into the dialogue box.\n\nr0: window_id\nr1: preprocessor flags (see PreprocessString)\nr2: string_id\nr3: pointer to preprocessor args (see PreprocessString)",
    )

    ShowStringInDialogueBox = Symbol(
        None,
        None,
        None,
        "Preprocesses the passed string and puts it into the dialogue box.\n\nr0: window_id\nr1: preprocessor flags (see PreprocessString)\nr2: string\nr3: pointer to preprocessor args (see PreprocessString)",
    )

    ShowDialogueBox = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: window_id",
    )

    ReadStringFromDialogueBox = Symbol(
        None,
        None,
        None,
        "Copies data from the dialogue box's string buffer into an output buffer.\n\nr0: window_id\nr1: [output] string buffer\nr2: number of bytes to read",
    )

    UpdateDialogueBox = Symbol(
        None,
        None,
        None,
        "Window update function for dialogue boxes.\n\nr0: window pointer",
    )

    CreatePortraitBox = Symbol(
        None,
        None,
        None,
        "Creates a window containing a character portrait. Also see struct portrait_box.\n\nThis is commonly paired with a dialogue box, but can also be used standalone.\n\nIf framed, the window box type will be 0xFC, otherwise it will be 0xF9.\n\nThe new window will always default to PORTRAIT_BOX_DEFAULT_WINDOW_PARAMS.\n\nr0: screen index\nr1: palette_idx\nr2: framed\nreturn: window_id",
    )

    ClosePortraitBox = Symbol(
        None,
        None,
        None,
        "Closes a window created with CreatePortraitBox.\n\nr0: window_id",
    )

    PortraitBoxNeedsUpdate = Symbol(
        None,
        None,
        None,
        "Checks if a portrait box has a state of PORTRAIT_BOX_TRY_UPDATE or PORTRAIT_BOX_UPDATE.\n\nr0: window_id\nreturn: bool",
    )

    ShowPortraitInPortraitBox = Symbol(
        None,
        None,
        None,
        "Stages a portrait to be rendered in a portrait box at next update (sets portrait_box::buffer_state).\n\nIf portrait is NULL, the default portrait will be shown (see InitPortraitParams).\n\nr0: window_id\nr1: portrait params pointer",
    )

    HidePortraitBox = Symbol(
        None,
        None,
        None,
        "Flags a portrait box to be hidden at next update (sets portrait_box::hide) if it's not already in the PORTRAIT_BOX_HIDDEN state, and resets its buffer state.\n\nr0: window_id",
    )

    UpdatePortraitBox = Symbol(
        None,
        None,
        None,
        "Window update function for portrait boxes.\n\nr0: window pointer",
    )

    CreateTextBox = Symbol(
        None,
        None,
        None,
        "Calls CreateTextBoxInternal, sets the callback without an argument, and returns the window_id.\n\nr0: window_params\nr1: text box callback function\nreturn: window_id",
    )

    CreateTextBoxWithArg = Symbol(
        None,
        None,
        None,
        "Calls CreateTextBoxInternal, sets the callback with an argument, and returns the window_id.\n\nr0: window_params\nr1: text box callback with arg function\nr2: callback argument\nreturn: window_id",
    )

    CloseTextBox = Symbol(
        None,
        None,
        None,
        "Closes a window created with CreateTextBox or CreateTextBoxWithArg.\n\nr0: window_id",
    )

    CloseTextBox2 = Symbol(
        None,
        None,
        None,
        "Seems to do some things with the text box, before doing the same things that CloseTextBox does.\n\nr0: window_id",
    )

    CreateTextBoxInternal = Symbol(
        None,
        None,
        None,
        "Creates a window containing simple text, without much advanced functionality. Also see struct text_box.\n\nIf window_params is NULL, TEXT_BOX_DEFAULT_WINDOW_PARAMS will be used. Otherwise, it will be copied onto the window, ignoring the update and contents fields.\n\nr0: window_params\nreturn: text_box pointer",
    )

    UpdateTextBox = Symbol(
        None, None, None, "Window update function for text boxes.\n\nr0: window pointer"
    )

    IsTextBoxActive = Symbol(
        None,
        None,
        None,
        "This is a guess.\n\nChecks if the state of a text box is not 7.\n\nr0: window_id\nreturn: bool",
    )

    CreateAreaNameBox = Symbol(
        None,
        None,
        None,
        "Creates a window containing the area name, as resolved from the '[area:0]' tag.\n\nThis only seems to be used for the 'area name' text box in the top-level menu in ground mode (not dungeon mode), and the analogous text box on the world map transition screen before entering a dungeon.\n\nIf window_params is NULL, AREA_NAME_BOX_DEFAULT_WINDOW_PARAMS will be used. Otherwise, it will be copied onto the window, ignoring the update and contents fields. If window_params::width is 0, it will be computed based on the contained text. If window_params::height is 0, it will default to 2.\n\nIf window_extra_info is non-NULL, it will be copied onto the window. Note that window_extra_info can only be NULL if there are no window_flags set that require extra info.\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: ID (for preprocessor_args)\nreturn: window_id",
    )

    SetAreaNameBoxState3 = Symbol(
        None, None, None, "Sets the state of an area name box to 3.\n\nr0: window_id"
    )

    CloseAreaNameBox = Symbol(
        None,
        None,
        None,
        "Closes a window created with CreateAreaNameBox.\n\nr0: window_id",
    )

    IsAreaNameBoxActive = Symbol(
        None,
        None,
        None,
        "This is a guess.\n\nChecks if the state of an area name box is something other than 2 or 4.\n\nr0: window_id\nreturn: bool",
    )

    UpdateAreaNameBox = Symbol(
        None,
        None,
        None,
        "Window update function for area name boxes.\n\nr0: window pointer",
    )

    CreateControlsChart = Symbol(
        None,
        None,
        None,
        "Creates a window containing a chart of player controls for some context. Also see struct controls_chart.\n\nThis is usually used for static top-screen control reference charts.\n\nIf window_params is NULL, CONTROLS_CHART_DEFAULT_WINDOW_PARAMS will be used. Otherwise, it will be copied onto the window, ignoring the update and contents fields.\n\nIf window_extra_info is non-NULL, it will be copied onto the window. Note that window_extra_info can only be NULL if there are no window_flags set that require extra info.\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: string ID\nreturn: window_id",
    )

    CloseControlsChart = Symbol(
        None,
        None,
        None,
        "Closes a window created with CreateControlsChart.\n\nr0: window_id",
    )

    IsControlsChartActive = Symbol(
        None,
        None,
        None,
        "This is a guess.\n\nChecks if the state of a controls chart is something other than 2 or 4.\n\nr0: window_id\nreturn: bool",
    )

    UpdateControlsChart = Symbol(
        None,
        None,
        None,
        "Window update function for controls charts.\n\nr0: window pointer",
    )

    CreateAlertBox = Symbol(
        None,
        None,
        None,
        "Creates a window containing text that will disappear after a certain amount of time. Also see struct alert_box.\n\nThis is only used in dungeon mode, for the 'popup alert' messages about things happening in the dungeon (which will also be accessible in the message logs).\n\nIf window_params is NULL, ALERT_BOX_DEFAULT_WINDOW_PARAMS will be used. Otherwise, it will be copied onto the window, ignoring the update and contents fields.\n\nr0: window_params\nreturn: window_id",
    )

    CloseAlertBox = Symbol(
        None,
        None,
        None,
        "Closes a window created with CreateAlertBox.\n\nr0: window_id",
    )

    IsAlertBoxActive = Symbol(
        None,
        None,
        None,
        "This is a guess.\n\nChecks if the state of an alert box is 3.\n\nr0: window_id\nreturn: bool",
    )

    UpdateAlertBox = Symbol(
        None,
        None,
        None,
        "Window update function for alert boxes.\n\nr0: window pointer",
    )

    CreateAdvancedTextBox = Symbol(
        None,
        None,
        None,
        "Calls CreateAdvancedTextBoxInternal with all the selectable items on one page (n_items_per_page = n_items), sets the callback without an argument, and returns the window_id.\n\nIf window_params is NULL, ADVANCED_TEXT_BOX_DEFAULT_WINDOW_PARAMS will be used. Otherwise, it will be copied onto the window, ignoring the update and contents fields.\n\nIf window_extra_info is non-NULL, it will be copied onto the window. Note that window_extra_info can only be NULL if there are no window_flags set that require extra info.\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: text box callback function\nstack[0]: number of selectable items\nreturn: window_id",
    )

    CreateAdvancedTextBoxWithArg = Symbol(
        None,
        None,
        None,
        "Calls CreateAdvancedTextBoxInternal with all the selectable items on one page (n_items_per_page = n_items), sets the callback with an argument, and returns the window_id.\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: text box callback with arg function\nstack[0]: callback argument\nstack[1]: number of selectable items\nreturn: window_id",
    )

    CreateAdvancedTextBoxInternal = Symbol(
        None,
        None,
        None,
        "Creates a window containing text formatted in complex, potentially sectioned layouts. Also see struct advanced_text_box.\n\nThis is usually used to display text with 'pretty' formatting in certain contexts, such as the message log, the move selection menu, team member summaries, etc.\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: total number of selectable items\nstack[0]: number of selectable items per page\nreturn: advanced_text_box pointer",
    )

    SetAdvancedTextBoxPartialMenu = Symbol(
        None,
        None,
        None,
        "Seems to set advanced_text_box::flags::partial_menu to the given value?\n\nr0: window_id\nr1: partial_menu flag value",
    )

    SetAdvancedTextBoxField0x1C4 = Symbol(
        None,
        None,
        None,
        "Sets the value of advanced_text_box::field_0x1c4 to the given value.\n\nr0: window_id\nr1: value",
    )

    SetAdvancedTextBoxField0x1C2 = Symbol(
        None, None, None, "Sets advanced_text_box::field_0x1c2 to 1.\n\nr0: window_id"
    )

    CloseAdvancedTextBox2 = Symbol(
        None,
        None,
        None,
        "Seems to do some things with the text box, before doing the same things that CloseAdvancedTextBox does.\n\nr0: window_id",
    )

    SetAdvancedTextBoxState5 = Symbol(
        None,
        None,
        None,
        "Sets the state of an advanced text box to 5.\n\nr0: window_id",
    )

    CloseAdvancedTextBox = Symbol(
        None,
        None,
        None,
        "Closes a window created with CreateAdvancedTextBox or CreateAdvancedTextBoxWithArg.\n\nr0: window_id",
    )

    IsAdvancedTextBoxActive = Symbol(
        None,
        None,
        None,
        "This is a guess.\n\nChecks if the state of an advanced text box is something other than 6 or 7.\n\nr0: window_id\nreturn: bool",
    )

    GetAdvancedTextBoxFlags2 = Symbol(
        None,
        None,
        None,
        "Gets the value of advanced_text_box::flags2.\n\nr0: window_id\nreturn: flags2",
    )

    SetUnkAdvancedTextBoxFn = Symbol(
        None,
        None,
        None,
        "Sets the value of advanced_text_box::field_0x1b4 to the given function pointer.\n\nr0: window_id\nr1: some function pointer?",
    )

    SetUnkAdvancedTextBoxWindowFn = Symbol(
        None,
        None,
        None,
        "Sets the value of advanced_text_box::field_0x1b8 to the given function pointer.\n\nr0: window_id\nr1: some function pointer?",
    )

    UpdateAdvancedTextBox = Symbol(
        None,
        None,
        None,
        "Window update function for advanced text boxes.\n\nr0: window pointer",
    )

    PlayAdvancedTextBoxInputSound = Symbol(
        None,
        None,
        None,
        "Calls PlayWindowInputSound for an advanced text box.\n\nr0: window_id\nr1: index for PlayWindowInputSound",
    )

    CreateTeamSelectionMenu = Symbol(
        None,
        None,
        None,
        "Creates a window containing a menu for selecting a single team member. Also see struct team_selection_menu.\n\nIf window_params::width and/or window_params::height are 0, they will be computed based on the contained text.\n\nThis appears to be used for various shop (and shop-like) interfaces when a single team member needs to be selected. For example, the Electivire Link Shop, the Chimecho Assembly, the Croagunk Swap Shop, and Luminous Spring. It's unknown if this is used for other contexts besides team member selection.\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: function to get the menu item text for a given team member\nstack[0]: total number of options\nstack[1]: number of options per page\nreturn: window_id",
    )

    CloseTeamSelectionMenu = Symbol(
        None,
        None,
        None,
        "Closes a window created with CreateTeamSelectionMenu.\n\nr0: window_id",
    )

    IsTeamSelectionMenuActive = Symbol(
        None,
        None,
        None,
        "This is a guess.\n\nChecks if the state of a team selection menu is something other than 6 or 7.\n\nr0: window_id\nreturn: bool",
    )

    UpdateTeamSelectionMenu = Symbol(
        None,
        None,
        None,
        "Window update function for team selection menus.\n\nr0: window pointer",
    )

    IsTeamSelectionMenuState3 = Symbol(
        None,
        None,
        None,
        "Checks if the state of a team selection menu is 3.\n\nr0: window_id",
    )

    CalcMenuHeightDiv8 = Symbol(
        None,
        None,
        None,
        "Calculates the window height (divided by 8, as in struct window_params) of a menu, given its items and input flags.\n\nFor certain input flags, the number of options per page will be clamped to the total number of options if the per-page count exceeds the total.\n\nr0: window_flags\nr1: window_extra_info pointer\nr2: total number of options\nr3: number of options per page\nreturn: height / 8",
    )

    InitWindowInput = Symbol(
        None,
        None,
        None,
        "This seems to be called when creating most interactive windows that respond to user input, like menus (but also other interactive windows like scroll boxes and advanced text boxes). It presumably sets up the state necessary for detecting and responding to user input.\n\nr0: window_input_ctx pointer\nr1: window_flags\nr2: window_extra_info pointer\nr3: window rectangle\nstack[0]: total number of selectable items\nstack[1]: number of selectable items per page",
    )

    IsMenuOptionActive = Symbol(
        None,
        None,
        None,
        "Called whenever a menu option is selected. Returns whether the option is active or not.\n\nr0: ?\nreturn: True if the menu option is enabled, false otherwise.",
    )

    PlayWindowInputSound = Symbol(
        None,
        None,
        None,
        "Plays a 'beep' sound when giving an input to an interactive window (typically, when choosing a menu option).\n\nr0: window_input_ctx pointer\nr1: Some kind of index used to determine the ID of the sound to play",
    )

    InitInventoryMenuInput = Symbol(
        None,
        None,
        None,
        "Almost exactly the same as InitWindowInput, except two differences in field assignments on the window input context, one of which uses an extra parameter.\n\nr0: inventory_menu_input_ctx pointer\nr1: window_flags\nr2: window_extra_info pointer\nr3: window rectangle\nstack[0]: total number of selectable items\nstack[1]: number of selectable items per page\nstack[2]: ?",
    )

    ShowKeyboard = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: string ID\nr1: buffer1\nr2: ???\nr3: buffer2\nreturn: ?",
    )

    GetKeyboardStatus = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nreturn: ?"
    )

    GetKeyboardStringResult = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nreturn: ?"
    )

    TeamSelectionMenuGetItem = Symbol(
        None,
        None,
        None,
        "Gets the menu item text (member name) for a given team member for a team selection menu.\n\nr0: buffer\nr1: team member index\nreturn: menu item text (points into buffer)",
    )

    PrintMoveOptionMenu = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nNo params."
    )

    PrintIqSkillsMenu = Symbol(
        None,
        None,
        None,
        "Draws the IQ skills menu for a certain monster.\n\nr0: Monster species\nr1: Pointer to bitarray where the enabled skills will be written when enabling or disabling them in the menu\nr2: Monster IQ\nr3: True if the monster is blinded",
    )

    GetNotifyNote = Symbol(
        None, None, None, "Returns the current value of NOTIFY_NOTE.\n\nreturn: bool"
    )

    SetNotifyNote = Symbol(
        None, None, None, "Sets NOTIFY_NOTE to the given value.\n\nr0: bool"
    )

    InitSpecialEpisodeHero = Symbol(
        None,
        None,
        None,
        "Removes/invalidates the special episode member slots, zero inits the special episode treasure bag, zero inits the\nspecial episode Kecleon shops, zero inits VAR_WORLD_MAP_MARK_LIST_SPECIAL, sets VAR_SPECIAL_EPISODE_OPEN_OLD for\nthe corresponding special episode, and initializes the hero for the special episode.\n\nNo params.",
    )

    EventFlagBackupVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for EventFlagBackup.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nNo params.",
    )

    InitMainTeamAfterQuiz = Symbol(
        None,
        None,
        None,
        "Implements SPECIAL_PROC_INIT_MAIN_TEAM_AFTER_QUIZ (see ScriptSpecialProcessCall).\n\nNo params.",
    )

    InitSpecialEpisodePartners = Symbol(
        None,
        None,
        None,
        "Initializes the partners for the current special episode and sets the team to be the hero and partner only.\nImplements SPECIAL_PROC_0x3 (see ScriptSpecialProcessCall). \n\nNo params.",
    )

    InitSpecialEpisodeExtraPartner = Symbol(
        None,
        None,
        None,
        "Initializes any partners/special episode members that join the team later in a special episode. This is used to add\nCelebi in the In the Future of Darkness special episode.\nImplements SPECIAL_PROC_0x4 (see ScriptSpecialProcessCall).\n\nNo params.",
    )

    ReadStringSave = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nr0: buffer"
    )

    CheckStringSave = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: buffer\nreturn: bool",
    )

    WriteSaveFile = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: save_info\nr1: buffer\nr2: size\nreturn: status code",
    )

    ReadSaveFile = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: save_info\nr1: buffer\nr2: size\nreturn: status code",
    )

    CalcChecksum = Symbol(
        None,
        None,
        None,
        "Calculates the checksum of the save file and stores it at the start of the data.\n\nr0: Pointer to a buffer containing the save data\nr1: Size in bytes",
    )

    CheckChecksumInvalid = Symbol(
        None,
        None,
        None,
        "Calculates the checksum of the save file and compares it with the one stored in it.\n\nr0: Pointer to a buffer containing the save data\nr1: Size in bytes\nreturn: True if the calculated and stored checksums don't match, false if they do.",
    )

    NoteSaveBase = Symbol(
        None,
        None,
        None,
        "Probably related to saving or quicksaving?\n\nThis function prints the debug message 'NoteSave Base %d %d' with some values. It's also the only place where GetRngSeed is called.\n\nr0: Irdkwia's notes: state ID\nothers: ?\nreturn: status code",
    )

    WriteQuickSaveInfo = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: buffer\nr1: size",
    )

    ReadSaveHeader = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    NoteLoadBase = Symbol(
        None,
        None,
        None,
        "Probably related to loading a save file or quicksave?\n\nThis function prints the debug message 'NoteLoad Base %d' with some value. It's also the only place where SetRngSeed is called.\n\nreturn: status code",
    )

    ReadQuickSaveInfo = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: buffer\nr1: size\nreturn: status code",
    )

    GetGameMode = Symbol(
        None, None, None, "Gets the value of GAME_MODE.\n\nreturn: game mode"
    )

    InitScriptVariableValues = Symbol(
        None,
        None,
        None,
        "Initialize the script variable values table (SCRIPT_VARS_VALUES).\n\nThe whole table is first zero-initialized. Then, all script variable values are first initialized to their defaults, after which some of them are overwritten with other hard-coded values.\n\nNo params.",
    )

    InitEventFlagScriptVars = Symbol(
        None,
        None,
        None,
        "Initializes an assortment of event flag script variables (see the code for an exhaustive list).\n\nNo params.",
    )

    ZinitScriptVariable = Symbol(
        None,
        None,
        None,
        "Zero-initialize the values of the given script variable.\n\nr0: pointer to the local variable table (only needed if id >= VAR_LOCAL0)\nr1: script variable ID",
    )

    LoadScriptVariableRaw = Symbol(
        None,
        None,
        None,
        "Loads a script variable descriptor for a given ID.\n\nr0: [output] script variable descriptor pointer\nr1: pointer to the local variable table (doesn't need to be valid; just controls the output value pointer)\nr2: script variable ID",
    )

    LoadScriptVariableValue = Symbol(
        None,
        None,
        None,
        "Loads the value of a script variable.\n\nr0: pointer to the local variable table (only needed if id >= VAR_LOCAL0)\nr1: script variable ID\nreturn: value",
    )

    LoadScriptVariableValueAtIndex = Symbol(
        None,
        None,
        None,
        "Loads the value of a script variable at some index (for script variables that are arrays).\n\nr0: pointer to the local variable table (only needed if id >= VAR_LOCAL0)\nr1: script variable ID\nr2: value index for the given script var\nreturn: value",
    )

    SaveScriptVariableValue = Symbol(
        None,
        None,
        None,
        "Saves the given value to a script variable.\n\nr0: pointer to local variable table (only needed if id >= VAR_LOCAL0)\nr1: script variable ID\nr2: value to save",
    )

    SaveScriptVariableValueAtIndex = Symbol(
        None,
        None,
        None,
        "Saves the given value to a script variable at some index (for script variables that are arrays).\n\nr0: pointer to local variable table (only needed if id >= VAR_LOCAL0)\nr1: script variable ID\nr2: value index for the given script var\nr3: value to save",
    )

    LoadScriptVariableValueSum = Symbol(
        None,
        None,
        None,
        "Loads the sum of all values of a given script variable (for script variables that are arrays).\n\nr0: pointer to the local variable table (only needed if id >= VAR_LOCAL0)\nr1: script variable ID\nreturn: sum of values",
    )

    LoadScriptVariableValueBytes = Symbol(
        None,
        None,
        None,
        "Loads some number of bytes from the value of a given script variable.\n\nr0: script variable ID\nr1: [output] script variable value bytes\nr2: number of bytes to load",
    )

    SaveScriptVariableValueBytes = Symbol(
        None,
        None,
        None,
        "Saves some number of bytes to the given script variable.\n\nr0: script variable ID\nr1: bytes to save\nr2: number of bytes",
    )

    ScriptVariablesEqual = Symbol(
        None,
        None,
        None,
        "Checks if two script variables have equal values. For arrays, compares elementwise for the length of the first variable.\n\nr0: pointer to the local variable table (only needed if id >= VAR_LOCAL0)\nr1: script variable ID 1\nr2: script variable ID 2\nreturn: true if values are equal, false otherwise",
    )

    EventFlagResume = Symbol(
        None,
        None,
        None,
        "Restores BACKUP event flag script variables (see the code for an exhaustive list) to their\nrespective script variables, but only in certain game modes.\n\nThis function prints the debug string 'EventFlag BackupGameMode %d' with the game mode.\n\nNo params.",
    )

    EventFlagBackup = Symbol(
        None,
        None,
        None,
        "Saves event flag script variables (see the code for an exhaustive list) to their respective BACKUP script variables, but only in certain game modes.\n\nThis function prints the debug string 'EventFlag BackupGameMode %d' with the game mode.\n\nNo params.",
    )

    DumpScriptVariableValues = Symbol(
        None,
        None,
        None,
        "Runs EventFlagBackup, then copies the script variable values table (SCRIPT_VARS_VALUES) to the given pointer.\n\nr0: destination pointer for the data dump\nreturn: always 1",
    )

    RestoreScriptVariableValues = Symbol(
        None,
        None,
        None,
        "Restores the script variable values table (SCRIPT_VARS_VALUES) with the given data. The source data is assumed to be exactly 1024 bytes in length.\n\nIrdkwia's notes: CheckCorrectVersion\n\nr0: raw data to copy to the values table\nreturn: whether the restored value for VAR_VERSION is equal to its default value",
    )

    InitScenarioScriptVars = Symbol(
        None,
        None,
        None,
        "Initializes most of the SCENARIO_* script variables (except SCENARIO_TALK_BIT_FLAG for some reason). Also initializes the PLAY_OLD_GAME variable.\n\nNo params.",
    )

    SetScenarioScriptVar = Symbol(
        None,
        None,
        None,
        "Sets the given SCENARIO_* script variable with a given pair of values [val0, val1].\n\nIn the special case when the ID is VAR_SCENARIO_MAIN, and the set value is different from the old one, the REQUEST_CLEAR_COUNT script variable will be set to 0.\n\nr0: script variable ID\nr1: val0\nr2: val1",
    )

    GetSpecialEpisodeType = Symbol(
        None,
        None,
        None,
        "Gets the special episode type from the SPECIAL_EPISODE_TYPE script variable.\n\nreturn: special episode type",
    )

    SetSpecialEpisodeType = Symbol(
        None,
        None,
        None,
        "Sets the special episode type by changing the SPECIAL_EPISODE_TYPE script variable.\n\nr0: special episode type",
    )

    GetExecuteSpecialEpisodeType = Symbol(
        None,
        None,
        None,
        "Gets the special episode type from the EXECUTE_SPECIAL_EPISODE_TYPE script variable.\n\nreturn: special episode type",
    )

    IsSpecialEpisodeOpen = Symbol(
        None,
        None,
        None,
        "Checks if a special episode is unlocked from the SPECIAL_EPISODE_OPEN script variable.\n\nr0: special episode type\nreturn: bool",
    )

    HasPlayedOldGame = Symbol(
        None,
        None,
        None,
        "Returns the value of the VAR_PLAY_OLD_GAME script variable.\n\nreturn: bool",
    )

    GetPerformanceFlagWithChecks = Symbol(
        None,
        None,
        None,
        "Returns the value of one of the flags in VAR_PERFORMANCE_PROGRESS_LIST, with some edge cases.\n\nList of cases where the function behaves differently:\n- If the requested flag is 0, returns true if and only if SCENARIO_MAIN == 0x35\n- If the requested flag is 1 or 2 and GAME_MODE == GAME_MODE_SPECIAL_EPISODE, returns true\n- If the requested flag is between 3 and 7 (both included) and GAME_MODE == GAME_MODE_SPECIAL_EPISODE, returns false\n\nr0: ID of the flag to get\nreturn: Value of the flag",
    )

    GetScenarioBalance = Symbol(
        None,
        None,
        None,
        "Returns the current SCENARIO_BALANCE value.\n\nThe exact value returned depends on multiple factors:\n- If the first special episode is active, returns 1\n- If a different special episode is active, returns 3\n- If the SCENARIO_BALANCE_DEBUG variable is >= 0, returns its value\n- In all other cases, the value of the SCENARIO_BALANCE_FLAG variable is returned\n\nreturn: Current SCENARIO_BALANCE value.",
    )

    ScenarioFlagBackup = Symbol(
        None,
        None,
        None,
        "Saves scenario flag script variables (SCENARIO_SELECT, SCENARIO_MAIN_BIT_FLAG) to their respective BACKUP script variables, but only in certain game modes.\n\nThis function prints the debug string 'ScenarioFlag BackupGameMode %d' with the game mode.\n\nNo params.",
    )

    InitWorldMapScriptVars = Symbol(
        None,
        None,
        None,
        "Initializes the WORLD_MAP_* script variable values (IDs 0x55-0x57).\n\nNo params.",
    )

    InitDungeonListScriptVars = Symbol(
        None,
        None,
        None,
        "Initializes the DUNGEON_*_LIST script variable values (IDs 0x4f-0x54).\n\nNo params.",
    )

    SetDungeonConquest = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dungeon ID\nr1: bit_value",
    )

    GetDungeonMode = Symbol(
        None,
        None,
        None,
        "Returns the mode of the specified dungeon\n\nr0: Dungeon ID\nreturn: Dungeon mode",
    )

    GlobalProgressAlloc = Symbol(
        None,
        None,
        None,
        "Allocates a new global progress struct.\n\nThis updates the global pointer and returns a copy of that pointer.\n\nreturn: pointer to a newly allocated global progress struct",
    )

    ResetGlobalProgress = Symbol(
        None, None, None, "Zero-initializes the global progress struct.\n\nNo params."
    )

    SetMonsterFlag1 = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: monster ID",
    )

    GetMonsterFlag1 = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: monster ID\nreturn: ?",
    )

    SetMonsterFlag2 = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: monster ID",
    )

    HasMonsterBeenAttackedInDungeons = Symbol(
        None,
        None,
        None,
        "Checks whether the specified monster has been attacked by the player at some point in their adventure during an exploration.\n\nThe check is performed using the result of passing the ID to FemaleToMaleForm.\n\nr0: Monster ID\nreturn: True if the specified mosnter (after converting its ID through FemaleToMaleForm) has been attacked by the player before, false otherwise.",
    )

    SetDungeonTipShown = Symbol(
        None,
        None,
        None,
        "Marks a dungeon tip as already shown to the player\n\nr0: Dungeon tip ID",
    )

    GetDungeonTipShown = Symbol(
        None,
        None,
        None,
        "Checks if a dungeon tip has already been shown before or not.\n\nr0: Dungeon tip ID\nreturn: True if the tip has been shown before, false otherwise.",
    )

    SetMaxReachedFloor = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dungeon ID\nr1: max floor",
    )

    GetMaxReachedFloor = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dungeon ID\nreturn: max floor",
    )

    IncrementNbAdventures = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nNo params."
    )

    GetNbAdventures = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nreturn: # adventures",
    )

    CanMonsterSpawn = Symbol(
        None,
        None,
        None,
        "Always returns true.\n\nThis function seems to be a debug switch that the developers may have used to disable the random enemy spawn. \nIf it returned false, the call to SpawnMonster inside TrySpawnMonsterAndTickSpawnCounter would not be executed.\n\nr0: monster ID\nreturn: bool (always true)",
    )

    IncrementExclusiveMonsterCounts = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: monster ID",
    )

    CopyProgressInfoTo = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: write_info\nothers: ?",
    )

    CopyProgressInfoFromScratchTo = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: start_address\nr1: total_length\nreturn: ?",
    )

    CopyProgressInfoFrom = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: read_info",
    )

    CopyProgressInfoFromScratchFrom = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: start_address\nr1: total_length",
    )

    InitKaomadoStream = Symbol(
        None,
        None,
        None,
        "Initializes the stream used to load all Kaomado portraits, called once on game start!\n\nNo params.",
    )

    InitPortraitParams = Symbol(
        None,
        None,
        None,
        "Initializes a struct portrait_params.\n\nThe emote is set to PORTRAIT_NONE and the layout to the default. Everything else is initialized to 0.\n\nr0: portrait params pointer",
    )

    InitPortraitParamsWithMonsterId = Symbol(
        None,
        None,
        None,
        "Calls InitPortraitParams, and also initializes emote to PORTRAIT_NORMAL and monster ID to the passed argument.\n\nr0: portrait params pointer\nr1: monster ID",
    )

    SetPortraitEmotion = Symbol(
        None,
        None,
        None,
        "Sets the emote in the passed portrait params, only if the monster ID isn't MONSTER_NONE.\n\nr0: portrait params pointer\nr1: emotion ID",
    )

    SetPortraitLayout = Symbol(
        None,
        None,
        None,
        "Sets the layout in the passed portrait from the array of possible layouts.\n\nIf the layout is 32 or if the monster ID is MONSTER_NONE, then it does nothing.\n\nr0: portrait params pointer\nr1: layout index",
    )

    SetPortraitOffset = Symbol(
        None,
        None,
        None,
        "Offsets the portrait from the original offset determined by the layout, by the vector passed as argument.\n\nIf the monster ID is MONSTER_NONE, then it does nothing.\n\nr0: portrait params pointer\nr1: (x, y) offset in tiles from the original offset, derived from the layout",
    )

    AllowPortraitDefault = Symbol(
        None,
        None,
        None,
        "Allows the portrait to try and load the default emote (PORTRAIT_NORMAL) if it can't find the specified emote.\n\nr0: portrait params pointer\nr1: allow default",
    )

    IsValidPortrait = Symbol(
        None,
        None,
        None,
        "Returns whether this portrait params represents a valid portrait.\n\nr0: portrait params pointer\nreturn: bool",
    )

    LoadPortrait = Symbol(
        None,
        None,
        None,
        "Tries to load the portrait data associated with the passed portrait params.\n\nReturns whether the operation was successful (the portrait could be found). If the passed buffer is null, the check if performed without loading any data.\n\nThis function also modifies the flip fields in the passed portrait params.\n\nr0: portrait params pointer\nr1: kaomado_buffer pointer\nreturn: portrait exists",
    )

    WonderMailPasswordToMission = Symbol(
        None,
        None,
        None,
        "Tries to convert a Wonder Mail S password to a mission struct.\n\nReturns whether the conversion was successful. This function does not include any checks if the mission itself is valid, only if the code is valid.\n\nr0: string\nr1: Pointer to the struct where the data of the converted mission will be written to\nreturn: successful conversion",
    )

    SetEnterDungeon = Symbol(
        None,
        None,
        None,
        "Used to set the dungeon that will be accessed when switching from ground to dungeon mode.\n\nr0: Dungeon ID",
    )

    InitDungeonInit = Symbol(
        None,
        None,
        None,
        "Initializes the dungeon_init struct before entering a dungeon.\n\nr0: [output] Pointer to the struct to init\nr1: Dungeon ID",
    )

    IsNoLossPenaltyDungeon = Symbol(
        None,
        None,
        None,
        "Returns true if the specified dungeon shouldn't have a loss penalty.\n\nIf true you won't lose your money and items upon fainting. Also used to initialize dungeon_init::skip_faint_animation_flag.\n\nReturns: True for DUNGEON_CRYSTAL_LAKE and DUNGEON_5TH_STATION_CLEARING, as well as for DUNGEON_DEEP_STAR_CAVE_TEAM_ROGUE if the ground variable SIDE01_BOSS2ND is 0; false otherwise.",
    )

    CheckMissionRestrictions = Symbol(
        None,
        None,
        None,
        "Seems to be used to check if you have any missions that have unmet restrictions when trying to access a dungeon.\n\nr0: ?\nreturn: (?) Seems to be composed of multiple bitflags.",
    )

    GetNbFloors = Symbol(
        None,
        None,
        None,
        "Returns the number of floors of the given dungeon.\n\nThe result is hardcoded for certain dungeons, such as dojo mazes.\n\nr0: Dungeon ID\nreturn: Number of floors",
    )

    GetNbFloorsPlusOne = Symbol(
        None,
        None,
        None,
        "Returns the number of floors of the given dungeon + 1.\n\nr0: Dungeon ID\nreturn: Number of floors + 1",
    )

    GetDungeonGroup = Symbol(
        None,
        None,
        None,
        "Returns the dungeon group associated to the given dungeon.\n\nFor IDs greater or equal to dungeon_id::DUNGEON_NORMAL_FLY_MAZE, returns dungeon_group_id::DGROUP_MAROWAK_DOJO.\n\nr0: Dungeon ID\nreturn: Group ID",
    )

    GetNbPrecedingFloors = Symbol(
        None,
        None,
        None,
        "Given a dungeon ID, returns the total amount of floors summed by all the previous dungeons in its group.\n\nThe value is normally pulled from dungeon_data_list_entry::n_preceding_floors_group, except for dungeons with an ID >= dungeon_id::DUNGEON_NORMAL_FLY_MAZE, for which this function always returns 0.\n\nr0: Dungeon ID\nreturn: Number of preceding floors of the dungeon",
    )

    GetNbFloorsDungeonGroup = Symbol(
        None,
        None,
        None,
        "Returns the total amount of floors among all the dungeons in the dungeon group of the specified dungeon.\n\nr0: Dungeon ID\nreturn: Total number of floors in the group of the specified dungeon",
    )

    DungeonFloorToGroupFloor = Symbol(
        None,
        None,
        None,
        "Given a dungeon ID and a floor number, returns a struct with the corresponding dungeon group and floor number in that group.\n\nThe function normally uses the data in mappa_s.bin to calculate the result, but there's some dungeons (such as dojo mazes) that have hardcoded return values.\n\nIrdkwia's notes:\n  [r1]: dungeon_id\n  [r1+1]: dungeon_floor_id\n  [r0]: group_id\n  [r0+1]: group_floor_id\n\nr0: [output] Struct containing the dungeon group and floor group\nr1: Struct containing the dungeon ID and floor number",
    )

    GetMissionRank = Symbol(
        None,
        None,
        None,
        "Gets the mission rank for the given dungeon and floor.\n\nIf the dungeon ID is >= DUNGEON_NORMAL_FLY_MAZE or the group of the dungeon is > DGROUP_DUMMY_0x63, returns MISSION_RANK_E.\n\nr0: Dungeon and floor\nreturn: Mission rank",
    )

    GetOutlawLevel = Symbol(
        None,
        None,
        None,
        "Gets the level that should be used for outlaws for the given dungeon and floor\n\nr0: Dungeon and floor\nreturn: Outlaw level",
    )

    GetOutlawLeaderLevel = Symbol(
        None,
        None,
        None,
        "Gets the level that should be used for team leader outlaws for the given dungeon and floor. Identical to GetOutlawLevel.\n\nr0: Dungeon and floor\nreturn: Outlaw leader level",
    )

    GetOutlawMinionLevel = Symbol(
        None,
        None,
        None,
        "Gets the level that should be used for minion outlaws for the given dungeon and floor.\n\nr0: Dungeon and floor\nreturn: Outlaw minion level",
    )

    AddGuestMonster = Symbol(
        None,
        None,
        None,
        "Adds a guest monster to the active team\n\nr0: dungeon_init struct for the dungeon that is about to be entered\nr1: Number of the guest monster to add. Used when more than one monster is added.\nr2: Pointer to the guest monster entry to add to the team (usually located within GUEST_MONSTER_DATA)",
    )

    GetGroundNameId = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SetAdventureLogStructLocation = Symbol(
        None,
        None,
        None,
        "Sets the location of the adventure log struct in memory.\n\nSets it in a static memory location (At 0x22AB69C [US], 0x22ABFDC [EU], 0x22ACE58 [JP])\n\nNo params.",
    )

    SetAdventureLogDungeonFloor = Symbol(
        None,
        None,
        None,
        "Sets the current dungeon floor pair.\n\nr0: struct dungeon_floor_pair",
    )

    GetAdventureLogDungeonFloor = Symbol(
        None,
        None,
        None,
        "Gets the current dungeon floor pair.\n\nreturn: struct dungeon_floor_pair",
    )

    ClearAdventureLogStruct = Symbol(
        None, None, None, "Clears the adventure log structure.\n\nNo params."
    )

    SetAdventureLogCompleted = Symbol(
        None,
        None,
        None,
        "Marks one of the adventure log entry as completed.\n\nr0: entry ID",
    )

    IsAdventureLogNotEmpty = Symbol(
        None,
        None,
        None,
        "Checks if at least one of the adventure log entries is completed.\n\nreturn: bool",
    )

    GetAdventureLogCompleted = Symbol(
        None,
        None,
        None,
        "Checks if one adventure log entry is completed.\n\nr0: entry ID\nreturn: bool",
    )

    IncrementNbDungeonsCleared = Symbol(
        None,
        None,
        None,
        "Increments by 1 the number of dungeons cleared.\n\nImplements SPECIAL_PROC_INCREMENT_DUNGEONS_CLEARED (see ScriptSpecialProcessCall).\n\nNo params.",
    )

    GetNbDungeonsCleared = Symbol(
        None,
        None,
        None,
        "Gets the number of dungeons cleared.\n\nreturn: the number of dungeons cleared",
    )

    IncrementNbFriendRescues = Symbol(
        None,
        None,
        None,
        "Increments by 1 the number of successful friend rescues.\n\nNo params.",
    )

    GetNbFriendRescues = Symbol(
        None,
        None,
        None,
        "Gets the number of successful friend rescues.\n\nreturn: the number of successful friend rescues",
    )

    IncrementNbEvolutions = Symbol(
        None, None, None, "Increments by 1 the number of evolutions.\n\nNo params."
    )

    GetNbEvolutions = Symbol(
        None,
        None,
        None,
        "Gets the number of evolutions.\n\nreturn: the number of evolutions",
    )

    IncrementNbSteals = Symbol(
        None,
        None,
        None,
        "Leftover from Time & Darkness. Does not do anything.\n\nCalls to this matches the ones for incrementing the number of successful steals in Time & Darkness.\n\nNo params.",
    )

    IncrementNbEggsHatched = Symbol(
        None, None, None, "Increments by 1 the number of eggs hatched.\n\nNo params."
    )

    GetNbEggsHatched = Symbol(
        None,
        None,
        None,
        "Gets the number of eggs hatched.\n\nreturn: the number of eggs hatched",
    )

    GetNbPokemonJoined = Symbol(
        None,
        None,
        None,
        "Gets the number of different pokémon that joined.\n\nreturn: the number of different pokémon that joined",
    )

    GetNbMovesLearned = Symbol(
        None,
        None,
        None,
        "Gets the number of different moves learned.\n\nreturn: the number of different moves learned",
    )

    SetVictoriesOnOneFloor = Symbol(
        None,
        None,
        None,
        "Sets the record of victories on one floor.\n\nr0: the new record of victories",
    )

    GetVictoriesOnOneFloor = Symbol(
        None,
        None,
        None,
        "Gets the record of victories on one floor.\n\nreturn: the record of victories",
    )

    SetPokemonJoined = Symbol(
        None, None, None, "Marks one pokémon as joined.\n\nr0: monster ID"
    )

    SetPokemonBattled = Symbol(
        None, None, None, "Marks one pokémon as battled.\n\nr0: monster ID"
    )

    GetNbPokemonBattled = Symbol(
        None,
        None,
        None,
        "Gets the number of different pokémon that battled against you.\n\nreturn: the number of different pokémon that battled against you",
    )

    IncrementNbBigTreasureWins = Symbol(
        None,
        None,
        None,
        "Increments by 1 the number of big treasure wins.\n\nImplements SPECIAL_PROC_INCREMENT_BIG_TREASURE_WINS (see ScriptSpecialProcessCall).\n\nNo params.",
    )

    SetNbBigTreasureWins = Symbol(
        None,
        None,
        None,
        "Sets the number of big treasure wins.\n\nr0: the new number of big treasure wins",
    )

    GetNbBigTreasureWins = Symbol(
        None,
        None,
        None,
        "Gets the number of big treasure wins.\n\nreturn: the number of big treasure wins",
    )

    SetNbRecycled = Symbol(
        None,
        None,
        None,
        "Sets the number of items recycled.\n\nr0: the new number of items recycled",
    )

    GetNbRecycled = Symbol(
        None,
        None,
        None,
        "Gets the number of items recycled.\n\nreturn: the number of items recycled",
    )

    IncrementNbSkyGiftsSent = Symbol(
        None,
        None,
        None,
        "Increments by 1 the number of sky gifts sent.\n\nImplements SPECIAL_PROC_SEND_SKY_GIFT_TO_GUILDMASTER (see ScriptSpecialProcessCall).\n\nNo params.",
    )

    SetNbSkyGiftsSent = Symbol(
        None,
        None,
        None,
        "Sets the number of Sky Gifts sent.\n\nreturn: the number of Sky Gifts sent",
    )

    GetNbSkyGiftsSent = Symbol(
        None,
        None,
        None,
        "Gets the number of Sky Gifts sent.\n\nreturn: the number of Sky Gifts sent",
    )

    ComputeSpecialCounters = Symbol(
        None,
        None,
        None,
        "Computes the counters from the bit fields in the adventure log, as they are not updated automatically when bit fields are altered.\n\nAffects GetNbPokemonJoined, GetNbMovesLearned, GetNbPokemonBattled and GetNbItemAcquired.\n\nNo params.",
    )

    RecruitSpecialPokemonLog = Symbol(
        None,
        None,
        None,
        "Marks a specified special pokémon as recruited in the adventure log.\n\nIrdkwia's notes: Useless in Sky\n\nr0: monster ID",
    )

    IncrementNbFainted = Symbol(
        None,
        None,
        None,
        "Increments by 1 the number of times you fainted.\n\nNo params.",
    )

    GetNbFainted = Symbol(
        None,
        None,
        None,
        "Gets the number of times you fainted.\n\nreturn: the number of times you fainted",
    )

    SetItemAcquired = Symbol(
        None, None, None, "Marks one specific item as acquired.\n\nr0: item"
    )

    GetNbItemAcquired = Symbol(
        None,
        None,
        None,
        "Gets the number of items acquired.\n\nreturn: the number of items acquired",
    )

    SetChallengeLetterCleared = Symbol(
        None, None, None, "Sets a challenge letter as cleared.\n\nr0: challenge ID"
    )

    GetSentryDutyGamePoints = Symbol(
        None,
        None,
        None,
        "Gets the points for the associated rank in the footprints minigame.\n\nr0: the rank (range 0-4, 1st to 5th)\nreturn: points",
    )

    SetSentryDutyGamePoints = Symbol(
        None,
        None,
        None,
        "Sets a new record in the footprints minigame.\n\nr0: points\nreturn: the rank (range 0-4, 1st to 5th; -1 if out of ranking)",
    )

    CopyLogTo = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: write_info",
    )

    CopyLogFrom = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: read_info",
    )

    GetAbilityString = Symbol(
        None,
        None,
        None,
        "Copies the string for the ability id into the buffer.\n\nr0: [output] buffer\nr1: ability ID",
    )

    GetAbilityDescStringId = Symbol(
        None,
        None,
        None,
        "Gets the ability description string ID for the corresponding ability.\n\nr0: ability ID\nreturn: string ID",
    )

    GetTypeStringId = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: type ID\nreturn: string ID",
    )

    GetConversion2ConvertToType = Symbol(
        None,
        None,
        None,
        "Determines which type a monster with Conversion2 should turn into after being hit by a certain\ntype of move.\n\nr0: type ID\nreturn: type ID",
    )

    CopyBitsTo = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: write_info\nr1: buffer_write\nr2: nb_bits",
    )

    CopyBitsFrom = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: read_info\nr1: buffer_read\nr2: nb_bits",
    )

    StoreDefaultTeamData = Symbol(
        None,
        None,
        None,
        "Sets the name of the team for the main story to the default team name Poképals. Also initializes\nthe team to Normal Rank and possibly set Secret Rank unlocked to false?\n\nNo params.",
    )

    GetMainTeamNameWithCheck = Symbol(
        None,
        None,
        None,
        "Gets the name of the team for the main story with an additional check if the team name should be\n'???' because the story has not progressed enough.\n\nr0: [output] buffer",
    )

    GetMainTeamName = Symbol(
        None,
        None,
        None,
        "Gets the name of the team for the main story.\n\nr0: [output] buffer",
    )

    SetMainTeamName = Symbol(
        None,
        None,
        None,
        "Sets the main team name to the name in the passed buffer.\n\nr0: buffer",
    )

    GetRankupPoints = Symbol(
        None,
        None,
        None,
        "Returns the number of points required to reach the next rank.\n\nIf PERFORMANCE_PROGRESS_LIST[8] is 0 and the current rank is RANK_MASTER, or if the current rank is RANK_GUILDMASTER, returns 0.\n\nreturn: Points required to reach the next rank",
    )

    GetRank = Symbol(
        None,
        None,
        None,
        "Returns the team's rank\n\nIf PERFORMANCE_PROGRESS_LIST[8] is 0, the maximum rank that can be returned is RANK_MASTER.\n\nreturn: Rank",
    )

    GetRankStorageSize = Symbol(
        None,
        None,
        None,
        "Gets the size of storage for the current rank.\n\nreturn: storage size",
    )

    ResetPlayTimer = Symbol(None, None, None, "Reset the file timer.\n\nr0: play_time")

    PlayTimerTick = Symbol(
        None, None, None, "Advance the file timer by 1 frame.\n\nr0: play_time"
    )

    GetPlayTimeSeconds = Symbol(
        None,
        None,
        None,
        "Returns the current play time in seconds.\n\nreturn: play time in seconds",
    )

    SubFixedPoint = Symbol(
        None,
        None,
        None,
        "Compute the subtraction of two decimal fixed-point numbers (16 fraction bits).\n\nNumbers are in the format {16-bit integer part, 16-bit thousandths}, where the integer part is the lower word. Probably used primarily for belly.\n\nr0: number\nr1: decrement\nreturn: max(number - decrement, 0)",
    )

    BinToDecFixedPoint = Symbol(
        None,
        None,
        None,
        "Convert a binary fixed-point number (16 fraction bits) to the decimal fixed-point number (16 fraction bits) used for belly calculations. Thousandths are floored.\n\nIf <data> holds the raw binary data, a binary fixed-point number (16 fraction bits) has the value ((unsigned)data) * 2^-16), and the decimal fixed-point number (16 fraction bits) used for belly has the value (data & 0xffff) + (data >> 16)/1000.\n\nr0: pointer p, where ((const unsigned *)p)[1] is the fractional number in binary fixed-point format to convert\nreturn: fractional number in decimal fixed-point format",
    )

    CeilFixedPoint = Symbol(
        None,
        None,
        None,
        "Compute the ceiling of a decimal fixed-point number (16 fraction bits).\n\nNumbers are in the format {16-bit integer part, 16-bit thousandths}, where the integer part is the lower word. Probably used primarily for belly.\n\nr0: number\nreturn: ceil(number)",
    )

    DungeonGoesUp = Symbol(
        None,
        None,
        None,
        "Returns whether the specified dungeon is considered as going upward or not\n\nr0: dungeon id\nreturn: bool",
    )

    GetTurnLimit = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dungeon ID\nreturn: turn limit",
    )

    DoesNotSaveWhenEntering = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dungeon ID\nreturn: bool",
    )

    TreasureBoxDropsEnabled = Symbol(
        None,
        None,
        None,
        "Checks if enemy Treasure Box drops are enabled in the dungeon.\n\nr0: dungeon ID\nreturn: bool",
    )

    IsLevelResetDungeon = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dungeon ID\nreturn: bool",
    )

    GetMaxItemsAllowed = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dungeon ID\nreturn: max items allowed",
    )

    IsMoneyAllowed = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dungeon ID\nreturn: bool",
    )

    GetMaxRescueAttempts = Symbol(
        None,
        None,
        None,
        "Returns the maximum rescue attempts allowed in the specified dungeon.\n\nr0: dungeon id\nreturn: Max rescue attempts, or -1 if rescues are disabled.",
    )

    IsRecruitingAllowed = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dungeon ID\nreturn: bool",
    )

    GetLeaderChangeFlag = Symbol(
        None,
        None,
        None,
        "Returns true if the flag that allows changing leaders is set in the restrictions of the specified dungeon\n\nr0: dungeon id\nreturn: True if the restrictions of the current dungeon allow changing leaders, false otherwise.",
    )

    GetRandomMovementChance = Symbol(
        None,
        None,
        None,
        "Returns dungeon_restriction::random_movement_chance for the specified dungeon ID.\n\nr0: dungeon ID\nreturn: Random movement chance",
    )

    CanEnemyEvolve = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dungeon ID\nreturn: bool",
    )

    GetMaxMembersAllowed = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dungeon ID\nreturn: max members allowed",
    )

    IsIqEnabled = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dungeon ID\nreturn: bool",
    )

    IsTrapInvisibleWhenAttacking = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dungeon ID\nreturn: bool",
    )

    JoinedAtRangeCheck = Symbol(
        None,
        None,
        None,
        "Returns whether a certain joined_at field value is between dungeon_id::DUNGEON_JOINED_AT_BIDOOF and dungeon_id::DUNGEON_DUMMY_0xE3.\n\nIrdkwia's notes: IsSupportPokemon\n\nr0: joined_at id\nreturn: bool",
    )

    IsDojoDungeon = Symbol(
        None,
        None,
        None,
        "Checks if the given dungeon is a Marowak Dojo dungeon.\n\nr0: dungeon ID\nreturn: bool",
    )

    IsFutureDungeon = Symbol(
        None,
        None,
        None,
        "Checks if the given dungeon is a dungeon in the future arc of the main story.\n\nr0: dungeon ID\nreturn: bool",
    )

    IsSpecialEpisodeDungeon = Symbol(
        None,
        None,
        None,
        "Checks if the given dungeon is a special episode dungeon.\n\nr0: dungeon ID\nreturn: bool",
    )

    RetrieveFromItemList1 = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dungeon_info\nr1: ?\nreturn: ?",
    )

    IsForbiddenFloor = Symbol(
        None,
        None,
        None,
        "Related to missions floors forbidden\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: dungeon_info\nothers: ?\nreturn: bool",
    )

    Copy16BitsFrom = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: read_info\nr1: buffer_read",
    )

    RetrieveFromItemList2 = Symbol(
        None,
        None,
        None,
        "Same as RetrieveFromItemList1, except there is one more comparison\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: dungeon_info",
    )

    IsInvalidForMission = Symbol(
        None,
        None,
        None,
        "It's a guess\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: dungeon_id\nreturn: bool",
    )

    IsExpEnabledInDungeon = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dungeon_id\nreturn: bool",
    )

    IsSkyExclusiveDungeon = Symbol(
        None,
        None,
        None,
        "Also the dungeons where Giratina has its Origin Form\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: dungeon_id\nreturn: bool",
    )

    JoinedAtRangeCheck2 = Symbol(
        None,
        None,
        None,
        "Returns whether a certain joined_at field value is equal to dungeon_id::DUNGEON_BEACH or is between dungeon_id::DUNGEON_DUMMY_0xEC and dungeon_id::DUNGEON_DUMMY_0xF0.\n\nIrdkwia's notes: IsSEPokemon\n\nr0: joined_at id\nreturn: bool",
    )

    GetBagCapacity = Symbol(
        None,
        None,
        None,
        "Returns the player's bag capacity for a given point in the game.\n\nr0: scenario_balance\nreturn: bag capacity",
    )

    GetBagCapacitySpecialEpisode = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: se_type\nreturn: bag capacity",
    )

    GetRankUpEntry = Symbol(
        None,
        None,
        None,
        "Gets the rank up data for the specified rank.\n\nr0: rank index\nreturn: struct rankup_table_entry*",
    )

    GetBgRegionArea = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: offset\nr1: subregion_id\nr2: region_id\nreturn: ?",
    )

    LoadMonsterMd = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nNo params."
    )

    GetNameRaw = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dst_ptr\nr1: id",
    )

    GetName = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dst_ptr\nr1: id\nr2: color_id",
    )

    GetNameWithGender = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dst_ptr\nr1: id\nr2: color_id",
    )

    GetSpeciesString = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dst_ptr\nr1: id",
    )

    GetNameString = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: name",
    )

    GetSpriteIndex = Symbol(
        None,
        None,
        None,
        "Return the sprite index for this monster (inside m_attack.bin, m_ground.bin and monster.bin)\nAll three sprites have the same index\n\nr0: monster id\nreturn: sprite index",
    )

    GetDexNumber = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: dex number",
    )

    GetCategoryString = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: category",
    )

    GetMonsterGender = Symbol(
        None,
        None,
        None,
        "Returns the gender field of a monster given its ID.\n\nr0: monster id\nreturn: monster gender",
    )

    GetBodySize = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: body size",
    )

    GetSpriteSize = Symbol(
        None,
        None,
        None,
        "Returns the sprite size of the specified monster. If the size is between 1 and 6, 6 will be returned.\n\nr0: monster id\nreturn: sprite size",
    )

    GetSpriteFileSize = Symbol(
        None,
        None,
        None,
        "Returns the sprite file size of the specified monster.\n\nr0: monster id\nreturn: sprite file size",
    )

    GetShadowSize = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: shadow size",
    )

    GetSpeedStatus = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: speed status",
    )

    GetMobilityType = Symbol(
        None,
        None,
        None,
        "Gets the mobility type for a given monster species.\n\nr0: species ID\nreturn: mobility type",
    )

    GetRegenSpeed = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: regen speed",
    )

    GetCanMoveFlag = Symbol(
        None,
        None,
        None,
        "Returns the flag that determines if a monster can move in dungeons.\n\nr0: Monster ID\nreturn: 'Can move' flag",
    )

    GetChanceAsleep = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: chance asleep",
    )

    GetLowKickMultiplier = Symbol(
        None,
        None,
        None,
        "Gets the Low Kick (and Grass Knot) damage multiplier (i.e., weight) for the given species.\n\nr0: monster ID\nreturn: multiplier as a binary fixed-point number with 8 fraction bits.",
    )

    GetSize = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: size",
    )

    GetBaseHp = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: base HP",
    )

    CanThrowItems = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: bool",
    )

    CanEvolve = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: bool",
    )

    GetMonsterPreEvolution = Symbol(
        None,
        None,
        None,
        "Returns the pre-evolution id of a monster given its ID.\n\nr0: monster id\nreturn: ID of the monster that evolves into the one specified in r0",
    )

    GetBaseOffensiveStat = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nr1: stat index\nreturn: base attack/special attack stat",
    )

    GetBaseDefensiveStat = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nr1: stat index\nreturn: base defense/special defense stat",
    )

    GetType = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nr1: type index (0 for primary type or 1 for secondary type)\nreturn: type",
    )

    GetAbility = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nr1: ability index (0 for primary ability or 1 for secondary ability)\nreturn: ability",
    )

    GetRecruitRate2 = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: recruit rate 2",
    )

    GetRecruitRate1 = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: recruit rate 1",
    )

    GetExp = Symbol(
        None,
        None,
        None,
        "Base Formula = ((Level-1)*ExpYield)//10+ExpYield\nNote: Defeating an enemy without using a move will divide this amount by 2\n\nr0: id\nr1: level\nreturn: exp",
    )

    GetEvoParameters = Symbol(
        None,
        None,
        None,
        "Bx\nHas something to do with evolution\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: [output] struct_evo_param\nr1: id",
    )

    GetTreasureBoxChances = Symbol(
        None,
        None,
        None,
        "Has something to do with bytes 3C-3E\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: id\nr1: [output] struct_chances",
    )

    GetIqGroup = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: IQ group",
    )

    GetSpawnThreshold = Symbol(
        None,
        None,
        None,
        "Returns the spawn threshold of the given monster ID\n\nThe spawn threshold determines the minimum SCENARIO_BALANCE_FLAG value required by a monster to spawn in dungeons.\n\nr0: monster id\nreturn: Spawn threshold",
    )

    NeedsItemToSpawn = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: bool",
    )

    GetExclusiveItem = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nr1: determines which exclusive item\nreturn: exclusive item",
    )

    GetFamilyIndex = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: family index",
    )

    LoadM2nAndN2m = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nNo params."
    )

    GuestMonsterToGroundMonster = Symbol(
        None,
        None,
        None,
        "Inits a ground_monster entry with the given guest_monster struct.\n\nr0: [output] ground_monster struct to init\nr1: guest_monster struct to use",
    )

    StrcmpMonsterName = Symbol(
        None,
        None,
        None,
        "Checks if the string_buffer matches the name of the species\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: string_buffer\nr1: monster ID\nreturn: bool",
    )

    GetLvlUpEntry = Symbol(
        None,
        None,
        None,
        "Gets the level-up entry of the given monster ID at the specified level.\n\nThe monster's entire level up data is also decompressed to LEVEL_UP_DATA_DECOMPRESS_BUFFER, and its ID is stored in LEVEL_UP_DATA_MONSTER_ID.\n\nr0: [output] Level-up entry\nr1: monster ID\nr2: level",
    )

    GetEncodedHalfword = Symbol(
        None,
        None,
        None,
        "Decodes a 2-byte value that may be encoded using 1 or 2 bytes and writes it to the specified buffer.\n\nThe encoding system uses the most significant bit of the first byte to signal if the value is encoded as a single byte or as a halfword. If the bit is unset, the value is read as (encoded byte) & 0x7F. If it's set, the value is read as ((first encoded byte) & 0x7F << 7) | (second encoded byte) & 0x7F.\n\nr0: Pointer to encoded value\nr1: [output] Buffer where the resulting 2-byte value will be stored.\nreturn: Pointer to the next byte to decode",
    )

    GetEvoFamily = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: monster_str\nr1: evo_family_str\nreturn: nb_family",
    )

    GetEvolutions = Symbol(
        None,
        None,
        None,
        "Returns a list of all the possible evolutions for a given monster id.\n\nr0: Monster id\nr1: [Output] Array that will hold the list of monster ids the specified monster can evolve into\nr2: True to skip the check that prevents returning monsters with a different sprite size than the current one\nr3: True to skip the check that prevents Shedinja from being counted as a potential evolution\nreturn: Number of possible evolutions for the specified monster id",
    )

    ShuffleHiddenPower = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dmons_addr",
    )

    GetBaseForm = Symbol(
        None,
        None,
        None,
        "Checks if the specified monster ID corresponds to any of the pokémon that have multiple forms and returns the ID of the base form if so. If it doesn't, the same ID is returned.\n\nSome of the pokémon included in the check are Castform, Unown, Deoxys, Cherrim, Shaymin, and Giratina\n\nr0: Monster ID\nreturn: ID of the base form of the specified monster, or the same if the specified monster doesn't have a base form.",
    )

    GetBaseFormBurmyWormadamShellosGastrodonCherrim = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: base form",
    )

    GetBaseFormCastformCherrimDeoxys = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: base form",
    )

    GetAllBaseForms = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: base form",
    )

    GetDexNumberVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for GetDexNumber.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nr0: id\nreturn: dex number",
    )

    GetMonsterIdFromSpawnEntry = Symbol(
        None,
        None,
        None,
        "Returns the monster ID of the specified monster spawn entry\n\nr0: Pointer to the monster spawn entry\nreturn: monster_spawn_entry::id",
    )

    SetMonsterId = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: mons_spawn_str\nr1: monster ID",
    )

    SetMonsterLevelAndId = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: mons_spawn_str\nr1: level\nr2: monster ID",
    )

    GetMonsterLevelFromSpawnEntry = Symbol(
        None,
        None,
        None,
        "Returns the level of the specified monster spawn entry.\n\nr0: pointer to the monster spawn entry\nreturn: uint8_t",
    )

    GetMonsterGenderVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for GetMonsterGender.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nr0: monster id\nreturn: monster gender",
    )

    IsMonsterValid = Symbol(
        None,
        None,
        None,
        "Checks if an monster ID is valid.\n\nr0: monster ID\nreturn: bool",
    )

    IsUnown = Symbol(
        None,
        None,
        None,
        "Checks if a monster ID is an Unown.\n\nr0: monster ID\nreturn: bool",
    )

    IsShaymin = Symbol(
        None,
        None,
        None,
        "Checks if a monster ID is a Shaymin form.\n\nr0: monster ID\nreturn: bool",
    )

    IsCastform = Symbol(
        None,
        None,
        None,
        "Checks if a monster ID is a Castform form.\n\nr0: monster ID\nreturn: bool",
    )

    IsCherrim = Symbol(
        None,
        None,
        None,
        "Checks if a monster ID is a Cherrim form.\n\nr0: monster ID\nreturn: bool",
    )

    IsDeoxys = Symbol(
        None,
        None,
        None,
        "Checks if a monster ID is a Deoxys form.\n\nr0: monster ID\nreturn: bool",
    )

    GetSecondFormIfValid = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: monster ID\nreturn: second form",
    )

    FemaleToMaleForm = Symbol(
        None,
        None,
        None,
        "Returns the ID of the first form of the specified monster if the specified ID corresponds to a secondary form with female gender and the first form has male gender. If those conditions don't meet, returns the same ID unchanged.\n\nr0: Monster ID\nreturn: ID of the male form of the monster if the requirements meet, same ID otherwise.",
    )

    GetBaseFormCastformDeoxysCherrim = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id\nreturn: base form",
    )

    BaseFormsEqual = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: id1\nr1: id2\nreturn: if the base forms are the same",
    )

    DexNumbersEqual = Symbol(
        None,
        None,
        None,
        "Each Unown is considered as different\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: id1\nr1: id2\nreturn: bool",
    )

    GendersEqual = Symbol(
        None,
        None,
        None,
        "Checks if the genders for two monster IDs are equal.\n\nr0: id1\nr1: id2\nreturn: bool",
    )

    GendersEqualNotGenderless = Symbol(
        None,
        None,
        None,
        "Checks if the genders for two monster IDs are equal. Always returns false if either gender is GENDER_GENDERLESS.\n\nr0: id1\nr1: id2\nreturn: bool",
    )

    IsMonsterOnTeam = Symbol(
        None,
        None,
        None,
        "Checks if a given monster is on the exploration team (not necessarily the active party)?\n\nIrdkwia's notes:\n  recruit_strategy=0: strict equality\n  recruit_strategy=1: relative equality\n\nr0: monster ID\nr1: recruit_strategy\nreturn: bool",
    )

    GetNbRecruited = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: recruit_str",
    )

    IsValidTeamMember = Symbol(
        None,
        None,
        None,
        "Returns whether or not the team member at the given index is valid for the current game mode.\n\nDuring normal play, this will only be false for the special-episode-reserved indexes (2, 3, 4). During special episodes, this will be false for the hero and partner (0, 1).\n\nr0: team member index\nreturn: bool",
    )

    IsMainCharacter = Symbol(
        None,
        None,
        None,
        "Returns whether or not the team member at the given index is a 'main character'.\n\nDuring normal play, this will only be true for the hero and partner (0, 1). During special episodes, this will be true for the special-episode-reserved indexes (2, 3, 4).\n\nr0: team member index\nreturn: bool",
    )

    GetTeamMember = Symbol(
        None,
        None,
        None,
        "Gets the team member at the given index.\n\nr0: team member index\nreturn: ground monster pointer",
    )

    GetHeroMemberIdx = Symbol(
        None,
        None,
        None,
        "Returns the team member index of the hero (0) if the hero is valid, otherwise return -1.\n\nreturn: team member index",
    )

    GetPartnerMemberIdx = Symbol(
        None,
        None,
        None,
        "Returns the team member index of the partner (1) if the partner is valid, otherwise return -1.\n\nreturn: team member index",
    )

    GetMainCharacter1MemberIdx = Symbol(
        None,
        None,
        None,
        "Returns the team member index of the first main character for the given game mode, if valid, otherwise return -1.\n\nIn normal play, this will be the hero (0). During special episodes, this will be 2.\n\nreturn: team member index",
    )

    GetMainCharacter2MemberIdx = Symbol(
        None,
        None,
        None,
        "Returns the team member index of the second main character for the given game mode, if valid, otherwise return -1.\n\nIn normal play, this will be the partner (1). During special episodes, this will be 3 if there's a second main character.\n\nreturn: team member index",
    )

    GetMainCharacter3MemberIdx = Symbol(
        None,
        None,
        None,
        "Returns the team member index of the third main character for the given game mode, if valid, otherwise return -1.\n\nIn normal play, this will be invalid (-1). During special episodes, this will be 4 if there's a third main character.\n\nreturn: team member index",
    )

    GetHero = Symbol(
        None,
        None,
        None,
        "Returns the ground monster data of the hero.\n\nreturn: ground monster pointer",
    )

    GetPartner = Symbol(
        None,
        None,
        None,
        "Returns the ground monster data of the partner.\n\nreturn: ground monster pointer",
    )

    GetMainCharacter1 = Symbol(
        None,
        None,
        None,
        "Returns the ground monster data of the first main character for the given game mode.\n\nIn normal play, this will be the hero. During special episodes, this will be the first special episode main character (index 2).\n\nreturn: ground monster pointer",
    )

    GetMainCharacter2 = Symbol(
        None,
        None,
        None,
        "Returns the ground monster data of the second main character for the given game mode, or null if invalid.\n\nIn normal play, this will be the partner. During special episodes, this will be the second special episode main character (index 3) if one is present.\n\nreturn: ground monster pointer",
    )

    GetMainCharacter3 = Symbol(
        None,
        None,
        None,
        "Returns the ground monster data of the third main character for the given game mode, or null if invalid.\n\nIn normal play, this will be null. During special episodes, this will be the third special episode main character (index 4) if one is present.\n\nreturn: ground monster pointer",
    )

    GetFirstMatchingMemberIdx = Symbol(
        None,
        None,
        None,
        "Gets the first team member index (in the Chimecho Assembly) that has a specific monster ID, or -1 if there is none.\n\nIf valid, this will always be 5 or greater, since indexes 0-4 are reserved for main characters.\n\nr0: monster ID\nreturn: team member index of the first matching slot",
    )

    GetFirstEmptyMemberIdx = Symbol(
        None,
        None,
        None,
        "Gets the first unoccupied team member index (in the Chimecho Assembly), or -1 if there is none.\n\nIf valid, this will always be 5 or greater, since indexes 0-4 are reserved for main characters.\n\nr0: ?\nreturn: team member index of the first available slot",
    )

    IsMonsterNotNicknamed = Symbol(
        None,
        None,
        None,
        "Checks if the string_buffer matches the name of the species\n\nr0: ground monster pointer\nreturn: bool",
    )

    RemoveActiveMembersFromAllTeams = Symbol(
        None,
        None,
        None,
        "Removes all of the active monsters on every type of team from the team member table.\n\nNo params.",
    )

    RemoveActiveMembersFromSpecialEpisodeTeam = Symbol(
        None,
        None,
        None,
        "Removes the active monsters on the Special Episode Team from the team member table.\n\nNo params.",
    )

    RemoveActiveMembersFromRescueTeam = Symbol(
        None,
        None,
        None,
        "Removes the active monsters on the Rescue Team from the team member table.\n\nNo params.",
    )

    CheckTeamMemberIdx = Symbol(
        None,
        None,
        None,
        "Checks if a team member's member index (team_member::member_idx) is equal to certain values.\n\nThis is known to return true for some or all of the guest monsters.\n\nr0: member index\nreturn: True if the value is equal to 0x55AA or 0x5AA5",
    )

    IsMonsterIdInNormalRange = Symbol(
        None,
        None,
        None,
        "Checks if a monster ID is in the range [0, 554], meaning it's before the special story monster IDs and secondary gender IDs.\n\nr0: monster ID\nreturn: bool",
    )

    SetActiveTeam = Symbol(
        None,
        None,
        None,
        "Sets the specified team to active in TEAM_MEMBER_TABLE.\n\nr0: team ID",
    )

    GetActiveTeamMember = Symbol(
        None,
        None,
        None,
        "Returns a struct containing information about the active team member in the given slot index.\n\nr0: roster index\nreturn: team member pointer, or null if index is -1",
    )

    GetActiveRosterIndex = Symbol(
        None,
        None,
        None,
        "Searches for the roster index for the given team member within the current active roster.\n\nr0: team member index\nreturn: roster index if the team member is active, -1 otherwise",
    )

    TryAddMonsterToActiveTeam = Symbol(
        None,
        None,
        None,
        "Attempts to add a monster from the team member table to the active team.\n\nReturns the team index of the newly added monster. If the monster was already on the team, returns its current team index. If the monster is not on the team and there's no space left, returns -1.\n\nr0: member index\nreturn: Team index",
    )

    RemoveActiveMembersFromMainTeam = Symbol(
        None,
        None,
        None,
        "Removes the active monsters on the Main Team from the team member table.\n\nNo params.",
    )

    SetTeamSetupHeroAndPartnerOnly = Symbol(
        None,
        None,
        None,
        "Implements SPECIAL_PROC_SET_TEAM_SETUP_HERO_AND_PARTNER_ONLY (see ScriptSpecialProcessCall).\n\nNo params.",
    )

    SetTeamSetupHeroOnly = Symbol(
        None,
        None,
        None,
        "Implements SPECIAL_PROC_SET_TEAM_SETUP_HERO_ONLY (see ScriptSpecialProcessCall).\n\nNo params.",
    )

    GetPartyMembers = Symbol(
        None,
        None,
        None,
        "Appears to get the team's active party members. Implements most of SPECIAL_PROC_IS_TEAM_SETUP_SOLO (see ScriptSpecialProcessCall).\n\nr0: [output] Array of 4 2-byte values (they seem to be indexes of some sort) describing each party member, which will be filled in by the function. The input can be a null pointer if the party members aren't needed\nreturn: Number of party members",
    )

    RefillTeam = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nNo params."
    )

    ClearItem = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: team_id\nr1: check",
    )

    ChangeGiratinaFormIfSkyDungeon = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: dungeon ID",
    )

    GetIqSkillStringId = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: iq skill id\nreturn: iq skill string id",
    )

    DoesTacticFollowLeader = Symbol(
        None,
        None,
        None,
        "Returns whether or not the tactic involves following the team leader.\n\nr0: tactic_id\nreturn: bool",
    )

    GetUnlockedTactics = Symbol(
        None,
        None,
        None,
        "Returns an array with all the enabled tactics. TACTIC_NONE is used to fill the empty/unused entries\nin the array.\n\nr0: [output] Array of tactic_ids that are enabled\nr1: Monster level",
    )

    GetUnlockedTacticFlags = Symbol(
        None,
        None,
        None,
        "Returns an array with an entry for each tactic and if they're unlocked at the passed level.\n\nr0: [output] bool Array where the unlocked status of each tactic is stored\nr1: Monster level",
    )

    CanLearnIqSkill = Symbol(
        None,
        None,
        None,
        "Returns whether an IQ skill can be learned with a given IQ amount or not.\n\nIf the specified amount is 0, it always returns false.\n\nr0: IQ amount\nr1: IQ skill\nreturn: True if the specified skill can be learned with the specified IQ amount.",
    )

    GetLearnableIqSkills = Symbol(
        None,
        None,
        None,
        "Determines the list of IQ skills that a given monster can learn given its IQ value.\n\nThe list of skills is written in the array specified in r0. The array has 69 slots in total. Unused slots are set to 0.\n\nr0: [output] Array where the list of skills will be written\nr1: Monster species\nr2: Monster IQ\nreturn: Amount of skills written to the output array",
    )

    DisableIqSkill = Symbol(
        None,
        None,
        None,
        "Disables an IQ skill.\n\nr0: Pointer to the bitarray containing the list of enabled IQ skills\nr1: ID of the skill to disable",
    )

    EnableIqSkill = Symbol(
        None,
        None,
        None,
        "Enables an IQ skill and disables any other skills that are incompatible with it.\n\nr0: Pointer to the bitarray containing the list of enabled IQ skills\nr1: ID of the skill to enable",
    )

    GetSpeciesIqSkill = Symbol(
        None,
        None,
        None,
        "Gets the <index>th skill on the list of IQ skills that a given monster species can learn.\n\nr0: Species ID\nr1: Index (starting at 0)\nreturn: IQ skill ID",
    )

    DisableAllIqSkills = Symbol(
        None,
        None,
        None,
        "Disables all IQ skills in the bitarray.\n\nr0: Pointer to the bitarray containing the list of enabled IQ skills",
    )

    EnableAllLearnableIqSkills = Symbol(
        None,
        None,
        None,
        "Attempts to enable all the IQ skills available to the monster. If there are incompatible IQ skils,\nthe one with the highest ID will be activated while the others will be inactivated.\n\nr0: [output] Array where the list of skills will be written\nr1: Monster species\nr2: Monster IQ",
    )

    IqSkillFlagTest = Symbol(
        None,
        None,
        None,
        "Tests whether an IQ skill with a given ID is active.\n\nr0: IQ skill bitvector to test\nr1: IQ skill ID\nreturn: bool",
    )

    GetNextIqSkill = Symbol(
        None,
        None,
        None,
        "Returns the next IQ skill that a given monster will learn given its current IQ value, or IQ_NONE if the monster won't learn any more skills.\n\nr0: Monster ID\nr1: Monster IQ\nreturn: ID of the next skill learned by the monster, or IQ_NONE if the monster won't learn any more skills.",
    )

    GetExplorerMazeTeamName = Symbol(
        None,
        None,
        None,
        "Returns the name of the explorer maze team. If the language of the team name is different from the\nlanguage of selected in this game a default team name is written to the buffer instead.\n\nr0: [output] Buffer",
    )

    GetExplorerMazeMonster = Symbol(
        None,
        None,
        None,
        "Returns the data of a monster sent into the Explorer Dojo using the 'exchange teams' option.\n\nr0: Entry number (0-3)\nreturn: Ground monster data of the specified entry",
    )

    WriteMonsterInfoToSave = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: start_address\nr1: total_length\nreturn: ?",
    )

    ReadMonsterInfoFromSave = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: start_address\nr1: total_length",
    )

    WriteMonsterToSave = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: write_info\nr1: ground_monster",
    )

    ReadMonsterFromSave = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: read_info\nr1: ground_monster",
    )

    GetEvolutionPossibilities = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: ground_monster\nr1: evo_struct_addr",
    )

    GetMonsterEvoStatus = Symbol(
        None,
        None,
        None,
        "evo_status = 0: Not possible now\nevo_status = 1: Possible now\nevo_status = 2: No further\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: ground_monster\nreturn: evo_status",
    )

    CopyTacticString = Symbol(
        None,
        None,
        None,
        "Gets the string corresponding to a given string ID and copies it to the buffer specified in r0.\n\nThis function won't write more than 64 bytes.\n\nr0: [output] buffer\nr1: tactic_id",
    )

    GetStatBoostsForMonsterSummary = Symbol(
        None,
        None,
        None,
        "Gets the stat boosts from held items, exclusive items, and iq skills and stores them into the\nmonster_summary struct.\n\nr0: monster_summary\nr1: enum monster_id monster_id\nr2: pointer to held item\nr3: iq\nstack[0]: bool if Klutz is active",
    )

    CreateMonsterSummaryFromTeamMember = Symbol(
        None,
        None,
        None,
        "Creates a snapshot of the condition of a team_member struct in a monster_summary struct.\n\nr0: [output] monster_summary\nr1: team_member\nr2: bool is leader",
    )

    GetSosMailCount = Symbol(
        None,
        None,
        None,
        "Implements SPECIAL_PROC_GET_SOS_MAIL_COUNT (see ScriptSpecialProcessCall).\n\nr0: ?\nr1: some flag?\nreturn: SOS mail count",
    )

    IsMissionSuspendedAndValid = Symbol(
        None,
        None,
        None,
        "Checks if a mission is currently suspended and contains valid fields. Calls IsMissionValid for the validity check.\n\nr0: mission to check\nreturn: bool",
    )

    AreMissionsEquivalent = Symbol(
        None,
        None,
        None,
        "Checks if two missions are equivalent.\n\nr0: mission1\nr1: mission2\nreturn: bool",
    )

    IsMissionValid = Symbol(
        None,
        None,
        None,
        "Checks if a mission contains valid fields.\n\nFor example, a mission will be considered invalid if the ID of the monsters or items involved are out of bounds, if their entries are marked as invalid, if the destination floor does not exist, etc.\nIf the mission fails one of the checks, the game will print an error message explaining what is wrong using DebugPrint0.\n\nr0: mission to check\nreturn: True if the mission is valid, false if it's not.",
    )

    GenerateMission = Symbol(
        None,
        None,
        None,
        "Attempts to generate a random mission.\n\nr0: Pointer to something\nr1: Pointer to the struct where the data of the generated mission will be written to\nreturn: MISSION_GENERATION_SUCCESS if the mission was successfully generated, MISSION_GENERATION_FAILURE if it failed and MISSION_GENERATION_GLOBAL_FAILURE if it failed and the game shouldn't try to generate more.",
    )

    IsMissionTypeSpecialEpisode = Symbol(
        None,
        None,
        None,
        "Checks if a mission is for a Special Episode Transmission, which unlocks Special Episode 3. This specifically checks for a mission of type MISSION_SPECIAL_EPISODE and subtype 0x2.\n\nr0: mission pointer\nreturn: bool",
    )

    GenerateDailyMissions = Symbol(
        None,
        None,
        None,
        "Generates the missions displayed on the Job Bulletin Board and the Outlaw Notice Board.\n\nNo params.",
    )

    AlreadyHaveMission = Symbol(
        None,
        None,
        None,
        "Checks if a specified mission already exists in the Job List.\n\nr0: mission to check\nreturn: bool",
    )

    CountJobListMissions = Symbol(
        None,
        None,
        None,
        "Gets the number of missions currently in the Job List.\n\nreturn: number of missions",
    )

    DungeonRequestsDone = Symbol(
        None,
        None,
        None,
        "Seems to return the number of missions completed.\n\nPart of the implementation for SPECIAL_PROC_DUNGEON_HAD_REQUEST_DONE (see ScriptSpecialProcessCall).\n\nr0: ?\nr1: some flag?\nreturn: number of missions completed",
    )

    DungeonRequestsDoneWrapper = Symbol(
        None,
        None,
        None,
        "Calls DungeonRequestsDone with the second argument set to false.\n\nr0: ?\nreturn: number of mission completed",
    )

    AnyDungeonRequestsDone = Symbol(
        None,
        None,
        None,
        "Calls DungeonRequestsDone with the second argument set to true, and converts the integer output to a boolean.\n\nr0: ?\nreturn: bool: whether the number of missions completed is greater than 0",
    )

    AddMissionToJobList = Symbol(
        None, None, None, "Adds a mission to the Job List.\n\nr0: mission to add"
    )

    GetAcceptedMission = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: mission_id\nreturn: mission",
    )

    GetMissionByTypeAndDungeon = Symbol(
        None,
        None,
        None,
        "Returns the position on the mission list of the first mission of the specified type that takes place in the specified dungeon.\n\nIf the type of the mission has a subtype, the subtype of the checked mission must match the one in [r2] too for it to be returned.\n\nr0: Position on the mission list where the search should start. Missions before this position on the list will be ignored.\nr1: Mission type\nr2: Pointer to some struct that contains the subtype of the mission to check on its first byte\nr3: Dungeon ID\nreturn: Index of the first mission that meets the specified requirements, or -1 if there aren't any missions that do so.",
    )

    CheckAcceptedMissionByTypeAndDungeon = Symbol(
        None,
        None,
        None,
        "Returns true if there are any accepted missions on the mission list that are of the specified type and take place in the specified dungeon.\n\nIf the type of the mission has a subtype, the subtype of the checked mission must match the one in [r2] too for it to be returned.\n\nr0: Mission type\nr1: Pointer to some struct that contains the subtype of the mission to check on its first byte\nr2: Dungeon ID\nreturn: True if at least one mission meets the specified requirements, false otherwise.",
    )

    GetAllPossibleMonsters = Symbol(
        None,
        None,
        None,
        "Stores MISSION_MONSTER_LIST_PTR into the passed buffer and retrieves the number of monsters that can be used in a mission.\n\nr0: buffer\nreturn: Number of monsters usable for a mission",
    )

    GenerateAllPossibleMonstersList = Symbol(
        None,
        None,
        None,
        "Attempts to add monster IDs 1 (Bulbasaur) through 535 (Shaymin Sky) as entries to a heap-allocated list.\n\nIf no monsters are valid mission targets, the heap-allocated list is freed. Otherwise, sets MISSION_MONSTER_LIST_PTR and MISSION_MONSTER_COUNT.\n\nreturn: Number of monsters usable for a mission",
    )

    DeleteAllPossibleMonstersList = Symbol(
        None,
        None,
        None,
        "If MISSION_MONSTER_LIST_PTR is not null, frees its heap-allocated list and nulls MISSION_MONSTER_LIST_PTR and MISSION_MONSTER_COUNT.\n\nNo params.",
    )

    GenerateAllPossibleDungeonsList = Symbol(
        None,
        None,
        None,
        "Attempts to add dungeon IDs 1 (DUNGEON_TEST_DUNGEON) through 179 (DUNGEON_RESCUE) as entries to a heap-allocated list.\n\nIf no dungeons are valid mission targets, the heap-allocated list is freed. Otherwise, sets MISSION_DUNGEON_LIST_PTR and MISSION_DUNGEON_COUNT.\n\nreturn: Number of dungeons usable for a mission",
    )

    DeleteAllPossibleDungeonsList = Symbol(
        None,
        None,
        None,
        "If MISSION_DUNGEON_LIST_PTR is not null, frees its heap-allocated list and nulls MISSION_DUNGEON_LIST_PTR and MISSION_DUNGEON_COUNT.\n\nNo params.",
    )

    GenerateAllPossibleDeliverList = Symbol(
        None,
        None,
        None,
        "Attempts to add all items in ITEM_DELIVERY_TABLE as entries to a heap-allocated list.\n\nIf no items are valid for a delivery mission, the heap-allocated list is freed. Otherwise, sets MISSION_DELIVER_LIST_PTR and MISSION_DELIVER_COUNT.\n\nreturn: Number of deliverable items for a mission",
    )

    DeleteAllPossibleDeliverList = Symbol(
        None,
        None,
        None,
        "If MISSION_DELIVER_LIST_PTR is not null, frees its heap-allocated list and nulls MISSION_DELIVER_LIST_PTR and MISSION_DELIVER_COUNT.\n\nNo params.",
    )

    ClearMissionData = Symbol(
        None,
        None,
        None,
        "Given a mission struct, clears some of it fields.\n\nIn particular, mission::status is set to mission_status::MISSION_STATUS_INVALID, mission::dungeon_id is set to -1, mission::floor is set to 0 and mission::reward_type is set to mission_reward_type::MISSION_REWARD_MONEY.\n\nr0: Pointer to the mission to clear",
    )

    IsMonsterMissionAllowed = Symbol(
        None,
        None,
        None,
        "Checks if the specified monster is contained in the MISSION_BANNED_MONSTERS array.\n\nThe function converts the ID by calling GetBaseForm and FemaleToMaleForm first.\n\nr0: Monster ID\nreturn: False if the monster ID (after converting it) is contained in MISSION_BANNED_MONSTERS, true if it isn't.",
    )

    CanMonsterBeUsedForMissionWrapper = Symbol(
        None,
        None,
        None,
        "Calls CanMonsterBeUsedForMission with r1 = 1.\n\nr0: Monster ID\nreturn: Result of CanMonsterBeUsedForMission",
    )

    CanMonsterBeUsedForMission = Symbol(
        None,
        None,
        None,
        "Returns whether a certain monster can be used (probably as the client or as the target) when generating a mission.\n\nExcluded monsters include those that haven't been fought in dungeons yet, the second form of certain monsters and, if PERFOMANCE_PROGRESS_FLAG[9] is 0, monsters in MISSION_BANNED_STORY_MONSTERS, the species of the player and the species of the partner.\n\nr0: Monster ID\nr1: True to exclude monsters in the MISSION_BANNED_MONSTERS array, false to allow them\nreturn: True if the specified monster can be part of a mission",
    )

    IsMonsterMissionAllowedStory = Symbol(
        None,
        None,
        None,
        "Checks if the specified monster should be allowed to be part of a mission (probably as the client or the target), accounting for the progress on the story.\n\nIf PERFOMANCE_PROGRESS_FLAG[9] is true, the function returns true.\nIf it isn't, the function checks if the specified monster is contained in the MISSION_BANNED_STORY_MONSTERS array, or if it corresponds to the ID of the player or the partner.\n\nThe function converts the ID by calling GetBaseForm and FemaleToMaleForm first.\n\nr0: Monster ID\nreturn: True if PERFOMANCE_PROGRESS_FLAG[9] is true, false if it isn't and the monster ID (after converting it) is contained in MISSION_BANNED_STORY_MONSTERS or if it's the ID of the player or the partner, true otherwise.",
    )

    CanDungeonBeUsedForMission = Symbol(
        None,
        None,
        None,
        "Returns whether a certain dungeon can be used when generating a mission.\n\nExcluded dungeons include DUNGEON_ICE_AEGIS_CAVE, DUNGEON_DESTINY_TOWER, all Special Episode dungeons, dungeons with IDs greater than 174 (DUNGEON_STAR_CAVE), DUNGEON_CRYSTAL_CAVE and DUNGEON_CRYSTAL_CROSSING if PERFORMANCE_PROGRESS_LIST[9] is false, and any dungeon that does not have a dungeon mode of DMODE_OPEN_AND_REQUEST.\n\nr0: Dungeon ID\nreturn: True if the specified dungeon can be part of a mission",
    )

    CanSendItem = Symbol(
        None,
        None,
        None,
        "Returns whether a certain item can be sent to another player via Wonder Mail.\n\nr0: item ID\nr1: to_sky\nreturn: bool",
    )

    IsAvailableItem = Symbol(
        None,
        None,
        None,
        "Checks if a certain item is valid to be used in delivery missions. \n\nValidity entails a loop throughout all dungeons, checking if they have been visited before (via a call to GetMaxReachedFloor), and checking if the item is available within a dungeon's group (via a call to IsItemAvailableInDungeonGroup).\n\nr0: item ID\nreturn: bool",
    )

    GetAvailableItemDeliveryList = Symbol(
        None,
        None,
        None,
        "Iterates through ITEM_DELIVERY_TABLE and checks if each entry is valid to be used in delivery missions.\n\nr0: item_buffer\nreturn: Number of deliverable items for a mission",
    )

    GetActorMatchingStorageId = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: actor_id\nreturn: storage ID",
    )

    SetActorTalkMainAndActorTalkSub = Symbol(
        None,
        None,
        None,
        "Sets ACTOR_TALK_MAIN and ACTOR_TALK_SUB to given actor IDs.\n\nr0: actor_id for ACTOR_TALK_MAIN\nr1: actor_id for ACTOR_TALK_SUB",
    )

    SetActorTalkMain = Symbol(
        None,
        None,
        None,
        "Sets ACTOR_TALK_MAIN to be actor_id.\nImplements SPECIAL_PROC_SET_ACTOR_TALK_MAIN (see ScriptSpecialProcessCall).\n\nr0: actor_id",
    )

    SetActorTalkSub = Symbol(
        None,
        None,
        None,
        "Sets ACTOR_TALK_SUB to be actor_id.\nImplements SPECIAL_PROC_SET_ACTOR_TALK_SUB (see ScriptSpecialProcessCall).\n\nr0: actor_id",
    )

    RandomizeDemoActors = Symbol(
        None,
        None,
        None,
        "Randomly picks one of the 18 teams from DEMO_TEAMS and sets ENTITY_NPC_DEMO_HERO and ENTITY_NPC_DEMO_PARTNER\nto the randomly selected hero and partner.\nImplements SPECIAL_PROC_RANDOMIZE_DEMO_ACTORS (see ScriptSpecialProcessCall).\n\nNo params.",
    )

    ItemAtTableIdx = Symbol(
        None,
        None,
        None,
        "Gets info about the item at a given item table (not sure what this table is...) index.\n\nUsed by SPECIAL_PROC_COUNT_TABLE_ITEM_TYPE_IN_BAG and friends (see ScriptSpecialProcessCall).\n\nr0: table index\nr1: [output] pointer to an owned_item",
    )

    MainLoop = Symbol(
        None,
        None,
        None,
        "This function gets called shortly after the game is started. Contains a single infinite loop and has no return statement.\n\nNo params.",
    )

    CreateJobSummary = Symbol(
        None,
        None,
        None,
        "Creates a window containing a summary of a specific mission on the Top Screen.\n\nr0: mission pointer\nr1: ?",
    )

    DungeonSwapIdToIdx = Symbol(
        None,
        None,
        None,
        "Converts a dungeon ID to its corresponding index in DUNGEON_SWAP_ID_TABLE, or -1 if not found.\n\nr0: dungeon ID\nreturn: index",
    )

    DungeonSwapIdxToId = Symbol(
        None,
        None,
        None,
        "Converts an index in DUNGEON_SWAP_ID_TABLE to the corresponding dungeon ID, or DUNGEON_DUMMY_0xFF if the index is -1.\n\nr0: index\nreturn: dungeon ID",
    )

    GetDungeonModeSpecial = Symbol(
        None,
        None,
        None,
        "Returns the status of the given dungeon, with some modifications.\n\nIf the dungeon ID is DUNGEON_BEACH, returns DMODE_REQUEST.\nIf it's DUNGEON_JOINED_AT_UNKNOWN, returns DMODE_OPEN_AND_REQUEST.\nIf it's >= DUNGEON_NORMAL_FLY_MAZE and <= DUNGEON_DOJO_0xD3, returns DMODE_OPEN_AND_REQUEST.\nElse, calls GetDungeonMode and returns DMODE_REQUEST if the dungeon has been cleared, or DMODE_OPEN if it's not.\n\nr0: Dungeon ID\nreturn: Dungeon mode",
    )


class NaItcmArm9Data:

    SECURE = Symbol(
        None,
        None,
        None,
        "The header of the DS cartridge secure area. See https://problemkaputt.de/gbatek.htm#dscartridgesecurearea",
    )

    START_MODULE_PARAMS = Symbol(
        None, None, None, "Parameters used by the NitroSDK to read the ROM."
    )

    DEFAULT_MEMORY_ARENA_SIZE = Symbol(
        None,
        None,
        None,
        "Length in bytes of the default memory allocation arena, 1991680.",
    )

    LOG_MAX_ARG = Symbol(
        None, None, None, "The maximum argument value for the Log function, 2047."
    )

    DAMAGE_SOURCE_CODE_ORB_ITEM = Symbol(
        None,
        None,
        None,
        "The damage source value for any item in CATEGORY_ORBS, 0x262.",
    )

    DAMAGE_SOURCE_CODE_NON_ORB_ITEM = Symbol(
        None,
        None,
        None,
        "The damage source value for any item not in CATEGORY_ORBS, 0x263.",
    )

    AURA_BOW_ID_LAST = Symbol(None, None, None, "Highest item ID of the aura bows.")

    NUMBER_OF_ITEMS = Symbol(None, None, None, "Number of items in the game.")

    MAX_MONEY_CARRIED = Symbol(
        None, None, None, "Maximum amount of money the player can carry, 99999."
    )

    MAX_MONEY_STORED = Symbol(
        None,
        None,
        None,
        "Maximum amount of money the player can store in the Duskull Bank, 9999999.",
    )

    WINDOW_LIST_PTR = Symbol(None, None, None, "Hard-coded pointer to WINDOW_LIST.")

    SCRIPT_VARS_VALUES_PTR = Symbol(
        None, None, None, "Hard-coded pointer to SCRIPT_VARS_VALUES."
    )

    MAX_PLAY_TIME = Symbol(
        None,
        None,
        None,
        "Maximum number of seconds that the file timer counts up to.\n\n35999999 seconds (one second under 10000 hours).",
    )

    MONSTER_ID_LIMIT = Symbol(
        None, None, None, "One more than the maximum valid monster ID (0x483)."
    )

    MAX_RECRUITABLE_TEAM_MEMBERS = Symbol(
        None,
        None,
        None,
        "555, appears to be the maximum number of members recruited to an exploration team, at least for the purposes of some checks that need to iterate over all team members.",
    )

    NATURAL_LOG_VALUE_TABLE = Symbol(
        None,
        None,
        None,
        "A table of values for the natural log function corresponding to integer arguments in the range [0, 2047].\n\nEach value is stored as a 16-bit fixed-point number with 12 fractional bits. I.e., to get the actual natural log value, take the table entry and divide it by 2^12.\n\nThe value at an input of 0 is just listed as 0; the Log function makes sure the input is always at least 1 before reading the table.\n\ntype: int16_t[2048]",
    )

    CART_REMOVED_IMG_DATA = Symbol(None, None, None, "")

    STRING_DEBUG_EMPTY = Symbol(None, None, None, "")

    STRING_DEBUG_FORMAT_LINE_FILE = Symbol(None, None, None, "")

    STRING_DEBUG_NO_PROG_POS = Symbol(None, None, None, "")

    STRING_DEBUG_SPACED_PRINT = Symbol(None, None, None, "")

    STRING_DEBUG_FATAL = Symbol(None, None, None, "")

    STRING_DEBUG_NEWLINE = Symbol(None, None, None, "")

    STRING_DEBUG_LOG_NULL = Symbol(None, None, None, "")

    STRING_DEBUG_STRING_NEWLINE = Symbol(None, None, None, "")

    STRING_EFFECT_EFFECT_BIN = Symbol(None, None, None, "")

    STRING_MONSTER_MONSTER_BIN = Symbol(None, None, None, "")

    STRING_BALANCE_M_LEVEL_BIN = Symbol(None, None, None, "")

    STRING_DUNGEON_DUNGEON_BIN = Symbol(None, None, None, "")

    STRING_MONSTER_M_ATTACK_BIN = Symbol(None, None, None, "")

    STRING_MONSTER_M_GROUND_BIN = Symbol(None, None, None, "")

    STRING_FILE_DIRECTORY_INIT = Symbol(None, None, None, "")

    AVAILABLE_ITEMS_IN_GROUP_TABLE = Symbol(
        None,
        None,
        None,
        "100*0x80\nLinked to the dungeon group id\n\nNote: unverified, ported from Irdkwia's notes",
    )

    ARM9_UNKNOWN_TABLE__NA_2097FF8 = Symbol(
        None,
        None,
        None,
        "16*0x4 (0x2+0x2)\n\nNote: unverified, ported from Irdkwia's notes",
    )

    KECLEON_SHOP_ITEM_TABLE_LISTS_1 = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: enum item_id[4]",
    )

    KECLEON_SHOP_ITEM_TABLE_LISTS_2 = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: enum item_id[4]",
    )

    EXCLUSIVE_ITEM_STAT_BOOST_DATA = Symbol(
        None,
        None,
        None,
        "Contains stat boost effects for different exclusive item classes.\n\nEach 4-byte entry contains the boost data for (attack, defense, special attack, special defense), 1 byte each, for a specific exclusive item class, indexed according to the stat boost data index list.\n\ntype: struct exclusive_item_stat_boost_entry[15]",
    )

    EXCLUSIVE_ITEM_DEFENSE_BOOSTS = Symbol(
        None, None, None, "EXCLUSIVE_ITEM_STAT_BOOST_DATA, offset by 1"
    )

    EXCLUSIVE_ITEM_SPECIAL_ATTACK_BOOSTS = Symbol(
        None, None, None, "EXCLUSIVE_ITEM_STAT_BOOST_DATA, offset by 2"
    )

    EXCLUSIVE_ITEM_SPECIAL_DEFENSE_BOOSTS = Symbol(
        None, None, None, "EXCLUSIVE_ITEM_STAT_BOOST_DATA, offset by 3"
    )

    EXCLUSIVE_ITEM_EFFECT_DATA = Symbol(
        None,
        None,
        None,
        "Contains special effects for each exclusive item.\n\nEach entry is 2 bytes, with the first entry corresponding to the first exclusive item (Prism Ruff). The first byte is the exclusive item effect ID, and the second byte is an index into other data tables (related to the more generic stat boosting effects for specific monsters).\n\ntype: struct exclusive_item_effect_entry[956]",
    )

    EXCLUSIVE_ITEM_STAT_BOOST_DATA_INDEXES = Symbol(
        None, None, None, "EXCLUSIVE_ITEM_EFFECT_DATA, offset by 1"
    )

    RECYCLE_SHOP_ITEM_LIST = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    TYPE_SPECIFIC_EXCLUSIVE_ITEMS = Symbol(
        None,
        None,
        None,
        "Lists of type-specific exclusive items (silk, dust, gem, globe) for each type.\n\ntype: struct item_id_16[17][4]",
    )

    RECOIL_MOVE_LIST = Symbol(
        None,
        None,
        None,
        "Null-terminated list of all the recoil moves, as 2-byte move IDs.\n\ntype: struct move_id_16[11]",
    )

    PUNCH_MOVE_LIST = Symbol(
        None,
        None,
        None,
        "Null-terminated list of all the punch moves, as 2-byte move IDs.\n\ntype: struct move_id_16[16]",
    )

    MOVE_POWER_STARS_TABLE = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: int[6]",
    )

    MOVE_ACCURACY_STARS_TABLE = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: int[8]",
    )

    PARENT_MENU_DEFAULT_WINDOW_PARAMS = Symbol(
        None,
        None,
        None,
        "Default window_params for a simple_menu created with CreateParentMenuInternal.\n\nNote that x_offset and y_offset refer to the right and bottom edges, since they will be paired with the x_offset_end and y_offset_end window flags in CreateParentMenuInternal.\n\nAdditionally, width and height are 0, and will be computed in CreateParentMenuInternal.",
    )

    SIMPLE_MENU_DEFAULT_WINDOW_PARAMS = Symbol(
        None,
        None,
        None,
        "Default window_params for a simple_menu.\n\nNote that x_offset and y_offset refer to the right and bottom edges, since they will be paired with the x_offset_end and y_offset_end window flags in CreateSimpleMenuInternal.\n\nAdditionally, width and height are 0, and will be computed in CreateSimpleMenuInternal.",
    )

    ADVANCED_MENU_DEFAULT_WINDOW_PARAMS = Symbol(
        None,
        None,
        None,
        "Default window_params for an advanced_menu.\n\nNote that x_offset and y_offset refer to the right and bottom edges, since they will be paired with the x_offset_end and y_offset_end window flags in CreateAdvancedMenu.\n\nAdditionally, width and height are 0, and will be computed in CreateAdvancedMenu.",
    )

    COLLECTION_MENU_DEFAULT_WINDOW_PARAMS = Symbol(
        None,
        None,
        None,
        "Default window_params for a collection_menu.\n\nNote that x_offset and y_offset refer to the right and bottom edges, since they will be paired with the x_offset_end and y_offset_end window flags in CreateCollectionMenu.\n\nAdditionally, width and height are 0, and will be computed in CreateCollectionMenu.",
    )

    OPTIONS_MENU_DEFAULT_WINDOW_PARAMS = Symbol(
        None,
        None,
        None,
        "Default window_params for an options_menu.\n\nNote that x_offset and y_offset refer to the right and bottom edges, since they will be paired with the x_offset_end and y_offset_end window flags in CreateOptionsMenu.\n\nAdditionally, width and height are 0, and will be computed in CreateOptionsMenu.",
    )

    DEBUG_MENU_DEFAULT_WINDOW_PARAMS = Symbol(
        None,
        None,
        None,
        "Default window_params for a debug_menu.\n\nNote that x_offset and y_offset refer to the right and bottom edges, since they will be paired with the x_offset_end and y_offset_end window flags in CreateDebugMenu.\n\nAdditionally, width and height are 0, and will be computed in CreateDebugMenu.",
    )

    SCROLL_BOX_DEFAULT_WINDOW_PARAMS = Symbol(
        None, None, None, "Default window_params for a scroll_box."
    )

    DIALOGUE_BOX_DEFAULT_WINDOW_PARAMS = Symbol(
        None, None, None, "Default window_params for a dialogue_box."
    )

    PORTRAIT_BOX_DEFAULT_WINDOW_PARAMS = Symbol(
        None,
        None,
        None,
        "Default window_params for a portrait_box.\n\nNote that the screen and box type are unset, and are determined in CreatePortraitBox.",
    )

    TEXT_BOX_DEFAULT_WINDOW_PARAMS = Symbol(
        None, None, None, "Default window_params for a text_box."
    )

    AREA_NAME_BOX_DEFAULT_WINDOW_PARAMS = Symbol(
        None,
        None,
        None,
        "Default window_params for an area_name_box.\n\nNote that x_offset and y_offset refer to the right and bottom edges, since they will be paired with the x_offset_end and y_offset_end window flags in CreateAreaNameBox.\n\nAdditionally, width and height are 0, and will be computed in CreateAreaNameBox.",
    )

    CONTROLS_CHART_DEFAULT_WINDOW_PARAMS = Symbol(
        None, None, None, "Default window_params for a controls_chart."
    )

    ALERT_BOX_DEFAULT_WINDOW_PARAMS = Symbol(
        None, None, None, "Default window_params for an alert_box."
    )

    ADVANCED_TEXT_BOX_DEFAULT_WINDOW_PARAMS = Symbol(
        None,
        None,
        None,
        "Default window_params for an advanced_text_box.\n\nNote that x_offset and y_offset refer to the right and bottom edges, since they will be paired with the x_offset_end and y_offset_end window flags in CreateAdvancedTextBoxInternal.",
    )

    TEAM_SELECTION_MENU_DEFAULT_WINDOW_PARAMS = Symbol(
        None,
        None,
        None,
        "Default window_params for a team_selection_menu.\n\nNote that x_offset and y_offset refer to the right and bottom edges, since they will be paired with the x_offset_end and y_offset_end window flags in CreateTeamSelectionMenu.\n\nAdditionally, width and height are 0, and will be computed in CreateTeamSelectionMenu.",
    )

    PARTNER_TALK_KIND_TABLE = Symbol(
        None,
        None,
        None,
        "Table of values for the PARTNER_TALK_KIND script variable.\n\ntype: struct partner_talk_kind_table_entry[11]",
    )

    SCRIPT_VARS_LOCALS = Symbol(
        None,
        None,
        None,
        "List of special 'local' variables available to the script engine. There are 4 16-byte entries.\n\nEach entry has the same structure as an entry in SCRIPT_VARS.\n\ntype: struct script_local_var_table",
    )

    SCRIPT_VARS = Symbol(
        None,
        None,
        None,
        "List of predefined global variables that track game state, which are available to the script engine. There are 115 16-byte entries.\n\nThese variables underpin the various ExplorerScript global variables you can use in the SkyTemple SSB debugger.\n\ntype: struct script_var_table",
    )

    PORTRAIT_LAYOUTS = Symbol(
        None,
        None,
        None,
        "All the possible layouts a portrait can be placed in by default.\n\ntype: struct portrait_layout[32]",
    )

    KAOMADO_FILEPATH = Symbol(
        None,
        None,
        None,
        "'Path of the file where all the portraits are stored. 'FONT/kaomado.kao', padded with null to a multiple of 4'\n\ntype: char[20]",
    )

    WONDER_MAIL_BITS_MAP = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: uint8_t[32]",
    )

    WONDER_MAIL_BITS_SWAP = Symbol(
        None,
        None,
        None,
        "Last 2 bytes are unused\n\nNote: unverified, ported from Irdkwia's notes\n\ntype: uint8_t[36]",
    )

    ARM9_UNKNOWN_TABLE__NA_209E12C = Symbol(
        None,
        None,
        None,
        "52*0x2 + 2 bytes unused\n\nNote: unverified, ported from Irdkwia's notes",
    )

    ARM9_UNKNOWN_TABLE__NA_209E164 = Symbol(
        None, None, None, "256*0x1\n\nNote: unverified, ported from Irdkwia's notes"
    )

    ARM9_UNKNOWN_TABLE__NA_209E280 = Symbol(
        None, None, None, "32*0x1\n\nNote: unverified, ported from Irdkwia's notes"
    )

    WONDER_MAIL_ENCRYPTION_TABLE = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: uint8_t[256]",
    )

    DUNGEON_DATA_LIST = Symbol(
        None,
        None,
        None,
        "Data about every dungeon in the game.\n\nThis is an array of 180 dungeon data list entry structs. Each entry is 4 bytes, and contains floor count information along with an index into the bulk of the dungeon's data in mappa_s.bin.\n\nSee the struct definitions and End45's dungeon data document for more info.\n\ntype: struct dungeon_data_list_entry[180]",
    )

    ADVENTURE_LOG_ENCOUNTERS_MONSTER_IDS = Symbol(
        None,
        None,
        None,
        "List of monster IDs with a corresponding milestone in the Adventure Log.\n\ntype: struct monster_id_16[38]",
    )

    ARM9_UNKNOWN_DATA__NA_209E6BC = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    TACTIC_NAME_STRING_IDS = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: int16_t[12]",
    )

    STATUS_NAME_STRING_IDS = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: int16_t[102]",
    )

    DUNGEON_RETURN_STATUS_TABLE = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: struct dungeon_return_status[91]",
    )

    STATUSES_FULL_DESCRIPTION_STRING_IDS = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: struct status_description[103]",
    )

    ARM9_UNKNOWN_DATA__NA_209EAAC = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    MISSION_FLOOR_RANKS_AND_ITEM_LISTS_1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    MISSION_FLOORS_FORBIDDEN = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: struct mission_floors_forbidden[100]",
    )

    MISSION_FLOOR_RANKS_AND_ITEM_LISTS_2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    MISSION_FLOOR_RANKS_PTRS = Symbol(
        None,
        None,
        None,
        "Uses MISSION_FLOOR_RANKS_AND_ITEM_LISTS\n\nNote: unverified, ported from Irdkwia's notes",
    )

    DUNGEON_RESTRICTIONS = Symbol(
        None,
        None,
        None,
        "Data related to dungeon restrictions for every dungeon in the game.\n\nThis is an array of 256 dungeon restriction structs. Each entry is 12 bytes, and contains information about restrictions within the given dungeon.\n\nSee the struct definitions and End45's dungeon data document for more info.\n\ntype: struct dungeon_restriction[256]",
    )

    SPECIAL_BAND_STAT_BOOST = Symbol(
        None, None, None, "Stat boost value for the Special Band."
    )

    MUNCH_BELT_STAT_BOOST = Symbol(
        None, None, None, "Stat boost value for the Munch Belt."
    )

    GUMMI_STAT_BOOST = Symbol(
        None,
        None,
        None,
        "Stat boost value if a stat boost occurs when eating normal Gummis.",
    )

    MIN_IQ_EXCLUSIVE_MOVE_USER = Symbol(None, None, None, "")

    WONDER_GUMMI_IQ_GAIN = Symbol(
        None, None, None, "IQ gain when ingesting wonder gummis."
    )

    AURA_BOW_STAT_BOOST = Symbol(
        None, None, None, "Stat boost value for the aura bows."
    )

    MIN_IQ_ITEM_MASTER = Symbol(None, None, None, "")

    DEF_SCARF_STAT_BOOST = Symbol(
        None, None, None, "Stat boost value for the Defense Scarf."
    )

    POWER_BAND_STAT_BOOST = Symbol(
        None, None, None, "Stat boost value for the Power Band."
    )

    WONDER_GUMMI_STAT_BOOST = Symbol(
        None,
        None,
        None,
        "Stat boost value if a stat boost occurs when eating Wonder Gummis.",
    )

    ZINC_BAND_STAT_BOOST = Symbol(
        None, None, None, "Stat boost value for the Zinc Band."
    )

    EGG_HP_BONUS = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    EVOLUTION_HP_BONUS = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DAMAGE_FORMULA_FLV_SHIFT = Symbol(
        None,
        None,
        None,
        "The constant shift added to the 'FLV' intermediate quantity in the damage formula (see dungeon::last_move_damage_calc_flv), as a binary fixed-point number with 8 fraction bits (50).",
    )

    EVOLUTION_PHYSICAL_STAT_BONUSES = Symbol(
        None,
        None,
        None,
        "0x2: Atk + 0x2: Def\n\nNote: unverified, ported from Irdkwia's notes",
    )

    DAMAGE_FORMULA_CONSTANT_SHIFT = Symbol(
        None,
        None,
        None,
        "The constant shift applied to the overall output of the 'unshifted base' damage formula (the sum of the scaled AT, DEF, and ClampedLn terms), as a binary fixed-point number with 8 fraction bits (-311).\n\nThe value of -311 is notably equal to -round[DAMAGE_FORMULA_LN_PREFACTOR * ln(DAMAGE_FORMULA_LN_ARG_PREFACTOR * DAMAGE_FORMULA_FLV_SHIFT)]. This is probably not a coincidence.",
    )

    DAMAGE_FORMULA_FLV_DEFICIT_DIVISOR = Symbol(
        None,
        None,
        None,
        "The divisor of the (AT - DEF) term within the 'FLV' intermediate quantity in the damage formula (see dungeon::last_move_damage_calc_flv), as a binary fixed-point number with 8 fraction bits (8).",
    )

    EGG_STAT_BONUSES = Symbol(
        None,
        None,
        None,
        "0x2: Atk + 0x2: SpAtk + 0x2: Def + 0x2: SpDef\n\nNote: unverified, ported from Irdkwia's notes",
    )

    EVOLUTION_SPECIAL_STAT_BONUSES = Symbol(
        None,
        None,
        None,
        "0x2: SpAtk + 0x2: SpDef\n\nNote: unverified, ported from Irdkwia's notes",
    )

    DAMAGE_FORMULA_NON_TEAM_MEMBER_MODIFIER = Symbol(
        None,
        None,
        None,
        "The divisor applied to the overall output of the 'shifted base' damage formula (the sum of the scaled AT, Def, ClampedLn, and DAMAGE_FORMULA_CONSTANT_SHIFT terms) if the attacker is not a team member (and the current fixed room is not the substitute room...for some reason), as a binary fixed-point number with 8 fraction bits (85/64).",
    )

    DAMAGE_FORMULA_LN_PREFACTOR = Symbol(
        None,
        None,
        None,
        "The prefactor to the output of the ClampedLn in the damage formula, as a binary fixed-point number with 8 fraction bits (50).",
    )

    DAMAGE_FORMULA_DEF_PREFACTOR = Symbol(
        None,
        None,
        None,
        "The prefactor to the 'DEF' (defense) intermediate quantity in the damage formula (see dungeon::last_move_damage_calc_def), as a binary fixed-point number with 8 fraction bits (-0.5).",
    )

    DAMAGE_FORMULA_AT_PREFACTOR = Symbol(
        None,
        None,
        None,
        "The prefactor to the 'AT' (attack) intermediate quantity in the damage formula (see dungeon::last_move_damage_calc_at), as a binary fixed-point number with 8 fraction bits (153/256, which is close to 0.6).",
    )

    DAMAGE_FORMULA_LN_ARG_PREFACTOR = Symbol(
        None,
        None,
        None,
        "The prefactor to the argument of ClampedLn in the damage formula (FLV + DAMAGE_FORMULA_FLV_SHIFT), as a binary fixed-point number with 8 fraction bits (10).",
    )

    FORBIDDEN_FORGOT_MOVE_LIST = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: struct forbidden_forgot_move_entry[3]",
    )

    TACTICS_UNLOCK_LEVEL_TABLE = Symbol(None, None, None, "type: int16_t[12]")

    CLIENT_LEVEL_TABLE = Symbol(
        None,
        None,
        None,
        "Still a guess\n\nNote: unverified, ported from Irdkwia's notes\n\ntype: int16_t[16]",
    )

    OUTLAW_LEVEL_TABLE = Symbol(
        None,
        None,
        None,
        "Table of 2-byte outlaw levels for outlaw missions, indexed by mission rank.\n\ntype: int16_t[16]",
    )

    OUTLAW_MINION_LEVEL_TABLE = Symbol(
        None,
        None,
        None,
        "Table of 2-byte outlaw minion levels for outlaw hideout missions, indexed by mission rank.\n\ntype: int16_t[16]",
    )

    HIDDEN_POWER_BASE_POWER_TABLE = Symbol(
        None,
        None,
        None,
        "Still a guess\n\nNote: unverified, ported from Irdkwia's notes\n\ntype: int[10]",
    )

    VERSION_EXCLUSIVE_MONSTERS = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: struct version_exclusive_monster[23]",
    )

    IQ_SKILL_RESTRICTIONS = Symbol(
        None,
        None,
        None,
        "Table of 2-byte values for each IQ skill that represent a group. IQ skills in the same group can not be enabled at the same time.\n\ntype: int16_t[69]",
    )

    SECONDARY_TERRAIN_TYPES = Symbol(
        None,
        None,
        None,
        "The type of secondary terrain for each dungeon in the game.\n\nThis is an array of 200 bytes. Each byte is an enum corresponding to one dungeon.\n\ntype: struct secondary_terrain_type_8[200]",
    )

    SENTRY_DUTY_MONSTER_IDS = Symbol(
        None,
        None,
        None,
        "Table of monster IDs usable in the sentry duty minigame.\n\ntype: struct monster_id_16[102]",
    )

    IQ_SKILLS = Symbol(
        None,
        None,
        None,
        "Table of 4-byte values for each IQ skill that represent the required IQ value to unlock a skill.\n\ntype: int[69]",
    )

    IQ_GROUP_SKILLS = Symbol(None, None, None, "Irdkwia's notes: 25*16*0x1")

    MONEY_QUANTITY_TABLE = Symbol(
        None,
        None,
        None,
        "Table that maps money quantity codes (as recorded in, e.g., struct item) to actual amounts.\n\ntype: int[100]",
    )

    ARM9_UNKNOWN_TABLE__NA_20A20B0 = Symbol(
        None, None, None, "256*0x2\n\nNote: unverified, ported from Irdkwia's notes"
    )

    IQ_GUMMI_GAIN_TABLE = Symbol(None, None, None, "type: int16_t[18][18]")

    GUMMI_BELLY_RESTORE_TABLE = Symbol(None, None, None, "type: int16_t[18][18]")

    BAG_CAPACITY_TABLE_SPECIAL_EPISODES = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: uint32_t[5]",
    )

    BAG_CAPACITY_TABLE = Symbol(
        None,
        None,
        None,
        "Array of 4-byte integers containing the bag capacity for each bag level.\n\ntype: uint32_t[8]",
    )

    SPECIAL_EPISODE_MAIN_CHARACTERS = Symbol(
        None, None, None, "type: struct monster_id_16[100]"
    )

    GUEST_MONSTER_DATA = Symbol(
        None,
        None,
        None,
        "Data for guest monsters that join you during certain story dungeons.\n\nArray of 18 36-byte entries.\n\nSee the struct definitions and End45's dungeon data document for more info.\n\ntype: struct guest_monster[18]",
    )

    RANK_UP_TABLE = Symbol(None, None, None, "")

    DS_DOWNLOAD_TEAMS = Symbol(
        None,
        None,
        None,
        "Seems like this is just a collection of null-terminated lists concatenated together.\n\nNote: unverified, ported from Irdkwia's notes\n\nstruct monster_id_16[56]",
    )

    ARM9_UNKNOWN_PTR__NA_20A2C84 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    UNOWN_SPECIES_ADDITIONAL_CHARS = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: enum monster_id[28]",
    )

    MONSTER_SPRITE_DATA = Symbol(None, None, None, "")

    REMOTE_STRINGS = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    RANK_STRINGS_1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    MISSION_MENU_STRING_IDS_1 = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: int16_t[8]",
    )

    RANK_STRINGS_2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    MISSION_MENU_STRING_IDS_2 = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: int16_t[8]",
    )

    RANK_STRINGS_3 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    MISSION_DUNGEON_UNLOCK_TABLE = Symbol(
        None,
        None,
        None,
        "Irdkwia's notes: SpecialDungeonMissions\n\ntype: struct dungeon_unlock_entry[3]",
    )

    NO_SEND_ITEM_TABLE = Symbol(
        None,
        None,
        None,
        "A list of items that are forbidden from being used in a mission sent by Wonder Mail.\n\ntype: struct item_id_16[3]",
    )

    ARM9_UNKNOWN_TABLE__NA_20A3CC8 = Symbol(
        None,
        None,
        None,
        "14*0x2\nLinked to ARM9_UNKNOWN_TABLE__NA_20A3CE4\n\nNote: unverified, ported from Irdkwia's notes",
    )

    ARM9_UNKNOWN_TABLE__NA_20A3CE4 = Symbol(
        None, None, None, "8*0x2\n\nNote: unverified, ported from Irdkwia's notes"
    )

    ARM9_UNKNOWN_FUNCTION_TABLE__NA_20A3CF4 = Symbol(
        None,
        None,
        None,
        "Could be related to missions\n\nNote: unverified, ported from Irdkwia's notes",
    )

    MISSION_BANNED_STORY_MONSTERS = Symbol(
        None,
        None,
        None,
        "Null-terminated list of monster IDs that can't be used (probably as clients or targets) when generating missions before a certain point in the story.\n\nTo be precise, PERFOMANCE_PROGRESS_FLAG[9] must be enabled so these monsters can appear as mission clients.\n\ntype: struct monster_id_16[length / 2]",
    )

    ITEM_DELIVERY_TABLE = Symbol(
        None,
        None,
        None,
        "A list of valid items used for delivering an item for a mission client.\n\ntype: struct item_id_16[23]",
    )

    MISSION_RANK_POINTS = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: int[16]",
    )

    MISSION_BANNED_MONSTERS = Symbol(
        None,
        None,
        None,
        "Null-terminated list of monster IDs that can't be used (probably as clients or targets) when generating missions.\n\ntype: struct monster_id_16[124]",
    )

    MISSION_STRING_IDS = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: int16_t[964]",
    )

    LEVEL_LIST = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    EVENTS = Symbol(
        None,
        None,
        None,
        "Table of levels for the script engine, in which scenes can take place. There are a version-dependent number of 12-byte entries.\n\ntype: struct script_level[length / 12]",
    )

    ARM9_UNKNOWN_TABLE__NA_20A68BC = Symbol(
        None, None, None, "6*0x2\n\nNote: unverified, ported from Irdkwia's notes"
    )

    DEMO_TEAMS = Symbol(
        None,
        None,
        None,
        "18*0x4 (Hero ID 0x2, Partner ID 0x2)\n\nNote: unverified, ported from Irdkwia's notes",
    )

    ACTOR_LIST = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    ENTITIES = Symbol(
        None,
        None,
        None,
        "Table of entities for the script engine, which can move around and do things within a scene. There are 386 12-byte entries.\n\ntype: struct script_entity[386]",
    )

    JOB_WINDOW_PARAMS_1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    JOB_MENU_ITEMS_1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    JOB_MENU_ITEMS_2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    JOB_MENU_ITEMS_3 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    JOB_MENU_ITEMS_4 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    JOB_MENU_ITEMS_5 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    JOB_MENU_ITEMS_6 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    JOB_MENU_ITEMS_7 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    JOB_MENU_ITEMS_8 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    JOB_MENU_ITEMS_9 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    JOB_MENU_ITEMS_10 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    JOB_MENU_ITEMS_11 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    JOB_MENU_ITEMS_12 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    JOB_MENU_ITEMS_13 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    JOB_WINDOW_PARAMS_2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_SWAP_ID_TABLE = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: struct dungeon_id_8[212]",
    )

    MAP_MARKER_PLACEMENTS = Symbol(
        None,
        None,
        None,
        "The map marker position of each dungeon on the Wonder Map.\n\nThis is an array of 310 map marker structs. Each entry is 8 bytes, and contains positional information about a dungeon on the map.\n\nSee the struct definitions and End45's dungeon data document for more info.\n\ntype: struct map_marker[310]",
    )

    LFO_OUTPUT_VOICE_UPDATE_FLAGS = Symbol(None, None, None, "")

    TRIG_TABLE = Symbol(
        None,
        None,
        None,
        "Interleaved table of sine and cosine values at 4096 divisions over a full period (2π radians).\n\nMore precisely, the trig_values entry at index i corresponds to {sin(i * 2π/4096), cos(i * 2π/4096)} (each division is ~1/10 of a degree). Values are stored as signed fixed-point numbers with 12 fraction bits.\n\ntype: struct trig_values[4096]",
    )

    FX_ATAN_IDX_TABLE = Symbol(
        None,
        None,
        None,
        "Table of arctangent values at 129 divisions over the domain [0, 1].\n\nMore precisely, entry at index i corresponds to (atan(i/128) / (π/2)). Values are stored as signed fixed-point numbers with 14 fraction bits.",
    )

    TEX_PLTT_START_ADDR_TABLE = Symbol(None, None, None, "")

    TEX_START_ADDR_TABLE = Symbol(None, None, None, "")

    ARM9_UNKNOWN_TABLE__NA_20AE924 = Symbol(
        None, None, None, "724*0x1\n\nNote: unverified, ported from Irdkwia's notes"
    )

    MEMORY_ALLOCATION_ARENA_GETTERS = Symbol(
        None,
        None,
        None,
        "Functions to get the desired memory arena for allocating and freeing heap memory.\n\ntype: struct mem_arena_getters",
    )

    PRNG_SEQUENCE_NUM = Symbol(
        None,
        None,
        None,
        "[Runtime] The current PRNG sequence number for the general-purpose PRNG. See Rand16Bit for more information on how the general-purpose PRNG works.",
    )

    LOADED_OVERLAY_GROUP_0 = Symbol(
        None,
        None,
        None,
        "[Runtime] The overlay group ID of the overlay currently loaded in slot 0. A group ID of 0 denotes no overlay.\n\nOverlay group IDs that can be loaded in slot 0:\n- 0x06 (overlay 3)\n- 0x07 (overlay 6)\n- 0x08 (overlay 4)\n- 0x09 (overlay 5)\n- 0x0A (overlay 7)\n- 0x0B (overlay 8)\n- 0x0C (overlay 9)\n- 0x10 (overlay 12)\n- 0x11 (overlay 13)\n- 0x12 (overlay 14)\n- 0x13 (overlay 15)\n- 0x14 (overlay 16)\n- 0x15 (overlay 17)\n- 0x16 (overlay 18)\n- 0x17 (overlay 19)\n- 0x18 (overlay 20)\n- 0x19 (overlay 21)\n- 0x1A (overlay 22)\n- 0x1B (overlay 23)\n- 0x1C (overlay 24)\n- 0x1D (overlay 25)\n- 0x1E (overlay 26)\n- 0x1F (overlay 27)\n- 0x20 (overlay 28)\n- 0x21 (overlay 30)\n- 0x22 (overlay 31)\n- 0x23 (overlay 32)\n- 0x24 (overlay 33)\n\ntype: enum overlay_group_id",
    )

    LOADED_OVERLAY_GROUP_1 = Symbol(
        None,
        None,
        None,
        "[Runtime] The overlay group ID of the overlay currently loaded in slot 1. A group ID of 0 denotes no overlay.\n\nOverlay group IDs that can be loaded in slot 1:\n- 0x4 (overlay 1)\n- 0x5 (overlay 2)\n- 0xD (overlay 11)\n- 0xE (overlay 29)\n- 0xF (overlay 34)\n\ntype: enum overlay_group_id",
    )

    LOADED_OVERLAY_GROUP_2 = Symbol(
        None,
        None,
        None,
        "[Runtime] The overlay group ID of the overlay currently loaded in slot 2. A group ID of 0 denotes no overlay.\n\nOverlay group IDs that can be loaded in slot 2:\n- 0x1 (overlay 0)\n- 0x2 (overlay 10)\n- 0x3 (overlay 35)\n\ntype: enum overlay_group_id",
    )

    DEBUG_IS_INITIALIZED = Symbol(None, None, None, "")

    PACK_FILES_OPENED = Symbol(
        None,
        None,
        None,
        "[Runtime] A pointer to the 6 opened Pack files (listed at PACK_FILE_PATHS_TABLE)\n\ntype: struct pack_file_opened*",
    )

    PACK_FILE_PATHS_TABLE = Symbol(
        None,
        None,
        None,
        "List of pointers to path strings to all known pack files.\nThe game uses this table to load its resources when launching dungeon mode.\n\ntype: char*[6]",
    )

    GAME_STATE_VALUES = Symbol(None, None, None, "[Runtime]")

    BAG_ITEMS_PTR_MIRROR = Symbol(
        None,
        None,
        None,
        "[Runtime] Probably a mirror of ram.yml::BAG_ITEMS_PTR?\n\nNote: unverified, ported from Irdkwia's notes",
    )

    ITEM_DATA_TABLE_PTRS = Symbol(
        None,
        None,
        None,
        "[Runtime] List of pointers to various item data tables.\n\nThe first two pointers are definitely item-related (although the order appears to be flipped between EU/NA?). Not sure about the third pointer.",
    )

    DUNGEON_MOVE_TABLES = Symbol(
        None,
        None,
        None,
        "[Runtime] Seems to be some sort of region (a table of tables?) that holds pointers to various important tables related to moves.",
    )

    MOVE_DATA_TABLE_PTR = Symbol(
        None,
        None,
        None,
        "[Runtime] Points to the contents of the move data table loaded from waza_p.bin\n\ntype: struct move_data_table*",
    )

    WAN_TABLE = Symbol(
        None,
        None,
        None,
        "pointer to the list of wan sprite loaded in RAM\n\nstruct wan_table*",
    )

    RENDER_3D = Symbol(
        None,
        None,
        None,
        "The (seemingly) unique instance render_3d_global in the game\n\ntype: struct render_3d_global",
    )

    RENDER_3D_FUNCTIONS_64 = Symbol(
        None,
        None,
        None,
        "Pointers to the 8 functions available for rendering a render_3d_element_64\n\ntype: render_3d_element_64_fn_t[8]",
    )

    LANGUAGE_INFO_DATA = Symbol(None, None, None, "[Runtime]")

    TBL_TALK_GROUP_STRING_ID_START = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: int16_t[6]",
    )

    KEYBOARD_STRING_IDS = Symbol(
        None,
        None,
        None,
        "30*0x2\n\nNote: unverified, ported from Irdkwia's notes\n\ntype: int16_t[30]",
    )

    NOTIFY_NOTE = Symbol(
        None,
        None,
        None,
        "[Runtime] Flag related to saving and loading state?\n\ntype: bool",
    )

    DEFAULT_HERO_ID = Symbol(
        None,
        None,
        None,
        "The default monster ID for the hero (0x4: Charmander)\n\ntype: struct monster_id_16",
    )

    DEFAULT_PARTNER_ID = Symbol(
        None,
        None,
        None,
        "The default monster ID for the partner (0x1: Bulbasaur)\n\ntype: struct monster_id_16",
    )

    GAME_MODE = Symbol(
        None,
        None,
        None,
        "[Runtime] Game mode, see enum game_mode for possible values.\n\ntype: uint8_t",
    )

    GLOBAL_PROGRESS_PTR = Symbol(
        None, None, None, "[Runtime]\n\ntype: struct global_progress*"
    )

    ADVENTURE_LOG_PTR = Symbol(
        None, None, None, "[Runtime]\n\ntype: struct adventure_log*"
    )

    ITEM_TABLES_PTRS_1 = Symbol(
        None,
        None,
        None,
        "Irdkwia's notes: 26*0x4, uses MISSION_FLOOR_RANKS_AND_ITEM_LISTS",
    )

    UNOWN_SPECIES_ADDITIONAL_CHAR_PTR_TABLE = Symbol(
        None,
        None,
        None,
        "Uses UNOWN_SPECIES_ADDITIONAL_CHARS\n\nNote: unverified, ported from Irdkwia's notes\n\ntype: enum monster_id*[28]",
    )

    TEAM_MEMBER_TABLE_PTR = Symbol(None, None, None, "Pointer to TEAM_MEMBER_TABLE")

    MISSION_DELIVER_LIST_PTR = Symbol(
        None,
        None,
        None,
        "A pointer to a heap-allocated list of items usable for delivery missions",
    )

    MISSION_DELIVER_COUNT = Symbol(
        None, None, None, "The total number of items usable for delivery missions"
    )

    MISSION_DUNGEON_LIST_PTR = Symbol(
        None,
        None,
        None,
        "A pointer to a heap-allocated list of dungeons usable for missions",
    )

    MISSION_DUNGEON_COUNT = Symbol(
        None, None, None, "The total number of dungeons usable for missions"
    )

    MISSION_MONSTER_LIST_PTR = Symbol(
        None,
        None,
        None,
        "A pointer to a heap-allocated list of monsters usable for missions",
    )

    MISSION_MONSTER_COUNT = Symbol(
        None, None, None, "The total number of monsters usable for missions"
    )

    MISSION_LIST_PTR = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    REMOTE_STRING_PTR_TABLE = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: const char*[7]",
    )

    RANK_STRING_PTR_TABLE = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: const char*[16]",
    )

    SMD_EVENTS_FUN_TABLE = Symbol(
        None,
        None,
        None,
        "Table of all DSE events, see https://projectpokemon.org/docs/mystery-dungeon-nds/procyon-studios-digital-sound-elements-r12/\n\nIrdkwia's notes: named DSEEventFunctionPtrTable with length 0x3C0 (note the disagreement), 240*0x4.",
    )

    MUSIC_DURATION_LOOKUP_TABLE_1 = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: int16_t[128]",
    )

    MUSIC_DURATION_LOOKUP_TABLE_2 = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: int32_t[128]",
    )

    LFO_WAVEFORM_CALLBACKS = Symbol(None, None, None, "")

    IS_DISP_ON = Symbol(None, None, None, "")

    GXI_DMA_ID = Symbol(None, None, None, "")

    JUICE_BAR_NECTAR_IQ_GAIN = Symbol(
        None, None, None, "IQ gain when ingesting nectar at the Juice Bar."
    )

    TEXT_SPEED = Symbol(None, None, None, "Controls text speed.")

    HERO_START_LEVEL = Symbol(None, None, None, "Starting level of the hero.")

    PARTNER_START_LEVEL = Symbol(None, None, None, "Starting level of the partner.")


class NaItcmArm9Section:
    name = "arm9"
    description = "The main ARM9 binary.\n\nThis is the main binary that gets loaded when the game is launched, and contains the core code that runs the game, low level facilities such as memory allocation, compression, other external dependencies (such as linked libraries), and the functions and tables necessary to load overlays and dispatch execution to them.\n\nSpeaking generally, this is the program run by the Nintendo DS's main ARM946E-S CPU, which handles all gameplay mechanisms and graphics rendering."
    loadaddress = 0x1FF8000
    length = 0x4000
    functions = NaItcmArm9Functions
    data = NaItcmArm9Data


class NaItcmItcmFunctions:

    Render3dSetTextureParams = Symbol(
        [0x130],
        [0x1FF8130],
        None,
        "A wrapper around GeomSetTexImageParam that caches the VRAM offset on RENDER_3D.\n\nAlways disables flipping and sets color values of 0 to be transparent.\n\nr0: render_3d_texture_params pointer\nr1: texture VRAM offset",
    )

    Render3dSetPaletteBase = Symbol(
        [0x1CC],
        [0x1FF81CC],
        None,
        "Send the PLTT_BASE geometry engine command, that sets the texture palette base address. Also caches the base address on RENDER_3D.\nSee http://problemkaputt.de/gbatek.htm#ds3dtextureattributes for more information on the parameters.\n\nr0: render_3d_texture_params pointer\nr1: palette base address",
    )

    Render3dRectangle = Symbol(
        [0x224],
        [0x1FF8224],
        None,
        "RENDER_3D_FUNCTIONS[0]. Renders a render_3d_element with type RENDER_RECTANGLE.\n\nr0: render_3d_rectangle",
    )

    GeomSetPolygonAttributes = Symbol(
        [0x480],
        [0x1FF8480],
        None,
        "Send the POLYGON_ATTR geometry engine command, that defines some polygon attributes for rendering.\nSee https://problemkaputt.de/gbatek.htm#ds3dpolygonattributes for more information\n\nr0: polygon ID\nr1: alpha",
    )

    Render3dQuadrilateral = Symbol(
        [0x49C],
        [0x1FF849C],
        None,
        "RENDER_3D_FUNCTIONS[1]. Renders a render_3d_element with type RENDER_QUADRILATERAL.\n\nr0: render_3d_quadrilateral",
    )

    Render3dTiling = Symbol(
        [0x728],
        [0x1FF8728],
        None,
        "RENDER_3D_FUNCTIONS[2]. Renders a render_3d_element with type RENDER_TILING.\n\nr0: render_3d_tiling",
    )

    Render3dTextureInternal = Symbol(
        [0xA10],
        [0x1FF8A10],
        None,
        "Implements most of the rendering logic for Render3dTexture.\n\nr0: render_3d_texture",
    )

    Render3dTexture = Symbol(
        [0xC28],
        [0x1FF8C28],
        None,
        "RENDER_3D_FUNCTIONS[3]. Renders a render_3d_element with type RENDER_TEXTURE.\n\nThis is primarily just a wrapper around Render3dTextureInternal, with a preceding alpha check and calls to Render3dSetTextureParams and Render3dSetPaletteBase.\n\nr0: render_3d_texture",
    )

    Render3dTextureNoSetup = Symbol(
        [0xC60],
        [0x1FF8C60],
        None,
        "Same as Render3dTexture except without calls to Render3dSetTextureParams and Render3dSetPaletteBase to set up geometry engine parameters.\n\nPresumably used to render multiple texture tiles with the same parameters without the extra setup overhead? But this function doesn't actually seem to be referenced anywhere.\n\nr0: render_3d_texture",
    )

    NewRender3dElement = Symbol(
        [0xC78],
        [0x1FF8C78],
        None,
        "Return a new render_3d_element from RENDER_3D's render queue, to draw a new element using the 3d render engine later in the frame.\n\nreturn: render_3d_element or NULL if there is no more available space in the queue",
    )

    EnqueueRender3dTexture = Symbol(
        [0xCAC],
        [0x1FF8CAC],
        None,
        "Copies the first 40 bytes of a render_3d_element onto the render queue of RENDER_3D, with type set to RENDER_TEXTURE.\n\nr0: render_3d_element",
    )

    EnqueueRender3dTiling = Symbol(
        [0xCDC],
        [0x1FF8CDC],
        None,
        "Copies a render_3d_element onto the render queue of RENDER_3D, with type set to RENDER_TILING.\n\nr0: render_3d_element",
    )

    NewRender3dRectangle = Symbol(
        [0xD0C],
        [0x1FF8D0C],
        None,
        "Return a render_3d_element from NewRender3dElement with a type of RENDER_RECTANGLE, and all other fields in the first 38 bytes zeroed.\n\nreturn: render_3d_element or NULL if there is no more available space in the queue",
    )

    NewRender3dQuadrilateral = Symbol(
        [0xD3C],
        [0x1FF8D3C],
        None,
        "Return a render_3d_element from NewRender3dElement with a type of RENDER_QUADRILATERAL, and all other fields in the first 38 bytes zeroed.\n\nreturn: render_3d_element or NULL if there is no more available space in the queue",
    )

    NewRender3dTexture = Symbol(
        [0xD6C],
        [0x1FF8D6C],
        None,
        "Return a render_3d_element from NewRender3dElement with a type of RENDER_TEXTURE, and all other fields in the first 40 bytes zeroed.\n\nreturn: render_3d_element or NULL if there is no more available space in the queue",
    )

    NewRender3dTiling = Symbol(
        [0xD9C],
        [0x1FF8D9C],
        None,
        "Return a render_3d_element from NewRender3dElement with a type of RENDER_TILING, and all other fields zeroed.\n\nreturn: render_3d_element or NULL if there is no more available space in the queue",
    )

    Render3dProcessQueue = Symbol(
        [0xDCC],
        [0x1FF8DCC],
        None,
        "Perform rendering of the render queue of RENDER_3D structure. Does nothing if there are no elements, otherwise, sort them based on a value, and render them all consecutively.\n\nNo params.",
    )

    GetKeyN2MSwitch = Symbol(
        [0x1434],
        [0x1FF9434],
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: key\nr1: switch",
    )

    GetKeyN2M = Symbol(
        [0x1468],
        [0x1FF9468],
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: key\nreturn: monster ID",
    )

    GetKeyN2MBaseForm = Symbol(
        [0x14D4],
        [0x1FF94D4],
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: key\nreturn: monster ID",
    )

    GetKeyM2NSwitch = Symbol(
        [0x150C],
        [0x1FF950C],
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: monster ID\nr1: switch",
    )

    GetKeyM2N = Symbol(
        [0x1540],
        [0x1FF9540],
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: monster ID\nreturn: key",
    )

    GetKeyM2NBaseForm = Symbol(
        [0x15AC],
        [0x1FF95AC],
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: monster ID\nreturn: key",
    )

    HardwareInterrupt = Symbol(
        [0x15E8],
        [0x1FF95E8],
        None,
        "Called whenever a hardware interrupt takes place.\n\nReturns immediately if the IME flag is 0 or if none of the devices that requested an interrupt has the corresponding Interrupt Enable flag set.\nIt searches for the first device that requested an interrupt, clears its Interrupt Request flag, then jumps to the start of the corresponding interrupt function. The return address is manually set to ReturnFromInterrupt.\nThe address of the function to jump to is read from the interrupt vector at the start of the DTCM region (0x27E0000).\nThis function does not return.\n\nNo params.",
    )

    ReturnFromInterrupt = Symbol(
        [0x1650],
        [0x1FF9650],
        None,
        "The execution returns to this function after a hardware interrupt function is run.\n\nNo params.",
    )

    ShouldMonsterRunAwayVariationOutlawCheck = Symbol(
        [0x2390],
        [0x1FFA390],
        None,
        "Calls ShouldMonsterRunAwayVariation. If the result is true, returns true. Otherwise, returns true only if the monster's behavior field is equal to monster_behavior::BEHAVIOR_FLEEING_OUTLAW.\n\nr0: Entity pointer\nr1: ?\nreturn: True if ShouldMonsterRunAway returns true or the monster is a fleeing outlaw",
    )

    AiMovement = Symbol(
        [0x23C4],
        [0x1FFA3C4],
        None,
        "Used by the AI to determine the direction in which a monster should move\n\nr0: Entity pointer\nr1: ?",
    )

    CalculateAiTargetPos = Symbol(
        [0x32C8],
        [0x1FFB2C8],
        None,
        "Calculates the target position of an AI-controlled monster and stores it in the monster's ai_target_pos field\n\nr0: Entity pointer",
    )

    ChooseAiMove = Symbol(
        [0x3658],
        [0x1FFB658],
        None,
        "Determines if an AI-controlled monster will use a move and which one it will use\n\nr0: Entity pointer",
    )

    LightningRodStormDrainCheck = Symbol(
        [0x3E5C],
        [0x1FFBE5C],
        None,
        "Appears to check whether LightningRod or Storm Drain should draw in a move.\n\nr0: attacker pointer\nr1: defender pointer\nr2: move pointer\nr3: true if checking for Storm Drain, false if checking for LightningRod\nreturn: whether the move should be drawn in",
    )


class NaItcmItcmData:

    MEMORY_ALLOCATION_TABLE = Symbol(
        None,
        None,
        None,
        "[Runtime] Keeps track of all active heap allocations.\n\nThe memory allocator in the ARM9 binary uses region-based memory management (see https://en.wikipedia.org/wiki/Region-based_memory_management). The heap is broken up into smaller contiguous chunks called arenas (struct mem_arena), which are in turn broken up into chunks referred to as blocks (struct mem_block). Most of the time, an allocation results in a block being split off from a free part of an existing memory arena.\n\nNote: This symbol isn't actually part of the ITCM, it gets created at runtime on the spot in RAM that used to contain the code that was moved to the ITCM.\n\ntype: struct mem_alloc_table",
    )

    DEFAULT_MEMORY_ARENA = Symbol(
        None,
        None,
        None,
        "[Runtime] The default memory allocation arena. This is part of MEMORY_ALLOCATION_TABLE, but is also referenced on its own by various functions.\n\nNote: This symbol isn't actually part of the ITCM, it gets created at runtime on the spot in RAM that used to contain the code that was moved to the ITCM.\n\ntype: struct mem_arena",
    )

    DEFAULT_MEMORY_ARENA_BLOCKS = Symbol(
        None,
        None,
        None,
        "[Runtime] The block array for DEFAULT_MEMORY_ARENA.\n\nNote: This symbol isn't actually part of the ITCM, it gets created at runtime on the spot in RAM that used to contain the code that was moved to the ITCM.\n\ntype: struct mem_block[256]",
    )

    RENDER_3D_FUNCTIONS = Symbol(
        [0x120],
        [0x1FF8120],
        None,
        "Pointers to the 4 functions available for rendering a render_3d_element (in ITCM)\n\ntype: render_3d_element_fn_t[4]",
    )


class NaItcmItcmSection:
    name = "itcm"
    description = "The instruction TCM (tightly-coupled memory) and the corresponding region in the ARM9 binary.\n\nThe ITCM is a special area of low-latency memory meant for performance-critical routines. It's similar to an instruction cache, but more predictable. See the ARMv5 Architecture Reference Manual, Chapter B7 (https://developer.arm.com/documentation/ddi0100/i).\n\nThe Nintendo DS ITCM region is located at 0x0-0x7FFF in memory, but the 32 KiB segment is mirrored throughout the 16 MiB block from 0x0-0x1FFFFFF. The Explorers of Sky code seems to reference only the mirror at 0x1FF8000, the closest one to main memory.\n\nIn Explorers of Sky, a fixed region of the ARM9 binary appears to be loaded in the ITCM at all times, and seems to contain functions related to the dungeon AI, among other things. The ITCM has a max capacity of 0x8000, although not all of it is used."
    loadaddress = 0x1FF8000
    length = 0x4000
    functions = NaItcmItcmFunctions
    data = NaItcmItcmData


class NaItcmLibsFunctions:

    DseDriver_LoadDefaultSettings = Symbol(None, None, None, "")

    DseDriver_IsSettingsValid = Symbol(
        None,
        None,
        None,
        "r0: DSE driver settings\nreturn: Flags specifying what settings are invalid.",
    )

    DseDriver_ConfigureHeap = Symbol(None, None, None, "")

    DseDriver_Init = Symbol(None, None, None, "")

    Dse_SetError = Symbol(None, None, None, "")

    Dse_SetError2 = Symbol(None, None, None, "")

    DseUtil_ByteSwap32 = Symbol(None, None, None, "")

    SoundUtil_GetRandomNumber = Symbol(
        None, None, None, "return: random number in the range [0, 32767]"
    )

    DseMem_Init = Symbol(None, None, None, "")

    DseMem_Quit = Symbol(None, None, None, "")

    DseMem_AllocateUser = Symbol(None, None, None, "")

    DseMem_Allocate = Symbol(None, None, None, "")

    DseMem_AllocateThreadStack = Symbol(None, None, None, "")

    DseMem_Free = Symbol(None, None, None, "")

    DseMem_Clear = Symbol(None, None, None, "")

    DseFile_CheckHeader = Symbol(None, None, None, "")

    DseSwd_SysInit = Symbol(None, None, None, "")

    DseSwd_SysQuit = Symbol(None, None, None, "")

    DseSwd_SampleLoaderMain = Symbol(None, None, None, "")

    DseSwd_MainBankDummyCallback = Symbol(None, None, None, "")

    DseSwd_LoadMainBank = Symbol(None, None, None, "")

    DseSwd_LoadBank = Symbol(None, None, None, "")

    DseSwd_IsBankLoading = Symbol(None, None, None, "")

    DseSwd_LoadWaves = Symbol(None, None, None, "")

    DseSwd_LoadWavesInternal = Symbol(None, None, None, "")

    DseSwd_Unload = Symbol(None, None, None, "")

    ReadWaviEntry = Symbol(
        None,
        None,
        None,
        "Reads an entry from the pointer table of a wavi container and returns a pointer to the data of said entry, which contains information about a particular sample.\n\nr0: Wavi data struct\nr1: Entry index\nreturn: Pointer to the entry's data",
    )

    DseSwd_GetInstrument = Symbol(None, None, None, "")

    DseSwd_GetNextSplitInRange = Symbol(None, None, None, "")

    DseSwd_GetMainBankById = Symbol(None, None, None, "")

    DseSwd_GetBankById = Symbol(None, None, None, "")

    DseSwd_InitMainBankFileReader = Symbol(None, None, None, "")

    DseSwd_OpenMainBankFileReader = Symbol(None, None, None, "")

    DseSwd_CloseMainBankFileReader = Symbol(None, None, None, "")

    DseSwd_ReadMainBank = Symbol(None, None, None, "")

    DseBgm_DefaultSignalCallback = Symbol(None, None, None, "")

    DseBgm_Load = Symbol(None, None, None, "")

    DseBgm_Unload = Symbol(None, None, None, "")

    DseBgm_SetSignalCallback = Symbol(None, None, None, "")

    DseBgm_IsPlaying = Symbol(None, None, None, "")

    ResumeBgm = Symbol(
        None, None, None, "Uncertain.\n\nNote: unverified, ported from Irdkwia's notes"
    )

    DseBgm_Stop = Symbol(None, None, None, "")

    DseBgm_StopAll = Symbol(None, None, None, "")

    DseBgm_SetFades = Symbol(None, None, None, "")

    DseSequence_Start = Symbol(None, None, None, "")

    DseSequence_PauseList = Symbol(None, None, None, "")

    DseSequence_SetFades = Symbol(None, None, None, "")

    DseSequence_GetParameter = Symbol(None, None, None, "")

    DseSequence_GetSmallestNumLoops = Symbol(None, None, None, "")

    DseSequence_Reset = Symbol(None, None, None, "")

    DseSequence_Stop = Symbol(None, None, None, "")

    FindSmdlSongChunk = Symbol(
        None,
        None,
        None,
        "Finds the first song chunk within an SMDL file that has the specified value on its 0x10 field.\n\nSee https://projectpokemon.org/home/docs/mystery-dungeon-nds/dse-smdl-format-r13/.\n\nr0: Pointer to the start of the SMDL file\nr1: Value to search for\nreturn: Pointer to the first chunk that has the specified value + 0x10, or null if no chunk was found.",
    )

    DseSequence_LoadSong = Symbol(None, None, None, "")

    DseSequence_GetById = Symbol(None, None, None, "")

    DseSequence_AllocateNew = Symbol(None, None, None, "")

    DseSequence_Unload = Symbol(None, None, None, "")

    DseSequence_InitTracks = Symbol(None, None, None, "")

    DseBgm_SysSetupNoteList = Symbol(None, None, None, "")

    DseSe_SysReset = Symbol(None, None, None, "")

    DseSe_Load = Symbol(None, None, None, "")

    DseSe_Unload = Symbol(None, None, None, "")

    DseSe_GetUsedBankIDs = Symbol(None, None, None, "")

    DseSe_HasPlayingInstances = Symbol(None, None, None, "")

    DseSe_Play = Symbol(None, None, None, "")

    DseSe_GetEffectSong = Symbol(None, None, None, "")

    DseSe_CheckTooManyInstances = Symbol(None, None, None, "")

    DseSe_CheckTooManyInstancesInGroup = Symbol(None, None, None, "")

    DseSe_GetBestSeqAllocation = Symbol(None, None, None, "")

    DseSe_GetById = Symbol(None, None, None, "")

    DseSe_Stop = Symbol(None, None, None, "")

    DseSe_StopAll = Symbol(None, None, None, "")

    DseSe_StopSeq = Symbol(None, None, None, "")

    FlushChannels = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DseDriver_StartMainThread = Symbol(None, None, None, "")

    DseDriver_StartTickTimer = Symbol(None, None, None, "")

    DseDriver_NotifyTick = Symbol(None, None, None, "")

    DseDriver_Main = Symbol(None, None, None, "")

    DseSequence_TickNotes = Symbol(None, None, None, "")

    ParseDseEvent = Symbol(
        None,
        None,
        None,
        "Parses and executes a DSE event for the specified track, if necessary.\n\nThe function checks the time left before the next event (track_data::event_delay), and parses it if said time is 0.\n\nSee also https://projectpokemon.org/docs/mystery-dungeon-nds/procyon-studios-digital-sound-elements-r12/\n\nr0: Pointer to some struct that seems to hold the state of the audio engine\nr1: Pointer to track data",
    )

    UpdateSequencerTracks = Symbol(
        None,
        None,
        None,
        "From https://projectpokemon.org/docs/mystery-dungeon-nds/procyon-studios-digital-sound-elements-r12/",
    )

    DseSequence_TickFades = Symbol(None, None, None, "")

    DseTrackEvent_Invalid = Symbol(None, None, None, "")

    DseTrackEvent_WaitSame = Symbol(None, None, None, "")

    DseTrackEvent_WaitDelta = Symbol(None, None, None, "")

    DseTrackEvent_Wait8 = Symbol(None, None, None, "")

    DseTrackEvent_Wait16 = Symbol(None, None, None, "")

    DseTrackEvent_Wait24 = Symbol(None, None, None, "")

    DseTrackEvent_WaitUntilFadeout = Symbol(None, None, None, "")

    DseTrackEvent_EndTrack = Symbol(None, None, None, "")

    DseTrackEvent_MainLoopBegin = Symbol(None, None, None, "")

    DseTrackEvent_SubLoopBegin = Symbol(None, None, None, "")

    DseTrackEvent_SubLoopEnd = Symbol(None, None, None, "")

    DseTrackEvent_SubLoopBreakOnLastIteration = Symbol(None, None, None, "")

    DseTrackEvent_SetOctave = Symbol(None, None, None, "")

    DseTrackEvent_OctaveDelta = Symbol(None, None, None, "")

    DseTrackEvent_SetBpm = Symbol(None, None, None, "")

    DseTrackEvent_SetBpm2 = Symbol(None, None, None, "")

    DseTrackEvent_SetBank = Symbol(None, None, None, "")

    DseTrackEvent_SetBankMsb = Symbol(None, None, None, "")

    DseTrackEvent_SetBankLsb = Symbol(None, None, None, "")

    DseTrackEvent_Dummy1Byte = Symbol(None, None, None, "")

    DseTrackEvent_SetInstrument = Symbol(None, None, None, "")

    DseTrackEvent_SongVolumeFade = Symbol(None, None, None, "")

    DseTrackEvent_RestoreEnvelopeDefaults = Symbol(None, None, None, "")

    DseTrackEvent_SetEnvelopeAttackBegin = Symbol(None, None, None, "")

    DseTrackEvent_SetEnvelopeAttackTime = Symbol(None, None, None, "")

    DseTrackEvent_SetEnvelopeHoldTime = Symbol(None, None, None, "")

    DseTrackEvent_SetEnvelopeDecayTimeAndSustainLevel = Symbol(None, None, None, "")

    DseTrackEvent_SetEnvelopeSustainTime = Symbol(None, None, None, "")

    DseTrackEvent_SetEnvelopeReleaseTime = Symbol(None, None, None, "")

    DseTrackEvent_SetNoteDurationMultiplier = Symbol(None, None, None, "")

    DseTrackEvent_ForceLfoEnvelopeLevel = Symbol(None, None, None, "")

    DseTrackEvent_SetHoldNotes = Symbol(None, None, None, "")

    DseTrackEvent_SetFlagBit1Unknown = Symbol(None, None, None, "")

    DseTrackEvent_SetOptionalVolume = Symbol(None, None, None, "")

    DseTrackEvent_Dummy2Bytes = Symbol(None, None, None, "")

    DseTrackEvent_SetTuning = Symbol(None, None, None, "")

    DseTrackEvent_TuningDeltaCoarse = Symbol(None, None, None, "")

    DseTrackEvent_TuningDeltaFine = Symbol(None, None, None, "")

    DseTrackEvent_TuningDeltaFull = Symbol(None, None, None, "")

    DseTrackEvent_TuningFade = Symbol(None, None, None, "")

    DseTrackEvent_SetNoteRandomRegion = Symbol(None, None, None, "")

    DseTrackEvent_SetTuningJitterAmplitude = Symbol(None, None, None, "")

    DseTrackEvent_SetKeyBend = Symbol(None, None, None, "")

    DseTrackEvent_SetUnknown2 = Symbol(None, None, None, "")

    DseTrackEvent_SetKeyBendRange = Symbol(None, None, None, "")

    DseTrackEvent_SetupKeyBendLfo = Symbol(None, None, None, "")

    DseTrackEvent_SetupKeyBendLfoEnvelope = Symbol(None, None, None, "")

    DseTrackEvent_UseKeyBendLfo = Symbol(None, None, None, "")

    DseTrackEvent_SetVolume = Symbol(None, None, None, "")

    DseTrackEvent_VolumeDelta = Symbol(None, None, None, "")

    DseTrackEvent_VolumeFade = Symbol(None, None, None, "")

    DseTrackEvent_SetExpression = Symbol(None, None, None, "")

    DseTrackEvent_SetupVolumeLfo = Symbol(None, None, None, "")

    DseTrackEvent_SetupVolumeLfoEnvelope = Symbol(None, None, None, "")

    DseTrackEvent_UseVolumeLfo = Symbol(None, None, None, "")

    DseTrackEvent_SetPan = Symbol(None, None, None, "")

    DseTrackEvent_PanDelta = Symbol(None, None, None, "")

    DseTrackEvent_PanFade = Symbol(None, None, None, "")

    DseTrackEvent_SetupPanLfo = Symbol(None, None, None, "")

    DseTrackEvent_SetupPanLfoEnvelope = Symbol(None, None, None, "")

    DseTrackEvent_UsePanLfo = Symbol(None, None, None, "")

    DseTrackEvent_SetupLfo = Symbol(None, None, None, "")

    DseTrackEvent_SetupLfoEnvelope = Symbol(None, None, None, "")

    DseTrackEvent_SetLfoParameter = Symbol(None, None, None, "")

    DseTrackEvent_UseLfo = Symbol(None, None, None, "")

    DseTrackEvent_Signal = Symbol(None, None, None, "")

    DseTrackEvent_Dummy2Bytes2 = Symbol(None, None, None, "")

    DseSynth_Reset = Symbol(None, None, None, "")

    DseSynth_AllocateNew = Symbol(None, None, None, "")

    DseSynth_Unload = Symbol(None, None, None, "")

    DseSynth_ClearHeldNotes = Symbol(None, None, None, "")

    DseSynth_ResetAndSetBankAndSequence = Symbol(None, None, None, "")

    DseSynth_StopChannels = Symbol(None, None, None, "")

    DseSynth_ResetAllVoiceTimersAndVolumes = Symbol(None, None, None, "")

    DseSynth_RestoreHeldNotes = Symbol(None, None, None, "")

    DseSynth_SetGlobalVolumeIndex = Symbol(None, None, None, "")

    DseSynth_SetBend = Symbol(None, None, None, "")

    DseSynth_SetVolume = Symbol(None, None, None, "")

    DseSynth_SetPan = Symbol(None, None, None, "")

    DseSynth_SetBankAndSequence = Symbol(None, None, None, "")

    DseChannel_Init = Symbol(None, None, None, "")

    DseChannel_DeallocateVoices = Symbol(None, None, None, "")

    DseChannel_ResetTimerAndVolumeForVoices = Symbol(None, None, None, "")

    DseChannel_SetBank = Symbol(None, None, None, "")

    DseChannel_SetInstrument = Symbol(None, None, None, "")

    DseChannel_SetLfoConstEnvelopeLevel = Symbol(None, None, None, "")

    DseChannel_SetKeyBend = Symbol(None, None, None, "")

    DseChannel_AllocateNote = Symbol(None, None, None, "")

    DseChannel_ReleaseNoteInternal = Symbol(None, None, None, "")

    DseChannel_ChangeNote = Symbol(None, None, None, "")

    DseChannel_ReleaseNote = Symbol(None, None, None, "")

    DseVoice_PlayNote = Symbol(None, None, None, "")

    DseVoice_ReleaseNote = Symbol(None, None, None, "")

    DseVoice_UpdateParameters = Symbol(None, None, None, "")

    DseVoice_ResetAll = Symbol(None, None, None, "")

    DseVoice_ResetHW = Symbol(None, None, None, "")

    UpdateChannels = Symbol(
        None,
        None,
        None,
        "From https://projectpokemon.org/docs/mystery-dungeon-nds/procyon-studios-digital-sound-elements-r12/ and Irdkwia's notes.\n\nNo params.",
    )

    DseVoice_Cleanup = Symbol(None, None, None, "")

    DseVoice_Allocate = Symbol(None, None, None, "")

    DseVoice_Start = Symbol(None, None, None, "")

    DseVoice_ReleaseHeld = Symbol(None, None, None, "")

    DseVoice_Release = Symbol(None, None, None, "")

    DseVoice_Deallocate = Symbol(None, None, None, "")

    DseVoice_FlagForActivation = Symbol(None, None, None, "")

    DseVoice_FlagForDeactivation = Symbol(None, None, None, "")

    DseVoice_CountNumActiveInChannel = Symbol(None, None, None, "")

    DseVoice_UpdateHardware = Symbol(None, None, None, "")

    SoundEnvelope_Reset = Symbol(None, None, None, "r0: Sound envelope pointer")

    SoundEnvelopeParameters_Reset = Symbol(
        None, None, None, "r0: Sound envelope parameters pointer"
    )

    SoundEnvelopeParameters_CheckValidity = Symbol(
        None, None, None, "r0: Sound envelope parameters pointer"
    )

    SoundEnvelope_SetParameters = Symbol(
        None,
        None,
        None,
        "r0: Sound envelope pointer\nr1: Sound envelope parameters pointer",
    )

    SoundEnvelope_SetSlide = Symbol(
        None,
        None,
        None,
        "r0: Sound envelope pointer\nr1: Target volume\nr2: Music duration lookup table index",
    )

    UpdateTrackVolumeEnvelopes = Symbol(
        None,
        None,
        None,
        "From https://projectpokemon.org/docs/mystery-dungeon-nds/procyon-studios-digital-sound-elements-r12/\n\nr0: Sound envelope pointer",
    )

    SoundEnvelope_Release = Symbol(None, None, None, "r0: Sound envelope pointer")

    SoundEnvelope_Stop = Symbol(None, None, None, "r0: Sound envelope pointer")

    SoundEnvelope_ForceVolume = Symbol(
        None, None, None, "r0: Sound envelope pointer\nr1: Volume"
    )

    SoundEnvelope_Stop2 = Symbol(None, None, None, "r0: Sound envelope pointer")

    SoundEnvelope_Tick = Symbol(
        None, None, None, "r0: Sound envelope pointer\nreturn: Current volume"
    )

    SoundLfoBank_Reset = Symbol(None, None, None, "r0: LFO bank pointer")

    SoundLfoBank_Set = Symbol(
        None,
        None,
        None,
        "r0: LFO bank pointer\nr1: LFO settings pointer\nr2: Envelope level",
    )

    SoundLfoBank_SetConstEnvelopes = Symbol(
        None, None, None, "r0: LFO bank pointer\nr1: Level"
    )

    SoundLfoBank_Tick = Symbol(
        None, None, None, "r0: LFO bank pointer\nreturn: New voice update flags"
    )

    SoundLfoWave_InvalidFunc = Symbol(None, None, None, "r0: LFO pointer\nreturn: 0")

    SoundLfoWave_HalfSquareFunc = Symbol(
        None, None, None, "r0: LFO pointer\nreturn: LFO current output"
    )

    SoundLfoWave_FullSquareFunc = Symbol(
        None, None, None, "r0: LFO pointer\nreturn: LFO current output"
    )

    SoundLfoWave_HalfTriangleFunc = Symbol(
        None, None, None, "r0: LFO pointer\nreturn: LFO current output"
    )

    SoundLfoWave_FullTriangleFunc = Symbol(
        None, None, None, "r0: LFO pointer\nreturn: LFO current output"
    )

    SoundLfoWave_SawFunc = Symbol(
        None, None, None, "r0: LFO pointer\nreturn: LFO current output"
    )

    SoundLfoWave_ReverseSawFunc = Symbol(
        None, None, None, "r0: LFO pointer\nreturn: LFO current output"
    )

    SoundLfoWave_HalfNoiseFunc = Symbol(
        None, None, None, "r0: LFO pointer\nreturn: LFO current output"
    )

    SoundLfoWave_FullNoiseFunc = Symbol(
        None, None, None, "r0: LFO pointer\nreturn: LFO current output"
    )

    Crypto_RC4Init = Symbol(None, None, None, "")

    Mtx_LookAt = Symbol(None, None, None, "")

    Mtx_OrthoW = Symbol(None, None, None, "")

    FX_Div = Symbol(None, None, None, "")

    FX_GetDivResultFx64c = Symbol(None, None, None, "")

    FX_GetDivResult = Symbol(None, None, None, "")

    FX_InvAsync = Symbol(None, None, None, "")

    FX_DivAsync = Symbol(None, None, None, "")

    FX_DivS32 = Symbol(None, None, None, "")

    FX_ModS32 = Symbol(None, None, None, "")

    Vec_DotProduct = Symbol(None, None, None, "")

    Vec_CrossProduct = Symbol(None, None, None, "")

    Vec_Normalize = Symbol(None, None, None, "")

    Vec_Distance = Symbol(None, None, None, "")

    FX_Atan2Idx = Symbol(None, None, None, "")

    GX_Init = Symbol(None, None, None, "")

    GX_HBlankIntr = Symbol(None, None, None, "")

    GX_VBlankIntr = Symbol(None, None, None, "")

    GX_DispOff = Symbol(None, None, None, "")

    GX_DispOn = Symbol(None, None, None, "")

    GX_SetGraphicsMode = Symbol(None, None, None, "")

    Gxs_SetGraphicsMode = Symbol(None, None, None, "")

    GXx_SetMasterBrightness = Symbol(None, None, None, "")

    GX_InitGxState = Symbol(None, None, None, "")

    EnableVramBanksInSetDontSave = Symbol(
        None,
        None,
        None,
        "Enable the VRAM bank marked in the input set, but don’t mark them as enabled in ENABLED_VRAM_BANKS\n\nr0: vram_banks_set",
    )

    GX_SetBankForBg = Symbol(None, None, None, "")

    GX_SetBankForObj = Symbol(None, None, None, "")

    GX_SetBankForBgExtPltt = Symbol(None, None, None, "")

    GX_SetBankForObjExtPltt = Symbol(None, None, None, "")

    GX_SetBankForTex = Symbol(None, None, None, "")

    GX_SetBankForTexPltt = Symbol(None, None, None, "")

    GX_SetBankForClearImage = Symbol(None, None, None, "")

    GX_SetBankForArm7 = Symbol(None, None, None, "")

    GX_SetBankForLcdc = Symbol(None, None, None, "")

    GX_SetBankForSubBg = Symbol(None, None, None, "")

    GX_SetBankForSubObj = Symbol(None, None, None, "")

    GX_SetBankForSubBgExtPltt = Symbol(None, None, None, "")

    GX_SetBankForSubObjExtPltt = Symbol(None, None, None, "")

    EnableVramBanksInSet = Symbol(
        None,
        None,
        None,
        "Enable the VRAM banks in the input set. Will reset the pointed set to 0, and update ENABLED_VRAM_BANKS\n\nr0: vram_banks_set *",
    )

    GX_ResetBankForBgExtPltt = Symbol(None, None, None, "")

    GX_ResetBankForObjExtPltt = Symbol(None, None, None, "")

    GX_ResetBankForTex = Symbol(None, None, None, "")

    GX_ResetBankForTexPltt = Symbol(None, None, None, "")

    GX_ResetBankForSubBgExtPltt = Symbol(None, None, None, "")

    GX_ResetBankForSubObjExtPltt = Symbol(None, None, None, "")

    DisableBankForX = Symbol(None, None, None, "")

    GX_DisableBankForBg = Symbol(None, None, None, "")

    GX_DisableBankForObj = Symbol(None, None, None, "")

    GX_DisableBankForBgExtPltt = Symbol(None, None, None, "")

    GX_DisableBankForObjExtPltt = Symbol(None, None, None, "")

    GX_DisableBankForTex = Symbol(None, None, None, "")

    GX_DisableBankForTexPltt = Symbol(None, None, None, "")

    GX_DisableBankForClearImage = Symbol(None, None, None, "")

    GX_DisableBankForArm7 = Symbol(None, None, None, "")

    GX_DisableBankForLcdc = Symbol(None, None, None, "")

    GX_DisableBankForSubBg = Symbol(None, None, None, "")

    GX_DisableBankForSubObj = Symbol(None, None, None, "")

    GX_DisableBankForSubBgExtPltt = Symbol(None, None, None, "")

    GX_DisableBankForSubObjExtPltt = Symbol(None, None, None, "")

    G2_GetBG0ScrPtr = Symbol(None, None, None, "")

    G2S_GetBG0ScrPtr = Symbol(None, None, None, "")

    G2_GetBG1ScrPtr = Symbol(None, None, None, "")

    G2S_GetBG1ScrPtr = Symbol(None, None, None, "")

    G2_GetBG2ScrPtr = Symbol(None, None, None, "")

    G2_GetBG3ScrPtr = Symbol(None, None, None, "")

    G2_GetBG0CharPtr = Symbol(None, None, None, "")

    G2S_GetBG0CharPtr = Symbol(None, None, None, "")

    G2_GetBG1CharPtr = Symbol(None, None, None, "")

    G2S_GetBG1CharPtr = Symbol(None, None, None, "")

    G2_GetBG2CharPtr = Symbol(None, None, None, "")

    G2_GetBG3CharPtr = Symbol(None, None, None, "")

    G2x_SetBlendAlpha = Symbol(None, None, None, "")

    G2x_SetBlendBrightness = Symbol(None, None, None, "")

    G2x_ChangeBlendBrightness = Symbol(None, None, None, "")

    G3_LoadMtx44 = Symbol(None, None, None, "")

    G3_LoadMtx43 = Symbol(
        None,
        None,
        None,
        "Send the MTX_LOAD_4x3 geometry engine command, through a GXFIFO command. See https://problemkaputt.de/gbatek.htm#ds3dgeometrycommands and https://problemkaputt.de/gbatek.htm#ds3dmatrixloadmultiply for more information.\n\nThis pops the top of the current matrix stack (https://problemkaputt.de/gbatek.htm#ds3dmatrixstack) and sets it as the engine's 'current' matrix. It's commonly preceded by a MTX_PUSH command to populate the matrix stack with a matrix.\n\nr0: matrix_4x3 pointer",
    )

    G3_MultMtx43 = Symbol(
        None,
        None,
        None,
        "Send the MTX_MULT_4x3 geometry engine command, through a GXFIFO command. See https://problemkaputt.de/gbatek.htm#ds3dgeometrycommands and https://problemkaputt.de/gbatek.htm#ds3dmatrixloadmultiply for more information.\n\nThis pops the top of the current matrix stack (https://problemkaputt.de/gbatek.htm#ds3dmatrixstack) and left-multiplies the engine's 'current' matrix by the new matrix. It's commonly preceded by a MTX_PUSH command to populate the matrix stack with a matrix.\n\nr0: matrix_4x3 pointer",
    )

    G3X_Init = Symbol(None, None, None, "")

    G3X_Reset = Symbol(None, None, None, "")

    G3X_ClearFifo = Symbol(None, None, None, "")

    G3X_InitMtxStack = Symbol(None, None, None, "")

    G3X_ResetMtxStack = Symbol(None, None, None, "")

    G3X_SetClearColor = Symbol(None, None, None, "")

    G3X_InitTable = Symbol(None, None, None, "")

    G3X_GetMtxStackLevelPV = Symbol(None, None, None, "")

    G3X_GetMtxStackLevelPJ = Symbol(None, None, None, "")

    GXi_NopClearFifo128 = Symbol(None, None, None, "")

    G3i_OrthoW = Symbol(None, None, None, "")

    G3i_LookAt = Symbol(None, None, None, "")

    GX_LoadBgPltt = Symbol(None, None, None, "")

    Gxs_LoadBgPltt = Symbol(None, None, None, "")

    GX_LoadObjPltt = Symbol(None, None, None, "")

    Gxs_LoadObjPltt = Symbol(None, None, None, "")

    GX_LoadOam = Symbol(None, None, None, "")

    Gxs_LoadOam = Symbol(None, None, None, "")

    GX_LoadObj = Symbol(None, None, None, "")

    Gxs_LoadObj = Symbol(None, None, None, "")

    GX_LoadBg0Scr = Symbol(None, None, None, "")

    GX_LoadBg1Scr = Symbol(None, None, None, "")

    Gxs_LoadBg1Scr = Symbol(None, None, None, "")

    GX_LoadBg2Scr = Symbol(None, None, None, "")

    GX_LoadBg3Scr = Symbol(None, None, None, "")

    GX_LoadBg0Char = Symbol(None, None, None, "")

    Gxs_LoadBg0Char = Symbol(None, None, None, "")

    GX_LoadBg1Char = Symbol(None, None, None, "")

    Gxs_LoadBg1Char = Symbol(None, None, None, "")

    GX_LoadBg2Char = Symbol(None, None, None, "")

    GX_LoadBg3Char = Symbol(None, None, None, "")

    GX_BeginLoadBgExtPltt = Symbol(None, None, None, "")

    GX_EndLoadBgExtPltt = Symbol(None, None, None, "")

    GX_BeginLoadObjExtPltt = Symbol(None, None, None, "")

    GX_EndLoadObjExtPltt = Symbol(None, None, None, "")

    Gxs_BeginLoadBgExtPltt = Symbol(None, None, None, "")

    Gxs_EndLoadBgExtPltt = Symbol(None, None, None, "")

    Gxs_BeginLoadObjExtPltt = Symbol(None, None, None, "")

    Gxs_EndLoadObjExtPltt = Symbol(None, None, None, "")

    GX_BeginLoadTex = Symbol(None, None, None, "")

    GX_LoadTex = Symbol(None, None, None, "")

    GX_EndLoadTex = Symbol(None, None, None, "")

    GX_BeginLoadTexPltt = Symbol(None, None, None, "")

    GX_LoadTexPltt = Symbol(None, None, None, "")

    GX_EndLoadTexPltt = Symbol(None, None, None, "")

    GeomGxFifoSendMtx4x3 = Symbol(
        None,
        None,
        None,
        "Send a 4x3 matrix argument for a GXFIFO geometry engine command.\n\nThis function is used by GeomMtxLoad4x3 and GeomMtxMult4x3 to pass the matrix argument for a GXFIFO command after already having written the command code. See https://problemkaputt.de/gbatek.htm#ds3dgeometrycommands for more information.\n\nNote that the GXFIFO address is 0x4000400, but is (maybe) mirrored up to 0x400043F. This function is optimized to take advantage of this by writing 3 matrix entries at a time using ldmia and stmia instructions.\n\nr0: matrix_4x3 pointer\nr1: GXFIFO pointer",
    )

    GX_SendFifo64B = Symbol(None, None, None, "")

    OS_GetLockID = Symbol(None, None, None, "")

    IncrementThreadCount = Symbol(
        None,
        None,
        None,
        "Increments thread_info::thread_count by 1 and returns the new value.\n\nreturn: New thread count",
    )

    InsertThreadIntoList = Symbol(
        None,
        None,
        None,
        "Inserts a new thread into the linked thread list (see thread_info::thread_list_head).\n\nThe thread is inserted in sorted order.\n\nr0: Thread to insert",
    )

    StartThread = Symbol(
        None,
        None,
        None,
        "Called to start a new thread.\n\nInitializes the specified thread struct and some values on its stack area.\n\nr0: Struct of the thread to init\nr1: Pointer to the function to run on this thread\nr2: Pointer to a thread struct. Sometimes equal to r0. Sometimes null.\nr3: Pointer to the stack area for this thread. Not all the space is usable. See thread::usable_stack_pointer for more info.\nstack[0]: Stack size\nstack[1]: (?) Used to sort threads on a list",
    )

    ThreadExit = Symbol(
        None,
        None,
        None,
        "Function called by threads on exit.\n\nBase functions that contain an infinite loop that is not supposed to return and that have their stacks in main RAM have this function as their return address.\n\nNo params.",
    )

    SetThreadField0xB4 = Symbol(
        None,
        None,
        None,
        "Sets the given thread's field_0xB4 to the specified value.\n\nr0: Thread\nr1: Value to set",
    )

    InitThread = Symbol(
        None,
        None,
        None,
        "Initializes some fields of the given thread struct.\n\nMost notably, thread::flags, thread::function_address_plus_4, thread::stack_pointer_minus_4 and thread::usable_stack_pointer. Also initializes a few more fields with a value of 0.\nthread::flags is initialized to 0x1F, unless the address of the function is odd (???), in which case it's initialized to 0x3F.\n\nr0: Pointer to the thread to initialize\nr1: Pointer to the function the thread will run\nr2: Pointer to the start of the thread's stack area - 4",
    )

    GetTimer0Control = Symbol(
        None,
        None,
        None,
        "Returns the value of the control register for hardware timer 0\n\nreturn: Value of the control register",
    )

    ClearIrqFlag = Symbol(
        None,
        None,
        None,
        "Enables processor interrupts by clearing the i flag in the program status register (cpsr).\n\nreturn: Old value of cpsr & 0x80 (0x80 if interrupts were disabled, 0x0 if they were already enabled)",
    )

    EnableIrqFlag = Symbol(
        None,
        None,
        None,
        "Disables processor interrupts by setting the i flag in the program status register (cpsr).\n\nreturn: Old value of cpsr & 0x80 (0x80 if interrupts were already disabled, 0x0 if they were enabled)",
    )

    SetIrqFlag = Symbol(
        None,
        None,
        None,
        "Sets the value of the processor's interrupt flag according to the specified parameter.\n\nr0: Value to set the flag to (0x80 to set it, which disables interrupts; 0x0 to unset it, which enables interrupts)\nreturn: Old value of cpsr & 0x80 (0x80 if interrupts were disabled, 0x0 if they were enabled)",
    )

    EnableIrqFiqFlags = Symbol(
        None,
        None,
        None,
        "Disables processor all interrupts (both standard and fast) by setting the i and f flags in the program status register (cpsr).\n\nreturn: Old value of cpsr & 0xC0 (contains the previous values of the i and f flags)",
    )

    SetIrqFiqFlags = Symbol(
        None,
        None,
        None,
        "Sets the value of the processor's interrupt flags (i and f) according to the specified parameter.\n\nr0: Value to set the flags to (0xC0 to set both flags, 0x80 to set the i flag and clear the f flag, 0x40 to set the f flag and clear the i flag and 0x0 to clear both flags)\nreturn: Old value of cpsr & 0xC0 (contains the previous values of the i and f flags)",
    )

    GetIrqFlag = Symbol(
        None,
        None,
        None,
        "Gets the current value of the processor's interrupt request (i) flag\n\nreturn: cpsr & 0x80 (0x80 if interrupts are disabled, 0x0 if they are enabled)",
    )

    GetProcessorMode = Symbol(
        None,
        None,
        None,
        "Gets the processor's current operating mode.\n\nSee https://problemkaputt.de/gbatek.htm#armcpuflagsconditionfieldcond\n\nreturn: cpsr & 0x1f (the cpsr mode bits M4-M0)",
    )

    CountLeadingZeros = Symbol(
        None,
        None,
        None,
        "Counts the number of leading zeros in a 32-bit integer.\n\nr0: x\nreturn: clz(x)",
    )

    WaitForever2 = Symbol(
        None,
        None,
        None,
        "Calls EnableIrqFlag and WaitForInterrupt in an infinite loop.\n\nThis is called on fatal errors to hang the program indefinitely.\n\nNo params.",
    )

    WaitForInterrupt = Symbol(
        None,
        None,
        None,
        "Presumably blocks until the program receives an interrupt.\n\nThis just calls (in Ghidra terminology) coproc_moveto_Wait_for_interrupt(0). See https://en.wikipedia.org/wiki/ARM_architecture_family#Coprocessors.\n\nNo params.",
    )

    ArrayFill16 = Symbol(
        None,
        None,
        None,
        "Fills an array of 16-bit values with a given value.\n\nr0: value\nr1: ptr\nr2: len (# bytes)",
    )

    ArrayCopy16 = Symbol(
        None,
        None,
        None,
        "Copies an array of 16-bit values to another array of 16-bit values.\n\nThis is essentially an alternate implementation of Memcpy16, but with a different parameter order.\n\nr0: src\nr1: dest\nr2: len (# bytes)",
    )

    ArrayFill32 = Symbol(
        None,
        None,
        None,
        "Fills an array of 32-bit values with a given value.\n\nThis is essentially an alternate implementation of Memset32, but with a different parameter order.\n\nr0: value\nr1: ptr\nr2: len (# bytes)",
    )

    ArrayCopy32 = Symbol(
        None,
        None,
        None,
        "Copies an array of 32-bit values to another array of 32-bit values.\n\nThis is essentially an alternate implementation of Memcpy32, but with a different parameter order.\n\nr0: src\nr1: dest\nr2: len (# bytes)",
    )

    ArrayFill32Fast = Symbol(
        None,
        None,
        None,
        "Does the same thing as ArrayFill32, except the implementation uses an unrolled loop that sets 8 values per iteration, taking advantage of the stmia instruction.\n\nr0: value\nr1: ptr\nr2: len (# bytes)",
    )

    ArrayCopy32Fast = Symbol(
        None,
        None,
        None,
        "Does the same thing as ArrayCopy32, except the implementation uses an unrolled loop that copies 8 values per iteration, taking advantage of the ldmia/stmia instructions.\n\nr0: src\nr1: dest\nr2: len (# bytes)",
    )

    MemsetFast = Symbol(
        None,
        None,
        None,
        "A semi-optimized implementation of the memset(3) C library function.\n\nThis function was probably manually implemented by the developers, or was included as part of a library other than libc (the Nitro SDK probably?). See memset for what's probably the real libc function.\n\nThis function is optimized to set values in 4-byte chunks, properly dealing with pointer alignment. However, unlike the libc memset, there are no loop unrolling optimizations.\n\nr0: ptr\nr1: value\nr2: len (# bytes)",
    )

    MemcpyFast = Symbol(
        None,
        None,
        None,
        "Copies bytes from one buffer to another, similar to memcpy(3). Note that the source/destination buffer parameters swapped relative to the standard memcpy.\n\nThis function was probably manually implemented by the developers, or was included as part of a library other than libc (the Nitro SDK probably?). See memcpy for what's probably the real libc function.\n\nThis function is optimized to copy values in 4-byte chunks, properly dealing with pointer alignment.\n\nr0: src\nr1: dest\nr2: n (# bytes)",
    )

    AtomicExchange = Symbol(
        None,
        None,
        None,
        "Atomically replaces a pointer's pointee with a desired value, and returns the previous value.\n\nThis function is just a single swp instruction.\n\nr0: desired value\nr1: ptr\nreturn: previous value",
    )

    FileInit = Symbol(
        None,
        None,
        None,
        "Initializes a file_stream structure for file I/O.\n\nThis function must always be called before opening a file.\n\nr0: file_stream pointer",
    )

    GetOverlayInfo = Symbol(
        None,
        None,
        None,
        "Returns the y9.bin entry for the specified overlay\n\nr0: [output] Overlay info struct\nr1: ?\nr2: Overlay ID\nreturn: True if the entry could be loaded successfully?",
    )

    LoadOverlayInternal = Symbol(
        None,
        None,
        None,
        "Called by LoadOverlay to load an overlay into RAM given its info struct\n\nr0: Overlay info struct\nReturn: True if the overlay was loaded successfully?",
    )

    InitOverlay = Symbol(
        None,
        None,
        None,
        "Performs overlay initialization right after loading an overlay with LoadOverlayInternal.\n\nThis function is responsible for jumping to all the pointers located in the overlay's static init array, among other things.\n\nr0: Overlay info struct",
    )

    abs = Symbol(
        None,
        None,
        None,
        "Takes the absolute value of an integer.\n\nr0: x\nreturn: abs(x)",
    )

    mbtowc = Symbol(
        None,
        None,
        None,
        "The mbtowc(3) C library function.\n\nr0: pwc\nr1: s\nr2: n\nreturn: number of consumed bytes, or -1 on failure",
    )

    TryAssignByte = Symbol(
        None,
        None,
        None,
        "Assign a byte to the target of a pointer if the pointer is non-null.\n\nr0: pointer\nr1: value\nreturn: true on success, false on failure",
    )

    TryAssignByteWrapper = Symbol(
        None,
        None,
        None,
        "Wrapper around TryAssignByte.\n\nAccesses the TryAssignByte function with a weird chain of pointer dereferences.\n\nr0: pointer\nr1: value\nreturn: true on success, false on failure",
    )

    wcstombs = Symbol(
        None,
        None,
        None,
        "The wcstombs(3) C library function.\n\nr0: dest\nr1: src\nr2: n\nreturn: characters converted",
    )

    memcpy = Symbol(
        None,
        None,
        None,
        "The memcpy(3) C library function.\n\nr0: dest\nr1: src\nr2: n\nreturn: dest",
    )

    memmove = Symbol(
        None,
        None,
        None,
        "The memmove(3) C library function.\n\nThe implementation is nearly the same as memcpy, but it copies bytes from back to front if src < dst.\n\nr0: dest\nr1: src\nr2: n\nreturn: dest",
    )

    memset = Symbol(
        None,
        None,
        None,
        "The memset(3) C library function.\n\nThis is just a wrapper around memset_internal that returns the pointer at the end.\n\nr0: s\nr1: c (int, but must be a single-byte value)\nr2: n\nreturn: s",
    )

    memchr = Symbol(
        None,
        None,
        None,
        "The memchr(3) C library function.\n\nr0: s\nr1: c\nr2: n\nreturn: pointer to first occurrence of c in s, or a null pointer if no match",
    )

    memcmp = Symbol(
        None,
        None,
        None,
        "The memcmp(3) C library function.\n\nr0: s1\nr1: s2\nr2: n\nreturn: comparison value",
    )

    memset_internal = Symbol(
        None,
        None,
        None,
        "The actual memory-setting implementation for the memset(3) C library function.\n\nThis function is optimized to set bytes in 4-byte chunks for n >= 32, correctly handling any unaligned bytes at the front/back. In this case, it also further optimizes by unrolling a for loop to set 8 4-byte values at once (effectively a 32-byte chunk).\n\nr0: s\nr1: c (int, but must be a single-byte value)\nr2: n",
    )

    __vsprintf_internal_slice = Symbol(
        None,
        None,
        None,
        "This is what implements the bulk of __vsprintf_internal.\n\nThe __vsprintf_internal in the modern-day version of glibc relies on __vfprintf_internal; this function has a slightly different interface, but it serves a similar role.\n\nr0: function pointer to append to the string being built (__vsprintf_internal uses TryAppendToSlice)\nr1: string buffer slice\nr2: format\nr3: ap\nreturn: number of characters printed, excluding the null-terminator",
    )

    TryAppendToSlice = Symbol(
        None,
        None,
        None,
        "Best-effort append the given data to a slice. If the slice's capacity is reached, any remaining data will be truncated.\n\nr0: slice pointer\nr1: buffer of data to append\nr2: number of bytes in the data buffer\nreturn: true",
    )

    __vsprintf_internal = Symbol(
        None,
        None,
        None,
        "This is what implements vsprintf. It's akin to __vsprintf_internal in the modern-day version of glibc (in fact, it's probably an older version of this).\n\nr0: str\nr1: maxlen (vsprintf passes UINT32_MAX for this)\nr2: format\nr3: ap\nreturn: number of characters printed, excluding the null-terminator",
    )

    vsprintf = Symbol(
        None,
        None,
        None,
        "The vsprintf(3) C library function.\n\nr0: str\nr1: format\nr2: ap\nreturn: number of characters printed, excluding the null-terminator",
    )

    snprintf = Symbol(
        None,
        None,
        None,
        "The snprintf(3) C library function.\n\nThis calls __vsprintf_internal directly, so it's presumably the real snprintf.\n\nr0: str\nr1: n\nr2: format\n...: variadic\nreturn: number of characters printed, excluding the null-terminator",
    )

    sprintf = Symbol(
        None,
        None,
        None,
        "The sprintf(3) C library function.\n\nThis calls __vsprintf_internal directly, so it's presumably the real sprintf.\n\nr0: str\nr1: format\n...: variadic\nreturn: number of characters printed, excluding the null-terminator",
    )

    strlen = Symbol(
        None,
        None,
        None,
        "The strlen(3) C library function.\n\nr0: s\nreturn: length of s",
    )

    strcpy = Symbol(
        None,
        None,
        None,
        "The strcpy(3) C library function.\n\nThis function is optimized to copy characters in aligned 4-byte chunks if possible, correctly handling any unaligned bytes at the front/back.\n\nr0: dest\nr1: src\nreturn: dest",
    )

    strncpy = Symbol(
        None,
        None,
        None,
        "The strncpy(3) C library function.\n\nr0: dest\nr1: src\nr2: n\nreturn: dest",
    )

    strcat = Symbol(
        None,
        None,
        None,
        "The strcat(3) C library function.\n\nr0: dest\nr1: src\nreturn: dest",
    )

    strncat = Symbol(
        None,
        None,
        None,
        "The strncat(3) C library function.\n\nr0: dest\nr1: src\nr2: n\nreturn: dest",
    )

    strcmp = Symbol(
        None,
        None,
        None,
        "The strcmp(3) C library function.\n\nSimilarly to strcpy, this function is optimized to compare characters in aligned 4-byte chunks if possible.\n\nr0: s1\nr1: s2\nreturn: comparison value",
    )

    strncmp = Symbol(
        None,
        None,
        None,
        "The strncmp(3) C library function.\n\nr0: s1\nr1: s2\nr2: n\nreturn: comparison value",
    )

    strchr = Symbol(
        None,
        None,
        None,
        "The strchr(3) C library function.\n\nr0: string\nr1: c\nreturn: pointer to the located byte c, or null pointer if no match",
    )

    strcspn = Symbol(
        None,
        None,
        None,
        "The strcspn(3) C library function.\n\nr0: string\nr1: stopset\nreturn: offset of the first character in string within stopset",
    )

    strstr = Symbol(
        None,
        None,
        None,
        "The strstr(3) C library function.\n\nr0: haystack\nr1: needle\nreturn: pointer into haystack where needle starts, or null pointer if no match",
    )

    wcslen = Symbol(
        None,
        None,
        None,
        "The wcslen(3) C library function.\n\nr0: ws\nreturn: length of ws",
    )

    _dadd = Symbol(
        None,
        None,
        None,
        "Implements the addition operator for IEEE 754 double-precision floating-point numbers.\n\nThe result is returned in r0 and r1, in accordance with the Procedure Call Standard for the Arm Architecture (see https://github.com/ARM-software/abi-aa/blob/60a8eb8c55e999d74dac5e368fc9d7e36e38dda4/aapcs32/aapcs32.rst#result-return).\n\nAnalogous to __adddf3 in libgcc.\n\nr0: a (low bits)\nr1: a (high bits)\nr2: b (low bits)\nr3: b (high bits)\nreturn: a + b",
    )

    _d2f = Symbol(
        None,
        None,
        None,
        "Implements the double to float cast operator for IEEE 754 floating-point numbers.\n\nAnalogous to __truncdfsf2 in libgcc.\n\nr0: double (low bits)\nr1: double (high bits)\nreturn: (float)double",
    )

    _ll_ufrom_d = Symbol(
        None,
        None,
        None,
        "Implements the double to unsigned long long cast operation for IEEE 754 floating-point numbers.\n\nThe result is returned in r0 and r1, in accordance with the Procedure Call Standard for the Arm Architecture (see https://github.com/ARM-software/abi-aa/blob/60a8eb8c55e999d74dac5e368fc9d7e36e38dda4/aapcs32/aapcs32.rst#result-return).\n\nAnalogous to __fixunsdfti in libgcc.\n\nr0: double (low bits)\nr1: double (high bits)\nreturn: (unsigned long long)double",
    )

    _dflt = Symbol(
        None,
        None,
        None,
        "Implements the int to double cast operation for IEEE 754 floating-point numbers.\n\nThe result is returned in r0 and r1, in accordance with the Procedure Call Standard for the Arm Architecture (see https://github.com/ARM-software/abi-aa/blob/60a8eb8c55e999d74dac5e368fc9d7e36e38dda4/aapcs32/aapcs32.rst#result-return).\n\nAnalogous to __floatsidf in libgcc.\n\nr0: int\nreturn: (double)int",
    )

    _dfltu = Symbol(
        None,
        None,
        None,
        "Implements the unsigned int to double cast operation for IEEE 754 floating-point numbers.\n\nThe result is returned in r0 and r1, in accordance with the Procedure Call Standard for the Arm Architecture (see https://github.com/ARM-software/abi-aa/blob/60a8eb8c55e999d74dac5e368fc9d7e36e38dda4/aapcs32/aapcs32.rst#result-return).\n\nAnalogous to __floatunsidf in libgcc.\n\nr0: uint\nreturn: (double)uint",
    )

    _dmul = Symbol(
        None,
        None,
        None,
        "Implements the multiplication operator for IEEE 754 double-precision floating-point numbers.\n\nThe result is returned in r0 and r1, in accordance with the Procedure Call Standard for the Arm Architecture (see https://github.com/ARM-software/abi-aa/blob/60a8eb8c55e999d74dac5e368fc9d7e36e38dda4/aapcs32/aapcs32.rst#result-return).\n\nAnalogous to __muldf3 in libgcc.\n\nr0: a (low bits)\nr1: a (high bits)\nr2: b (low bits)\nr3: b (high bits)\nreturn: a * b",
    )

    _dsqrt = Symbol(
        None,
        None,
        None,
        "Analogous to the sqrt(3) C library function.\n\nThe result is returned in r0 and r1, in accordance with the Procedure Call Standard for the Arm Architecture (see https://github.com/ARM-software/abi-aa/blob/60a8eb8c55e999d74dac5e368fc9d7e36e38dda4/aapcs32/aapcs32.rst#result-return).\n\nr0: x (low bits)\nr1: x (high bits)\nreturn: sqrt(x)",
    )

    _dsub = Symbol(
        None,
        None,
        None,
        "Implements the subtraction operator for IEEE 754 double-precision floating-point numbers.\n\nThe result is returned in r0 and r1, in accordance with the Procedure Call Standard for the Arm Architecture (see https://github.com/ARM-software/abi-aa/blob/60a8eb8c55e999d74dac5e368fc9d7e36e38dda4/aapcs32/aapcs32.rst#result-return).\n\nAnalogous to __subdf3 in libgcc.\n\nr0: a (low bits)\nr1: a (high bits)\nr2: b (low bits)\nr3: b (high bits)\nreturn: a - b",
    )

    _fadd = Symbol(
        None,
        None,
        None,
        "Implements the addition operator for IEEE 754 floating-point numbers.\n\nAnalogous to __addsf3 in libgcc.\n\nr0: a\nr1: b\nreturn: a + b",
    )

    _dgeq = Symbol(
        None,
        None,
        None,
        "Implements the >= operator for IEEE 754 double-precision floating-point numbers.\n\nr0: a (low bits)\nr1: a (high bits)\nr2: b (low bits)\nr3: b (high bits)\nreturn: a >= b",
    )

    _dleq = Symbol(
        None,
        None,
        None,
        "Implements the <= operator for IEEE 754 double-precision floating-point numbers.\n\nr0: a (low bits)\nr1: a (high bits)\nr2: b (low bits)\nr3: b (high bits)\nreturn: a <= b",
    )

    _dls = Symbol(
        None,
        None,
        None,
        "Implements the < operator for IEEE 754 double-precision floating-point numbers.\n\nr0: a (low bits)\nr1: a (high bits)\nr2: b (low bits)\nr3: b (high bits)\nreturn: a < b",
    )

    _deq = Symbol(
        None,
        None,
        None,
        "Implements the == operator for IEEE 754 double-precision floating-point numbers.\n\nr0: a (low bits)\nr1: a (high bits)\nr2: b (low bits)\nr3: b (high bits)\nreturn: a == b",
    )

    _dneq = Symbol(
        None,
        None,
        None,
        "Implements the != operator for IEEE 754 double-precision floating-point numbers.\n\nr0: a (low bits)\nr1: a (high bits)\nr2: b (low bits)\nr3: b (high bits)\nreturn: a != b",
    )

    _fls = Symbol(
        None,
        None,
        None,
        "Implements the < operator for IEEE 754 floating-point numbers.\n\nr0: a\nr1: b\nreturn: a < b",
    )

    _fdiv = Symbol(
        None,
        None,
        None,
        "Implements the division operator for IEEE 754 floating-point numbers.\n\nAnalogous to __divsf3 in libgcc.\n\nr0: dividend\nr1: divisor\nreturn: dividend / divisor",
    )

    _f2d = Symbol(
        None,
        None,
        None,
        "Implements the float to double cast operation for IEEE 754 floating-point numbers.\n\nAnalogous to __extendsfdf2 in libgcc.\n\nThe result is returned in r0 and r1, in accordance with the Procedure Call Standard for the Arm Architecture (see https://github.com/ARM-software/abi-aa/blob/60a8eb8c55e999d74dac5e368fc9d7e36e38dda4/aapcs32/aapcs32.rst#result-return).\n\nr0: float\nreturn: (double)float",
    )

    _ffix = Symbol(
        None,
        None,
        None,
        "Implements the float to int cast operation for IEEE 754 floating-point numbers. The output saturates if the input is out of the representable range for the int type.\n\nAnalogous to __fixsfsi in libgcc.\n\nr0: float\nreturn: (int)float",
    )

    _fflt = Symbol(
        None,
        None,
        None,
        "Implements the int to float cast operation for IEEE 754 floating-point numbers.\n\nAnalogous to __floatsisf in libgcc.\n\nr0: int\nreturn: (float)int",
    )

    _ffltu = Symbol(
        None,
        None,
        None,
        "Implements the unsigned int to float cast operation for IEEE 754 floating-point numbers.\n\nAnalogous to __floatunsisf in libgcc.\n\nr0: uint\nreturn: (float)uint",
    )

    _fmul = Symbol(
        None,
        None,
        None,
        "Implements the multiplication operator for IEEE 754 floating-point numbers.\n\nAnalogous to __mulsf3 in libgcc.\n\nr0: a\nr1: b\nreturn: a * b",
    )

    sqrtf = Symbol(
        None, None, None, "The sqrtf(3) C library function.\n\nr0: x\nreturn: sqrt(x)"
    )

    _fsub = Symbol(
        None,
        None,
        None,
        "Implements the subtraction operator for IEEE 754 floating-point numbers.\n\nAnalogous to __subsf3 in libgcc.\n\nr0: a\nr1: b\nreturn: a - b",
    )

    _ll_mod = Symbol(
        None,
        None,
        None,
        "Implements the modulus operator for signed long longs.\n\nThe result is returned in r0 and r1, in accordance with the Procedure Call Standard for the Arm Architecture (see https://github.com/ARM-software/abi-aa/blob/60a8eb8c55e999d74dac5e368fc9d7e36e38dda4/aapcs32/aapcs32.rst#result-return).\n\nAnalogous to __modti3 in libgcc.\n\nr0: dividend (low bits)\nr1: dividend (high bits)\nr2: divisor (low bits)\nr3: divisor (high bits)\nreturn: dividend % divisor",
    )

    _ll_sdiv = Symbol(
        None,
        None,
        None,
        "Implements the division operator for signed long longs.\n\nThe result is returned in r0 and r1, in accordance with the Procedure Call Standard for the Arm Architecture (see https://github.com/ARM-software/abi-aa/blob/60a8eb8c55e999d74dac5e368fc9d7e36e38dda4/aapcs32/aapcs32.rst#result-return).\n\nAnalogous to __divti3 in libgcc.\n\nr0: dividend (low bits)\nr1: dividend (high bits)\nr2: divisor (low bits)\nr3: divisor (high bits)\nreturn: dividend / divisor",
    )

    _ll_udiv = Symbol(
        None,
        None,
        None,
        "Implements the division operator for unsigned long longs.\n\nThe result is returned in r0 and r1, in accordance with the Procedure Call Standard for the Arm Architecture (see https://github.com/ARM-software/abi-aa/blob/60a8eb8c55e999d74dac5e368fc9d7e36e38dda4/aapcs32/aapcs32.rst#result-return).\n\nAnalogous to __udivti3 in libgcc.\n\nr0: dividend (low bits)\nr1: dividend (high bits)\nr2: divisor (low bits)\nr3: divisor (high bits)\nreturn: dividend / divisor",
    )

    _ull_mod = Symbol(
        None,
        None,
        None,
        "Implements the modulus operator for unsigned long longs.\n\nThe result is returned in r0 and r1, in accordance with the Procedure Call Standard for the Arm Architecture (see https://github.com/ARM-software/abi-aa/blob/60a8eb8c55e999d74dac5e368fc9d7e36e38dda4/aapcs32/aapcs32.rst#result-return).\n\nAnalogous to __umodti3 in libgcc.\n\nr0: dividend (low bits)\nr1: dividend (high bits)\nr2: divisor (low bits)\nr3: divisor (high bits)\nreturn: dividend % divisor",
    )

    _ll_mul = Symbol(
        None,
        None,
        None,
        "Implements the multiplication operator for signed long longs.\n\nThe result is returned in r0 and r1, in accordance with the Procedure Call Standard for the Arm Architecture (see https://github.com/ARM-software/abi-aa/blob/60a8eb8c55e999d74dac5e368fc9d7e36e38dda4/aapcs32/aapcs32.rst#result-return).\n\nAnalogous to __multi3 in libgcc.\n\nr0: a (low bits)\nr1: a (high bits)\nr2: b (low bits)\nr3: b (high bits)\nreturn: a * b",
    )

    _s32_div_f = Symbol(
        None,
        None,
        None,
        "Implements the division operator for signed ints.\n\nAnalogous to __divsi3 in libgcc.\n\nThe return value is a 64-bit integer, with the quotient (dividend / divisor) in the lower 32 bits and the remainder (dividend % divisor) in the upper 32 bits. In accordance with the Procedure Call Standard for the Arm Architecture (see https://github.com/ARM-software/abi-aa/blob/60a8eb8c55e999d74dac5e368fc9d7e36e38dda4/aapcs32/aapcs32.rst#result-return), this means that the quotient is returned in r0 and the remainder is returned in r1.\n\nr0: dividend\nr1: divisor\nreturn: (quotient) | (remainder << 32)",
    )

    _u32_div_f = Symbol(
        None,
        None,
        None,
        "Implements the division operator for unsigned ints.\n\nAnalogous to __udivsi3 in libgcc.\n\nThe return value is a 64-bit integer, with the quotient (dividend / divisor) in the lower 32 bits and the remainder (dividend % divisor) in the upper 32 bits. In accordance with the Procedure Call Standard for the Arm Architecture (see https://github.com/ARM-software/abi-aa/blob/60a8eb8c55e999d74dac5e368fc9d7e36e38dda4/aapcs32/aapcs32.rst#result-return), this means that the quotient is returned in r0 and the remainder is returned in r1.\nNote: This function falls through to _u32_div_not_0_f.\n\nr0: dividend\nr1: divisor\nreturn: (quotient) | (remainder << 32)",
    )

    _u32_div_not_0_f = Symbol(
        None,
        None,
        None,
        "Subsidiary function to _u32_div_f. Skips the initial check for divisor == 0.\n\nThe return value is a 64-bit integer, with the quotient (dividend / divisor) in the lower 32 bits and the remainder (dividend % divisor) in the upper 32 bits. In accordance with the Procedure Call Standard for the Arm Architecture (see https://github.com/ARM-software/abi-aa/blob/60a8eb8c55e999d74dac5e368fc9d7e36e38dda4/aapcs32/aapcs32.rst#result-return), this means that the quotient is returned in r0 and the remainder is returned in r1.\nThis function appears to only be called internally.\n\nr0: dividend\nr1: divisor\nreturn: (quotient) | (remainder << 32)",
    )

    _drdiv = Symbol(
        None,
        None,
        None,
        "The same as _ddiv, but with the parameters reversed.\n\nThis simply swaps the first and second parameters, then falls through to _ddiv.\n\nThe result is returned in r0 and r1, in accordance with the Procedure Call Standard for the Arm Architecture (see https://github.com/ARM-software/abi-aa/blob/60a8eb8c55e999d74dac5e368fc9d7e36e38dda4/aapcs32/aapcs32.rst#result-return).\n\nr0: divisor (low bits)\nr1: divisor (high bits)\nr2: dividend (low bits)\nr3: dividend (high bits)\nreturn: dividend / divisor",
    )

    _ddiv = Symbol(
        None,
        None,
        None,
        "Implements the division operator for IEEE 754 double-precision floating-point numbers.\n\nThe result is returned in r0 and r1, in accordance with the Procedure Call Standard for the Arm Architecture (see https://github.com/ARM-software/abi-aa/blob/60a8eb8c55e999d74dac5e368fc9d7e36e38dda4/aapcs32/aapcs32.rst#result-return).\n\nAnalogous to __divdf3 in libgcc.\n\nr0: dividend (low bits)\nr1: dividend (high bits)\nr2: divisor (low bits)\nr3: divisor (high bits)\nreturn: dividend / divisor",
    )

    _fp_init = Symbol(
        None,
        None,
        None,
        "Meant to do set up for floating point calculations? Does nothing.\n\nNo params.",
    )


class NaItcmLibsData:

    pass


class NaItcmLibsSection:
    name = "libs"
    description = "System libraries linked to the main ARM9 binary.\n\nThis includes code from common NDS system libraries like the Nitro SDK (which contains NDS-specific functionality as well as utilities akin to libc and libgcc).\n\nWhere the library region starts and ends is a guess, but there appear to be fairly sharp boundaries. The function directly before it calls functions at lower memory addresses outside of the region, while all functions in the region only call other functions within the region. The bytes after the region seem to be the start of a global data region, used by both the libraries and the rest of ARM9."
    loadaddress = None
    length = None
    functions = NaItcmLibsFunctions
    data = NaItcmLibsData


class NaItcmMove_effectsFunctions:

    DoMoveDamage = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage.\nRelevant moves: Many!\n\nThis just wraps DealDamage with a multiplier of 1 (i.e., the fixed-point number 0x100).\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether or not damage was dealt",
    )

    DoMoveIronTail = Symbol(
        None,
        None,
        None,
        "Move effect: Iron Tail\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageMultihitUntilMiss = Symbol(
        None,
        None,
        None,
        "Move effect: Deal multihit damage until a strike misses\nRelevant moves: Ice Ball, Rollout\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveYawn = Symbol(
        None,
        None,
        None,
        "Move effect: Yawn\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSleep = Symbol(
        None,
        None,
        None,
        "Move effect: Put target enemies to sleep\nRelevant moves: Lovely Kiss, Sing, Spore, Grasswhistle, Hypnosis, Sleep Powder, Dark Void\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveNightmare = Symbol(
        None,
        None,
        None,
        "Move effect: Nightmare\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveMorningSun = Symbol(
        None,
        None,
        None,
        "Move effect: Morning Sun\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveVitalThrow = Symbol(
        None,
        None,
        None,
        "Move effect: Vital Throw\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDig = Symbol(
        None,
        None,
        None,
        "Move effect: Dig\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSweetScent = Symbol(
        None,
        None,
        None,
        "Move effect: Sweet Scent\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveCharm = Symbol(
        None,
        None,
        None,
        "Move effect: Charm\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveRainDance = Symbol(
        None,
        None,
        None,
        "Move effect: Rain Dance\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveHail = Symbol(
        None,
        None,
        None,
        "Move effect: Hail\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveHealStatus = Symbol(
        None,
        None,
        None,
        "Move effect: Heal the team's status conditions\nRelevant moves: Aromatherapy, Heal Bell, Refresh\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveBubble = Symbol(
        None,
        None,
        None,
        "Move effect: Bubble\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveEncore = Symbol(
        None,
        None,
        None,
        "Move effect: Encore\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveRage = Symbol(
        None,
        None,
        None,
        "Move effect: Rage\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSuperFang = Symbol(
        None,
        None,
        None,
        "Move effect: Super Fang\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMovePainSplit = Symbol(
        None,
        None,
        None,
        "Move effect: Pain Split\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveTorment = Symbol(
        None,
        None,
        None,
        "Move effect: Torment\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveStringShot = Symbol(
        None,
        None,
        None,
        "Move effect: String Shot\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSwagger = Symbol(
        None,
        None,
        None,
        "Move effect: Swagger\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSnore = Symbol(
        None,
        None,
        None,
        "Move effect: Snore\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveScreech = Symbol(
        None,
        None,
        None,
        "Move effect: Screech\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageCringe30 = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage with a 30% chance (ROCK_SLIDE_CRINGE_CHANCE) of inflicting the cringe status on the defender.\nRelevant moves: Rock Slide, Astonish, Iron Head, Dark Pulse, Air Slash, Zen Headbutt, Dragon Rush\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether or not damage was dealt",
    )

    DoMoveWeatherBall = Symbol(
        None,
        None,
        None,
        "Move effect: Weather Ball\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveWhirlpool = Symbol(
        None,
        None,
        None,
        "Move effect: Whirlpool\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveFakeTears = Symbol(
        None,
        None,
        None,
        "Move effect: Fake Tears\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSpite = Symbol(
        None,
        None,
        None,
        "Move effect: Spite\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveFocusEnergy = Symbol(
        None,
        None,
        None,
        "Move effect: Focus Energy\nRelevant moves: Focus Energy, MOVE_TAG_0x1AC\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSmokescreen = Symbol(
        None,
        None,
        None,
        "Move effect: Smokescreen\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveMirrorMove = Symbol(
        None,
        None,
        None,
        "Move effect: Mirror Move\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveOverheat = Symbol(
        None,
        None,
        None,
        "Move effect: Overheat\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveAuroraBeam = Symbol(
        None,
        None,
        None,
        "Move effect: Aurora Beam\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveMemento = Symbol(
        None,
        None,
        None,
        "Move effect: Memento\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveOctazooka = Symbol(
        None,
        None,
        None,
        "Move effect: Octazooka\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveFlatter = Symbol(
        None,
        None,
        None,
        "Move effect: Flatter\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveWillOWisp = Symbol(
        None,
        None,
        None,
        "Move effect: Will-O-Wisp\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveReturn = Symbol(
        None,
        None,
        None,
        "Move effect: Return\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveGrudge = Symbol(
        None,
        None,
        None,
        "Move effect: Grudge\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveCounter = Symbol(
        None,
        None,
        None,
        "Move effect: Give the user the Counter status\nRelevant moves: Pursuit, Counter, Payback\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageBurn10FlameWheel = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage with a 10% chance (FLAME_WHEEL_BURN_CHANCE) of burning the defender.\nRelevant moves: Flame Wheel, Lava Plume\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageBurn10 = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage with a 10% chance (FLAMETHROWER_BURN_CHANCE) of burning the defender.\nRelevant moves: Flamethrower, Fire Blast, Heat Wave, Ember, Fire Punch\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveExpose = Symbol(
        None,
        None,
        None,
        "Move effect: Expose all Ghost-type enemies, and reset evasion boosts\nRelevant moves: Odor Sleuth, Foresight\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDoubleTeam = Symbol(
        None,
        None,
        None,
        "Move effect: Double Team\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveGust = Symbol(
        None,
        None,
        None,
        "Move effect: Gust\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveBoostDefense1 = Symbol(
        None,
        None,
        None,
        "Move effect: Boost the user's defense by one stage\nRelevant moves: Harden, Withdraw\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveParalyze = Symbol(
        None,
        None,
        None,
        "Move effect: Paralyze the defender if possible\nRelevant moves: Disable, Stun Spore, Glare\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveBoostAttack1 = Symbol(
        None,
        None,
        None,
        "Move effect: Boost the user's attack by one stage\nRelevant moves: Sharpen, Howl, Meditate\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveRazorWind = Symbol(
        None,
        None,
        None,
        "Move effect: Razor Wind\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveBide = Symbol(
        None,
        None,
        None,
        "Move effect: Give the user the Bide status\nRelevant moves: Bide, Revenge, Avalanche\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveBideUnleash = Symbol(
        None,
        None,
        None,
        "Move effect: Unleashes the Bide status\nRelevant moves: Bide (unleashing), Revenge (unleashing), Avalanche (unleashing)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveCrunch = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage with a 20% chance (CRUNCH_LOWER_DEFENSE_CHANCE) of lowering the defender's defense.\nRelevant moves: Crunch, Shadow Ball via Nature Power\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether or not damage was dealt",
    )

    DoMoveDamageCringe20 = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage with a 20% chance (BITE_CRINGE_CHANCE) of inflicting the cringe status on the defender.\nRelevant moves: Bite, Needle Arm, Stomp, Rolling Kick\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageParalyze20 = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage with a 20% chance (THUNDER_PARALYZE_CHANCE) of paralyzing the defender.\nRelevant moves: Thunder, ThunderPunch, Force Palm, Discharge\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether or not damage was dealt",
    )

    DoMoveEndeavor = Symbol(
        None,
        None,
        None,
        "Move effect: Endeavor\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveFacade = Symbol(
        None,
        None,
        None,
        "Move effect: Facade\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageLowerSpeed20 = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage with a 20% chance (CONSTRICT_LOWER_SPEED_CHANCE) of lowering the defender's speed.\nRelevant moves: Constrict, Bubblebeam\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether or not damage was dealt",
    )

    DoMoveBrickBreak = Symbol(
        None,
        None,
        None,
        "Move effect: Brick Break\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageLowerSpeed100 = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage and lower the defender's speed.\nRelevant moves: Rock Tomb, Icy Wind, Mud Shot\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveFocusPunch = Symbol(
        None,
        None,
        None,
        "Move effect: Focus Punch\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageDrain = Symbol(
        None,
        None,
        None,
        "Move effect: Deal draining damage, healing the attacker by a proportion of the damage dealt.\nRelevant moves: Giga Drain, Leech Life, Mega Drain, Drain Punch\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether or not damage was dealt",
    )

    DoMoveReversal = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage with a higher multiplier the lower the attacker's HP is.\nRelevant moves: Reversal, Flail\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSmellingSalt = Symbol(
        None,
        None,
        None,
        "Move effect: SmellingSalt\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveMetalSound = Symbol(
        None,
        None,
        None,
        "Move effect: Metal Sound\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveTickle = Symbol(
        None,
        None,
        None,
        "Move effect: Tickle\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveShadowHold = Symbol(
        None,
        None,
        None,
        "Move effect: Inflict the Shadow Hold status on the defender\nRelevant moves: Spider Web, Mean Look\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveHaze = Symbol(
        None,
        None,
        None,
        "Move effect: Haze\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageMultihitFatigue = Symbol(
        None,
        None,
        None,
        "Move effect: Deal multihit damage, then confuse the attacker\nRelevant moves: Outrage, Petal Dance\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageWeightDependent = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage, multiplied by a weight-dependent factor.\nRelevant moves: Low Kick, Grass Knot\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether or not damage was dealt",
    )

    DoMoveDamageBoostAllStats = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage, with a 20% (SILVER_WIND_BOOST_CHANCE) to boost the user's attack, special attack, defense, special defense, and speed.\nRelevant moves: Silver Wind, AncientPower, Ominous Wind\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSynthesis = Symbol(
        None,
        None,
        None,
        "Move effect: Synthesis\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveBoostSpeed1 = Symbol(
        None,
        None,
        None,
        "Move effect: Boost the team's movement speed by one stage\nRelevant moves: Agility, Speed Boost (item effect), MOVE_TAG_0x1AA, Tailwind\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveRapidSpin = Symbol(
        None,
        None,
        None,
        "Move effect: Rapid Spin\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSureShot = Symbol(
        None,
        None,
        None,
        "Move effect: Give the user the Sure-Shot status\nRelevant moves: Mind Reader, Lock-On\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveCosmicPower = Symbol(
        None,
        None,
        None,
        "Move effect: Cosmic Power\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSkyAttack = Symbol(
        None,
        None,
        None,
        "Move effect: Sky Attack\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageFreeze15 = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage with a 15% chance (POWDER_SNOW_FREEZE_CHANCE) of freezing the defender.\nRelevant moves: Powder Snow, Blizzard, Ice Punch, Ice Beam\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether or not damage was dealt",
    )

    DoMoveMeteorMash = Symbol(
        None,
        None,
        None,
        "Move effect: Meteor Mash\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveEndure = Symbol(
        None,
        None,
        None,
        "Move effect: Endure\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveLowerSpeed1 = Symbol(
        None,
        None,
        None,
        "Move effect: Lower the defender's defense by one stage\nRelevant moves: Scary Face, Cotton Spore\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageConfuse10 = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage with a 10% chance (PSYBEAM_CONFUSE_CHANCE) of confusing the defender.\nRelevant moves: Psybeam, Signal Beam, Confusion, Chatter, Rock Climb\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMovePsywave = Symbol(
        None,
        None,
        None,
        "Move effect: Psywave\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageLowerDefensiveStatVariable = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage with some chance of lowering one of the defender's defensive stats.\nRelevant moves: Psychic, Acid, Seed Flare, Earth Power, Bug Buzz, Flash Cannon\n\nNote that this move effect handler has a slightly different parameter list than all the others. Which defensive stat is lowered, the chance of lowering, and the number of stages to lower are all specified as arguments by the caller.\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: stat index for the defensive stat to lower\nstack[0]: number of defensive stat stages to lower\nstack[1]: percentage chance of lowering the defensive stat\nstack[2]: item ID\nreturn: whether the move was successfully used",
    )

    DoMovePsychoBoost = Symbol(
        None,
        None,
        None,
        "Move effect: Psycho Boost\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveUproar = Symbol(
        None,
        None,
        None,
        "Move effect: Uproar\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveWaterSpout = Symbol(
        None,
        None,
        None,
        "Move effect: Water Spout\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMovePsychUp = Symbol(
        None,
        None,
        None,
        "Move effect: Psych Up\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageWithRecoil = Symbol(
        None,
        None,
        None,
        "Move effect: Deals damage, inflicting recoil damage on the attacker.\nRelevant moves: Submission, Take Down, Volt Tackle, Wood Hammer, Brave Bird\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: bool, whether or not damage was dealt",
    )

    EntityIsValidMoveEffects = Symbol(
        None, None, None, "See overlay29.yml::EntityIsValid"
    )

    DoMoveRecoverHp = Symbol(
        None,
        None,
        None,
        "Move effect: Recover 50% of the user's max HP\nRelevant moves: Recover, Slack Off\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveEarthquake = Symbol(
        None,
        None,
        None,
        "Move effect: Earthquake\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    GetNaturePowerVariant = Symbol(
        None,
        None,
        None,
        "Gets the nature power variant for the current dungeon, based on the tileset ID.\n\nreturn: nature power variant",
    )

    DoMoveNaturePower = Symbol(
        None,
        None,
        None,
        "Move effect: Nature Power\n\nr0: attacker pointer\nr1: defender pointer\nr2: move (unused)\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageParalyze10 = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage with a 10% chance (LICK_PARALZYE_CHANCE) of paralyzing the defender.\nRelevant moves: Lick, Spark, Body Slam, DragonBreath\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSelfdestruct = Symbol(
        None,
        None,
        None,
        "Move effect: Selfdestruct\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveShadowBall = Symbol(
        None,
        None,
        None,
        "Move effect: Shadow Ball\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveCharge = Symbol(
        None,
        None,
        None,
        "Move effect: Charge\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveThunderbolt = Symbol(
        None,
        None,
        None,
        "Move effect: Thunderbolt\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveMist = Symbol(
        None,
        None,
        None,
        "Move effect: Mist\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveFissure = Symbol(
        None,
        None,
        None,
        "Move effect: Fissure\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageCringe10 = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage with a 10% chance (EXTRASENSORY_CRINGE_CHANCE) to inflict the cringe status on the defender.\nRelevant moves: Extrasensory, Hyper Fang, Bone Club\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSafeguard = Symbol(
        None,
        None,
        None,
        "Move effect: Safeguard\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveAbsorb = Symbol(
        None,
        None,
        None,
        "Move effect: Absorb\n\nThis is essentially identical to DoMoveDamageDrain, except the ordering of the instructions is slightly different enough to introduce subtle variations in functionality.\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether or not damage was dealt",
    )

    DefenderAbilityIsActiveMoveEffects = Symbol(
        None, None, None, "See overlay29.yml::DefenderAbilityIsActive"
    )

    DoMoveSkillSwap = Symbol(
        None,
        None,
        None,
        "Move effect: Skill Swap\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSketch = Symbol(
        None,
        None,
        None,
        "Move effect: Sketch\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveHeadbutt = Symbol(
        None,
        None,
        None,
        "Move effect: Headbutt\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDoubleEdge = Symbol(
        None,
        None,
        None,
        "Move effect: Double-Edge\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSandstorm = Symbol(
        None,
        None,
        None,
        "Move effect: Sandstorm\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveLowerAccuracy1 = Symbol(
        None,
        None,
        None,
        "Move effect: Lower the defender's accuracy by one stage\nRelevant moves: Sand-Attack, Kinesis, Flash\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamagePoison40 = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage with a 40% chance (SMOG_POISON_CHANCE) of poisoning the defender.\nRelevant moves: Smog, Cross Poison, Gunk Shot, Poison Jab\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether or not damage was dealt",
    )

    DoMoveGrowth = Symbol(
        None,
        None,
        None,
        "Move effect: Growth\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSacredFire = Symbol(
        None,
        None,
        None,
        "Move effect: Sacred Fire\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveOhko = Symbol(
        None,
        None,
        None,
        "Move effect: Possibly one-hit KO the defender\nRelevant moves: Sheer Cold, Guillotine\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSolarBeam = Symbol(
        None,
        None,
        None,
        "Move effect: SolarBeam\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSonicBoom = Symbol(
        None,
        None,
        None,
        "Move effect: SonicBoom\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveFly = Symbol(
        None,
        None,
        None,
        "Move effect: Fly\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveExplosion = Symbol(
        None,
        None,
        None,
        "Move effect: Explosion\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDive = Symbol(
        None,
        None,
        None,
        "Move effect: Dive\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveWaterfall = Symbol(
        None,
        None,
        None,
        "Move effect: Waterfall\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageLowerAccuracy40 = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage with a 40% chance (MUDDY_WATER_LOWER_ACCURACY_CHANCE) of lowering the defender's accuracy.\nRelevant moves: Muddy Water, Mud Bomb, Mirror Shot\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether or not damage was dealt",
    )

    DoMoveStockpile = Symbol(
        None,
        None,
        None,
        "Move effect: Stockpile\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveTwister = Symbol(
        None,
        None,
        None,
        "Move effect: Twister\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveTwineedle = Symbol(
        None,
        None,
        None,
        "Move effect: Twineedle\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveRecoverHpTeam = Symbol(
        None,
        None,
        None,
        "Move effect: Recover 25% HP for all team members\nRelevant moves: Softboiled, Milk Drink\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveMinimize = Symbol(
        None,
        None,
        None,
        "Move effect: Minimize\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSeismicToss = Symbol(
        None,
        None,
        None,
        "Move effect: Seismic Toss\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveConfuse = Symbol(
        None,
        None,
        None,
        "Move effect: Confuse target enemies if possible.\nRelevant moves: Confuse Ray, Supersonic, Sweet Kiss, Teeter Dance, Totter (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveTaunt = Symbol(
        None,
        None,
        None,
        "Move effect: Taunt\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveMoonlight = Symbol(
        None,
        None,
        None,
        "Move effect: Moonlight\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveHornDrill = Symbol(
        None,
        None,
        None,
        "Move effect: Horn Drill\n\nThis is exactly the same as DoMoveOhko, except there's a call to SubstitutePlaceholderStringTags at the end.\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSwordsDance = Symbol(
        None,
        None,
        None,
        "Move effect: Swords Dance\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveConversion = Symbol(
        None,
        None,
        None,
        "Move effect: Conversion\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveConversion2 = Symbol(
        None,
        None,
        None,
        "Move effect: Conversion 2\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveHelpingHand = Symbol(
        None,
        None,
        None,
        "Move effect: Helping Hand\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveBoostDefense2 = Symbol(
        None,
        None,
        None,
        "Move effect: Boost the defender's defense stat by two stages\nRelevant moves: Iron Defense, Acid Armor, Barrier\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveWarp = Symbol(
        None,
        None,
        None,
        "Move effect: Warp the target to another tile on the floor\nRelevant moves: Teleport, Warp (item effect), MOVE_TAG_0x1A8\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveThundershock = Symbol(
        None,
        None,
        None,
        "Move effect: Thundershock\n\nThis is identical to DoMoveDamageParalyze10, except it uses a different data symbol for the paralysis chance (but it's still 10%).\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveThunderWave = Symbol(
        None,
        None,
        None,
        "Move effect: Thunder Wave\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveZapCannon = Symbol(
        None,
        None,
        None,
        "Move effect: Zap Cannon\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveBlock = Symbol(
        None,
        None,
        None,
        "Move effect: Block\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMovePoison = Symbol(
        None,
        None,
        None,
        "Move effect: Poison the defender if possible\nRelevant moves: Poison Gas, PoisonPowder\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveToxic = Symbol(
        None,
        None,
        None,
        "Move effect: Toxic\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMovePoisonFang = Symbol(
        None,
        None,
        None,
        "Move effect: Poison Fang\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamagePoison18 = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage with an 18% chance (POISON_STING_POISON_CHANCE) to poison the defender.\nRelevant moves: Poison Sting, Sludge, Sludge Bomb\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveJumpKick = Symbol(
        None,
        None,
        None,
        "Move effect: Jump Kick\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveBounce = Symbol(
        None,
        None,
        None,
        "Move effect: Bounce\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveHiJumpKick = Symbol(
        None,
        None,
        None,
        "Move effect: Hi Jump Kick\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveTriAttack = Symbol(
        None,
        None,
        None,
        "Move effect: Tri Attack\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSwapItems = Symbol(
        None,
        None,
        None,
        "Move effect: Swaps the held items of the attacker and defender.\nRelevant moves: Trick, Switcheroo\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveTripleKick = Symbol(
        None,
        None,
        None,
        "Move effect: Triple Kick\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSport = Symbol(
        None,
        None,
        None,
        "Move effect: Activate the relevant sport condition (Mud Sport, Water Sport) on the floor\nRelevant moves: Mud Sport, Water Sport\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveMudSlap = Symbol(
        None,
        None,
        None,
        "Move effect: Mud-Slap\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageStealItem = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage and steal the defender's item if possible.\nRelevant moves: Thief, Covet\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveAmnesia = Symbol(
        None,
        None,
        None,
        "Move effect: Amnesia\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveNightShade = Symbol(
        None,
        None,
        None,
        "Move effect: Night Shade\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveGrowl = Symbol(
        None,
        None,
        None,
        "Move effect: Growl\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSurf = Symbol(
        None,
        None,
        None,
        "Move effect: Surf\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveRolePlay = Symbol(
        None,
        None,
        None,
        "Move effect: Role Play\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSunnyDay = Symbol(
        None,
        None,
        None,
        "Move effect: Sunny Day\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveLowerDefense1 = Symbol(
        None,
        None,
        None,
        "Move effect: Lower the defender's defense by one stage\nRelevant moves: Tail Whip, Leer\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveWish = Symbol(
        None,
        None,
        None,
        "Move effect: Wish\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveFakeOut = Symbol(
        None,
        None,
        None,
        "Move effect: Fake Out\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSleepTalk = Symbol(
        None,
        None,
        None,
        "Move effect: Sleep Talk\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMovePayDay = Symbol(
        None,
        None,
        None,
        "Move effect: Pay Day\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveAssist = Symbol(
        None,
        None,
        None,
        "Move effect: Assist\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveRest = Symbol(
        None,
        None,
        None,
        "Move effect: Rest\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveIngrain = Symbol(
        None,
        None,
        None,
        "Move effect: Ingrain\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSwallow = Symbol(
        None,
        None,
        None,
        "Move effect: Swallow\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveCurse = Symbol(
        None,
        None,
        None,
        "Move effect: Curse\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSuperpower = Symbol(
        None,
        None,
        None,
        "Move effect: Superpower\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSteelWing = Symbol(
        None,
        None,
        None,
        "Move effect: Steel Wing\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSpitUp = Symbol(
        None,
        None,
        None,
        "Move effect: Spit Up\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDynamicPunch = Symbol(
        None,
        None,
        None,
        "Move effect: DynamicPunch\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveKnockOff = Symbol(
        None,
        None,
        None,
        "Move effect: Knock Off\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSplash = Symbol(
        None,
        None,
        None,
        "Move effect: Splash\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSetDamage = Symbol(
        None,
        None,
        None,
        "Move effect: Give the user the Set Damage status\nRelevant moves: Doom Desire, Future Sight\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveBellyDrum = Symbol(
        None,
        None,
        None,
        "Move effect: Belly Drum\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveLightScreen = Symbol(
        None,
        None,
        None,
        "Move effect: Light Screen\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSecretPower = Symbol(
        None,
        None,
        None,
        "Move effect: Secret Power\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageConfuse30 = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage with a 30% chance (DIZZY_PUNCH_CONFUSE_CHANCE) to confuse the defender.\nRelevant moves: Dizzy Punch, Water Pulse\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveBulkUp = Symbol(
        None,
        None,
        None,
        "Move effect: Bulk Up\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMovePause = Symbol(
        None,
        None,
        None,
        "Move effect: Inflicts the Paused status on the defender\nRelevant moves: Imprison, Observer (item effect), MOVE_TAG_0x1AD\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveFeatherDance = Symbol(
        None,
        None,
        None,
        "Move effect: FeatherDance\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveBeatUp = Symbol(
        None,
        None,
        None,
        "Move effect: Beat Up\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveBlastBurn = Symbol(
        None,
        None,
        None,
        "Move effect: Blast Burn\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveCrushClaw = Symbol(
        None,
        None,
        None,
        "Move effect: Crush Claw\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveBlazeKick = Symbol(
        None,
        None,
        None,
        "Move effect: Blaze Kick\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMovePresent = Symbol(
        None,
        None,
        None,
        "Move effect: Present\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveEruption = Symbol(
        None,
        None,
        None,
        "Move effect: Eruption\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveTransform = Symbol(
        None,
        None,
        None,
        "Move effect: Transform\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMovePoisonTail = Symbol(
        None,
        None,
        None,
        "Move effect: Poison Tail\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveBlowback = Symbol(
        None,
        None,
        None,
        "Move effect: Blows the defender back\nRelevant moves: Whirlwind, Roar, Blowback (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveCamouflage = Symbol(
        None,
        None,
        None,
        "Move effect: Camouflage\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveTailGlow = Symbol(
        None,
        None,
        None,
        "Move effect: Tail Glow\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageConstrict10 = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage with a 10% (WHIRLPOOL_CONSTRICT_CHANCE) chance to constrict, and with a damage multiplier dependent on the move used.\nRelevant moves: Clamp, Bind, Sand Tomb, Fire Spin, Magma Storm\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether or not damage was dealt",
    )

    DoMovePerishSong = Symbol(
        None,
        None,
        None,
        "Move effect: Perish Song\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveWrap = Symbol(
        None,
        None,
        None,
        "Move effect: Wrap\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSpikes = Symbol(
        None,
        None,
        None,
        "Move effect: Spikes\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveMagnitude = Symbol(
        None,
        None,
        None,
        "Move effect: Magnitude\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveMagicCoat = Symbol(
        None,
        None,
        None,
        "Move effect: Magic Coat\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveProtect = Symbol(
        None,
        None,
        None,
        "Move effect: Try to give the user the Protect status\nRelevant moves: Protect, Detect\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDefenseCurl = Symbol(
        None,
        None,
        None,
        "Move effect: Defense Curl\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDecoy = Symbol(
        None,
        None,
        None,
        "Move effect: Inflict the Decoy status on the target\nRelevant moves: Follow Me, Substitute, Decoy Maker (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveMistBall = Symbol(
        None,
        None,
        None,
        "Move effect: Mist Ball\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDestinyBond = Symbol(
        None,
        None,
        None,
        "Move effect: Destiny Bond\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveMirrorCoat = Symbol(
        None,
        None,
        None,
        "Move effect: Mirror Coat\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveCalmMind = Symbol(
        None,
        None,
        None,
        "Move effect: Calm Mind\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveHiddenPower = Symbol(
        None,
        None,
        None,
        "Move effect: Hidden Power\n\nThis is exactly the same as DoMoveDamage (both are wrappers around DealDamage), except this function always returns true.\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveMetalClaw = Symbol(
        None,
        None,
        None,
        "Move effect: Metal Claw\n\n Note that this move effect handler has a slightly different parameter list than all the others. Which offensive stat is boosted is specified by the caller.\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: stat index for the offensive stat to boost\nstack[0]: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveAttract = Symbol(
        None,
        None,
        None,
        "Move effect: Attract\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveCopycat = Symbol(
        None,
        None,
        None,
        "Move effect: The attacker uses the move last used by enemy it's facing.\nRelevant moves: Mimic, Copycat\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveFrustration = Symbol(
        None,
        None,
        None,
        "Move effect: Frustration\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveLeechSeed = Symbol(
        None,
        None,
        None,
        "Move effect: Leech Seed\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveMetronome = Symbol(
        None,
        None,
        None,
        "Move effect: Metronome\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDreamEater = Symbol(
        None,
        None,
        None,
        "Move effect: Dream Eater\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSnatch = Symbol(
        None,
        None,
        None,
        "Move effect: Snatch\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveRecycle = Symbol(
        None,
        None,
        None,
        "Move effect: Recycle\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveReflect = Symbol(
        None,
        None,
        None,
        "Move effect: Reflect\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDragonRage = Symbol(
        None,
        None,
        None,
        "Move effect: Dragon Rage\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDragonDance = Symbol(
        None,
        None,
        None,
        "Move effect: Dragon Dance\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSkullBash = Symbol(
        None,
        None,
        None,
        "Move effect: Skull Bash\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageLowerSpecialDefense50 = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage with a 50% (LUSTER_PURGE_LOWER_SPECIAL_DEFENSE_CHANCE) chance to lower special defense.\nRelevant moves: Luster Purge, Energy Ball, Focus Blast\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveStruggle = Symbol(
        None,
        None,
        None,
        "Move effect: Struggle\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveRockSmash = Symbol(
        None,
        None,
        None,
        "Move effect: Rock Smash\nRelevant moves: Rock Smash, MOVE_UNNAMED_0x169\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSeeTrap = Symbol(
        None,
        None,
        None,
        "Move effect: See-Trap (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveTakeaway = Symbol(
        None,
        None,
        None,
        "Move effect: Takeaway (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveRebound = Symbol(
        None,
        None,
        None,
        "Move effect: Rebound (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSwitchPositions = Symbol(
        None,
        None,
        None,
        "Move effect: Switches the user's position with positions of other monsters in the room.\nRelevant moves: Baton Pass, Switcher (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveStayAway = Symbol(
        None,
        None,
        None,
        "Move effect: Stay Away (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveCleanse = Symbol(
        None,
        None,
        None,
        "Move effect: Cleanse (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSiesta = Symbol(
        None,
        None,
        None,
        "Move effect: Siesta (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveTwoEdge = Symbol(
        None,
        None,
        None,
        "Move effect: Two-Edge (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveNoMove = Symbol(
        None,
        None,
        None,
        "Move effect: No-Move (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveScan = Symbol(
        None,
        None,
        None,
        "Move effect: Scan (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMovePowerEars = Symbol(
        None,
        None,
        None,
        "Move effect: Power-Ears (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveTransfer = Symbol(
        None,
        None,
        None,
        "Move effect: Transfer (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSlowDown = Symbol(
        None,
        None,
        None,
        "Move effect: Slow Down (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSearchlight = Symbol(
        None,
        None,
        None,
        "Move effect: Searchlight (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMovePetrify = Symbol(
        None,
        None,
        None,
        "Move effect: Petrifies the target\nRelevant moves: Petrify (item effect), MOVE_TAG_0x1A9\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMovePounce = Symbol(
        None,
        None,
        None,
        "Move effect: Pounce (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveTrawl = Symbol(
        None,
        None,
        None,
        "Move effect: Trawl (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveEscape = Symbol(
        None,
        None,
        None,
        "Move effect: Escape (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDrought = Symbol(
        None,
        None,
        None,
        "Move effect: Drought (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveTrapBuster = Symbol(
        None,
        None,
        None,
        "Move effect: Trap Buster (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveWildCall = Symbol(
        None,
        None,
        None,
        "Move effect: Wild Call (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveInvisify = Symbol(
        None,
        None,
        None,
        "Move effect: Invisify (item effect)\n\nThis function sets r1 = r0 before calling TryInvisify, so the effect will always be applied to the user regardless of the move settings.\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveOneShot = Symbol(
        None,
        None,
        None,
        "Move effect: One-Shot (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveHpGauge = Symbol(
        None,
        None,
        None,
        "Move effect: HP Gauge (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveVacuumCut = Symbol(
        None,
        None,
        None,
        "Move effect: Vacuum Cut\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveReviver = Symbol(
        None,
        None,
        None,
        "Move effect: Reviver (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveShocker = Symbol(
        None,
        None,
        None,
        "Move effect: Shocker (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveEcho = Symbol(
        None,
        None,
        None,
        "Move effect: Echo (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveFamish = Symbol(
        None,
        None,
        None,
        "Move effect: Famish (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveOneRoom = Symbol(
        None,
        None,
        None,
        "Move effect: One-Room (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveFillIn = Symbol(
        None,
        None,
        None,
        "Move effect: Fill-In (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveTrapper = Symbol(
        None,
        None,
        None,
        "Move effect: Trapper (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveItemize = Symbol(
        None,
        None,
        None,
        "Move effect: Itemize (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveHurl = Symbol(
        None,
        None,
        None,
        "Move effect: Hurls the target\nRelevant moves: Strength, Hurl (item effect), Fling\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveMobile = Symbol(
        None,
        None,
        None,
        "Move effect: Mobile (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveSeeStairs = Symbol(
        None,
        None,
        None,
        "Move effect: See Stairs (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveLongToss = Symbol(
        None,
        None,
        None,
        "Move effect: Long Toss (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMovePierce = Symbol(
        None,
        None,
        None,
        "Move effect: Pierce (item effect)\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveHammerArm = Symbol(
        None,
        None,
        None,
        "Move effect: Hammer Arm\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveAquaRing = Symbol(
        None,
        None,
        None,
        "Move effect: Aqua Ring\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveGastroAcid = Symbol(
        None,
        None,
        None,
        "Move effect: Gastro Acid\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveHealingWish = Symbol(
        None,
        None,
        None,
        "Move effect: Healing Wish\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveCloseCombat = Symbol(
        None,
        None,
        None,
        "Move effect: Close Combat\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveLuckyChant = Symbol(
        None,
        None,
        None,
        "Move effect: Lucky Chant\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveGuardSwap = Symbol(
        None,
        None,
        None,
        "Move effect: Guard Swap\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveHealOrder = Symbol(
        None,
        None,
        None,
        "Move effect: Heal Order\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveHealBlock = Symbol(
        None,
        None,
        None,
        "Move effect: Heal Block\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveThunderFang = Symbol(
        None,
        None,
        None,
        "Move effect: Thunder Fang\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDefog = Symbol(
        None,
        None,
        None,
        "Move effect: Defog\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveTrumpCard = Symbol(
        None,
        None,
        None,
        "Move effect: Trump Card\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveIceFang = Symbol(
        None,
        None,
        None,
        "Move effect: Ice Fang\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMovePsychoShift = Symbol(
        None,
        None,
        None,
        "Move effect: Psycho Shift\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveEmbargo = Symbol(
        None,
        None,
        None,
        "Move effect: Embargo\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveBrine = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage, with a 2x multiplier if the defender is at or below half HP.\nRelevant moves: Brine, Assurance\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveNaturalGift = Symbol(
        None,
        None,
        None,
        "Move effect: Natural Gift\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveGyroBall = Symbol(
        None,
        None,
        None,
        "Move effect: Gyro Ball\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveShadowForce = Symbol(
        None,
        None,
        None,
        "Move effect: Shadow Force\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveGravity = Symbol(
        None,
        None,
        None,
        "Move effect: Gravity\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveStealthRock = Symbol(
        None,
        None,
        None,
        "Move effect: Stealth Rock\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveChargeBeam = Symbol(
        None,
        None,
        None,
        "Move effect: Charge Beam\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageEatItem = Symbol(
        None,
        None,
        None,
        "Move effect: Deals damage, and eats any beneficial items the defender is holding.\nRelevant moves: Pluck, Bug Bite\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveAcupressure = Symbol(
        None,
        None,
        None,
        "Move effect: Acupressure\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveMagnetRise = Symbol(
        None,
        None,
        None,
        "Move effect: Magnet Rise\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveToxicSpikes = Symbol(
        None,
        None,
        None,
        "Move effect: Toxic Spikes\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveLastResort = Symbol(
        None,
        None,
        None,
        "Move effect: Last Resort\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveTrickRoom = Symbol(
        None,
        None,
        None,
        "Move effect: Trick Room\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveWorrySeed = Symbol(
        None,
        None,
        None,
        "Move effect: Worry Seed\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDamageHpDependent = Symbol(
        None,
        None,
        None,
        "Move effect: Deal damage, with a multiplier dependent on the defender's current HP.\nRelevant moves: Wring Out, Crush Grip\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveHeartSwap = Symbol(
        None,
        None,
        None,
        "Move effect: Heart Swap\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveRoost = Symbol(
        None,
        None,
        None,
        "Move effect: Roost\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMovePowerSwap = Symbol(
        None,
        None,
        None,
        "Move effect: Power Swap\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMovePowerTrick = Symbol(
        None,
        None,
        None,
        "Move effect: Power Trick\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveFeint = Symbol(
        None,
        None,
        None,
        "Move effect: Feint\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveFlareBlitz = Symbol(
        None,
        None,
        None,
        "Move effect: Flare Blitz\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDefendOrder = Symbol(
        None,
        None,
        None,
        "Move effect: Defend Order\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveFireFang = Symbol(
        None,
        None,
        None,
        "Move effect: Fire Fang\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveLunarDance = Symbol(
        None,
        None,
        None,
        "Move effect: Lunar Dance\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveMiracleEye = Symbol(
        None,
        None,
        None,
        "Move effect: Miracle Eye\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveWakeUpSlap = Symbol(
        None,
        None,
        None,
        "Move effect: Wake-Up Slap\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveMetalBurst = Symbol(
        None,
        None,
        None,
        "Move effect: Metal Burst\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveHeadSmash = Symbol(
        None,
        None,
        None,
        "Move effect: Head Smash\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveCaptivate = Symbol(
        None,
        None,
        None,
        "Move effect: Captivate\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveLeafStorm = Symbol(
        None,
        None,
        None,
        "Move effect: Leaf Storm\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveDracoMeteor = Symbol(
        None,
        None,
        None,
        "Move effect: Draco Meteor\n\nNote that this move effect handler has an extra parameter that can be used to disable the special attack drop.\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nr4: disable special attack drop\nreturn: whether the move was successfully used",
    )

    DoMoveRockPolish = Symbol(
        None,
        None,
        None,
        "Move effect: Rock Polish\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveNastyPlot = Symbol(
        None,
        None,
        None,
        "Move effect: Nasty Plot\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveTag0x1AB = Symbol(
        None,
        None,
        None,
        "Move effect: MOVE_TAG_0x1AB\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveTag0x1A6 = Symbol(
        None,
        None,
        None,
        "Move effect: MOVE_TAG_0x1A6\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )

    DoMoveTag0x1A7 = Symbol(
        None,
        None,
        None,
        "Move effect: MOVE_TAG_0x1A7\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether the move was successfully used",
    )


class NaItcmMove_effectsData:

    MAX_HP_CAP_MOVE_EFFECTS = Symbol(None, None, None, "See overlay29.yml::MAX_HP_CAP")

    LUNAR_DANCE_PP_RESTORATION = Symbol(
        None, None, None, "The amount of PP restored by Lunar Dance (999)."
    )


class NaItcmMove_effectsSection:
    name = "move_effects"
    description = "Move effect handlers for individual moves, called by ExecuteMoveEffect (and also the Metronome and Nature Power tables).\n\nThis subregion contains only the move effect handlers themselves, and not necessarily all the utility functions used by the move effect handlers (such as the damage calculation functions). These supporting utilities are in the main overlay29 block."
    loadaddress = None
    length = None
    functions = NaItcmMove_effectsFunctions
    data = NaItcmMove_effectsData


class NaItcmOverlay0Functions:

    pass


class NaItcmOverlay0Data:

    TOP_MENU_MUSIC_ID = Symbol(None, None, None, "Music ID to play in the top menu.")


class NaItcmOverlay0Section:
    name = "overlay0"
    description = "Likely contains supporting data and code related to the top menu.\n\nThis is loaded together with overlay 1 while in the top menu. Since it's in overlay group 2 (together with overlay 10, which is another 'data' overlay), this overlay probably plays a similar role. It mentions several files from the BACK folder that are known backgrounds for the top menu."
    loadaddress = None
    length = None
    functions = NaItcmOverlay0Functions
    data = NaItcmOverlay0Data


class NaItcmOverlay1Functions:

    CreateMainMenus = Symbol(
        None,
        None,
        None,
        "Prepares the top menu and sub menu, adding the different options that compose them.\n\nContains multiple calls to AddMainMenuOption and AddSubMenuOption. Some of them are conditionally executed depending on which options should be unlocked.\n\nNo params.",
    )

    AddMainMenuOption = Symbol(
        None,
        None,
        None,
        "Adds an option to the top menu.\n\nThis function is called for each one of the options in the top menu. It loops the MAIN_MENU data field, if the specified action ID does not exist there, the option won't be added.\n\nr0: Action ID\nr1: True if the option should be enabled, false otherwise",
    )

    AddSubMenuOption = Symbol(
        None,
        None,
        None,
        "Adds an option to the 'Other' submenu on the top menu.\n\nThis function is called for each one of the options in the submenu. It loops the SUBMENU data field, if the specified action ID does not exist there, the option won't be added.\n\nr0: Action ID\nr1: True if the option should be enabled, false otherwise",
    )

    ProcessContinueScreenContents = Symbol(
        None,
        None,
        None,
        "Fetches the required data and creates all the strings to display the contents shown in the window\nwhen choosing continue in the main menu.\n\nr0: undefined4",
    )


class NaItcmOverlay1Data:

    PRINTS_STRINGS = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    PRINTS_STRUCT = Symbol(
        None, None, None, "62*0x8\n\nNote: unverified, ported from Irdkwia's notes"
    )

    MAIN_MENU_WINDOW_PARAMS_1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    MAIN_MENU_WINDOW_PARAMS_2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    MAIN_MENU_WINDOW_PARAMS_3 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    MAIN_MENU_WINDOW_PARAMS_4 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    CONTINUE_CHOICE = Symbol(None, None, None, "")

    SUBMENU = Symbol(None, None, None, "")

    MAIN_MENU = Symbol(None, None, None, "")

    MAIN_MENU_WINDOW_PARAMS_5 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    MAIN_MENU_WINDOW_PARAMS_6 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    MAIN_MENU_WINDOW_PARAMS_7 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    MAIN_MENU_ITEMS_CONFIRM = Symbol(None, None, None, "")

    MAIN_MENU_WINDOW_PARAMS_8 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    MAIN_MENU_WINDOW_PARAMS_9 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    MAIN_DEBUG_MENU_ITEMS_1 = Symbol(None, None, None, "")

    MAIN_MENU_WINDOW_PARAMS_10 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    MAIN_DEBUG_MENU_ITEMS_2 = Symbol(None, None, None, "")


class NaItcmOverlay1Section:
    name = "overlay1"
    description = "Likely controls the top menu.\n\nThis is loaded together with overlay 0 while in the top menu. Since it's in overlay group 1 (together with other 'main' overlays like overlay 11 and overlay 29), this is probably the controller.\n\nSeems to contain code related to Wi-Fi rescue. It mentions several files from the GROUND and BACK folders."
    loadaddress = None
    length = None
    functions = NaItcmOverlay1Functions
    data = NaItcmOverlay1Data


class NaItcmOverlay10Functions:

    CreateInventoryMenu = Symbol(
        None,
        None,
        None,
        "Creates a window containing a menu for inventory management. Also see struct inventory_menu.\n\nThis is used for the Treasure Bag menu, the item information/price window in dungeon Kecleon shops, and possibly other things.\n\nIf window_params is NULL, INVENTORY_MENU_DEFAULT_WINDOW_PARAMS will be used. Otherwise, it will be copied onto the window, ignoring the update and contents fields. If window_params::width and/or window_params::height are 0, they will be computed based on the contained text.\n\nIf window_extra_info is non-NULL, it will be copied onto the window. Note that window_extra_info can only be NULL if there are no window_flags set that require extra info.\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: some function pointer?\nstack[0]: ?\nstack[1]: total number of items\nstack[2]: number of items per page\nstack[3]: ?\nreturn: window_id",
    )

    SetInventoryMenuState0 = Symbol(
        None, None, None, "Sets an inventory menu to state 0.\n\nr0: window_id"
    )

    SetInventoryMenuState6 = Symbol(
        None, None, None, "Sets an inventory menu to state 6.\n\nr0: window_id"
    )

    CloseInventoryMenu = Symbol(
        None,
        None,
        None,
        "Closes a window created with CreateInventoryMenu.\n\nr0: window_id",
    )

    IsInventoryMenuActive = Symbol(
        None,
        None,
        None,
        "This is a guess.\n\nChecks if the state of an inventory menu is something other than 7 or 8\n\nr0: window_id\nreturn: bool",
    )

    CheckInventoryMenuField0x1A0 = Symbol(
        None,
        None,
        None,
        "Checks if inventory_menu::field_0x1a0 is 0.\n\nr0: window_id\nreturn: bool",
    )

    PopInventoryMenuField0x1A3 = Symbol(
        None,
        None,
        None,
        "Sets inventory_menu::field_0x1a3 to 0 and returns the old value.\n\nr0: window_id\nreturn: old value",
    )

    UpdateInventoryMenu = Symbol(
        None,
        None,
        None,
        "Window update function for inventory menus.\n\nr0: window pointer",
    )

    IsInventoryMenuState3 = Symbol(
        None,
        None,
        None,
        "Checks if an inventory menu has a state value of 3.\n\nr0: window_id\nreturn: bool",
    )

    SprintfStatic = Symbol(
        None,
        None,
        None,
        "Statically defined copy of sprintf(3) in overlay 10. See arm9.yml for more information.\n\nr0: str\nr1: format\n...: variadic\nreturn: number of characters printed, excluding the null-terminator",
    )

    GetEffectAnimationField0x19 = Symbol(
        None,
        None,
        None,
        "Calls GetEffectAnimation and returns field 0x19.\n\nr0: anim_id\nreturn: GetEffectAnimation(anim_id)->field_0x19.",
    )

    AnimationHasMoreFrames = Symbol(
        None,
        None,
        None,
        "Just a guess. This is called in a loop in PlayEffectAnimation, and the output controls whether or not AdvanceFrame continues to be called.\n\nr0: ?\nreturn: whether or not the animation still has more frames left?",
    )

    GetEffectAnimation = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: anim_id\nreturn: effect animation pointer",
    )

    GetMoveAnimation = Symbol(
        None,
        None,
        None,
        "Get the move animation corresponding to the given move ID.\n\nr0: move_id\nreturn: move animation pointer",
    )

    GetSpecialMonsterMoveAnimation = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: ent_id\nreturn: special monster move animation pointer",
    )

    GetTrapAnimation = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: trap_id\nreturn: trap animation",
    )

    GetItemAnimation1 = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item_id\nreturn: first field of the item animation info",
    )

    GetItemAnimation2 = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: item_id\nreturn: second field of the item animation info",
    )

    GetMoveAnimationSpeed = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: move_id\nreturn: anim_ent_ptr (This might be a mistake? It seems to be an integer, not a pointer)",
    )

    DrawTeamStats = Symbol(
        None,
        None,
        None,
        "Handles creating the windows, sprites, etc. for the team stats top screen display.\n\nr0: undefined4\nr1: int\nr2: undefined4\nr3: uint32_t\nreturn: undefined4",
    )

    UpdateTeamStats = Symbol(
        None,
        None,
        None,
        "Handles updating the team stats top screen display.\n\nNo params.",
    )

    FreeTeamStats = Symbol(
        None,
        None,
        None,
        "Handles the procedure to close the team stats top screen display.\n\nFirst it deletes the sprites, then it closes the portrait boxes and then the text boxes containing the stats for all 4 team members.\n\nreturn: always 1, seems unused",
    )

    FreeMapAndTeam = Symbol(
        None,
        None,
        None,
        "Handles the procedure to close the map and team top screen display.\n\nreturn: always 1, seems unused",
    )

    ProcessTeamStatsLvHp = Symbol(
        None,
        None,
        None,
        "Appears to populate the Lv./HP row in the 'Team stats' top screen.\n\nr0: index of some kind",
    )

    ProcessTeamStatsNameGender = Symbol(
        None,
        None,
        None,
        "Appears to populate the name/gender row in the 'Team stats' top screen.\n\nr0: index of some kind",
    )

    IsBackgroundTileset = Symbol(
        None,
        None,
        None,
        "Given a tileset ID, returns whether it's a background or a regular tileset\n\nIn particular, returns r0 >= 0xAA\n\nr0: Tileset ID\nreturn: True if the tileset ID corresponds to a background, false if it corresponds to a regular tileset",
    )

    InitTilesetBuffer = Symbol(
        None,
        None,
        None,
        "Initializes a buffer that contains data related to tilesets (such as dungeon::unknown_file_buffer_0x102A8).\n\nCalls AllocAndLoadFileInPack and DecompressAtNormalVeneer.\n\nr0: Pointer to the buffer to init\nr1: Tileset ID\nr2: Memory allocation flags",
    )

    MainGame = Symbol(
        None,
        None,
        None,
        "Contains several functions that handle switching between ground and dungeon mode. It also handles other situations, like what happens right after exiting a dungeon.\n\nThe function doesn't get called until the player selects the option to resume a saved game and doesn't return until the player returns to the main menu.\n\nr0: End condition code? Seems to control what tasks get run and what transition happens when the dungeon ends\nreturn: return code?",
    )


class NaItcmOverlay10Data:

    INVENTORY_MENU_DEFAULT_WINDOW_PARAMS = Symbol(
        None,
        None,
        None,
        "Default window_params for an inventory_menu.\n\nNote that x_offset and y_offset refer to the right and bottom edges, since they will be paired with the x_offset_end and y_offset_end window flags in CreateInventoryMenu.\n\nAdditionally, width and height are 0, and will be computed in CreateInventoryMenu.",
    )

    FIRST_DUNGEON_WITH_MONSTER_HOUSE_TRAPS = Symbol(
        None,
        None,
        None,
        "The first dungeon that can have extra traps spawn in Monster Houses, Dark Hill\n\ntype: struct dungeon_id_8",
    )

    BAD_POISON_DAMAGE_COOLDOWN = Symbol(
        None,
        None,
        None,
        "The number of turns between passive bad poison (toxic) damage.",
    )

    PROTEIN_STAT_BOOST = Symbol(
        None, None, None, "The permanent attack boost from ingesting a Protein."
    )

    WATERFALL_CRINGE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Waterfall inflicting the cringe status, as a percentage (30%).",
    )

    AURORA_BEAM_LOWER_ATTACK_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Aurora Beam halving attack, as a percentage (60%).",
    )

    SPAWN_CAP_NO_MONSTER_HOUSE = Symbol(
        None,
        None,
        None,
        "The maximum number of enemies that can spawn on a floor without a monster house (15).",
    )

    OREN_BERRY_DAMAGE = Symbol(
        None, None, None, "Damage dealt by eating an Oren Berry."
    )

    IRON_TAIL_LOWER_DEFENSE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Iron Tail lowering defense, as a percentage (30%).",
    )

    TWINEEDLE_POISON_CHANCE = Symbol(
        None, None, None, "The chance of Twineedle poisoning, as a percentage (20%)."
    )

    EXTRASENSORY_CRINGE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Extrasensory (and others, see DoMoveDamageCringe10) inflicting the cringe status, as a percentage (10%).",
    )

    ROCK_SLIDE_CRINGE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Rock Slide (and others, see DoMoveDamageCringe30) inflicting the cringe status, as a percentage (30%)",
    )

    CRUNCH_LOWER_DEFENSE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Crunch (and others, see DoMoveDamageLowerDef20) lowering defense, as a percentage (20%).",
    )

    FOREWARN_FORCED_MISS_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Forewarn forcing a move to miss, as a percentage (20%).",
    )

    UNOWN_STONE_DROP_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of an Unown dropping an Unown stone, as a percentage (33%).",
    )

    SITRUS_BERRY_HP_RESTORATION = Symbol(
        None, None, None, "The amount of HP restored by eating a Sitrus Berry."
    )

    MUDDY_WATER_LOWER_ACCURACY_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Muddy Water (and others, see DoMoveDamageLowerAccuracy40) lowering accuracy, as a percentage (40%).",
    )

    SILVER_WIND_BOOST_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Silver Wind (and others, see DoMoveDamageBoostAllStats) boosting all stats, as a percentage (20%).",
    )

    POISON_TAIL_POISON_CHANCE = Symbol(
        None, None, None, "The chance of Poison Tail poisoning, as a percentage (10%)."
    )

    THUNDERSHOCK_PARALYZE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Thundershock paralyzing, as a percentage (10%).",
    )

    BOUNCE_PARALYZE_CHANCE = Symbol(
        None, None, None, "The chance of Bounce paralyzing, as a percentage (30%)"
    )

    HEADBUTT_CRINGE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Headbutt inflicting the cringe status, as a percentage (25%).",
    )

    FIRE_FANG_CRINGE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Fire Fang inflicting the cringe status, as a percentage (25%).",
    )

    SACRED_FIRE_BURN_CHANCE = Symbol(
        None, None, None, "The chance of Sacred Fire burning, as a percentage (50%)."
    )

    WHIRLPOOL_CONSTRICTION_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Whirlpool inflicting the constriction status, as a percentage (10%).",
    )

    EXP_ELITE_EXP_BOOST = Symbol(
        None,
        None,
        None,
        "The percentage increase in experience from the Exp. Elite IQ skill",
    )

    MONSTER_HOUSE_MAX_NON_MONSTER_SPAWNS = Symbol(
        None,
        None,
        None,
        "The maximum number of extra non-monster spawns (items/traps) in a Monster House, 7",
    )

    HEAL_ORDER_HP_RESTORATION = Symbol(
        None, None, None, "The amount of HP restored by Heal Order (40)."
    )

    STEEL_WING_BOOST_DEFENSE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Steel Wing boosting defense, as a percentage (20%).",
    )

    GOLD_THORN_POWER = Symbol(None, None, None, "Attack power for Golden Thorns.")

    BURN_DAMAGE = Symbol(None, None, None, "Damage dealt by the burn status condition.")

    POISON_DAMAGE = Symbol(
        None, None, None, "Damage dealt by the poison status condition."
    )

    SPAWN_COOLDOWN = Symbol(
        None,
        None,
        None,
        "The number of turns between enemy spawns under normal conditions.",
    )

    MIST_BALL_LOWER_SPECIAL_ATTACK_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Mist Ball lowering special attack, as a percentage (50%).",
    )

    CHARGE_BEAM_BOOST_SPECIAL_ATTACK_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Charge Beam boosting special attack, as a percentage (40%).",
    )

    ORAN_BERRY_FULL_HP_BOOST = Symbol(
        None,
        None,
        None,
        "The permanent HP boost from eating an Oran Berry at full HP (0).",
    )

    LIFE_SEED_HP_BOOST = Symbol(
        None, None, None, "The permanent HP boost from eating a Life Seed."
    )

    OCTAZOOKA_LOWER_ACCURACY_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Octazooka lowering accuracy, as a percentage (60%).",
    )

    LUSTER_PURGE_LOWER_SPECIAL_DEFENSE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Luster Purge (and others, see DoMoveDamageLowerSpecialDefense50) lowering special defense, as a percentage (50%).",
    )

    SUPER_LUCK_CRIT_RATE_BOOST = Symbol(
        None, None, None, "The critical hit rate (additive) boost from Super Luck, 10%."
    )

    CONSTRICT_LOWER_SPEED_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Constrict (and others, see DoMoveDamageLowerSpeed20) lowering speed, as a percentage (20%).",
    )

    ICE_FANG_FREEZE_CHANCE = Symbol(
        None, None, None, "The chance of Ice Fang freezing, as a percentage (15%)."
    )

    SMOG_POISON_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Smog (and others, see DoMoveDamagePoison40) poisoning, as a percentage (40%).",
    )

    LICK_PARALYZE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Lick (and others, see DoMoveDamageParalyze10) paralyzing, as a percentage (10%).",
    )

    THUNDER_FANG_PARALYZE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Thunder Fang paralyzing, as a percentage (10%).",
    )

    BITE_CRINGE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Bite (and others, see DoMoveDamageCringe20) inflicting the cringe status, as a percentage (20%)",
    )

    SKY_ATTACK_CRINGE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Sky Attack inflicting the cringe status, as a percentage (25%).",
    )

    ICE_FANG_CRINGE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Ice Fang inflicting the cringe status, as a percentage (25%).",
    )

    BLAZE_KICK_BURN_CHANCE = Symbol(
        None, None, None, "The chance of Blaze Kick burning, as a percentage (10%)."
    )

    FLAMETHROWER_BURN_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Flamethrower (and others, see DoMoveDamageBurn10) burning, as a percentage (10%).",
    )

    DIZZY_PUNCH_CONFUSE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Dizzy Punch (and others, see DoMoveDamageConfuse30) confusing, as a percentage (30%).",
    )

    SECRET_POWER_EFFECT_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Secret Power inflicting an effect, as a percentage (30%).",
    )

    METAL_CLAW_BOOST_ATTACK_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Metal Claw boosting attack, as a percentage (20%).",
    )

    TECHNICIAN_MOVE_POWER_THRESHOLD = Symbol(
        None,
        None,
        None,
        "The move power threshold for Technician (4). Moves whose base power doesn't exceed this value will receive a 50% damage boost.",
    )

    SONICBOOM_FIXED_DAMAGE = Symbol(
        None, None, None, "The amount of fixed damage dealt by SonicBoom (20)."
    )

    RAIN_ABILITY_BONUS_REGEN = Symbol(
        None,
        None,
        None,
        "The passive bonus health regen given when the weather is rain for the abilities rain dish and dry skin.",
    )

    LEECH_SEED_HP_DRAIN = Symbol(
        None, None, None, "The amount of health drained by leech seed status."
    )

    EXCLUSIVE_ITEM_EXP_BOOST = Symbol(
        None,
        None,
        None,
        "The percentage increase in experience from exp-boosting exclusive items.",
    )

    AFTERMATH_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of the Aftermath ability activating, as a percentage (50%).",
    )

    SET_DAMAGE_STATUS_DAMAGE = Symbol(
        None,
        None,
        None,
        "The fixed amount of damage dealt when the Set Damage status condition is active (30).",
    )

    INTIMIDATOR_ACTIVATION_CHANCE = Symbol(
        None, None, None, "The percentage chance that Intimidator will activate."
    )

    TYPE_ADVANTAGE_MASTER_CRIT_RATE = Symbol(
        None, None, None, "The flat critical hit rate with Type-Advantage Master, 40%."
    )

    ORAN_BERRY_HP_RESTORATION = Symbol(
        None, None, None, "The amount of HP restored by eating a Oran Berry."
    )

    SITRUS_BERRY_FULL_HP_BOOST = Symbol(
        None,
        None,
        None,
        "The permanent HP boost from eating a Sitrus Berry at full HP.",
    )

    SNORE_CRINGE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Snore inflicting the cringe status, as a percentage (30%).",
    )

    METEOR_MASH_BOOST_ATTACK_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Meteor Mash boosting attack, as a percentage (20%).",
    )

    CRUSH_CLAW_LOWER_DEFENSE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Crush Claw lowering defense, as a percentage (50%).",
    )

    BURN_DAMAGE_COOLDOWN = Symbol(
        None, None, None, "The number of turns between passive burn damage."
    )

    SHADOW_BALL_LOWER_SPECIAL_DEFENSE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Shadow Ball lowering special defense, as a percentage (20%).",
    )

    STICK_POWER = Symbol(None, None, None, "Attack power for Sticks.")

    BUBBLE_LOWER_SPEED_CHANCE = Symbol(
        None, None, None, "The chance of Bubble lowering speed, as a percentage (10%)."
    )

    ICE_BODY_BONUS_REGEN = Symbol(
        None,
        None,
        None,
        "The passive bonus health regen given when the weather is hail for the ability ice body.",
    )

    POWDER_SNOW_FREEZE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Powder Snow (and others, see DoMoveDamageFreeze15) freezing, as a percentage (15%).",
    )

    POISON_STING_POISON_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Poison Sting (and others, see DoMoveDamagePoison18) poisoning, as a percentage (18%).",
    )

    SPAWN_COOLDOWN_THIEF_ALERT = Symbol(
        None,
        None,
        None,
        "The number of turns between enemy spawns when the Thief Alert condition is active.",
    )

    POISON_FANG_POISON_CHANCE = Symbol(
        None, None, None, "The chance of Poison Fang poisoning, as a percentage (30%)."
    )

    WEATHER_MOVE_TURN_COUNT = Symbol(
        None,
        None,
        None,
        "The number of turns the moves rain dance, hail, sandstorm, sunny day and defog change the weather for. (3000)",
    )

    THUNDER_PARALYZE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Thunder (and others, see DoMoveDamageParalyze20) paralyzing, as a percentage (20%)",
    )

    THUNDERBOLT_PARALYZE_CHANCE = Symbol(
        None, None, None, "The chance of Thunderbolt paralyzing, as a percentage (15%)."
    )

    MONSTER_HOUSE_MAX_MONSTER_SPAWNS = Symbol(
        None,
        None,
        None,
        "The maximum number of monster spawns in a Monster House, 30, but multiplied by 2/3 for some reason (so the actual maximum is 45)",
    )

    TWISTER_CRINGE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Twister inflicting the cringe status, as a percentage (10%).",
    )

    SPEED_BOOST_TURNS = Symbol(
        None,
        None,
        None,
        "Number of turns (250) after which Speed Boost will trigger and increase speed by one stage.",
    )

    FAKE_OUT_CRINGE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Fake Out inflicting the cringe status, as a percentage (35%).",
    )

    THUNDER_FANG_CRINGE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Thunder Fang inflicting the cringe status, as a percentage (25%).",
    )

    FLARE_BLITZ_BURN_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Flare Blitz burning, as a percentage (25%). This value is also used for the Fire Fang burn chance.",
    )

    FLAME_WHEEL_BURN_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Flame Wheel (and others, see DoMoveDamageBurn10FlameWheel) burning, as a percentage (10%).",
    )

    PSYBEAM_CONFUSE_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Psybeam (and others, see DoMoveDamageConfuse10) confusing, as a percentage (10%).",
    )

    TRI_ATTACK_STATUS_CHANCE = Symbol(
        None,
        None,
        None,
        "The chance of Tri Attack inflicting any status condition, as a percentage (20%).",
    )

    MIRACLE_CHEST_EXP_BOOST = Symbol(
        None,
        None,
        None,
        "The percentage increase in experience from the Miracle Chest item",
    )

    WONDER_CHEST_EXP_BOOST = Symbol(
        None,
        None,
        None,
        "The percentage increase in experience from the Wonder Chest item",
    )

    SPAWN_CAP_WITH_MONSTER_HOUSE = Symbol(
        None,
        None,
        None,
        "The maximum number of enemies that can spawn on a floor with a monster house, not counting those in the monster house (4).",
    )

    POISON_DAMAGE_COOLDOWN = Symbol(
        None, None, None, "The number of turns between passive poison damage."
    )

    LEECH_SEED_DAMAGE_COOLDOWN = Symbol(
        None, None, None, "The number of turns between leech seed health drain."
    )

    THROWN_ITEM_HIT_CHANCE = Symbol(
        None, None, None, "Chance of a hurled item hitting the target (90%)."
    )

    GEO_PEBBLE_DAMAGE = Symbol(None, None, None, "Damage dealt by Geo Pebbles.")

    GRAVELEROCK_DAMAGE = Symbol(None, None, None, "Damage dealt by Gravelerocks.")

    RARE_FOSSIL_DAMAGE = Symbol(None, None, None, "Damage dealt by Rare Fossils.")

    GINSENG_CHANCE_3 = Symbol(
        None,
        None,
        None,
        "The percentage chance for...something to be set to 3 in a calculation related to the Ginseng boost.",
    )

    ZINC_STAT_BOOST = Symbol(
        None, None, None, "The permanent special defense boost from ingesting a Zinc."
    )

    IRON_STAT_BOOST = Symbol(
        None, None, None, "The permanent defense boost from ingesting an Iron."
    )

    CALCIUM_STAT_BOOST = Symbol(
        None, None, None, "The permanent special attack boost from ingesting a Calcium."
    )

    WISH_BONUS_REGEN = Symbol(
        None, None, None, "The passive bonus regen given by the wish status condition."
    )

    DRAGON_RAGE_FIXED_DAMAGE = Symbol(
        None, None, None, "The amount of fixed damage dealt by Dragon Rage (30)."
    )

    CORSOLA_TWIG_POWER = Symbol(None, None, None, "Attack power for Corsola Twigs.")

    CACNEA_SPIKE_POWER = Symbol(None, None, None, "Attack power for Cacnea Spikes.")

    GOLD_FANG_POWER = Symbol(None, None, None, "Attack power for Gold Fangs.")

    SILVER_SPIKE_POWER = Symbol(None, None, None, "Attack power for Silver Spikes.")

    IRON_THORN_POWER = Symbol(None, None, None, "Attack power for Iron Thorns.")

    SCOPE_LENS_CRIT_RATE_BOOST = Symbol(
        None,
        None,
        None,
        "The critical hit rate (additive) boost from the Scope Lens/Patsy Band items and the Sharpshooter IQ skill, 15%.",
    )

    HEALING_WISH_HP_RESTORATION = Symbol(
        None,
        None,
        None,
        "The amount of HP restored by Healing Wish (999). This also applies to Lunar Dance.",
    )

    ME_FIRST_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The damage multiplier applied to attacks copied by Me First, as a fixed-point number with 8 fraction bits (1.5).",
    )

    FACADE_DAMAGE_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The Facade damage multiplier for users with a status condition, as a binary fixed-point number with 8 fraction bits (0x200 -> 2x).",
    )

    IMPRISON_TURN_RANGE = Symbol(
        None,
        None,
        None,
        "The turn range for the Paused status inflicted by Imprison, [3, 6).\n\ntype: int16_t[2]",
    )

    SLEEP_TURN_RANGE = Symbol(
        None,
        None,
        None,
        "Appears to control the range of turns for which the sleep condition can last.\n\nThe first two bytes are the low value of the range, and the later two bytes are the high value.",
    )

    NIGHTMARE_TURN_RANGE = Symbol(
        None,
        None,
        None,
        "The turn range for the Nightmare status inflicted by Nightmare, [4, 8).\n\ntype: int16_t[2]",
    )

    BURN_DAMAGE_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The extra damage multiplier for moves when the attacker is burned, as a fixed-point number with 8 fraction bits (the raw value is 0xCC, which is close to 0.8).\n\nUnlike in the main series, this multiplier is applied regardless of whether the move being used is physical or special.",
    )

    REST_TURN_RANGE = Symbol(
        None,
        None,
        None,
        "The turn range for the Napping status inflicted by Rest, [1, 4).\n\ntype: int16_t[2]",
    )

    MATCHUP_SUPER_EFFECTIVE_MULTIPLIER_ERRATIC_PLAYER = Symbol(
        None,
        None,
        None,
        "The damage multiplier corresponding to MATCHUP_SUPER_EFFECTIVE when Erratic Player is active, as a fixed-point number with 8 fraction bits (the raw value is 0x1B3, the closest possible representation of 1.7).",
    )

    MATCHUP_IMMUNE_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The damage multiplier corresponding to MATCHUP_IMMUNE, as a fixed-point number with 8 fraction bits (0.5).",
    )

    SPORT_CONDITION_TURN_RANGE = Symbol(
        None,
        None,
        None,
        "The turn range for the sport conditions activated by Mud Sport and Water Sport, [10, 12).\n\ntype: int16_t[2]",
    )

    SURE_SHOT_TURN_RANGE = Symbol(
        None,
        None,
        None,
        "The turn range for the Sure Shot status inflicted by Mind Reader and Lock-On, [10, 12).\n\ntype: int16_t[2]",
    )

    DETECT_BAND_MOVE_ACCURACY_DROP = Symbol(
        None,
        None,
        None,
        "The (subtractive) move accuracy drop induced on an attacker if the defender is wearing a Detect Band (30).",
    )

    TINTED_LENS_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The extra damage multiplier for not-very-effective moves when Tinted Lens is active, as a fixed-point number with 8 fraction bits (the raw value is 0x133, the closest possible representation of 1.2).",
    )

    SMOKESCREEN_TURN_RANGE = Symbol(
        None,
        None,
        None,
        "The turn range for the Whiffer status inflicted by Smokescreen, [1, 4).\n\ntype: int16_t[2]",
    )

    SHADOW_FORCE_DAMAGE_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The damage multiplier for Shadow Force, as a fixed-point number with 8 fraction bits (2).",
    )

    DIG_DAMAGE_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The damage multiplier for Dig, as a fixed-point number with 8 fraction bits (2).",
    )

    DIVE_DAMAGE_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The damage multiplier for Dive, as a fixed-point number with 8 fraction bits (2).",
    )

    BOUNCE_DAMAGE_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The damage multiplier for Bounce, as a fixed-point number with 8 fraction bits (2).",
    )

    POWER_PITCHER_DAMAGE_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The multiplier for projectile damage from Power Pitcher (1.5), as a binary fixed-point number (8 fraction bits)",
    )

    QUICK_DODGER_MOVE_ACCURACY_DROP = Symbol(
        None,
        None,
        None,
        "The (subtractive) move accuracy drop induced on an attacker if the defender has the Quick Dodger IQ skill (10).",
    )

    MATCHUP_NOT_VERY_EFFECTIVE_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The damage multiplier corresponding to MATCHUP_NOT_VERY_EFFECTIVE, as a fixed-point number with 8 fraction bits (the raw value is 0x1B4, the closest possible representation of 1/√2).",
    )

    MATCHUP_SUPER_EFFECTIVE_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The damage multiplier corresponding to MATCHUP_SUPER_EFFECTIVE, as a fixed-point number with 8 fraction bits (the raw value is 0x166, the closest possible representation of 1.4).",
    )

    MATCHUP_NEUTRAL_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The damage multiplier corresponding to MATCHUP_NEUTRAL, as a fixed-point number with 8 fraction bits (1).",
    )

    MATCHUP_IMMUNE_MULTIPLIER_ERRATIC_PLAYER = Symbol(
        None,
        None,
        None,
        "The damage multiplier corresponding to MATCHUP_IMMUNE when Erratic Player is active, as a fixed-point number with 8 fraction bits (0.25).",
    )

    MATCHUP_NOT_VERY_EFFECTIVE_MULTIPLIER_ERRATIC_PLAYER = Symbol(
        None,
        None,
        None,
        "The damage multiplier corresponding to MATCHUP_NOT_VERY_EFFECTIVE when Erratic Player is active, as a fixed-point number with 8 fraction bits (0.5).",
    )

    MATCHUP_NEUTRAL_MULTIPLIER_ERRATIC_PLAYER = Symbol(
        None,
        None,
        None,
        "The damage multiplier corresponding to MATCHUP_NEUTRAL when Erratic Player is active, as a fixed-point number with 8 fraction bits (1).",
    )

    AIR_BLADE_DAMAGE_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The multiplier for damage from the Air Blade (1.5), as a binary fixed-point number (8 fraction bits)",
    )

    KECLEON_SHOP_BOOST_CHANCE_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The boosted kecleon shop spawn chance multiplier (~1.2) as a binary fixed-point number (8 fraction bits).",
    )

    HIDDEN_STAIRS_SPAWN_CHANCE_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The hidden stairs spawn chance multiplier (~1.2) as a binary fixed-point number (8 fraction bits), if applicable. See ShouldBoostHiddenStairsSpawnChance in overlay 29.",
    )

    YAWN_TURN_RANGE = Symbol(
        None,
        None,
        None,
        "The turn range for the Yawning status inflicted by Yawn, [2, 2].\n\ntype: int16_t[2]",
    )

    SPEED_BOOST_TURN_RANGE = Symbol(
        None,
        None,
        None,
        "Appears to control the range of turns for which a speed boost can last.\n\nThe first two bytes are the low value of the range, and the later two bytes are the high value.",
    )

    SOLARBEAM_DAMAGE_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The default damage multiplier for SolarBeam, as a fixed-point number with 8 fraction bits (2).",
    )

    SKY_ATTACK_DAMAGE_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The damage multiplier for Sky Attack, as a fixed-point number with 8 fraction bits (2).",
    )

    RAZOR_WIND_DAMAGE_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The damage multiplier for Razor Wind, as a fixed-point number with 8 fraction bits (2).",
    )

    FOCUS_PUNCH_DAMAGE_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The damage multiplier for Focus Punch, as a fixed-point number with 8 fraction bits (2).",
    )

    SKULL_BASH_DAMAGE_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The damage multiplier for Skull Bash, as a fixed-point number with 8 fraction bits (2).",
    )

    FLY_DAMAGE_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The damage multiplier for Fly, as a fixed-point number with 8 fraction bits (2).",
    )

    WEATHER_BALL_TYPE_TABLE = Symbol(
        None,
        None,
        None,
        "Maps each weather type (by index, see enum weather_id) to the corresponding Weather Ball type.\n\ntype: struct type_id_8[8]",
    )

    LAST_RESORT_DAMAGE_MULT_TABLE = Symbol(
        None,
        None,
        None,
        "Table of damage multipliers for Last Resort for different numbers of moves out of PP, where each entry is a binary fixed-point number with 8 fraction bits.\n\nIf n is the number of moves out of PP not counting Last Resort itself, the table is indexed by (n - 1).\n\ntype: int[4]",
    )

    SYNTHESIS_HP_RESTORATION_TABLE = Symbol(
        None,
        None,
        None,
        "Maps each weather type (by index, see enum weather_id) to the corresponding HP restoration value for Synthesis.\n\ntype: int16_t[8]",
    )

    ROOST_HP_RESTORATION_TABLE = Symbol(
        None,
        None,
        None,
        "Maps each weather type (by index, see enum weather_id) to the corresponding HP restoration value for Roost.\n\nEvery entry in this table is 40.\n\ntype: int16_t[8]",
    )

    MOONLIGHT_HP_RESTORATION_TABLE = Symbol(
        None,
        None,
        None,
        "Maps each weather type (by index, see enum weather_id) to the corresponding HP restoration value for Moonlight.\n\ntype: int16_t[8]",
    )

    MORNING_SUN_HP_RESTORATION_TABLE = Symbol(
        None,
        None,
        None,
        "Maps each weather type (by index, see enum weather_id) to the corresponding HP restoration value for Morning Sun.\n\ntype: int16_t[8]",
    )

    REVERSAL_DAMAGE_MULT_TABLE = Symbol(
        None,
        None,
        None,
        "Table of damage multipliers for Reversal/Flail at different HP ranges, where each entry is a binary fixed-point number with 8 fraction bits.\n\ntype: int[4]",
    )

    WATER_SPOUT_DAMAGE_MULT_TABLE = Symbol(
        None,
        None,
        None,
        "Table of damage multipliers for Water Spout at different HP ranges, where each entry is a binary fixed-point number with 8 fraction bits.\n\ntype: int[4]",
    )

    WRING_OUT_DAMAGE_MULT_TABLE = Symbol(
        None,
        None,
        None,
        "Table of damage multipliers for Wring Out/Crush Grip at different HP ranges, where each entry is a binary fixed-point number with 8 fraction bits.\n\ntype: int[4]",
    )

    ERUPTION_DAMAGE_MULT_TABLE = Symbol(
        None,
        None,
        None,
        "Table of damage multipliers for Eruption at different HP ranges, where each entry is a binary fixed-point number with 8 fraction bits.\n\ntype: int[4]",
    )

    WEATHER_BALL_DAMAGE_MULT_TABLE = Symbol(
        None,
        None,
        None,
        "Maps each weather type (by index, see enum weather_id) to the corresponding Weather Ball damage multiplier, where each entry is a binary fixed-point number with 8 fraction bits.\n\ntype: int[8]",
    )

    EAT_ITEM_EFFECT_IGNORE_LIST = Symbol(
        None,
        None,
        None,
        "List of item IDs that should be ignored by the ShouldTryEatItem function. The last entry is null.",
    )

    CASTFORM_WEATHER_ATTRIBUTE_TABLE = Symbol(
        None,
        None,
        None,
        "Maps each weather type (by index, see enum weather_id) to the corresponding Castform type and form.\n\ntype: struct castform_weather_attributes[8]",
    )

    BAD_POISON_DAMAGE_TABLE = Symbol(
        None,
        None,
        None,
        "Table for how much damage each tick of badly poisoned should deal. The table is filled with 0x0006, but could use different values for each entry.",
    )

    TYPE_MATCHUP_COMBINATOR_TABLE = Symbol(
        None,
        None,
        None,
        "Table of type matchup combinations.\n\nEach row corresponds to a single type matchup that results from combining two individual type matchups together. For example, combining MATCHUP_NOT_VERY_EFFECTIVE with MATCHUP_SUPER_EFFECTIVE results in MATCHUP_NEUTRAL.\n\ntype: struct type_matchup_combinator_table",
    )

    OFFENSIVE_STAT_STAGE_MULTIPLIERS = Symbol(
        None,
        None,
        None,
        "Table of multipliers for offensive stats (attack/special attack) for each stage 0-20, as binary fixed-point numbers (8 fraction bits)",
    )

    DEFENSIVE_STAT_STAGE_MULTIPLIERS = Symbol(
        None,
        None,
        None,
        "Table of multipliers for defensive stats (defense/special defense) for each stage 0-20, as binary fixed-point numbers (8 fraction bits)",
    )

    NATURE_POWER_TABLE = Symbol(
        None,
        None,
        None,
        "Maps enum nature_power_variant to the associated move ID and effect handler.\n\ntype: struct wildcard_move_desc[15]",
    )

    APPLES_AND_BERRIES_ITEM_IDS = Symbol(
        None,
        None,
        None,
        "Table of item IDs for Apples and Berries, which trigger the exclusive item effect EXCLUSIVE_EFF_RECOVER_HP_FROM_APPLES_AND_BERRIES.\n\ntype: struct item_id_16[66]",
    )

    RECRUITMENT_LEVEL_BOOST_TABLE = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: int16_t[102]",
    )

    NATURAL_GIFT_ITEM_TABLE = Symbol(
        None,
        None,
        None,
        "Maps items to their type and base power if used with Natural Gift.\n\nAny item not listed in this table explicitly will be Normal type with a base power of 1 when used with Natural Gift.\n\ntype: struct natural_gift_item_info[34]",
    )

    RANDOM_MUSIC_ID_TABLE = Symbol(
        None,
        None,
        None,
        "Table of music IDs for dungeons with a random assortment of music tracks.\n\nThis is a table with 30 rows, each with 4 2-byte music IDs. Each row contains the possible music IDs for a given group, from which the music track will be selected randomly.\n\ntype: struct music_id_16[30][4]",
    )

    SHOP_ITEM_CHANCES = Symbol(
        None,
        None,
        None,
        "8 * 6 * 3 * 0x2\n\nNote: unverified, ported from Irdkwia's notes",
    )

    MALE_ACCURACY_STAGE_MULTIPLIERS = Symbol(
        None,
        None,
        None,
        "Table of multipliers for the accuracy stat for males for each stage 0-20, as binary fixed-point numbers (8 fraction bits)",
    )

    MALE_EVASION_STAGE_MULTIPLIERS = Symbol(
        None,
        None,
        None,
        "Table of multipliers for the evasion stat for males for each stage 0-20, as binary fixed-point numbers (8 fraction bits)",
    )

    FEMALE_ACCURACY_STAGE_MULTIPLIERS = Symbol(
        None,
        None,
        None,
        "Table of multipliers for the accuracy stat for females for each stage 0-20, as binary fixed-point numbers (8 fraction bits)",
    )

    FEMALE_EVASION_STAGE_MULTIPLIERS = Symbol(
        None,
        None,
        None,
        "Table of multipliers for the evasion stat for females for each stage 0-20, as binary fixed-point numbers (8 fraction bits)",
    )

    MUSIC_ID_TABLE = Symbol(
        None,
        None,
        None,
        "List of music IDs used in dungeons with a single music track.\n\nThis is an array of 170 2-byte music IDs, and is indexed into by the music value in the floor properties struct for a given floor. Music IDs with the highest bit set (0x8000) are indexes into the RANDOM_MUSIC_ID_TABLE.\n\ntype: struct music_id_16[170] (or not a music ID if the highest bit is set)",
    )

    TYPE_MATCHUP_TABLE = Symbol(
        None,
        None,
        None,
        "Table of type matchups.\n\nEach row corresponds to the type matchups of a specific attack type, with each entry within the row specifying the type's effectiveness against a target type.\n\ntype: struct type_matchup_table",
    )

    FIXED_ROOM_MONSTER_SPAWN_STATS_TABLE = Symbol(
        None,
        None,
        None,
        "Table of stats for monsters that can spawn in fixed rooms, pointed into by the FIXED_ROOM_MONSTER_SPAWN_TABLE.\n\nThis is an array of 99 12-byte entries containing stat spreads for one monster entry each.\n\ntype: struct fixed_room_monster_spawn_stats_entry[99]",
    )

    METRONOME_TABLE = Symbol(
        None,
        None,
        None,
        "Something to do with the moves that Metronome can turn into.\n\ntype: struct wildcard_move_desc[168]",
    )

    TILESET_PROPERTIES = Symbol(None, None, None, "type: struct tileset_property[199]")

    FIXED_ROOM_PROPERTIES_TABLE = Symbol(
        None,
        None,
        None,
        "Table of properties for fixed rooms.\n\nThis is an array of 256 12-byte entries containing properties for a given fixed room ID.\n\nSee the struct definitions and End45's dungeon data document for more info.\n\ntype: struct fixed_room_properties_entry[256]",
    )

    TRAP_ANIMATION_INFO = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: struct trap_animation[26]",
    )

    ITEM_ANIMATION_INFO = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: struct item_animation[1400]",
    )

    MOVE_ANIMATION_INFO = Symbol(None, None, None, "type: struct move_animation[563]")

    EFFECT_ANIMATION_INFO = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: struct effect_animation[700]",
    )

    SPECIAL_MONSTER_MOVE_ANIMATION_INFO = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: struct special_monster_move_animation[7422]",
    )


class NaItcmOverlay10Section:
    name = "overlay10"
    description = "Appears to be used both during ground mode and dungeon mode. With dungeon mode, whereas overlay 29 contains the main dungeon engine, this overlay seems to contain routines and data for dungeon mechanics."
    loadaddress = None
    length = None
    functions = NaItcmOverlay10Functions
    data = NaItcmOverlay10Data


class NaItcmOverlay11Functions:

    UnlockScriptingLock = Symbol(
        None,
        None,
        None,
        "Unlocks a scripting lock.\n\nSets the corresponding byte to 1 on LOCK_NOTIFY_ARRAY to signal that the scripting engine should handle the unlock. Also sets a global unlock flag, used to tell the scripting engine that the state of locks have changed and they should be checked again.\n\nr0: ID of the lock to unlock",
    )

    FuncThatCallsRunNextOpcode = Symbol(
        None,
        None,
        None,
        "Called up to 16 times per frame. Exact purpose unknown.\n\nr0: Looks like a pointer to some struct containing data about the current state of scripting engine",
    )

    RunNextOpcode = Symbol(
        None,
        None,
        None,
        "Runs the next scripting opcode.\n\nContains a switch statement based on the opcode ([r0+1C]).\n\nr0: Looks like a pointer to some struct containing data about the current state of scripting engine",
    )

    HandleUnlocks = Symbol(
        None,
        None,
        None,
        "Checks if a script unlock happened by reading entries from LOCK_NOTIFY_ARRAY and handles the ones that were set.\n\nIf the global unlock flag is not set, returns immediately. If it is, the function loops LOCK_NOTIFY_ARRAY, checking for true values. If it finds one, resets it back to 0 and handles the unlock.\n\nNo params.",
    )

    LoadFileFromRomVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for LoadFileFromRom.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nr0: [output] pointer to an IO struct {ptr, len}\nr1: file path string pointer\nr2: flags",
    )

    SsbLoad2 = Symbol(None, None, None, "")

    ProcessScriptParam = Symbol(
        None,
        None,
        None,
        "Checks if the two most significant bits (0x8000 and 0x4000) are set on a given script opcode parameter, and modifies the value if so.\n\nr0: On input, the parameter. On output, the modified parameter if either of the two bits listed above is set, same parameter otherwise.",
    )

    StationLoadHanger = Symbol(None, None, None, "")

    ScriptStationLoadTalk = Symbol(None, None, None, "")

    SsbLoad1 = Symbol(None, None, None, "")

    ScriptSpecialProcessCall = Symbol(
        None,
        None,
        None,
        "Processes calls to the OPCODE_PROCESS_SPECIAL script opcode.\n\nr0: some struct containing a callback of some sort, only used for special process ID 18\nr1: special process ID\nr2: first argument, if relevant? Probably corresponds to the second parameter of OPCODE_PROCESS_SPECIAL\nr3: second argument, if relevant? Probably corresponds to the third parameter of OPCODE_PROCESS_SPECIAL\nreturn: return value of the special process if it has one, otherwise 0",
    )

    GetCoroutineInfo = Symbol(
        None,
        None,
        None,
        "Returns information about a coroutine in unionall\n\nIt's used by the CallCommon code to pull the data required to call the coroutine, so maybe the function returns data required to call a coroutine instead of info about the coroutine itself.\n\nr0: [output] Coroutine info\nr1: Coroutine ID\nreturn: True if the coroutine is valid? It's false only if the coroutine's offset is 0.",
    )

    GetSpecialRecruitmentSpecies = Symbol(
        None,
        None,
        None,
        "Returns an entry from RECRUITMENT_TABLE_SPECIES.\n\nNote: This indexes without doing bounds checking.\n\nr0: index into RECRUITMENT_TABLE_SPECIES\nreturn: enum monster_id",
    )

    PrepareMenuAcceptTeamMember = Symbol(
        None,
        None,
        None,
        "Implements SPECIAL_PROC_PREPARE_MENU_ACCEPT_TEAM_MEMBER (see ScriptSpecialProcessCall).\n\nr0: index into RECRUITMENT_TABLE_SPECIES",
    )

    InitRandomNpcJobs = Symbol(
        None,
        None,
        None,
        "Implements SPECIAL_PROC_INIT_RANDOM_NPC_JOBS (see ScriptSpecialProcessCall).\n\nr0: job type? 0 is a random NPC job, 1 is a bottle mission\nr1: ?",
    )

    GetRandomNpcJobType = Symbol(
        None,
        None,
        None,
        "Implements SPECIAL_PROC_GET_RANDOM_NPC_JOB_TYPE (see ScriptSpecialProcessCall).\n\nreturn: job type?",
    )

    GetRandomNpcJobSubtype = Symbol(
        None,
        None,
        None,
        "Implements SPECIAL_PROC_GET_RANDOM_NPC_JOB_SUBTYPE (see ScriptSpecialProcessCall).\n\nreturn: job subtype?",
    )

    GetRandomNpcJobStillAvailable = Symbol(
        None,
        None,
        None,
        "Implements SPECIAL_PROC_GET_RANDOM_NPC_JOB_STILL_AVAILABLE (see ScriptSpecialProcessCall).\n\nreturn: bool",
    )

    AcceptRandomNpcJob = Symbol(
        None,
        None,
        None,
        "Implements SPECIAL_PROC_ACCEPT_RANDOM_NPC_JOB (see ScriptSpecialProcessCall).\n\nreturn: bool",
    )

    GroundMainLoop = Symbol(
        None,
        None,
        None,
        "Appears to be the main loop for ground mode.\n\nBased on debug print statements and general code structure, it seems contain a core loop, and dispatches to various functions in response to different events.\n\nr0: mode, which is stored globally and used in switch statements for dispatch\nreturn: return code",
    )

    GetAllocArenaGround = Symbol(
        None,
        None,
        None,
        "The GetAllocArena function used for ground mode. See SetMemAllocatorParams for more information.\n\nFor (flags & 0xFF):\n  8, 15, 16: GROUND_MEMORY_ARENA_1\n  14: GROUND_MEMORY_ARENA_2\n  other: null (default arena)\n\nr0: initial memory arena pointer, or null\nr1: flags (see MemAlloc)\nreturn: memory arena pointer, or null",
    )

    GetFreeArenaGround = Symbol(
        None,
        None,
        None,
        "The GetFreeArena function used for ground mode. See SetMemAllocatorParams for more information.\n\nr0: initial memory arena pointer, or null\nr1: pointer to free\nreturn: memory arena pointer, or null",
    )

    GroundMainReturnDungeon = Symbol(
        None,
        None,
        None,
        "Implements SPECIAL_PROC_RETURN_DUNGEON (see ScriptSpecialProcessCall).\n\nNo params.",
    )

    GroundMainNextDay = Symbol(
        None,
        None,
        None,
        "Implements SPECIAL_PROC_NEXT_DAY (see ScriptSpecialProcessCall).\n\nNo params.",
    )

    JumpToTitleScreen = Symbol(
        None,
        None,
        None,
        "Implements SPECIAL_PROC_JUMP_TO_TITLE_SCREEN and SPECIAL_PROC_0x1A (see ScriptSpecialProcessCall).\n\nr0: int, argument value for SPECIAL_PROC_JUMP_TO_TITLE_SCREEN and -1 for SPECIAL_PROC_0x1A\nreturn: bool (but note that the special process ignores this and always returns 0)",
    )

    ReturnToTitleScreen = Symbol(
        None,
        None,
        None,
        "Implements SPECIAL_PROC_RETURN_TO_TITLE_SCREEN (see ScriptSpecialProcessCall).\n\nr0: fade duration\nreturn: bool (but note that the special process ignores this and always returns 0)",
    )

    ScriptSpecialProcess0x16 = Symbol(
        None,
        None,
        None,
        "Implements SPECIAL_PROC_0x16 (see ScriptSpecialProcessCall).\n\nr0: bool",
    )

    IsScreenFadeInProgress = Symbol(
        None,
        None,
        None,
        "Used for example in the handler functions of the top screen types in ground mode to check whether the top screen fade is complete or not.\n\nreturn: True if the top screen is still fading, false if it's done fading.",
    )

    LoadBackgroundAttributes = Symbol(
        None,
        None,
        None,
        "Open and read an entry from the MAP_BG/bg_list.dat\n\nDocumentation on this format can be found here:\nhttps://github.com/SkyTemple/skytemple-files/tree/55b3017631a8a1b0f106111ef91a901dc394c6df/skytemple_files/graphics/bg_list_dat\n\nr0: [output] The entry\nr1: background ID",
    )

    LoadMapType10 = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: [output] buffer_ptr\nr1: map_id\nr2: dungeon_info_str\nr3: additional_info",
    )

    LoadMapType11 = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: [output] buffer_ptr\nr1: map_id\nr2: dungeon_info_str\nr3: additional_info",
    )

    GetSpecialLayoutBackground = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: bg_id\nr1: dungeon_info_str\nr2: additional_info\nr3: copy_fixed_room_layout",
    )

    SetAnimDataFields = Symbol(
        None,
        None,
        None,
        "Sets some fields on the animation struct?\n\nr0: animation pointer\nr1: ?",
    )

    SetAnimDataFieldsWrapper = Symbol(
        None,
        None,
        None,
        "Calls SetAnimDataFields with the second argument right-shifted by 16.",
    )

    InitAnimDataFromOtherAnimData = Symbol(
        None,
        None,
        None,
        "Appears to partially copy some animation data into another animation struct, plus doing extra initialization on the destination struct.\n\nr0: dst\nr1: src",
    )

    SetAnimDataFields2 = Symbol(
        None,
        None,
        None,
        "Sets some fields on the animation struct, based on the params?\n\nr0: animation pointer\nr1: flags\nr2: ?",
    )

    GetIdleAnimationType = Symbol(
        None,
        None,
        None,
        "Given a monster species, returns the type of idle animation it should have.\n\nPossible values are 'freeze animation #0' (0x300), 'loop animation #7' (0x807) and 'freeze animation #7' (0x307).\n\nr0: Monster ID\nr1: (?) Could contain data about the animation the monster is currently playing\nreturn: Animation data",
    )

    LoadObjectAnimData = Symbol(
        None,
        None,
        None,
        "Loads the animation (WAN) data for a given object index?\n\nr0: animation pointer\nr1: object index\nr2: flags",
    )

    InitAnimDataFromOtherAnimDataVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for InitAnimDataFromOtherAnimData.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nr0: dst\nr1: src",
    )

    AnimRelatedFunction = Symbol(
        None,
        None,
        None,
        "Does more stuff related to animations...probably?\n\nr0: animation pointer?\nothers: ?",
    )

    AllocAndInitPartnerFollowDataAndLiveActorList = Symbol(
        None,
        None,
        None,
        "Allocate and initialize the partner follow data and the live actor list (in GROUND_STATE_PTRS)\n\nNo params.",
    )

    InitPartnerFollowDataAndLiveActorList = Symbol(
        None,
        None,
        None,
        "Initialize the partner follow data and the live actor list (in GROUND_STATE_PTRS, doesn’t perform the allocation of the structures)\n\nNo params.",
    )

    DeleteLiveActor = Symbol(
        None,
        None,
        None,
        "Remove the actor from the overworld actor list (in GROUND_STATE_PTRS)\n\nr0: the index of the actor in the live actor list",
    )

    ChangeActorAnimation = Symbol(
        None,
        None,
        None,
        "Used by the SetAnimation opcode to change the animation of an actor.\n\nIt's responsible for breaking down the SetAnimation parameter and determining which animation to play and which flags to set.\n\nr0: ?\nr1: SetAnimation parameter",
    )

    InitPartnerFollowData = Symbol(
        None,
        None,
        None,
        "Initialize the partner follow data structure, without allocating it (in GROUND_STATE_PTRS)\n\nNo params.",
    )

    GetDirectionLiveActor = Symbol(
        None,
        None,
        None,
        "Put the direction of the actor in the destination\n\nr0: live actor\nr1: destination address (1 byte)",
    )

    SetDirectionLiveActor = Symbol(
        None,
        None,
        None,
        "Store the direction in the actor structure\n-1 input is ignored\nUnsure if this change the animation\n\nr0: live actor\nr1: direction",
    )

    CreateTeamInfoBox = Symbol(
        None,
        None,
        None,
        "Creates a window containing team information (rank and money carried) for the top-level menu in ground mode. Also see struct team_info_box.\n\nThe new window will always default to TEAM_INFO_BOX_DEFAULT_WINDOW_PARAMS.\n\nreturn: window_id",
    )

    CloseTeamInfoBox = Symbol(
        None,
        None,
        None,
        "Closes a window created with CreateTeamInfoBox.\n\nr0: window_id",
    )

    IsTeamInfoBoxActive = Symbol(
        None,
        None,
        None,
        "This is a guess.\n\nChecks if the state of a team info box is not 5.\n\nr0: window_id\nreturn: bool",
    )

    UpdateTeamInfoBox = Symbol(
        None,
        None,
        None,
        "Window update function for team info boxes.\n\nr0: window pointer",
    )

    CreateTopGroundMenu = Symbol(
        None,
        None,
        None,
        "Creates a parent menu (containing Items, Team, etc.) and two other windows upon pressing X in the overworld.\n\nreturn: always 1",
    )

    CloseTopGroundMenu = Symbol(
        None,
        None,
        None,
        "Closes the three windows created by CreateOverworldMenu.\n\nNo params.",
    )

    UpdateTopGroundMenu = Symbol(
        None,
        None,
        None,
        "Window update function for the top-level ground mode menu.\n\nreturn: status code",
    )

    IsBagNotEmpty = Symbol(
        None,
        None,
        None,
        "Checks if the bag has at least one valid item. Notably used in CreateTopGroundMenu to decide if the 'Items' option should be enabled.\n\nreturn: bool",
    )

    SprintfStatic = Symbol(
        None,
        None,
        None,
        "Statically defined copy of sprintf(3) in overlay 11. See arm9.yml for more information.\n\nr0: str\nr1: format\n...: variadic\nreturn: number of characters printed, excluding the null-terminator",
    )

    GetExclusiveItemRequirements = Symbol(
        None,
        None,
        None,
        "Used to calculate the items required to get a certain exclusive item in the swap shop.\n\nr0: ?\nr1: ?",
    )

    HandleControlsTopScreenGround = Symbol(
        None,
        None,
        None,
        "Handles the controls top screen display in the overworld.\n\nFor some reason the implementation seems considerably jankier in ground mode. In dungeon mode there's this structure for the top screen that has handlers for creating, updating and closing the various top screen layouts in a sort of polymorphic way. Here there's just a separate function for every layout that gets called every frame and seems to have a switch-case to handle everything about it.\n\nNo params.",
    )

    GetDungeonMapPos = Symbol(
        None,
        None,
        None,
        "Checks if a dungeon should be displayed on the map and the position where it should be displayed if so.\n\nr0: [Output] Buffer where the coordinates of the map marker will be stored. The coordinates are shifted 8 bits to the left, so they are probably fixed-point numbers instead of integers.\nr1: Dungeon ID\nreturn: True if the dungeon should be displayed on the map, false otherwise.",
    )

    WorldMapSetMode = Symbol(
        None,
        None,
        None,
        "Function called by the script function 'worldmap_SetMode'\nDefine the mode of the world map, which can among other things be used to decide if the player character should appear on the world map\nThe mode is set even if no world map is set\n\nr0: world map mode",
    )

    WorldMapSetCamera = Symbol(
        None,
        None,
        None,
        "Function called with the script function 'worldmap_SetCamera'.\nSet the map marker the world map should try to center on (while still ensuring it doesn't go over the background border)\nHas no effect if no map is currently set\n\nr0: map marker id",
    )

    StatusUpdate = Symbol(
        None,
        None,
        None,
        "Implements SPECIAL_PROC_STATUS_UPDATE (see ScriptSpecialProcessCall).\n\nNo params.",
    )

    HandleTeamStatsGround = Symbol(
        None,
        None,
        None,
        "Handles the team stats top screen display in the overworld.\n\nFor some reason the implementation seems considerably jankier in ground mode. In dungeon mode there's this structure for the top screen that has handlers for creating, updating and closing the various top screen layouts in a sort of polymorphic way. Here there's just a separate function for every layout that gets called every frame and seems to have a switch-case to handle everything about it.\n\nNo params.",
    )


class NaItcmOverlay11Data:

    OVERLAY11_UNKNOWN_TABLE__NA_2316A38 = Symbol(
        None,
        None,
        None,
        "Multiple entries are pointers to the string 'script.c'\n\nNote: unverified, ported from Irdkwia's notes\n\ntype: undefined4[40]",
    )

    SCRIPT_COMMAND_PARSING_DATA = Symbol(
        None, None, None, "Used by ScriptCommandParsing somehow"
    )

    SCRIPT_OP_CODE_NAMES = Symbol(
        None,
        None,
        None,
        "Opcode name strings pointed to by entries in SCRIPT_OP_CODES (script_opcode::name)",
    )

    SCRIPT_OP_CODES = Symbol(
        None,
        None,
        None,
        "Table of opcodes for the script engine. There are 383 8-byte entries.\n\nThese opcodes underpin the various ExplorerScript functions you can call in the SkyTemple SSB debugger.\n\ntype: struct script_opcode_table",
    )

    OVERLAY11_DEBUG_STRINGS = Symbol(
        None,
        None,
        None,
        "Strings used with various debug printing functions throughout the overlay",
    )

    C_ROUTINE_NAMES = Symbol(
        None,
        None,
        None,
        "Common routine name strings pointed to by entries in C_ROUTINES (common_routine::name)",
    )

    C_ROUTINES = Symbol(
        None,
        None,
        None,
        "Common routines used within the unionall.ssb script (the master script). There are 701 8-byte entries.\n\nThese routines underpin the ExplorerScript coroutines you can call in the SkyTemple SSB debugger.\n\ntype: struct common_routine_table",
    )

    GROUND_WEATHER_TABLE = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: struct ground_weather_entry[12]",
    )

    GROUND_WAN_FILES_TABLE = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: char[343][12]",
    )

    OBJECTS = Symbol(
        None,
        None,
        None,
        "Table of objects for the script engine, which can be placed in scenes. There are a version-dependent number of 12-byte entries.\n\ntype: struct script_object[length / 12]",
    )

    RECRUITMENT_TABLE_LOCATIONS = Symbol(
        None,
        None,
        None,
        "Table of dungeon IDs corresponding to entries in RECRUITMENT_TABLE_SPECIES.\n\ntype: struct dungeon_id_16[22]",
    )

    RECRUITMENT_TABLE_LEVELS = Symbol(
        None,
        None,
        None,
        "Table of levels for recruited Pokémon, corresponding to entries in RECRUITMENT_TABLE_SPECIES.\n\ntype: int16_t[22]",
    )

    RECRUITMENT_TABLE_SPECIES = Symbol(
        None,
        None,
        None,
        "Table of Pokémon recruited at special locations, such as at the ends of certain dungeons (e.g., Dialga or the Seven Treasures legendaries) or during a cutscene (e.g., Cresselia and Manaphy).\n\nInterestingly, this includes both Heatran genders. It also includes Darkrai for some reason?\n\ntype: struct monster_id_16[22]",
    )

    LEVEL_TILEMAP_LIST = Symbol(
        None,
        None,
        None,
        "Irdkwia's notes: FIXED_FLOOR_GROUND_ASSOCIATION\n\ntype: struct level_tilemap_list_entry[81]",
    )

    SETANIMATION_TABLE = Symbol(
        None,
        None,
        None,
        "Table that associates the parameter of the SetAnimation scripting opcode to animation data.\n\nThe first entry is unused and has a value of 0xFFFF.",
    )

    TEAM_INFO_BOX_DEFAULT_WINDOW_PARAMS = Symbol(
        None, None, None, "Default window_params for a team_info_box."
    )

    OVERLAY11_OVERLAY_LOAD_TABLE = Symbol(
        None,
        None,
        None,
        "The overlays that can be loaded while this one is loaded.\n\nEach entry is 16 bytes, consisting of:\n- overlay group ID (see arm9.yml or enum overlay_group_id in the C headers for a mapping between group ID and overlay number)\n- function pointer to entry point\n- function pointer to destructor\n- possibly function pointer to frame-update function?\n\ntype: struct overlay_load_entry[21]",
    )

    UNIONALL_RAM_ADDRESS = Symbol(None, None, None, "[Runtime]")

    GROUND_STATE_MAP = Symbol(None, None, None, "[Runtime]")

    GROUND_STATE_WEATHER = Symbol(
        None, None, None, "[Runtime] Same structure format as GROUND_STATE_MAP"
    )

    GROUND_STATE_PTRS = Symbol(
        None,
        None,
        None,
        "Host pointers to multiple structure used for performing an overworld scene\n\ntype: struct main_ground_data",
    )

    WORLD_MAP_MODE = Symbol(None, None, None, "The current world map")


class NaItcmOverlay11Section:
    name = "overlay11"
    description = "The script engine.\n\nThis is the 'main' overlay of ground mode. The script engine is what runs the ground mode scripts contained in the SCRIPT folder, which are written in a custom scripting language. These scripts encode things like cutscenes, screen transitions, ground mode events, and tons of other things related to ground mode."
    loadaddress = None
    length = None
    functions = NaItcmOverlay11Functions
    data = NaItcmOverlay11Data


class NaItcmOverlay12Functions:

    pass


class NaItcmOverlay12Data:

    pass


class NaItcmOverlay12Section:
    name = "overlay12"
    description = "Unused; all zeroes."
    loadaddress = None
    length = None
    functions = NaItcmOverlay12Functions
    data = NaItcmOverlay12Data


class NaItcmOverlay13Functions:

    EntryOverlay13 = Symbol(
        None,
        None,
        None,
        "Main function of this overlay.\n\nNote: unverified, ported from Irdkwia's notes\n\nNo params.",
    )

    ExitOverlay13 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nNo params."
    )

    Overlay13SwitchFunctionNa238A1C8 = Symbol(
        None,
        None,
        None,
        "Handles the 'return' value from MENU_PERSONALITY_TEST called by scripts. \n\nreturn: int?",
    )

    Overlay13SwitchFunctionNa238A574 = Symbol(
        None,
        None,
        None,
        "Handles the menus and dialogue boxes associated with the personality quiz.\n\nNo params.",
    )

    GetPersonality = Symbol(
        None,
        None,
        None,
        "Returns the personality obtained after answering all the questions.\n\nThe value to return is determined by checking the points obtained for each the personalities and returning the one with the highest amount of points.\n\nreturn: Personality (0-15)",
    )

    GetOptionStringFromID = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes. The first parameter and the return value point to the same string (which is passed directly into PreprocessString as the first argument), so I'm not sure why they're named differently... Seems like a mistake?\n\nr0: menu_id\nr1: option_id\nreturn: process",
    )

    WaitForNextStep = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: switch_case",
    )


class NaItcmOverlay13Data:

    QUIZ_BORDER_COLOR_TABLE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    PORTRAIT_ATTRIBUTES = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    QUIZ_MALE_FEMALE_BOOST_TABLE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY13_UNKNOWN_STRUCT__NA_238C024 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    QUIZ_WINDOW_PARAMS_1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    QUIZ_WINDOW_PARAMS_2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    QUIZ_WINDOW_PARAMS_3 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    QUIZ_WINDOW_PARAMS_4 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    QUIZ_MENU_ITEMS_1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    STARTERS_PARTNER_IDS = Symbol(None, None, None, "type: struct monster_id_16[21]")

    STARTERS_HERO_IDS = Symbol(None, None, None, "type: struct monster_id_16[32]")

    STARTERS_TYPE_INCOMPATIBILITY_TABLE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    STARTERS_STRINGS = Symbol(None, None, None, "Irdkwia's notes: InsightsStringIDs")

    QUIZ_QUESTION_STRINGS = Symbol(None, None, None, "0x2 * (66 questions)")

    QUIZ_ANSWER_STRINGS = Symbol(
        None, None, None, "0x2 * (175 answers + null-terminator)"
    )

    QUIZ_ANSWER_POINTS = Symbol(
        None,
        None,
        None,
        "0x10 * (174 answers?)\n\nNote: unverified, ported from Irdkwia's notes",
    )

    OVERLAY13_RESERVED_SPACE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY13_UNKNOWN_POINTER__NA_238CEA0 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY13_UNKNOWN_POINTER__NA_238CEA4 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY13_UNKNOWN_POINTER__NA_238CEA8 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    QUIZ_WINDOW_PARAMS_5 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    QUIZ_WINDOW_PARAMS_6 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    QUIZ_DEBUG_MENU_ITEMS = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY13_UNKNOWN_STRUCT__NA_238CF14 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    QUIZ_QUESTION_ANSWER_ASSOCIATIONS = Symbol(
        None,
        None,
        None,
        "0x2 * (66 questions)\n\nNote: unverified, ported from Irdkwia's notes",
    )


class NaItcmOverlay13Section:
    name = "overlay13"
    description = "Controls the personality test, including the available partners and playable Pokémon. The actual personality test questions are stored in the MESSAGE folder."
    loadaddress = None
    length = None
    functions = NaItcmOverlay13Functions
    data = NaItcmOverlay13Data


class NaItcmOverlay14Functions:

    SentrySetupState = Symbol(
        None,
        None,
        None,
        "Allocates and initializes the sentry duty struct.\n\nPossibly the entrypoint of this overlay?\n\nr0: controls initial game state? If 2, the minigame starts in state 4 rather than state 6.\nreturn: always 1",
    )

    SentryUpdateDisplay = Symbol(
        None,
        None,
        None,
        "Seems to update various parts of the display, such as the round number.\n\nNo params.",
    )

    SentrySetExitingState = Symbol(
        None,
        None,
        None,
        "Sets the completion state to exiting, triggering the minigame to run its exit sequence.\n\nNo params.",
    )

    SentryRunState = Symbol(
        None,
        None,
        None,
        "Run the minigame according to the current game state, or handle the transition to a new state if one has been set.\n\nThe game is implemented using the state machine programming pattern. This function appears to contain the top-level code for running a single 'turn' of the state machine, although presumably there's a higher level game engine that's calling this function in a loop somewhere.\n\nreturn: return code for the engine driving the minigame? Seems like 1 to keep going and 4 to stop",
    )

    SentrySetStateIntermediate = Symbol(
        None,
        None,
        None,
        "Queues up a new intermediate game state to transition to, where the transition handler will be called immediately by SentryRunState after the current state handler has returned.\n\nr0: new state",
    )

    SentryState0 = Symbol(None, None, None, "No params.")

    SentryState1 = Symbol(None, None, None, "No params.")

    SentryState2 = Symbol(None, None, None, "No params.")

    SentryState3 = Symbol(None, None, None, "No params.")

    SentryState4 = Symbol(None, None, None, "No params.")

    SentryStateExit = Symbol(
        None, None, None, "State 0x5: Exit (wraps SentrySetExitingState).\n\nNo params."
    )

    SentryState6 = Symbol(None, None, None, "No params.")

    SentryState7 = Symbol(
        None,
        None,
        None,
        "This state corresponds to when Loudred tells you the instructions for the minigame (STRING_ID_SENTRY_INSTRUCTIONS).\n\nNo params.",
    )

    SentryState8 = Symbol(None, None, None, "No params.")

    SentryState9 = Symbol(None, None, None, "No params.")

    SentryStateA = Symbol(
        None,
        None,
        None,
        "This state corresponds to when Loudred alerts you that someone is coming (STRING_ID_SENTRY_HERE_COMES).\n\nNo params.",
    )

    SentryStateB = Symbol(None, None, None, "No params.")

    SentryStateGenerateChoices = Symbol(
        None,
        None,
        None,
        "State 0xC: Generate the four choices for a round.\n\nNo params.",
    )

    SentryStateGetUserChoice = Symbol(
        None,
        None,
        None,
        "State 0xD: Wait for the player to select an answer.\n\nNo params.",
    )

    SentryStateFinalizeRound = Symbol(
        None,
        None,
        None,
        "State 0xE: Deal with the bookkeeping after the player has made a final choice for the round.\n\nThis includes things like incrementing the round counter. It also appears to check the final point count on the last round to determine the player's overall performance.\n\nNo params.",
    )

    SentryStateF = Symbol(None, None, None, "No params.")

    SentryState10 = Symbol(None, None, None, "No params.")

    SentryState11 = Symbol(
        None,
        None,
        None,
        "This state corresponds to when the partner tells you to try again after the player makes a wrong selection for the first time (STRING_ID_SENTRY_TRY_AGAIN).\n\nNo params.",
    )

    SentryState12 = Symbol(None, None, None, "No params.")

    SentryState13 = Symbol(
        None,
        None,
        None,
        "This state corresponds to when Loudred tells you that you're out of time (STRING_ID_SENTRY_OUT_OF_TIME).\n\nNo params.",
    )

    SentryState14 = Symbol(
        None,
        None,
        None,
        "This state corresponds to when the player is shouting their guess (STRING_ID_SENTRY_FOOTPRINT_IS_6EE), and when Loudred tells the visitor to come in (STRING_ID_SENTRY_COME_IN_6EF).\n\nNo params.",
    )

    SentryState15 = Symbol(None, None, None, "No params.")

    SentryState16 = Symbol(None, None, None, "No params.")

    SentryState17 = Symbol(
        None,
        None,
        None,
        "This state corresponds to when Loudred tells the player that they chose the wrong answer (STRING_ID_SENTRY_WRONG, STRING_ID_SENTRY_BUCK_UP).\n\nNo params.",
    )

    SentryState18 = Symbol(None, None, None, "No params.")

    SentryState19 = Symbol(
        None,
        None,
        None,
        "This state seems to be similar to state 0x14, when the player is shouting their guess (STRING_ID_SENTRY_FOOTPRINT_IS_6EC), and when Loudred tells the visitor to come in (STRING_ID_SENTRY_COME_IN_6ED), but used in a different context (different state transitions to and from this state).\n\nNo params.",
    )

    SentryState1A = Symbol(None, None, None, "No params.")

    SentryStateFinalizePoints = Symbol(
        None,
        None,
        None,
        "State 0x1B: Apply any modifiers to the player's point total, such as granting 2000 bonus points for 100% correctness.\n\nNo params.",
    )

    SentryState1C = Symbol(
        None,
        None,
        None,
        "This state corresponds to when Loudred tells the player that they chose the correct answer ('Yep! Looks like you're right!').\n\nNo params.",
    )

    SentryState1D = Symbol(None, None, None, "No params.")

    SentryState1E = Symbol(
        None,
        None,
        None,
        "This state corresponds to one of the possible dialogue options when you've finished all the rounds (STRING_ID_SENTRY_KEEP_YOU_WAITING, STRING_ID_SENTRY_THATLL_DO_IT).\n\nNo params.",
    )

    SentryState1F = Symbol(None, None, None, "No params.")

    SentryState20 = Symbol(
        None,
        None,
        None,
        "This state corresponds to one of the possible dialogue options when you've finished all the rounds (STRING_ID_SENTRY_NO_MORE_VISITORS, STRING_ID_SENTRY_THATS_ALL).\n\nNo params.",
    )

    SentryState21 = Symbol(None, None, None, "No params.")


class NaItcmOverlay14Data:

    SENTRY_DUTY_STRUCT_SIZE = Symbol(
        None, None, None, "Number of bytes in the sentry duty struct (14548)."
    )

    SENTRY_LOUDRED_MONSTER_ID = Symbol(
        None, None, None, "Monster ID for Loudred, used as the speaker ID for dialogue."
    )

    STRING_ID_SENTRY_TOP_SESSIONS = Symbol(
        None,
        None,
        None,
        "String ID 0x6D9:\n Here are the rankings for the\ntop sentry sessions.",
    )

    STRING_ID_SENTRY_INSTRUCTIONS = Symbol(
        None,
        None,
        None,
        "String ID 0x6D8:\n Look at the footprint on the top\nscreen, OK? Then identify the Pokémon![C]\n You can get only [CS:V]two wrong[CR], OK?\n[partner] will keep an eye on things!",
    )

    STRING_ID_SENTRY_HERE_COMES = Symbol(
        None,
        None,
        None,
        "String ID 0x6DA:\n Here comes a Pokémon! Check\nits footprint and tell me what it is!",
    )

    STRING_ID_SENTRY_WHOSE_FOOTPRINT = Symbol(
        None, None, None, "String ID 0x6DB:\n Whose footprint is this?[W:60]"
    )

    STRING_ID_SENTRY_TRY_AGAIN = Symbol(
        None, None, None, "String ID 0x6EB:\n Huh? I don't think so. Try again!"
    )

    STRING_ID_SENTRY_OUT_OF_TIME = Symbol(
        None,
        None,
        None,
        "String ID 0x6DC:\n [se_play:0][W:30]Out of time! Pick up the pace![W:75]",
    )

    STRING_ID_SENTRY_FOOTPRINT_IS_6EE = Symbol(
        None,
        None,
        None,
        "String ID 0x6EE:\n The footprint is [kind:]'s!\nThe footprint is [kind:]'s![W:60]",
    )

    STRING_ID_SENTRY_COME_IN_6EF = Symbol(
        None, None, None, "String ID 0x6EF:\n Heard ya! Come in, visitor![W:30]"
    )

    STRING_ID_SENTRY_WRONG = Symbol(
        None,
        None,
        None,
        "String ID 0x6F1:\n ......[se_play:0][W:30]Huh?! Looks wrong to me![W:50]",
    )

    STRING_ID_SENTRY_BUCK_UP = Symbol(
        None,
        None,
        None,
        "String ID 0x6F2 (and also used as Loudred's speaker ID after subtracting 0x5B0):\n The correct answer is\n[kind:]! Buck up! And snap to it![se_play:0][W:120]",
    )

    STRING_ID_SENTRY_FOOTPRINT_IS_6EC = Symbol(
        None,
        None,
        None,
        "String ID 0x6EC:\n The footprint is [kind:]'s!\nThe footprint is [kind:]'s![W:60]",
    )

    STRING_ID_SENTRY_COME_IN_6ED = Symbol(
        None, None, None, "String ID 0x6ED:\n Heard ya! Come in, visitor![W:30]"
    )

    STRING_ID_SENTRY_KEEP_YOU_WAITING = Symbol(
        None, None, None, "String ID 0x6F3:\n [se_play:0]Sorry to keep you waiting."
    )

    STRING_ID_SENTRY_THATLL_DO_IT = Symbol(
        None,
        None,
        None,
        "String ID 0x6F4:\n [partner] and [hero]![C]\n That'll do it! Now get back here!",
    )

    SENTRY_CHATOT_MONSTER_ID = Symbol(
        None, None, None, "Monster ID for Chatot, used as the speaker ID for dialogue."
    )

    STRING_ID_SENTRY_NO_MORE_VISITORS = Symbol(
        None,
        None,
        None,
        "String ID 0x6F5:\n [se_play:0]No more visitors! No more\nvisitors! ♪",
    )

    STRING_ID_SENTRY_THATS_ALL = Symbol(
        None,
        None,
        None,
        "String ID 0x6F6:\n OK, got that![C]\n Hey, [partner] and\n[hero]![C]\n That's all for today! Now get\nback here!",
    )

    SENTRY_GROVYLE_MONSTER_ID = Symbol(
        None,
        None,
        None,
        "Monster ID for Grovyle, which appears to be explicitly excluded when generating species choices.",
    )

    SENTRY_DEBUG_MENU_ITEMS = Symbol(None, None, None, "")

    SENTRY_DUTY_PTR = Symbol(None, None, None, "Pointer to the SENTRY_DUTY_STRUCT.")

    SENTRY_DUTY_STATE_HANDLER_TABLE = Symbol(
        None,
        None,
        None,
        "Null-terminated table of handler functions for the different states in the state machine. See SentryRunState.\n\ntype: state_handler_fn_t[35]",
    )


class NaItcmOverlay14Section:
    name = "overlay14"
    description = "Runs the sentry duty minigame."
    loadaddress = None
    length = None
    functions = NaItcmOverlay14Functions
    data = NaItcmOverlay14Data


class NaItcmOverlay15Functions:

    pass


class NaItcmOverlay15Data:

    BANK_MAIN_MENU_ITEMS = Symbol(None, None, None, "")

    BANK_WINDOW_PARAMS_1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    BANK_WINDOW_PARAMS_2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    BANK_WINDOW_PARAMS_3 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    BANK_WINDOW_PARAMS_4 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    BANK_WINDOW_PARAMS_5 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY15_RESERVED_SPACE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY15_UNKNOWN_POINTER__NA_238B180 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )


class NaItcmOverlay15Section:
    name = "overlay15"
    description = "Controls the Duskull Bank."
    loadaddress = None
    length = None
    functions = NaItcmOverlay15Functions
    data = NaItcmOverlay15Data


class NaItcmOverlay16Functions:

    pass


class NaItcmOverlay16Data:

    EVO_MENU_ITEMS_CONFIRM = Symbol(None, None, None, "")

    EVO_SUBMENU_ITEMS = Symbol(None, None, None, "")

    EVO_MAIN_MENU_ITEMS = Symbol(None, None, None, "")

    EVO_MENU_STRING_IDS = Symbol(
        None, None, None, "26*0x2\n\nNote: unverified, ported from Irdkwia's notes"
    )

    EVO_WINDOW_PARAMS_1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    EVO_WINDOW_PARAMS_2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    EVO_WINDOW_PARAMS_3 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    EVO_WINDOW_PARAMS_4 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    EVO_WINDOW_PARAMS_5 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    EVO_WINDOW_PARAMS_6 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    EVO_WINDOW_PARAMS_7 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY16_RESERVED_SPACE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY16_UNKNOWN_POINTER__NA_238CE40 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY16_UNKNOWN_POINTER__NA_238CE58 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )


class NaItcmOverlay16Section:
    name = "overlay16"
    description = "Controls Luminous Spring."
    loadaddress = None
    length = None
    functions = NaItcmOverlay16Functions
    data = NaItcmOverlay16Data


class NaItcmOverlay17Functions:

    pass


class NaItcmOverlay17Data:

    ASSEMBLY_WINDOW_PARAMS_1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    ASSEMBLY_WINDOW_PARAMS_2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    ASSEMBLY_WINDOW_PARAMS_3 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    ASSEMBLY_WINDOW_PARAMS_4 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    ASSEMBLY_WINDOW_PARAMS_5 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    ASSEMBLY_MENU_ITEMS_CONFIRM = Symbol(None, None, None, "")

    ASSEMBLY_MAIN_MENU_ITEMS_1 = Symbol(None, None, None, "")

    ASSEMBLY_MAIN_MENU_ITEMS_2 = Symbol(None, None, None, "")

    ASSEMBLY_SUBMENU_ITEMS_1 = Symbol(None, None, None, "")

    ASSEMBLY_SUBMENU_ITEMS_2 = Symbol(None, None, None, "")

    ASSEMBLY_SUBMENU_ITEMS_3 = Symbol(None, None, None, "")

    ASSEMBLY_SUBMENU_ITEMS_4 = Symbol(None, None, None, "")

    ASSEMBLY_SUBMENU_ITEMS_5 = Symbol(None, None, None, "")

    ASSEMBLY_SUBMENU_ITEMS_6 = Symbol(None, None, None, "")

    ASSEMBLY_SUBMENU_ITEMS_7 = Symbol(None, None, None, "")

    OVERLAY17_FUNCTION_POINTER_TABLE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY17_RESERVED_SPACE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY17_UNKNOWN_POINTER__NA_238BE00 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY17_UNKNOWN_POINTER__NA_238BE04 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY17_UNKNOWN_POINTER__NA_238BE08 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )


class NaItcmOverlay17Section:
    name = "overlay17"
    description = "Controls the Chimecho Assembly."
    loadaddress = None
    length = None
    functions = NaItcmOverlay17Functions
    data = NaItcmOverlay17Data


class NaItcmOverlay18Functions:

    pass


class NaItcmOverlay18Data:

    LINK_SHOP_WINDOW_PARAMS_1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    LINK_SHOP_WINDOW_PARAMS_2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    LINK_SHOP_WINDOW_PARAMS_3 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    LINK_SHOP_WINDOW_PARAMS_4 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    LINK_SHOP_WINDOW_PARAMS_5 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    LINK_SHOP_WINDOW_PARAMS_6 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    LINK_SHOP_WINDOW_PARAMS_7 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    LINK_SHOP_WINDOW_PARAMS_8 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    LINK_SHOP_WINDOW_PARAMS_9 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    LINK_SHOP_WINDOW_PARAMS_10 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    LINK_SHOP_WINDOW_PARAMS_11 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    LINK_SHOP_MENU_ITEMS_CONFIRM = Symbol(None, None, None, "")

    LINK_SHOP_SUBMENU_ITEMS_1 = Symbol(None, None, None, "")

    LINK_SHOP_SUBMENU_ITEMS_2 = Symbol(None, None, None, "")

    LINK_SHOP_MAIN_MENU_ITEMS = Symbol(None, None, None, "")

    LINK_SHOP_SUBMENU_ITEMS_3 = Symbol(None, None, None, "")

    LINK_SHOP_SUBMENU_ITEMS_4 = Symbol(None, None, None, "")

    LINK_SHOP_SUBMENU_ITEMS_5 = Symbol(None, None, None, "")

    LINK_SHOP_SUBMENU_ITEMS_6 = Symbol(None, None, None, "")

    LINK_SHOP_SUBMENU_ITEMS_7 = Symbol(None, None, None, "")

    OVERLAY18_FUNCTION_POINTER_TABLE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY18_RESERVED_SPACE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY18_UNKNOWN_POINTER__NA_238D620 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY18_UNKNOWN_POINTER__NA_238D624 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY18_UNKNOWN_POINTER__NA_238D628 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )


class NaItcmOverlay18Section:
    name = "overlay18"
    description = "Controls the Electivire Link Shop."
    loadaddress = None
    length = None
    functions = NaItcmOverlay18Functions
    data = NaItcmOverlay18Data


class NaItcmOverlay19Functions:

    GetBarItem = Symbol(
        None,
        None,
        None,
        "Gets the struct bar_item from BAR_AVAILABLE_ITEMS with the specified item ID.\n\nr0: item ID\nreturn: struct bar_item*",
    )

    GetRecruitableMonsterAll = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nreturn: int?",
    )

    GetRecruitableMonsterList = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nreturn: int?",
    )

    GetRecruitableMonsterListRestricted = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nreturn: int?",
    )


class NaItcmOverlay19Data:

    OVERLAY19_UNKNOWN_TABLE__NA_238DAE0 = Symbol(
        None, None, None, "4*0x2\n\nNote: unverified, ported from Irdkwia's notes"
    )

    BAR_UNLOCKABLE_DUNGEONS_TABLE = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: struct dungeon_id_16[6]",
    )

    BAR_RECRUITABLE_MONSTER_TABLE = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: struct monster_id_16[108]",
    )

    BAR_AVAILABLE_ITEMS = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\ntype: struct bar_item[66]",
    )

    OVERLAY19_UNKNOWN_STRING_IDS__NA_238E178 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY19_UNKNOWN_STRUCT__NA_238E1A4 = Symbol(
        None, None, None, "5*0x8\n\nNote: unverified, ported from Irdkwia's notes"
    )

    OVERLAY19_UNKNOWN_STRING_IDS__NA_238E1CC = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    BAR_WINDOW_PARAMS_1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    BAR_WINDOW_PARAMS_2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    BAR_WINDOW_PARAMS_3 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    BAR_MENU_ITEMS_CONFIRM_1 = Symbol(None, None, None, "")

    BAR_MENU_ITEMS_CONFIRM_2 = Symbol(None, None, None, "")

    OVERLAY19_UNKNOWN_STRING_IDS__NA_238E238 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    BAR_MAIN_MENU_ITEMS = Symbol(None, None, None, "")

    BAR_SUBMENU_ITEMS_1 = Symbol(None, None, None, "")

    BAR_SUBMENU_ITEMS_2 = Symbol(None, None, None, "")

    OVERLAY19_RESERVED_SPACE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY19_UNKNOWN_POINTER__NA_238E360 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY19_UNKNOWN_POINTER__NA_238E364 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )


class NaItcmOverlay19Section:
    name = "overlay19"
    description = "Controls Spinda's Juice Bar."
    loadaddress = None
    length = None
    functions = NaItcmOverlay19Functions
    data = NaItcmOverlay19Data


class NaItcmOverlay2Functions:

    pass


class NaItcmOverlay2Data:

    pass


class NaItcmOverlay2Section:
    name = "overlay2"
    description = "Controls the Nintendo WFC Settings interface, accessed from the top menu (Other > Nintendo WFC > Nintendo WFC Settings). Presumably contains code for Nintendo Wi-Fi setup."
    loadaddress = None
    length = None
    functions = NaItcmOverlay2Functions
    data = NaItcmOverlay2Data


class NaItcmOverlay20Functions:

    pass


class NaItcmOverlay20Data:

    OVERLAY20_UNKNOWN_POINTER__NA_238CF7C = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    RECYCLE_MENU_ITEMS_CONFIRM_1 = Symbol(None, None, None, "")

    RECYCLE_MENU_ITEMS_CONFIRM_2 = Symbol(None, None, None, "")

    RECYCLE_SUBMENU_ITEMS_1 = Symbol(None, None, None, "")

    RECYCLE_SUBMENU_ITEMS_2 = Symbol(None, None, None, "")

    RECYCLE_MAIN_MENU_ITEMS_1 = Symbol(None, None, None, "")

    OVERLAY20_UNKNOWN_TABLE__NA_238D014 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    RECYCLE_WINDOW_PARAMS_1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    RECYCLE_WINDOW_PARAMS_2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    RECYCLE_WINDOW_PARAMS_3 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    RECYCLE_WINDOW_PARAMS_4 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    RECYCLE_WINDOW_PARAMS_5 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    RECYCLE_WINDOW_PARAMS_6 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    RECYCLE_MAIN_MENU_ITEMS_2 = Symbol(None, None, None, "")

    RECYCLE_WINDOW_PARAMS_7 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    RECYCLE_WINDOW_PARAMS_8 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    RECYCLE_WINDOW_PARAMS_9 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    RECYCLE_WINDOW_PARAMS_10 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    RECYCLE_WINDOW_PARAMS_11 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    RECYCLE_MAIN_MENU_ITEMS_3 = Symbol(None, None, None, "")

    OVERLAY20_RESERVED_SPACE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY20_UNKNOWN_POINTER__NA_238D120 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY20_UNKNOWN_POINTER__NA_238D124 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY20_UNKNOWN_POINTER__NA_238D128 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY20_UNKNOWN_POINTER__NA_238D12C = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )


class NaItcmOverlay20Section:
    name = "overlay20"
    description = "Controls the Recycle Shop."
    loadaddress = None
    length = None
    functions = NaItcmOverlay20Functions
    data = NaItcmOverlay20Data


class NaItcmOverlay21Functions:

    pass


class NaItcmOverlay21Data:

    SWAP_SHOP_WINDOW_PARAMS_1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SWAP_SHOP_MENU_ITEMS_CONFIRM = Symbol(None, None, None, "")

    SWAP_SHOP_SUBMENU_ITEMS_1 = Symbol(None, None, None, "")

    SWAP_SHOP_SUBMENU_ITEMS_2 = Symbol(None, None, None, "")

    SWAP_SHOP_MAIN_MENU_ITEMS_1 = Symbol(None, None, None, "")

    SWAP_SHOP_MAIN_MENU_ITEMS_2 = Symbol(None, None, None, "")

    SWAP_SHOP_SUBMENU_ITEMS_3 = Symbol(None, None, None, "")

    OVERLAY21_UNKNOWN_STRING_IDS = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SWAP_SHOP_WINDOW_PARAMS_2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SWAP_SHOP_WINDOW_PARAMS_3 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SWAP_SHOP_WINDOW_PARAMS_4 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SWAP_SHOP_WINDOW_PARAMS_5 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SWAP_SHOP_WINDOW_PARAMS_6 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SWAP_SHOP_WINDOW_PARAMS_7 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SWAP_SHOP_WINDOW_PARAMS_8 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SWAP_SHOP_WINDOW_PARAMS_9 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY21_JP_STRING = Symbol(None, None, None, "合成：")

    OVERLAY21_RESERVED_SPACE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY21_UNKNOWN_POINTER__NA_238CF40 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY21_UNKNOWN_POINTER__NA_238CF44 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )


class NaItcmOverlay21Section:
    name = "overlay21"
    description = "Controls the Croagunk Swap Shop."
    loadaddress = None
    length = None
    functions = NaItcmOverlay21Functions
    data = NaItcmOverlay21Data


class NaItcmOverlay22Functions:

    pass


class NaItcmOverlay22Data:

    SHOP_WINDOW_PARAMS_1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SHOP_WINDOW_PARAMS_2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY22_UNKNOWN_STRUCT__NA_238E85C = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SHOP_MENU_ITEMS_CONFIRM = Symbol(None, None, None, "")

    SHOP_MAIN_MENU_ITEMS_1 = Symbol(None, None, None, "")

    SHOP_MAIN_MENU_ITEMS_2 = Symbol(None, None, None, "")

    SHOP_MAIN_MENU_ITEMS_3 = Symbol(None, None, None, "")

    OVERLAY22_UNKNOWN_STRING_IDS = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SHOP_WINDOW_PARAMS_3 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SHOP_WINDOW_PARAMS_4 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SHOP_WINDOW_PARAMS_5 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SHOP_WINDOW_PARAMS_6 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SHOP_WINDOW_PARAMS_7 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SHOP_WINDOW_PARAMS_8 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SHOP_WINDOW_PARAMS_9 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    SHOP_WINDOW_PARAMS_10 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY22_RESERVED_SPACE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY22_UNKNOWN_POINTER__NA_238EC60 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY22_UNKNOWN_POINTER__NA_238EC64 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY22_UNKNOWN_POINTER__NA_238EC68 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY22_UNKNOWN_POINTER__NA_238EC6C = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY22_UNKNOWN_POINTER__NA_238EC70 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )


class NaItcmOverlay22Section:
    name = "overlay22"
    description = "Controls the Kecleon Shop in Treasure Town."
    loadaddress = None
    length = None
    functions = NaItcmOverlay22Functions
    data = NaItcmOverlay22Data


class NaItcmOverlay23Functions:

    pass


class NaItcmOverlay23Data:

    OVERLAY23_UNKNOWN_VALUE__NA_238D2E8 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY23_UNKNOWN_VALUE__NA_238D2EC = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY23_UNKNOWN_STRUCT__NA_238D2F0 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    STORAGE_MENU_ITEMS_CONFIRM = Symbol(None, None, None, "")

    STORAGE_MAIN_MENU_ITEMS_1 = Symbol(None, None, None, "")

    STORAGE_MAIN_MENU_ITEMS_2 = Symbol(None, None, None, "")

    STORAGE_MAIN_MENU_ITEMS_3 = Symbol(None, None, None, "")

    STORAGE_MAIN_MENU_ITEMS_4 = Symbol(None, None, None, "")

    OVERLAY23_UNKNOWN_STRING_IDS = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    STORAGE_WINDOW_PARAMS_1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    STORAGE_WINDOW_PARAMS_2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    STORAGE_WINDOW_PARAMS_3 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    STORAGE_WINDOW_PARAMS_4 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    STORAGE_WINDOW_PARAMS_5 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    STORAGE_WINDOW_PARAMS_6 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    STORAGE_WINDOW_PARAMS_7 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    STORAGE_WINDOW_PARAMS_8 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY23_RESERVED_SPACE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY23_UNKNOWN_POINTER__NA_238D8A0 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )


class NaItcmOverlay23Section:
    name = "overlay23"
    description = (
        "Controls Kangaskhan Storage (both in Treasure Town and via Kangaskhan Rocks)."
    )
    loadaddress = None
    length = None
    functions = NaItcmOverlay23Functions
    data = NaItcmOverlay23Data


class NaItcmOverlay24Functions:

    pass


class NaItcmOverlay24Data:

    OVERLAY24_UNKNOWN_STRUCT__NA_238C508 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY24_UNKNOWN_STRUCT__NA_238C514 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DAYCARE_MENU_ITEMS_CONFIRM = Symbol(None, None, None, "")

    DAYCARE_MAIN_MENU_ITEMS = Symbol(None, None, None, "")

    OVERLAY24_UNKNOWN_STRING_IDS = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DAYCARE_WINDOW_PARAMS_1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DAYCARE_WINDOW_PARAMS_2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DAYCARE_WINDOW_PARAMS_3 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DAYCARE_WINDOW_PARAMS_4 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DAYCARE_WINDOW_PARAMS_5 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY24_RESERVED_SPACE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY24_UNKNOWN_POINTER__NA_238C600 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )


class NaItcmOverlay24Section:
    name = "overlay24"
    description = "Controls the Chansey Day Care."
    loadaddress = None
    length = None
    functions = NaItcmOverlay24Functions
    data = NaItcmOverlay24Data


class NaItcmOverlay25Functions:

    pass


class NaItcmOverlay25Data:

    OVERLAY25_UNKNOWN_STRUCT__NA_238B498 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    APPRAISAL_WINDOW_PARAMS_1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    APPRAISAL_MENU_ITEMS_CONFIRM = Symbol(None, None, None, "")

    APPRAISAL_MAIN_MENU_ITEMS = Symbol(None, None, None, "")

    APPRAISAL_SUBMENU_ITEMS = Symbol(None, None, None, "")

    OVERLAY25_UNKNOWN_STRING_IDS = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    APPRAISAL_WINDOW_PARAMS_2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    APPRAISAL_WINDOW_PARAMS_3 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    APPRAISAL_WINDOW_PARAMS_4 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    APPRAISAL_WINDOW_PARAMS_5 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    APPRAISAL_WINDOW_PARAMS_6 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    APPRAISAL_WINDOW_PARAMS_7 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    APPRAISAL_WINDOW_PARAMS_8 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY25_RESERVED_SPACE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY25_UNKNOWN_POINTER__NA_238B5E0 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )


class NaItcmOverlay25Section:
    name = "overlay25"
    description = "Controls Xatu Appraisal."
    loadaddress = None
    length = None
    functions = NaItcmOverlay25Functions
    data = NaItcmOverlay25Data


class NaItcmOverlay26Functions:

    pass


class NaItcmOverlay26Data:

    OVERLAY26_UNKNOWN_TABLE__NA_238AE20 = Symbol(
        None,
        None,
        None,
        "0x6 + 11*0xC + 0x2\n\nNote: unverified, ported from Irdkwia's notes",
    )

    OVERLAY26_RESERVED_SPACE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY26_UNKNOWN_POINTER__NA_238AF60 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY26_UNKNOWN_POINTER__NA_238AF64 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY26_UNKNOWN_POINTER__NA_238AF68 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY26_UNKNOWN_POINTER__NA_238AF6C = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY26_UNKNOWN_POINTER5__NA_238AF70 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )


class NaItcmOverlay26Section:
    name = "overlay26"
    description = "Related to mission completion. It's loaded when the dungeon completion summary is shown upon exiting a dungeon, and during the cutscenes where you collect mission rewards from clients."
    loadaddress = None
    length = None
    functions = NaItcmOverlay26Functions
    data = NaItcmOverlay26Data


class NaItcmOverlay27Functions:

    pass


class NaItcmOverlay27Data:

    OVERLAY27_UNKNOWN_VALUE__NA_238C948 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY27_UNKNOWN_VALUE__NA_238C94C = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY27_UNKNOWN_STRUCT__NA_238C950 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DISCARD_ITEMS_MENU_ITEMS_CONFIRM = Symbol(None, None, None, "")

    DISCARD_ITEMS_SUBMENU_ITEMS_1 = Symbol(None, None, None, "")

    DISCARD_ITEMS_SUBMENU_ITEMS_2 = Symbol(None, None, None, "")

    DISCARD_ITEMS_MAIN_MENU_ITEMS = Symbol(None, None, None, "")

    OVERLAY27_UNKNOWN_STRING_IDS = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DISCARD_WINDOW_PARAMS_1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DISCARD_WINDOW_PARAMS_2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DISCARD_WINDOW_PARAMS_3 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DISCARD_WINDOW_PARAMS_4 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DISCARD_WINDOW_PARAMS_5 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DISCARD_WINDOW_PARAMS_6 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DISCARD_WINDOW_PARAMS_7 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DISCARD_WINDOW_PARAMS_8 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY27_RESERVED_SPACE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY27_UNKNOWN_POINTER__NA_238CE80 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY27_UNKNOWN_POINTER__NA_238CE84 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )


class NaItcmOverlay27Section:
    name = "overlay27"
    description = "Controls the special episode item discard menu."
    loadaddress = None
    length = None
    functions = NaItcmOverlay27Functions
    data = NaItcmOverlay27Data


class NaItcmOverlay28Functions:

    pass


class NaItcmOverlay28Data:

    pass


class NaItcmOverlay28Section:
    name = "overlay28"
    description = "Controls the staff credits sequence."
    loadaddress = None
    length = None
    functions = NaItcmOverlay28Functions
    data = NaItcmOverlay28Data


class NaItcmOverlay29Functions:

    GetWeatherColorTable = Symbol(
        None,
        None,
        None,
        "Gets a pointer to the floor's color table given the current weather.\n\nThe returned table contains 1024 color entries.\n\nr0: Weather ID\nreturn: color table pointer",
    )

    DungeonAlloc = Symbol(
        None,
        None,
        None,
        "Allocates a new dungeon struct.\n\nThis updates the master dungeon pointer and returns a copy of that pointer.\n\nreturn: pointer to a newly allocated dungeon struct",
    )

    GetDungeonPtrMaster = Symbol(
        None,
        None,
        None,
        "Returns the master dungeon pointer (a global, see DUNGEON_PTR_MASTER).\n\nreturn: pointer to a newly allocated dungeon struct",
    )

    DungeonZInit = Symbol(
        None,
        None,
        None,
        "Zero-initializes the dungeon struct pointed to by the master dungeon pointer.\n\nNo params.",
    )

    DungeonFree = Symbol(
        None,
        None,
        None,
        "Frees the dungeons struct pointer to by the master dungeon pointer, and nullifies the pointer.\n\nNo params.",
    )

    RunDungeon = Symbol(
        None,
        None,
        None,
        "Called at the start of a dungeon. Initializes the dungeon struct from specified dungeon data. Includes a loop that does not break until the dungeon is cleared, and another one inside it that runs until the current floor ends.\n\nr0: Pointer to the struct containing info used to initialize the dungeon. See type dungeon_init for details.\nr1: Pointer to the dungeon data struct that will be used during the dungeon.",
    )

    EntityIsValid = Symbol(
        None,
        None,
        None,
        "Checks if an entity pointer points to a valid entity (not entity type 0, which represents no entity).\n\nr0: entity pointer\nreturn: bool",
    )

    GetFloorType = Symbol(
        None,
        None,
        None,
        "Get the current floor type.\n\nFloor types:\n  0 appears to mean the current floor is 'normal'\n  1 appears to mean the current floor is a fixed floor\n  2 means the current floor has a rescue point\n\nreturn: floor type",
    )

    TryForcedLoss = Symbol(
        None,
        None,
        None,
        "Attempts to trigger a forced loss of the type specified in dungeon::forced_loss_reason.\n\nr0: if true, the function will not check for the end of the floor condition and will skip other (unknown) actions in case of forced loss.\nreturn: true if the forced loss happens, false otherwise",
    )

    IsBossFight = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: fixed_room_id\nreturn: bool",
    )

    IsCurrentFixedRoomBossFight = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nreturn: bool",
    )

    IsMarowakTrainingMaze = Symbol(
        None,
        None,
        None,
        "Check if the current dungeon is one of the training mazes in Marowak Dojo (this excludes Final Maze).\n\nreturn: bool",
    )

    FixedRoomIsSubstituteRoom = Symbol(
        None,
        None,
        None,
        "Checks if the current fixed room is the 'substitute room' (ID 0x6E).\n\nreturn: bool",
    )

    StoryRestrictionsEnabled = Symbol(
        None,
        None,
        None,
        "Returns true if certain special restrictions are enabled.\n\nIf true, you will get kicked out of the dungeon if a team member that passes the arm9::JoinedAtRangeCheck2 check faints.\n\nreturn: !dungeon::nonstory_flag || dungeon::hidden_land_flag",
    )

    GetScenarioBalanceVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for GetScenarioBalance.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-",
    )

    FadeToBlack = Symbol(
        None,
        None,
        None,
        "Fades the screen to black across several frames.\n\nNo params.",
    )

    CheckTouchscreenArea = Symbol(
        None,
        None,
        None,
        "Checks if the currently pressed touchscreen position is within the specified area.\n\nr0: Area lower X coordinate\nr1: Area lower Y coordinate\nr2: Area upper X coordinate\nr3: Area upper Y coordinate\nreturn: True if the specified area contains the currently pressed touchscreen position, false otherwise.",
    )

    GetTrapInfo = Symbol(
        None,
        None,
        None,
        "Given a trap entity, returns the pointer to the trap info struct it contains.\n\nr0: Entity pointer\nreturn: Trap data pointer",
    )

    GetItemInfo = Symbol(
        None,
        None,
        None,
        "Given an item entity, returns the pointer to the item info struct it contains.\n\nr0: Entity pointer\nreturn: Item data pointer",
    )

    GetTileAtEntity = Symbol(
        None,
        None,
        None,
        "Returns a pointer to the tile where an entity is located.\n\nr0: pointer to entity\nreturns: pointer to tile",
    )

    UpdateEntityPixelPos = Symbol(
        None,
        None,
        None,
        "Updates an entity's pixel_pos field using the specified pixel_position struct, or its own pos field if it's null.\n\nr0: Entity pointer\nr1: Pixel position to use, or null to use the entity's own position",
    )

    CreateEnemyEntity = Symbol(
        None,
        None,
        None,
        "Creates and initializes the entity struct of a newly spawned enemy monster. Fails if there's 16 enemies on the floor already.\n\nIt could also be used to spawn fixed room allies, since those share their slots on the entity list.\n\nr0: Monster ID\nreturn: Pointer to the newly initialized entity, or null if the entity couldn't be initialized",
    )

    SpawnTrap = Symbol(
        None,
        None,
        None,
        "Spawns a trap on the floor. Fails if there are more than 64 traps already on the floor.\n\nThis modifies the appropriate fields on the dungeon struct, initializing new entries in the entity table and the trap info list.\n\nr0: trap ID\nr1: position\nr2: team (see struct trap::team)\nr3: flags (see struct trap::team)\nreturn: entity pointer for the newly added trap, or null on failure",
    )

    SpawnItemEntity = Symbol(
        None,
        None,
        None,
        "Spawns a blank item entity on the floor. Fails if there are more than 64 items already on the floor.\n\nThis initializes a new entry in the entity table and points it to the corresponding slot in the item info list.\n\nr0: position\nreturn: entity pointer for the newly added item, or null on failure",
    )

    ShouldMinimapDisplayEntity = Symbol(
        None,
        None,
        None,
        "Checks if a given entity should be displayed on the minimap\n\nr0: Entity pointer\nreturn: True if the entity should be displayed on the minimap",
    )

    ShouldDisplayEntity = Symbol(
        None,
        None,
        None,
        "Checks if an entity should be displayed or not.\n\nFor example, it returns false if the entity is an invisible enemy.\nAlso used to determine if messages that involve a certain entity should be displayed or suppressed.\n\nr0: Entity pointer\nr1: (?) Seems to be 1 for monsters and 0 for items.\nreturn: True if the entity and its associated messages should be displayed, false if they shouldn't.",
    )

    ShouldDisplayEntityWrapper = Symbol(
        None,
        None,
        None,
        "Calls ShouldDisplayEntity with r1 = 0\n\nr0: Entity pointer\nreturn: True if the entity and its associated messages should be displayed, false if they shouldn't.",
    )

    CanSeeTarget = Symbol(
        None,
        None,
        None,
        "Checks if a given monster can see another monster.\n\nCalls IsPositionActuallyInSight. Also checks if the user is blinded, if the target is invisible, etc.\nThis function is almost the same as CanTargetEntity, the only difference is that the latter calls IsPositionInSight instead.\n\nr0: User entity pointer\nr1: Target entity pointer\nreturn: True if the user can see the target, false otherwise",
    )

    CanTargetEntity = Symbol(
        None,
        None,
        None,
        "Checks if a monster can target another entity when controlled by the AI.\nMore specifically, it checks if the target is invisible, if the user can see invisible monsters, if the user is blinded and if the target position is in sight from the position of the user (this last check is done by calling IsPositionInSight with the user's and the target's position).\nThis function is almost the same as CanSeeTarget, the only difference is that the latter calls IsPositionActuallyInSight instead.\n\nr0: User entity pointer\nr1: Target entity pointer\nreturn: True if the user can target the target, false otherwise",
    )

    CanTargetPosition = Symbol(
        None,
        None,
        None,
        "Checks if a monster can target a position. This function just calls IsPositionInSight using the position of the user as the origin.\n\nr0: Entity pointer\nr1: Target position\nreturn: True if the specified monster can target the target position, false otherwise.",
    )

    GetTeamMemberIndex = Symbol(
        None,
        None,
        None,
        "Given a pointer to an entity, returns its index on the entity list, or null if the entity can't be found on the first 4 slots of the list.\n\nr0: Pointer to the entity to find\nreturn: Index of the specified entity on the entity list, or null if it's not on the first 4 slots.",
    )

    SubstitutePlaceholderStringTags = Symbol(
        None,
        None,
        None,
        "Replaces instances of a given placeholder tag by the string representation of the given entity.\n\nFrom the eos-move-effects docs (which are somewhat nebulous): 'Replaces the string at StringID [r0] by the string representation of the target [r1] (aka its name). Any message with the string manipulator '[string:StringID]' will use that string'.\n\nThe game uses various placeholder tags in its strings, which you can read about here: https://textbox.skytemple.org/.\n\nr0: string ID (unclear what this means)\nr1: entity pointer\nr2: ?",
    )

    UpdateMapSurveyorFlag = Symbol(
        None,
        None,
        None,
        "Sets the Map Surveyor flag in the dungeon struct to true if a team member has Map Surveyor, sets it to false otherwise.\n\nThis function has two variants: in the EU ROM, it will return true if the flag was changed. The NA version will return the new value of the flag instead.\n\nreturn: bool",
    )

    PointCameraToMonster = Symbol(
        None,
        None,
        None,
        "Points the camera to the specified monster.\n\nr0: Entity pointer\nr1: ?",
    )

    UpdateCamera = Symbol(
        None,
        None,
        None,
        "Called every frame. Sets the camera to the right coordinates depending on the monster it points to.\n\nIt also takes care of updating the minimap, checking which elements should be shown on it, as well as whether the screen should be black due to the blinker status.\n\nr0: ?",
    )

    ItemIsActive = Symbol(
        None,
        None,
        None,
        "Checks if a monster is holding a certain item that isn't disabled by Klutz.\n\nr0: entity pointer\nr1: item ID\nreturn: bool",
    )

    GetVisibilityRange = Symbol(
        None,
        None,
        None,
        "Returns dungeon::display_data::visibility_range. If the visibility range is 0, returns 2 instead.\n\nreturn: Visibility range of the current floor, or 2 if the visibility is 0.",
    )

    RevealWholeFloor = Symbol(
        None,
        None,
        None,
        "Sets the luminous state for the floor and marks all the tiles on the floor as revealed.\n\nMore specifically, sets dungeon::display_data::luminous to 1, sets visibility_flags::f_revealed for all tiles on the floor, calls UpdateCamera, UpdateTrapsVisibility, UpdateMinimap and logs the message 'It became brighter on the floor!'.\n\nr0: Pointer to the entity who revealed the floor",
    )

    PlayEffectAnimationEntity = Symbol(
        None,
        None,
        None,
        "Just a guess. This appears to be paired often with GetEffectAnimationField0x19, and also has calls AnimationHasMoreFrames in a loop alongside AdvanceFrame(66) calls.\n\nThe third parameter skips the loop entirely. It seems like in this case the function might just preload some animation frames for later use??\n\nr0: entity pointer\nr1: Effect ID\nr2: appears to be a flag for actually running the animation now? If this is 0, the AdvanceFrame loop is skipped entirely.\nothers: ?\nreturn: status code, or maybe the number of frames or something? Either way, -1 seems to indicate the animation being finished or something?",
    )

    PlayEffectAnimationPos = Symbol(
        None,
        None,
        None,
        "Takes a position struct in r0 and converts it to a pixel position struct before calling PlayEffectAnimationPixelPos\n\nr0: Position where the effect should be played\nr1: Effect ID\nr2: Unknown flag (same as the one in PlayEffectAnimationEntity)\nreturn: Result of call to PlayEffectAnimationPixelPos",
    )

    PlayEffectAnimationPixelPos = Symbol(
        None,
        None,
        None,
        "Seems like a variant of PlayEffectAnimationEntity that uses pixel coordinates as its first parameter instead of an entity pointer.\n\nr0: Pixel position where the effect should be played\nr1: Effect ID\nr2: Unknown flag (same as the one in PlayEffectAnimationEntity)\nreturn: Same as PlayEffectAnimationEntity",
    )

    AnimationDelayOrSomething = Symbol(
        None,
        None,
        None,
        "Called whenever most (all?) animations are played. Does not return until the animation is over.\n\nMight wait until the animation is done? Contains several loops that call AdvanceFrame.\n\nr0: ?",
    )

    UpdateStatusIconFlags = Symbol(
        None,
        None,
        None,
        "Sets a monster's status_icon_flags bitfield according to its current status effects. Does not affect a Sudowoodo in the 'permanent sleep' state (statuses::sleep == 0x7F).\n\nSome of the status effect in monster::statuses are used as an index to access an array, where every group of 8 bytes represents a bitmask. All masks are added in a bitwise OR and then stored in monster::status_icon.\n\nAlso sets icon flags for statuses::exposed, statuses::grudge, critical HP and lowered stats with explicit checks, and applies the effect of the Identifier Orb (see dungeon::identify_orb_flag).\n\nr0: entity pointer",
    )

    PlayEffectAnimation0x171Full = Symbol(
        None,
        None,
        None,
        "Just a guess. Calls PlayEffectAnimation with data from animation ID 0x171, with the third parameter of PlayEffectAnimation set to true.\n\nr0: entity pointer",
    )

    PlayEffectAnimation0x171 = Symbol(
        None,
        None,
        None,
        "Just a guess. Calls PlayEffectAnimation with data from animation ID 0x171.\n\nr0: entity pointer",
    )

    ShowPpRestoreEffect = Symbol(
        None,
        None,
        None,
        "Displays the graphical effect on a monster that just recovered PP.\n\nr0: entity pointer",
    )

    PlayEffectAnimation0x1A9 = Symbol(
        None,
        None,
        None,
        "Just a guess. Calls PlayEffectAnimation with data from animation ID 0x1A9.\n\nr0: entity pointer",
    )

    PlayEffectAnimation0x18E = Symbol(
        None,
        None,
        None,
        "Just a guess. Calls PlayEffectAnimation with data from animation ID 0x18E.\n\nr0: entity pointer",
    )

    LoadMappaFileAttributes = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nThis function processes the monster spawn list of the current floor, checking which species can spawn, capping the amount of spawnable species on the floor to 14, randomly choosing which 14 species will spawn and ensuring that the sprite size of all the species combined does not exceed the maximum of 0x58000 bytes (352 KB). Kecleon and the Decoy are always included in the random selection.\nThe function also processes the floor's item spawn lists. When loading fixed rooms from the hidden staircase, the game forces the number of spawnable species to 0.\n\nr0: quick_saved\nr1: disable_monsters\nr2: special_process",
    )

    GetItemIdToSpawn = Symbol(
        None,
        None,
        None,
        "Randomly picks an item to spawn using one of the floor's item spawn lists and returns its ID.\n\nIf the function fails to properly choose an item (due to, for example, a corrupted item list), ITEM_POKE is returned.\n\nr0: Which item list to use\nreturn: Item ID",
    )

    MonsterSpawnListPartialCopy = Symbol(
        None,
        None,
        None,
        "Copies all entries in the floor's monster spawn list that have a sprite size >= 6 to the specified buffer.\n\nThe parameter in r1 can be used to specify how many entries are already present in the buffer. Entries added by this function will be placed after those, and the total returned in r1 will account for existing entries as well.\n\nr0: [output] Buffer where the result will be stored\nr1: Current amount of entries in the buffer\nreturn: New amount of entries in the buffer",
    )

    IsOnMonsterSpawnList = Symbol(
        None,
        None,
        None,
        "Returns true if the specified monster is included in the floor's monster spawn list (the modified list after a maximum of 14 different species were chosen, not the raw list read from the mappa file).\n\nr0: Monster ID\nreturn: bool",
    )

    GetMonsterIdToSpawn = Symbol(
        None,
        None,
        None,
        "Randomly picks a monster to spawn using the floor's monster spawn list and returns its ID.\n\nr0: the spawn weight to use (0 for normal, 1 for monster house)\nreturn: monster ID",
    )

    GetMonsterLevelToSpawn = Symbol(
        None,
        None,
        None,
        "Get the level of the monster to be spawned, given its id.\n\nr0: monster ID\nreturn: Level of the monster to be spawned, or 1 if the specified ID can't be found on the floor's spawn table.",
    )

    AllocTopScreenStatus = Symbol(
        None,
        None,
        None,
        "Allocates and initializes the top_screen_status struct when entering dungeon mode.\n\nNo params.",
    )

    FreeTopScreenStatus = Symbol(
        None,
        None,
        None,
        "Gets called when leaving dungeon mode, calls FreeTopScreen and then also frees the allocated memory to the top_screen_status struct.\n\nNo params.",
    )

    InitializeTeamStats = Symbol(
        None,
        None,
        None,
        "Initializes the team stats top screen.\n\nreturn: always 1, seems unused",
    )

    UpdateTeamStatsWrapper = Symbol(
        None,
        None,
        None,
        "Contains a check and calls UpdateTeamStats in overlay10.\n\nreturn: always 1, seems unused",
    )

    FreeTeamStatsWrapper = Symbol(
        None,
        None,
        None,
        "Calls a function that calls FreeTeamStats in overlay10.\n\nreturn: always 1, seems unused",
    )

    AssignTopScreenHandlers = Symbol(
        None,
        None,
        None,
        "Sets the handler functions of the top screen type.\n\nr0: Array where the handler function pointers get written to.\nr1: init_func\nr2: update_func\nr3: ?\nstack[0]: free_func",
    )

    HandleTopScreenFades = Symbol(
        None,
        None,
        None,
        "Used to initialize and uninitialize the top screen in dungeon mode in conjunction with handling the fade status of the screen.\n\nFor example, when a fade out is done, it calls the necessary functions to close the top screen windows. When it starts fading in again, it re-creates all the necessary windows corresponding to the top screen type setting.\n\nNo params.",
    )

    FreeTopScreen = Symbol(
        None,
        None,
        None,
        "Gets called twice when fading out the top screen. First it calls the free_func of the top screen type and sets the handlers to null and on the second pass it just returns.\n\nreturn: always 1, seems unused",
    )

    GetDirectionTowardsPosition = Symbol(
        None,
        None,
        None,
        "Gets the direction in which a monster should move to go from the origin position to the target position\n\nr0: Origin position\nr1: Target position\nreturn: Direction in which to move to reach the target position from the origin position",
    )

    GetChebyshevDistance = Symbol(
        None,
        None,
        None,
        "Returns the Chebyshev distance between two positions. Calculated as max(abs(x0-x1), abs(y0-y1)).\n\nr0: Position A\nr1: Position B\nreturn: Chebyshev Distance between position A and position B",
    )

    IsPositionActuallyInSight = Symbol(
        None,
        None,
        None,
        "Checks if a given target position is in sight from a given origin position.\nIf the origin position is on a hallway or r2 is true, checks if both positions are within <dungeon::display_data::visibility_range> tiles of each other.\nIf the origin position is on a room, checks that the target position is within the boundaries of said room.\n\nr0: Origin position\nr1: Target position\nr2: True to assume the entity standing on the origin position has the dropeye status\nreturn: True if the target position is in sight from the origin position",
    )

    IsPositionInSight = Symbol(
        None,
        None,
        None,
        "Checks if a given target position is in sight from a given origin position.\nThere's multiple factors that affect this check, but generally, it's true if both positions are in the same room (by checking if the target position is within the boundaries of the room where the origin position is) or within 2 tiles of each other.\n\nr0: Origin position\nr1: Target position\nr2: True to assume the entity standing on the origin position has the dropeye status\nreturn: True if the target position is in sight from the origin position",
    )

    GetLeader = Symbol(
        None,
        None,
        None,
        "Gets the pointer to the entity that is currently leading the team, or null if none of the first 4 entities is a valid monster with its is_team_leader flag set. It also sets LEADER_PTR to the result before returning it.\n\nreturn: Pointer to the current leader of the team or null if there's no valid leader.",
    )

    GetLeaderMonster = Symbol(
        None,
        None,
        None,
        "Returns a pointer to the monster data of the current leader.\n\nNo params.",
    )

    FindNearbyUnoccupiedTile = Symbol(
        None,
        None,
        None,
        "Searches for an unoccupied tile near some origin.\n\nA tile is considered 'unoccupied' if it's not a key door, and has no object or monster on it. In 'random room' mode, the tile must also not be in a hallway, and must not have the stairs.\n\nThe first unoccupied tile found is returned. The search order is randomized in 'random room' mode, otherwise the search order is fixed based on the input displacement array.\n\nr0: [output] position\nr1: origin position\nr2: array of displacements from the origin position to consider\nr3: number of elements in displacements array\nstack[0]: random room mode flag\nreturn: whether a tile was successfully found",
    )

    FindClosestUnoccupiedTileWithin2 = Symbol(
        None,
        None,
        None,
        "Searches for the closest unoccupied tile within 2 steps of the given origin.\n\nCalls FindNearbyUnoccupiedTile with DISPLACEMENTS_WITHIN_2_SMALLEST_FIRST.\n\nr0: [output] position\nr1: origin position\nr2: random room mode flag\nreturn: whether a tile was successfully found",
    )

    FindFarthestUnoccupiedTileWithin2 = Symbol(
        None,
        None,
        None,
        "Searches for the farthest unoccupied tile within 2 steps of the given origin.\n\nCalls FindNearbyUnoccupiedTile with DISPLACEMENTS_WITHIN_2_LARGEST_FIRST.\n\nr0: [output] position\nr1: origin position\nr2: random room mode flag\nreturn: whether a tile was successfully found",
    )

    FindUnoccupiedTileWithin3 = Symbol(
        None,
        None,
        None,
        "Searches for an unoccupied tile within 3 steps of the given origin.\n\nCalls FindNearbyUnoccupiedTile with DISPLACEMENTS_WITHIN_3.\n\nr0: [output] position\nr1: origin position\nr2: random room mode flag\nreturn: whether a tile was successfully found",
    )

    TickStatusTurnCounter = Symbol(
        None,
        None,
        None,
        "Ticks down a turn counter for a status condition. If the counter equals 0x7F, it will not be decreased.\n\nr0: pointer to the status turn counter\nreturn: new counter value",
    )

    AdvanceFrame = Symbol(
        None,
        None,
        None,
        "Advances one frame. Does not return until the next frame starts.\n\nr0: ? - Unused by the function",
    )

    DisplayAnimatedNumbers = Symbol(
        None,
        None,
        None,
        "Displays numbers or the 'MISS' text above a monster. Normally used to display damage amounts, although it also has other uses (such as showing the stockpile count).\n\nr0: Amount to display. Can be negative. 9999 displays 'MISS' instead.\nr1: Entity above which the numbers will be displayed\nr2: True to display a plus or minus sign before the numbers, false to hide it\nr3: Color of the numbers. NUMBER_COLOR_AUTO to determine it automatically.",
    )

    SetDungeonRngPreseed23Bit = Symbol(
        None,
        None,
        None,
        "Sets the preseed in the global dungeon PRNG state, using 23 bits from the input. See GenerateDungeonRngSeed for more information.\n\nGiven the input preseed23, the actual global preseed is set to (preseed23 & 0xFFFFFF | 1), so only bits 1-23 of the input are used.\n\nr0: preseed23",
    )

    GenerateDungeonRngSeed = Symbol(
        None,
        None,
        None,
        "Generates a seed with which to initialize the dungeon PRNG.\n\nThe seed is calculated by starting with a different seed, the 'preseed' x0 (defaults to 1, but can be set by other functions). The preseed is iterated twice with the same recurrence relation used in the primary LCG to generate two pseudorandom 32-bit numbers x1 and x2. The output seed is then computed as\n  seed = (x1 & 0xFF0000) | (x2 >> 0x10) | 1\nThe value x1 is then saved as the new preseed.\n\nThis method of seeding the dungeon PRNG appears to be used only sometimes, depending on certain flags in the data for a given dungeon.\n\nreturn: RNG seed",
    )

    GetDungeonRngPreseed = Symbol(
        None,
        None,
        None,
        "Gets the current preseed stored in the global dungeon PRNG state. See GenerateDungeonRngSeed for more information.\n\nreturn: current dungeon RNG preseed",
    )

    SetDungeonRngPreseed = Symbol(
        None,
        None,
        None,
        "Sets the preseed in the global dungeon PRNG state. See GenerateDungeonRngSeed for more information.\n\nr0: preseed",
    )

    InitDungeonRng = Symbol(
        None,
        None,
        None,
        "Initialize (or reinitialize) the dungeon PRNG with a given seed. The primary LCG and the five secondary LCGs are initialized jointly, and with the same seed.\n\nr0: seed",
    )

    DungeonRand16Bit = Symbol(
        None,
        None,
        None,
        "Computes a pseudorandom 16-bit integer using the dungeon PRNG.\n\nNote that the dungeon PRNG is only used in dungeon mode (as evidenced by these functions being in overlay 29). The game uses another lower-quality PRNG (see arm9.yml) for other needs.\n\nRandom numbers are generated with a linear congruential generator (LCG). The game actually maintains 6 separate sequences that can be used for generation: a primary LCG and 5 secondary LCGs. The generator used depends on parameters set on the global PRNG state.\n\nAll dungeon LCGs have a modulus of 2^32 and a multiplier of 1566083941 (see DUNGEON_PRNG_LCG_MULTIPLIER). The primary LCG uses an increment of 1, while the secondary LCGs use an increment of 2531011 (see DUNGEON_PRNG_LCG_INCREMENT_SECONDARY). So, for example, the primary LCG uses the recurrence relation:\n  x = (1566083941*x_prev + 1) % 2^32\n\nSince the dungeon LCGs generate 32-bit integers rather than 16-bit, the primary LCG yields 16-bit values by taking the upper 16 bits of the computed 32-bit value. The secondary LCGs yield 16-bit values by taking the lower 16 bits of the computed 32-bit value.\n\nAll of the dungeon LCGs have a hard-coded default seed of 1, but in practice the seed is set with a call to InitDungeonRng during dungeon initialization.\n\nreturn: pseudorandom int on the interval [0, 65535]",
    )

    DungeonRandInt = Symbol(
        None,
        None,
        None,
        "Compute a pseudorandom integer under a given maximum value using the dungeon PRNG.\n\nr0: high\nreturn: pseudorandom integer on the interval [0, high - 1]",
    )

    DungeonRandRange = Symbol(
        None,
        None,
        None,
        "Compute a pseudorandom value between two integers using the dungeon PRNG.\n\nr0: x\nr1: y\nreturn: pseudorandom integer on the interval [min(x, y), max(x, y) - 1]",
    )

    DungeonRandOutcome = Symbol(
        None,
        None,
        None,
        "Returns the result of a possibly biased coin flip (a Bernoulli random variable) with some success probability p, using the dungeon PRNG.\n\nr0: success percentage (100*p)\nreturn: true with probability p, false with probability (1-p)",
    )

    CalcStatusDuration = Symbol(
        None,
        None,
        None,
        "Seems to calculate the duration of a volatile status on a monster.\n\nr0: entity pointer\nr1: pointer to a turn range (an array of two shorts {lower, higher})\nr2: flag for whether or not to factor in the Self Curer IQ skill and the Natural Cure ability\nreturn: number of turns for the status condition",
    )

    DungeonRngUnsetSecondary = Symbol(
        None,
        None,
        None,
        "Sets the dungeon PRNG to use the primary LCG for subsequent random number generation, and also resets the secondary LCG index back to 0.\n\nSimilar to DungeonRngSetPrimary, but DungeonRngSetPrimary doesn't modify the secondary LCG index if it was already set to something other than 0.\n\nNo params.",
    )

    DungeonRngSetSecondary = Symbol(
        None,
        None,
        None,
        "Sets the dungeon PRNG to use one of the 5 secondary LCGs for subsequent random number generation.\n\nr0: secondary LCG index",
    )

    DungeonRngSetPrimary = Symbol(
        None,
        None,
        None,
        "Sets the dungeon PRNG to use the primary LCG for subsequent random number generation.\n\nNo params.",
    )

    MusicTableIdxToMusicId = Symbol(
        None,
        None,
        None,
        "Used to convert an index that refers to a MUSIC_ID_TABLE entry to a regular music ID.\n\nr0: Music table index\nreturn: Music ID",
    )

    ChangeDungeonMusic = Symbol(
        None,
        None,
        None,
        "Replace the currently playing music with the provided music\n\nr0: music ID",
    )

    TrySwitchPlace = Symbol(
        None,
        None,
        None,
        "The user entity attempts to switch places with the target entity (i.e. by the effect of the Switcher Orb). \n\nThe function checks for the Suction Cups ability for both the user and the target, and for the Mold Breaker ability on the user.\n\nr0: pointer to user entity\nr1: pointer to target entity",
    )

    SetLeaderActionFields = Symbol(
        None,
        None,
        None,
        "Sets the leader's monster::action::action_id to the specified value.\n\nAlso sets monster::action::action_use_idx and monster::action::field_0xA to 0, as well as monster::action::field_0x10 and monster::action::field_0x12 to -1.\n\nr0: ID of the action to set",
    )

    ClearMonsterActionFields = Symbol(
        None,
        None,
        None,
        "Clears the fields related to AI in the monster's data struct, setting them all to 0.\nSpecifically, monster::action::action_id, monster::action::action_use_idx and monster::action::field_0xA are cleared.\n\nr0: Pointer to the monster's action field",
    )

    SetMonsterActionFields = Symbol(
        None,
        None,
        None,
        "Sets some the fields related to AI in the monster's data struct.\nSpecifically, monster::action::action_id, monster::action::action_use_idx and monster::action::field_0xA. The last 2 are always set to 0.\n\nr0: Pointer to the monster's action field\nr1: Value to set monster::action::action_id to.",
    )

    SetActionPassTurnOrWalk = Symbol(
        None,
        None,
        None,
        "Sets a monster's action to action::ACTION_PASS_TURN or action::ACTION_WALK, depending on the result of GetCanMoveFlag for the monster's ID.\n\nr0: Pointer to the monster's action field\nr1: Monster ID",
    )

    GetItemToUseByIndex = Symbol(
        None,
        None,
        None,
        "Returns a pointer to the item that is about to be used by a monster given its index.\n\nr0: Entity pointer\nr1: Item index\nreturn: Pointer to the item",
    )

    GetItemToUse = Symbol(
        None,
        None,
        None,
        "Returns a pointer to the item that is about to be used by a monster.\n\nr0: Entity pointer\nr1: Parameter index in monster::action_data::action_parameters. Will be used to use to determine the index of the used item.\nr2: Unused\nreturn: Pointer to the item",
    )

    GetItemAction = Symbol(
        None,
        None,
        None,
        "Returns the action ID that corresponds to an item given its ID.\n\nThe action is based on the category of the item (see ITEM_CATEGORY_ACTIONS), unless the specified ID is 0x16B, in which case ACTION_UNK_35 is returned.\nSome items can have unexpected actions, such as thrown items, which have ACTION_NOTHING. This is done to prevent duplicate actions from being listed in the menu (since items always have a 'throw' option), since a return value of ACTION_NOTHING prevents the option from showing up in the menu.\n\nr0: Item ID\nreturn: Action ID associated with the specified item",
    )

    RemoveUsedItem = Symbol(
        None,
        None,
        None,
        "Removes an item from the bag or from the floor after using it\n\nr0: Pointer to the entity that used the item\nr1: Parameter index in monster::action_data::action_parameters. Will be used to use to determine the index of the used item.",
    )

    AddDungeonSubMenuOption = Symbol(
        None,
        None,
        None,
        "Adds an option to the list of actions that can be taken on a pokémon, item or move to the currently active sub-menu on dungeon mode (team, moves, items, etc.).\n\nr0: Action ID\nr1: True if the option should be enabled, false otherwise",
    )

    DisableDungeonSubMenuOption = Symbol(
        None,
        None,
        None,
        "Disables an option that was addeed to a dungeon sub-menu.\n\nr0: Action ID of the option that should be disabled",
    )

    SetActionRegularAttack = Symbol(
        None,
        None,
        None,
        "Sets a monster's action to action::ACTION_REGULAR_ATTACK, with a specified direction.\n\nr0: Pointer to the monster's action field\nr1: Direction in which to use the move. Gets stored in monster::action::direction.",
    )

    SetActionUseMovePlayer = Symbol(
        None,
        None,
        None,
        "Sets a monster's action to action::ACTION_USE_MOVE_PLAYER, with a specified monster and move index.\n\nr0: Pointer to the monster's action field\nr1: Index of the monster that is using the move on the entity list. Gets stored in monster::action::action_use_idx.\nr2: Index of the move to use (0-3). Gets stored in monster::action::field_0xA.",
    )

    SetActionUseMoveAi = Symbol(
        None,
        None,
        None,
        "Sets a monster's action to action::ACTION_USE_MOVE_AI, with a specified direction and move index.\n\nr0: Pointer to the monster's action field\nr1: Index of the move to use (0-3). Gets stored in monster::action::action_use_idx.\nr2: Direction in which to use the move. Gets stored in monster::action::direction.",
    )

    RunFractionalTurn = Symbol(
        None,
        None,
        None,
        "The main function which executes the actions that take place in a fractional turn. Called in a loop by RunDungeon while IsFloorOver returns false.\n\nr0: first loop flag (true when the function is first called during a floor)",
    )

    RunLeaderTurn = Symbol(
        None,
        None,
        None,
        "Handles the leader's turn. Includes a movement speed check that might cause it to return early if the leader isn't fast enough to act in this fractional turn. If that check (and some others) pass, the function does not return until the leader performs an action.\n\nr0: ?\nreturn: true if the leader has performed an action",
    )

    TrySpawnMonsterAndActivatePlusMinus = Symbol(
        None,
        None,
        None,
        "Called at the beginning of RunFractionalTurn. Executed only if FRACTIONAL_TURN_SEQUENCE[fractional_turn * 2] is not 0.\n\nFirst it calls TrySpawnMonsterAndTickSpawnCounter, then tries to activate the Plus and Minus abilities for both allies and enemies, and finally calls TryForcedLoss.\n\nNo params.",
    )

    IsFloorOver = Symbol(
        None,
        None,
        None,
        "Checks if the current floor should end, and updates dungeon::floor_loop_status if required.\nIf the player has been defeated, sets dungeon::floor_loop_status to floor_loop_status::FLOOR_LOOP_LEADER_FAINTED.\nIf dungeon::end_floor_flag is 1 or 2, sets dungeon::floor_loop_status to floor_loop_status::FLOOR_LOOP_NEXT_FLOOR.\n\nreturn: true if the current floor should end",
    )

    DecrementWindCounter = Symbol(
        None,
        None,
        None,
        "Decrements dungeon::wind_turns and displays a wind warning message if required.\n\nNo params.",
    )

    SetForcedLossReason = Symbol(
        None,
        None,
        None,
        "Sets dungeon::forced_loss_reason to the specified value\n\nr0: Forced loss reason",
    )

    GetForcedLossReason = Symbol(
        None,
        None,
        None,
        "Returns dungeon::forced_loss_reason\n\nreturn: forced_loss_reason",
    )

    BindTrapToTile = Symbol(
        None,
        None,
        None,
        "Sets the given tile's associated object to be the given trap, and sets the visibility of the trap.\n\nr0: tile pointer\nr1: entity pointer\nr2: visibility flag",
    )

    SpawnEnemyTrapAtPos = Symbol(
        None,
        None,
        None,
        "A convenience wrapper around SpawnTrap and BindTrapToTile. Always passes 0 for the team parameter (making it an enemy trap).\n\nr0: trap ID\nr1: x position\nr2: y position\nr3: flags\nstack[0]: visibility flag",
    )

    PrepareTrapperTrap = Symbol(
        None,
        None,
        None,
        "Saves the relevant information in the dungeon struct to later place a trap at the\nlocation of the entity. (Only called with trap ID 0x19 (TRAP_NONE), but could be used \nwith others).\n\nr0: entity pointer\nr1: trap ID\nr2: team (see struct trap::team)",
    )

    TrySpawnTrap = Symbol(
        None,
        None,
        None,
        "Checks if the a trap can be placed on the tile. If the trap ID is >= TRAP_NONE (the\nlast value for a trap), randomly select another trap (except for wonder tile). After\n30 failed attempts to select a non-wonder tile trap ID, default to chestnut trap.\nIf the checks pass, spawn the trap.\n\nr0: position\nr1: trap ID\nr2: team (see struct trap::team)\nr3: visibility flag\nreturn: true if a trap was spawned succesfully",
    )

    TrySpawnTrapperTrap = Symbol(
        None,
        None,
        None,
        "If the flag for a trapper trap is set, handles spawning a trap based upon the\ninformation inside the dungeon struct. Uses the entity for logging a message\ndepending on success or failure.\n\nr0: entity pointer\nreturn: true if a trap was spawned succesfully",
    )

    TryTriggerTrap = Symbol(
        None,
        None,
        None,
        "Called whenever a monster steps on a trap.\n\nThe function will try to trigger it. Nothing will happen if the pokémon has the same team as the trap. The attempt to trigger the trap can also fail due to IQ skills, due to the trap failing to work (random chance), etc.\n\nr0: Entity who stepped on the trap\nr1: Trap position\nr2: ?\nr3: ?",
    )

    ApplyMudTrapEffect = Symbol(
        None,
        None,
        None,
        "Randomly lowers attack, special attack, defense, or special defense of the defender by 3 stages.\n\nr0: attacker entity pointer\nr1: defender entity pointer",
    )

    ApplyStickyTrapEffect = Symbol(
        None,
        None,
        None,
        "If the defender is the leader, randomly try to make something in the bag sticky. Otherwise, try to make the item the monster is holding sticky.\n\nr0: attacker entity pointer\nr1: defender entity pointer",
    )

    ApplyGrimyTrapEffect = Symbol(
        None,
        None,
        None,
        "If the defender is the leader, randomly try to turn food items in the toolbox into\ngrimy food. Otherwise, try to make the food item the monster is holding grimy food.\n\nr0: attacker entity pointer\nr1: defender entity pointer",
    )

    ApplyPitfallTrapEffect = Symbol(
        None,
        None,
        None,
        "If the defender is the leader, end the current floor unless it has a rescue point.\nOtherwise, make the entity faint and ignore reviver seeds. If not called by a random\ntrap, break the grate on the pitfall trap.\n\nr0: attacker entity pointer\nr1: defender entity pointer\nr2: tile pointer\nr3: bool caused by random trap",
    )

    ApplySummonTrapEffect = Symbol(
        None,
        None,
        None,
        "Randomly spawns 2-4 enemy monsters around the position. The entity is only used for\nlogging messages.\n\nr0: entity pointer\nr1: position",
    )

    ApplyPpZeroTrapEffect = Symbol(
        None,
        None,
        None,
        "Tries to reduce the PP of one of the defender's moves to 0.\n\nr0: attacker entity pointer\nr1: defender entity pointer",
    )

    ApplyPokemonTrapEffect = Symbol(
        None,
        None,
        None,
        "Turns item in the same room as the tile at the position (usually just the entities's\nposition) into monsters. If the position is in a hallway, convert items in a 3x3 area\ncentered on the position into monsters.\n\nr0: entity pointer\nr1: position",
    )

    ApplyTripTrapEffect = Symbol(
        None,
        None,
        None,
        "Tries to drop the defender's item and places it on the floor.\n\nr0: attacker entity pointer\nr1: defender entity pointer",
    )

    ApplyStealthRockTrapEffect = Symbol(
        None,
        None,
        None,
        "Tries to apply the damage from the stealth rock trap but does nothing if the defender is a rock type.\n\nr0: attacker entity pointer\nr1: defender entity pointer",
    )

    ApplyToxicSpikesTrapEffect = Symbol(
        None,
        None,
        None,
        "Tries to inflict 10 damage on the defender and then tries to poison them.\n\nr0: attacker entity pointer\nr1: defender entity pointer",
    )

    ApplyRandomTrapEffect = Symbol(
        None,
        None,
        None,
        "Selects a random trap that isn't a wonder tile and isn't a random trap and calls\nApplyTrapEffect on all monsters that is different from the trap's team.\n\nr0: Triggered trap\nr1: User\nr2: Target, normally same as user\nr3: Tile that contains the trap\nstack[0]: position",
    )

    ApplyGrudgeTrapEffect = Symbol(
        None,
        None,
        None,
        "Spawns several monsters around the position and gives all monsters on the floor the\ngrudge status condition.\n\nr0: entity pointer\nr1: position",
    )

    ApplyTrapEffect = Symbol(
        None,
        None,
        None,
        "Performs the effect of a triggered trap.\n\nThe trap's animation happens before this function is called.\n\nr0: Triggered trap\nr1: User\nr2: Target, normally same as user\nr3: Tile that contains the trap\nstack[0]: position\nstack[1]: trap ID\nstack[2]: bool caused by random trap\nreturn: True if the trap should be destroyed after the effect is applied",
    )

    RevealTrapsNearby = Symbol(
        None,
        None,
        None,
        "Reveals traps within the monster's viewing range.\n\nr0: entity pointer",
    )

    ShouldRunMonsterAi = Symbol(
        None,
        None,
        None,
        "Checks a monster's monster_behavior to see whether or not the monster should use AI. Only called on monsters with\na monster_behavior greater than or equal to BEHAVIOR_FIXED_ENEMY. Returns false for BEHAVIOR_FIXED_ENEMY, \nBEHAVIOR_WANDERING_ENEMY_0x8, BEHAVIOR_SECRET_BAZAAR_KIRLIA, BEHAVIOR_SECRET_BAZAAR_MIME_JR,\nBEHAVIOR_SECRET_BAZAAR_SWALOT, BEHAVIOR_SECRET_BAZAAR_LICKILICKY, and BEHAVIOR_SECRET_BAZAAR_SHEDINJA.\n\nr0: monster entity pointer\nreturn: bool",
    )

    DebugRecruitingEnabled = Symbol(
        None,
        None,
        None,
        "Always returns true. Called by SpecificRecruitCheck.\n\nSeems to be a function used during development to disable recruiting. If it returns false, SpecificRecruitCheck will also return false.\n\nreturn: true",
    )

    TryActivateIqBooster = Symbol(
        None,
        None,
        None,
        "Increases the IQ of all team members holding the IQ Booster by floor_properties::iq_booster_value amount unless the\nvalue is 0.\n\nNo params.",
    )

    IsSecretBazaarNpcBehavior = Symbol(
        None,
        None,
        None,
        "Checks if a behavior ID corresponds to one of the Secret Bazaar NPCs.\n\nr0: monster behavior ID\nreturn: bool",
    )

    GetLeaderAction = Symbol(
        None,
        None,
        None,
        "Returns a pointer to the action data of the current leader (field 0x4A on its monster struct).\n\nNo params.",
    )

    GetEntityTouchscreenArea = Symbol(
        None,
        None,
        None,
        "Returns the area on the touchscreen that contains the sprite of the specified entity\n\nr0: Entity pointer\nr1: [output] struct where the result should be written",
    )

    SetLeaderAction = Symbol(
        None,
        None,
        None,
        "Sets the leader's action field depending on the inputs given by the player.\n\nThis function also accounts for other special situations that can force a certain action, such as when the leader is running. The function also takes care of opening the main menu when X is pressed.\nThe function generally doesn't return until the player has an action set.\n\nNo params.",
    )

    ShouldLeaderKeepRunning = Symbol(
        None,
        None,
        None,
        "Determines if the leader should keep running. Returns false if the leader bumps into something, or if an action that should stop the leader takes place.\n\nreturn: True if the leader should keep running, false if it should stop.",
    )

    CheckLeaderTile = Symbol(
        None,
        None,
        None,
        "Checks the tile the leader just stepped on and performs any required actions, such as picking up items, triggering traps, etc.\n\nContains a switch that checks the type of the tile the leader just stepped on.\n\nNo params.",
    )

    ChangeLeader = Symbol(
        None,
        None,
        None,
        "Tries to change the current leader to the monster specified by dungeon::new_leader.\n\nAccounts for situations that can prevent changing leaders, such as having stolen from a Kecleon shop. If one of those situations prevents changing leaders, prints the corresponding message to the message log.\n\nNo params.",
    )

    UseSingleUseItemWrapper = Symbol(
        None,
        None,
        None,
        "Same as UseSingleUseItem, but the second parameter is determined automatically from monster::action_data::action_parameter[1]::action_use_idx.\n\nr0: User",
    )

    UseSingleUseItem = Symbol(
        None,
        None,
        None,
        "Makes a monster use a single-use item. The item is deleted afterwards.\n\nThe item to use is determined by the user's monster::action_data::action_parameter[0].\n\nr0: User (monster who used the item)\nr1: Target (monster that consumes the item)",
    )

    UseThrowableItem = Symbol(
        None,
        None,
        None,
        "Makes a monster use a throwable item.\n\nThe item to use is determined by monster::action_data::action_parameter[0].\nIf the item's category is CATEGORY_THROWN_LINE or CATEGORY_THROWN_ARC, the game will attempt to decrement the count of the used item by 1. If it's not or there's only 1 item left, it is destroyed instead.\n\nr0: User (monster who used the item)",
    )

    ResetDamageData = Symbol(
        None,
        None,
        None,
        "Zeroes the damage data struct, which is output by the damage calculation function.\n\nr0: damage data pointer",
    )

    FreeLoadedAttackSpriteAndMore = Symbol(
        None,
        None,
        None,
        "Among other things, free another data structure in the attack sprite storage area/data\n\nNo params.",
    )

    SetAndLoadCurrentAttackAnimation = Symbol(
        None,
        None,
        None,
        "Load given sprite into the currently loaded attack sprite structure, replacing the previous one if already loaded.\n\nr0: pack id\nr1: file index\nreturn: sprite id in the loaded wan list",
    )

    ClearLoadedAttackSprite = Symbol(
        None,
        None,
        None,
        "Delete the data of the currently loaded attack sprite, if any.\nDoesn’t free the structure, which can continue to be used.\n\nNo params.",
    )

    GetLoadedAttackSpriteId = Symbol(
        None,
        None,
        None,
        "Get the sprite ID (in the loaded WAN list) of the currently loaded attack sprite, or 0 if none.\n\nreturn: sprite ID",
    )

    DungeonGetTotalSpriteFileSize = Symbol(
        None,
        None,
        None,
        "Checks Castform and Cherrim\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: monster ID\nreturn: sprite file size",
    )

    DungeonGetSpriteIndex = Symbol(
        None,
        None,
        None,
        "Gets the sprite index of the specified monster on this floor\n\nr0: Monster ID\nreturn: Sprite index of the specified monster ID",
    )

    JoinedAtRangeCheck2Veneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for arm9::JoinedAtRangeCheck2.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nNo params.",
    )

    FloorNumberIsEven = Symbol(
        None,
        None,
        None,
        "Checks if the current dungeon floor number is even (probably to determine whether an enemy spawn should be female).\n\nHas a special check to return false for Labyrinth Cave B10F (the Gabite boss fight).\n\nreturn: bool",
    )

    GetKecleonIdToSpawnByFloor = Symbol(
        None,
        None,
        None,
        "If the current floor number is even, returns female Kecleon's id (0x3D7), otherwise returns male Kecleon's id (0x17F).\n\nreturn: monster ID",
    )

    StoreSpriteFileIndexBothGenders = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: monster ID\nr1: file ID",
    )

    LoadMonsterSpriteInner = Symbol(
        None,
        None,
        None,
        "This is called by LoadMonsterSprite a bunch of times.\n\nr0: monster ID",
    )

    SwapMonsterWanFileIndex = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: src_id\nr1: dst_id",
    )

    LoadMonsterSprite = Symbol(
        None,
        None,
        None,
        "Loads the sprite of the specified monster to use it in a dungeon.\n\nIrdkwia's notes: Handles Castform/Cherrim/Deoxys\n\nr0: monster ID\nr1: ?",
    )

    DeleteMonsterSpriteFile = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: monster ID",
    )

    DeleteAllMonsterSpriteFiles = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nNo params."
    )

    EuFaintCheck = Symbol(
        None,
        None,
        None,
        "This function is exclusive to the EU ROM. Seems to perform a check to see if the monster who just fainted was a team member who should cause the minimap to be updated (or something like that, maybe related to the Map Surveyor IQ skill) and if it passes, updates the minimap.\nThe function ends by calling another 2 functions. In US ROMs, calls to EUFaintCheck are replaced by calls to those two functions. This seems to indicate that this function fixes some edge case glitch that can happen when a team member faints.\n\nr0: False if the fainted entity was a team member\nr1: True to set an unknown byte in the RAM to 1",
    )

    HandleFaint = Symbol(
        None,
        None,
        None,
        "Handles a fainted pokémon (reviving does not count as fainting).\n\nr0: Fainted entity\nr1: Damage source (move ID or greater than the max move id for other causes)\nr2: Entity responsible of the fainting",
    )

    MoveMonsterToPos = Symbol(
        None,
        None,
        None,
        "Moves a monster to the target position. Used both for regular movement and special movement (like teleportation).\n\nr0: Entity pointer\nr1: X target position\nr2: Y target position\nr3: ?",
    )

    CreateMonsterSummaryFromMonster = Symbol(
        None,
        None,
        None,
        "Creates a snapshot of the condition of a monster struct in a monster_summary struct.\n\nr0: [output] monster_summary\nr1: monster",
    )

    UpdateAiTargetPos = Symbol(
        None,
        None,
        None,
        "Given a monster, updates its target_pos field based on its current position and the direction in which it plans to attack.\n\nr0: Entity pointer",
    )

    SetMonsterTypeAndAbility = Symbol(
        None,
        None,
        None,
        "Checks Forecast ability\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: target entity pointer",
    )

    TryActivateSlowStart = Symbol(
        None,
        None,
        None,
        "Runs a check over all monsters on the field for the ability Slow Start, and lowers the speed of those who have it.\n\nNo params",
    )

    TryActivateArtificialWeatherAbilities = Symbol(
        None,
        None,
        None,
        "Runs a check over all monsters on the field for abilities that affect the weather and changes the floor's weather accordingly.\n\nNo params",
    )

    GetMonsterApparentId = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: target entity pointer\nr1: current_id\nreturn: ?",
    )

    TryActivateTraceAndColorChange = Symbol(
        None,
        None,
        None,
        "Tries to activate the abilities trace and color change if possible. Called after using\na move.\n\nr0: attacker entity pointer\nr1: defender entity pointer\nr2: move pointer",
    )

    DefenderAbilityIsActive = Symbol(
        None,
        None,
        None,
        "Checks if a defender has an active ability that isn't disabled by an attacker's Mold Breaker.\n\nThere are two versions of this function, which share the same logic but have slightly different assembly. This is probably due to differences in compiler optimizations at different addresses.\n\nr0: attacker pointer\nr1: defender pointer\nr2: ability ID to check on the defender\nr3: flag for whether the attacker's ability is enabled\nreturn: bool",
    )

    IsMonster = Symbol(
        None,
        None,
        None,
        "Checks if an entity is a monster (entity type 1).\n\nr0: entity pointer\nreturn: bool",
    )

    TryActivateConversion2 = Symbol(
        None,
        None,
        None,
        "Checks for the conversion2 status and applies the type change if applicable. Called\nafter using a move.\n\nr0: attacker entity pointer\nr1: defender entity pointer\nr2: move pointer",
    )

    TryActivateTruant = Symbol(
        None,
        None,
        None,
        "Checks if an entity has the ability Truant, and if so tries to apply the pause status to it.\n\nr0: pointer to entity",
    )

    TryPointCameraToMonster = Symbol(
        None,
        None,
        None,
        "Attempts to place the camera on top of the specified monster.\n\nIf the camera is already on top of the specified entity, the function does nothing.\n\nr0: Entity pointer. Must be a monster, otherwise the function does nothing.\nr1: ?\nr2: ?",
    )

    RestorePpAllMovesSetFlags = Symbol(
        None,
        None,
        None,
        "Restores PP for all moves, clears flags move::f_consume_2_pp, move::flags2_unk5 and move::flags2_unk7, and sets flag move::f_consume_pp.\nCalled when a monster is revived.\n\nr0: pointer to entity whose moves will be restored",
    )

    CheckTeamMemberIdxVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for CheckTeamMemberIdx.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nr0: member index\nreturn: True if the value is equal to 0x55AA or 0x5AA5",
    )

    IsMonsterIdInNormalRangeVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for IsMonsterIdInNormalRange.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nr0: monster ID\nreturn: bool",
    )

    BoostIQ = Symbol(
        None,
        None,
        None,
        "Tries to boost the target's IQ.\n\nr0: monster entity pointer\nr1: iq boost\nr2: bool suppress logs",
    )

    ShouldMonsterHeadToStairs = Symbol(
        None,
        None,
        None,
        "Checks if a given monster should try to reach the stairs when controlled by the AI\n\nr0: Entity pointer\nreturn: True if the monster should try to reach the stairs, false otherwise",
    )

    MewSpawnCheck = Symbol(
        None,
        None,
        None,
        "If the monster id parameter is 0x97 (Mew), returns false if either dungeon::mew_cannot_spawn or the second parameter are true.\n\nCalled before spawning an enemy, appears to be checking if Mew can spawn on the current floor.\n\nr0: monster id\nr1: return false if the monster id is Mew\nreturn: bool",
    )

    TryEndStatusWithAbility = Symbol(
        None,
        None,
        None,
        "Checks if any of the defender's active abilities would end one of their current status\nconditions. For example, if the ability Own Tempo will stop confusion.\n\nCalled after changing a monster's ability with skill swap, role play, or trace to\nremove statuses the monster should no longer be affected by.\n\nr0: attacker entity pointer\nr1: defender entity pointer",
    )

    ExclusiveItemEffectIsActive = Symbol(
        None,
        None,
        None,
        "Checks if a monster is a team member under the effects of a certain exclusive item effect.\n\nr0: entity pointer\nr1: exclusive item effect ID\nreturn: bool",
    )

    GetTeamMemberWithIqSkill = Symbol(
        None,
        None,
        None,
        "Returns an entity pointer to the first team member which has the specified iq skill.\n\nr0: iq skill id\nreturn: pointer to entity",
    )

    TeamMemberHasEnabledIqSkill = Symbol(
        None,
        None,
        None,
        "Returns true if any team member has the specified iq skill.\n\nr0: iq skill id\nreturn: bool",
    )

    TeamLeaderIqSkillIsEnabled = Symbol(
        None,
        None,
        None,
        "Returns true the leader has the specified iq skill.\n\nr0: iq skill id\nreturn: bool",
    )

    CountMovesOutOfPp = Symbol(
        None,
        None,
        None,
        "Returns how many of a monster's move are out of PP.\n\nr0: entity pointer\nreturn: number of moves out of PP",
    )

    HasSuperEffectiveMoveAgainstUser = Symbol(
        None,
        None,
        None,
        "Checks if the target has at least one super effective move against the user.\n\nr0: User\nr1: Target\nr2: If true, moves with a max Ginseng boost != 99 will be ignored\nreturn: True if the target has at least one super effective move against the user, false otherwise.",
    )

    TryEatItem = Symbol(
        None,
        None,
        None,
        "The user attempts to eat an item from the target.\n\nThe function tries to eat the target's held item first. If that's not possible and the target is part of the team, it attempts to eat a random edible item from the bag instead.\nFun fact: The code used to select the random bag item that will be eaten is poorly coded. As a result, there's a small chance of the first edible item in the bag being picked instead of a random one. The exact chance of this happening is (N/B)^B, where N is the amount of non-edible items in the bag and B is the total amount of items in the bag.\n\nr0: User\nr1: Target\nreturn: True if the attempt was successful",
    )

    CheckSpawnThreshold = Symbol(
        None,
        None,
        None,
        "Checks if a given monster ID can spawn in dungeons.\n\nThe function returns true if the monster's spawn threshold value is <= SCENARIO_BALANCE_FLAG\n\nr0: monster ID\nreturn: True if the monster can spawn, false otherwise",
    )

    HasLowHealth = Symbol(
        None,
        None,
        None,
        "Checks if the entity passed is a valid monster, and if it's at low health (below 25% rounded down)\n\nr0: entity pointer\nreturn: bool",
    )

    AreEntitiesAdjacent = Symbol(
        None,
        None,
        None,
        "Checks whether two entities are adjacent or not.\n\nThe function checks all 8 possible directions.\n\nr0: First entity\nr1: Second entity\nreturn: True if both entities are adjacent, false otherwise.",
    )

    IsSpecialStoryAlly = Symbol(
        None,
        None,
        None,
        "Checks if a monster is a special story ally.\n\nThis is a hard-coded check that looks at the monster's 'Joined At' field. If the value is in the range [DUNGEON_JOINED_AT_BIDOOF, DUNGEON_DUMMY_0xE3], this check will return true.\n\nr0: monster pointer\nreturn: bool",
    )

    IsExperienceLocked = Symbol(
        None,
        None,
        None,
        "Checks if a monster does not gain experience.\n\nThis basically just inverts IsSpecialStoryAlly, with the exception of also checking for the 'Joined At' field being DUNGEON_CLIENT (is this set for mission clients?).\n\nr0: monster pointer\nreturn: bool",
    )

    InitOtherMonsterData = Symbol(
        None,
        None,
        None,
        "Initializes stats, IQ skills and moves for a given monster\n\nMight only be used when spawning fixed room monsters.\n\nr0: Entity pointer\nr1: Fixed room monster stats index\nr2: Spawn direction? (when calling this function while spawning a fixed room monster, this is the parameter value associated to the spawn action, after converting it to a direction.)",
    )

    InitEnemySpawnStats = Symbol(
        None,
        None,
        None,
        "Initializes dungeon::enemy_spawn_stats. Might do something else too.\n\nNo params.",
    )

    InitEnemyStatsAndMoves = Symbol(
        None,
        None,
        None,
        "Initializes the HP, Atk, Sp. Atk, Def, Sp. Def and moveset of a newly spawned enemy. Might do something else too.\n\nr0: Pointer to the monster's move list\nr1: Pointer to the monster's current HP\nr2: Pointer to the monster's offensive stats\nr3: Pointer to the monster's defensive stats",
    )

    SpawnTeam = Symbol(
        None,
        None,
        None,
        "Seems to initialize and spawn the team when entering a dungeon.\n\nr0: ?",
    )

    SpawnInitialMonsters = Symbol(
        None,
        None,
        None,
        "Tries to spawn monsters on all the tiles marked for monster spawns. This includes normal enemies and mission targets (rescue targets, outlaws, etc.).\n\nA random initial position is selected as a starting point. Tiles are then swept over left-to-right, top-to-bottom, wrapping around when the map boundary is reached, until all tiles have been checked. The first marked tile encountered in the sweep is reserved for the mission target, but the actual spawning of the target is done last.\n\nNo params.",
    )

    SpawnMonster = Symbol(
        None,
        None,
        None,
        "Spawns the given monster on a tile.\n\nr0: pointer to struct spawned_monster_data\nr1: if true, the monster cannot spawn asleep, otherwise it will randomly be asleep\nreturn: pointer to entity",
    )

    InitTeamMember = Symbol(
        None,
        None,
        None,
        "Initializes a team member. Run at the start of each floor in a dungeon.\n\nr0: Monster ID\nr1: X position\nr2: Y position\nr3: Pointer to the struct containing the data of the team member to initialize\nstack[0]: ?\nstack[1]: ?\nstack[2]: ?\nstack[3]: ?\nstack[4]: ?",
    )

    InitMonster = Symbol(
        None,
        None,
        None,
        "Initializes the monster struct within the provided entity struct.\n\nr0: ?\nr1: Pointer to the entity whose monster struct should be initialized\nr2: pointer to the entity's spawned_monster_data struct\nr3: (?) Pointer to something",
    )

    SubInitMonster = Symbol(
        None,
        None,
        None,
        "Called by InitMonster. Initializes some fields on the monster struct.\n\nr0: pointer to monster to initialize\nr1: some flag",
    )

    MarkShopkeeperSpawn = Symbol(
        None,
        None,
        None,
        "Add a shopkeeper spawn to the list on the dungeon struct. Actual spawning is done later by SpawnShopkeepers.\n\nIf an existing entry in dungeon::shopkeeper_spawns exists with the same position, that entry is reused for the new spawn data. Otherwise, a new entry is appended to the array.\n\nr0: x position\nr1: y position\nr2: monster ID\nr3: monster behavior",
    )

    SpawnShopkeepers = Symbol(
        None,
        None,
        None,
        "Spawns all the shopkeepers in the dungeon struct's shopkeeper_spawns array.\n\nNo params.",
    )

    GetMaxHpAtLevel = Symbol(
        None,
        None,
        None,
        "Returns the max HP of a monster given its level.\n\nr0: Monster ID\nr1: Monster level\nreturn: Max HP at the given level",
    )

    GetOffensiveStatAtLevel = Symbol(
        None,
        None,
        None,
        "Returns the Atk / Sp. Atk of a monster given its level, capped to 255.\n\nr0: Monster ID\nr1: Monster level\nr2: Stat index (0: Atk, 1: Sp. Atk)\nreturn: Atk / Sp. Atk at the given level",
    )

    GetDefensiveStatAtLevel = Symbol(
        None,
        None,
        None,
        "Returns the Def / Sp. Def of a monster given its level, capped to 255.\n\nr0: Monster ID\nr1: Monster level\nr2: Stat index (0: Def, 1: Sp. Def)\nreturn: Def / Sp. Def at the given level",
    )

    GetOutlawSpawnData = Symbol(
        None,
        None,
        None,
        "Gets outlaw spawn data for the current floor.\n\nr0: [output] Outlaw spawn data",
    )

    ExecuteMonsterAction = Symbol(
        None,
        None,
        None,
        "Executes the set action for the specified monster. Used for both AI actions and player-inputted actions. If the action is not ACTION_NOTHING, ACTION_PASS_TURN, ACTION_WALK or ACTION_UNK_4, the monster's already_acted field is set to true. Includes a switch based on the action ID that performs the action, although some of them aren't handled by said swtich.\n\nr0: Pointer to monster entity\nreturn: If the result is true, the AI is run again for the current ally, and it performs another action. This can happen up to three times.",
    )

    TryActivateFlashFireOnAllMonsters = Symbol(
        None,
        None,
        None,
        "Checks every monster for apply_flash_fire_boost. If it's true, activates Flash Fire for the monster and sets\napply_flash_fire_boost back to false.\n\nNo params.",
    )

    HasStatusThatPreventsActing = Symbol(
        None,
        None,
        None,
        "Returns true if the monster has any status problem that prevents it from acting\n\nr0: Entity pointer\nreturn: True if the specified monster can't act because of a status problem, false otherwise.",
    )

    GetMobilityTypeCheckSlip = Symbol(
        None,
        None,
        None,
        "Returns the mobility type of a monster species, accounting for STATUS_SLIP.\n\nThe function also converts MOBILITY_LAVA and MOBILITY_WATER to other values if required.\n\nr0: Monster species\nr1: True if the monster can walk on water\nreturn: Mobility type",
    )

    GetMobilityTypeCheckSlipAndFloating = Symbol(
        None,
        None,
        None,
        "Returns the mobility type of a monster, accounting for STATUS_SLIP and the result of a call to IsFloating.\n\nr0: Entity pointer\nr1: Monster species\nreturn: Mobility type",
    )

    IsInvalidSpawnTile = Symbol(
        None,
        None,
        None,
        "Checks if a monster cannot spawn on the given tile for some reason.\n\nReasons include:\n- There's another monster on the tile\n- The tile is an impassable wall\n- The monster does not have the required mobility to stand on the tile\n\nr0: monster ID\nr1: tile pointer\nreturn: true means the monster CANNOT spawn on this tile",
    )

    GetMobilityTypeAfterIqSkills = Symbol(
        None,
        None,
        None,
        "Modifies the given mobility type to account for All-Terrain Hiker and Absolute Mover, if the user has them.\n\nr0: Entity pointer\nr1: Mobility type\nreturn: New mobility type, after accounting for the IQ skills mentioned above",
    )

    CannotStandOnTile = Symbol(
        None,
        None,
        None,
        "Checks if a given monster cannot stand on a given tile.\n\nReasons include:\n- The coordinates of the tile are out of bounds\n- There's another monster on the tile\n- The monster does not have the required mobility to stand on the tile\n\nr0: Entity pointer\nr1: Tile pointer\nreturn: True if the monster cannot stand on the specified tile, false if it can",
    )

    CalcSpeedStage = Symbol(
        None,
        None,
        None,
        "Calculates the speed stage of a monster from its speed up/down counters. The second parameter is the weight of each counter (how many stages it will add/remove), but appears to be always 1. \nTakes modifiers into account (paralysis, snowy weather, Time Tripper). Deoxys-speed, Shaymin-sky and enemy Kecleon during a thief alert get a flat +1 always.\n\nThe calculated speed stage is both returned and saved in the monster's statuses struct.\n\nr0: pointer to entity\nr1: speed counter weight\nreturn: speed stage",
    )

    CalcSpeedStageWrapper = Symbol(
        None,
        None,
        None,
        "Calls CalcSpeedStage with a speed counter weight of 1.\n\nr0: pointer to entity\nreturn: speed stage",
    )

    GetNumberOfAttacks = Symbol(
        None,
        None,
        None,
        "Returns the number of attacks that a monster can do in one turn (1 or 2).\n\nChecks for the abilities Swift Swim, Chlorophyll, Unburden, and for exclusive items.\n\nr0: pointer to entity\nreturns: int",
    )

    GetMonsterDisplayNameType = Symbol(
        None,
        None,
        None,
        "Determines how the name of a monster should be displayed.\n\nr0: Entity pointer\nreturn: Display name type",
    )

    GetMonsterName = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: buffer\nr1: TargetInfo",
    )

    SprintfStatic = Symbol(
        None,
        None,
        None,
        "Statically defined copy of sprintf(3) in overlay 29. See arm9.yml for more information.\n\nr0: str\nr1: format\n...: variadic\nreturn: number of characters printed, excluding the null-terminator",
    )

    IsMonsterDrowsy = Symbol(
        None,
        None,
        None,
        "Checks if a monster has the sleep, nightmare, or yawning status. Note that this excludes the napping status.\n\nr0: entity pointer\nreturn: bool",
    )

    MonsterHasNonvolatileNonsleepStatus = Symbol(
        None,
        None,
        None,
        "Checks if a monster has one of the statuses in the 'burn' group, which includes the traditionally non-volatile status conditions (except sleep) in the main series: STATUS_BURN, STATUS_POISONED, STATUS_BADLY_POISONED, STATUS_PARALYSIS, and STATUS_IDENTIFYING.\n\nSTATUS_IDENTIFYING is probably included based on enum status_id? Unless it's handled differently somehow.\n\nr0: entity pointer\nreturn: bool",
    )

    MonsterHasImmobilizingStatus = Symbol(
        None,
        None,
        None,
        "Checks if a monster has one of the non-self-inflicted statuses in the 'freeze' group, which includes status conditions that immobilize the monster: STATUS_FROZEN, STATUS_SHADOW_HOLD, STATUS_WRAPPED, STATUS_PETRIFIED, STATUS_CONSTRICTION, and STATUS_FAMISHED.\n\nr0: entity pointer\nreturn: bool",
    )

    MonsterHasAttackInterferingStatus = Symbol(
        None,
        None,
        None,
        "Checks if a monster has one of the statuses in the 'cringe' group, which includes status conditions that interfere with the monster's ability to attack: STATUS_CRINGE, STATUS_CONFUSED, STATUS_PAUSED, STATUS_COWERING, STATUS_TAUNTED, STATUS_ENCORE, STATUS_INFATUATED, and STATUS_DOUBLE_SPEED.\n\nSTATUS_DOUBLE_SPEED is probably included based on enum status_id? Unless it's handled differently somehow.\n\nr0: entity pointer\nreturn: bool",
    )

    MonsterHasSkillInterferingStatus = Symbol(
        None,
        None,
        None,
        "Checks if a monster has one of the non-self-inflicted statuses in the 'curse' group, which loosely includes status conditions that interfere with the monster's skills or ability to do things: STATUS_CURSED, STATUS_DECOY, STATUS_GASTRO_ACID, STATUS_HEAL_BLOCK, STATUS_EMBARGO.\n\nr0: entity pointer\nreturn: bool",
    )

    MonsterHasLeechSeedStatus = Symbol(
        None,
        None,
        None,
        "Checks if a monster is afflicted with Leech Seed.\n\nr0: entity pointer\nreturn: bool",
    )

    MonsterHasWhifferStatus = Symbol(
        None,
        None,
        None,
        "Checks if a monster has the whiffer status.\n\nr0: entity pointer\nreturn: bool",
    )

    IsMonsterVisuallyImpaired = Symbol(
        None,
        None,
        None,
        "Checks if a monster's vision is impaired somehow. This includes the checks in IsBlinded, as well as STATUS_CROSS_EYED and STATUS_DROPEYE.\n\nr0: entity pointer\nr1: flag for whether to check for the held item\nreturn: bool",
    )

    IsMonsterMuzzled = Symbol(
        None,
        None,
        None,
        "Checks if a monster has the muzzled status.\n\nr0: entity pointer\nreturn: bool",
    )

    MonsterHasMiracleEyeStatus = Symbol(
        None,
        None,
        None,
        "Checks if a monster has the Miracle Eye status.\n\nr0: entity pointer\nreturn: bool",
    )

    MonsterHasNegativeStatus = Symbol(
        None,
        None,
        None,
        "Checks if a monster has any 'negative' status conditions. This includes a wide variety of non-self-inflicted statuses that could traditionally be viewed as actual 'status conditions', as well as speed being lowered and moves being sealed.\n\nr0: entity pointer\nr1: flag for whether to check for the held item (see IsMonsterVisuallyImpaired)\nreturn: bool",
    )

    IsMonsterSleeping = Symbol(
        None,
        None,
        None,
        "Checks if a monster has the sleep, nightmare, or napping status.\n\nr0: entity pointer\nreturn: bool",
    )

    CanMonsterMoveInDirection = Symbol(
        None,
        None,
        None,
        "Checks if the given monster can move in the specified direction\n\nReturns false if any monster is standing on the target tile\n\nr0: Monster entity pointer\nr1: Direction to check\nreturn: bool",
    )

    GetDirectionalMobilityType = Symbol(
        None,
        None,
        None,
        "Returns the mobility type of a monster, after accounting for things that could affect it.\n\nList of checks: Mobile status, Mobile Scarf, All-Terrain Hiker and Absolute Mover.\n\nIf the specified direction is DIR_NONE, direction checks are skipped. If it's not, MOBILITY_INTANGIBLE is only returned if the direction is not diagonal.\n\nr0: Monster entity pointer\nr1: Base mobility type\nr2: Direction of mobility\nreturn: Final mobility type",
    )

    IsMonsterCornered = Symbol(
        None,
        None,
        None,
        "True if the given monster is cornered (it can't move in any direction)\n\nr0: Entity pointer\nreturn: True if the monster can't move in any direction, false otherwise.",
    )

    CanAttackInDirection = Symbol(
        None,
        None,
        None,
        "Returns whether a monster can attack in a given direction.\nThe check fails if the destination tile is impassable, contains a monster that isn't of type entity_type::ENTITY_MONSTER or if the monster can't directly move from the current tile into the destination tile.\n\nr0: Entity pointer\nr1: Direction\nreturn: True if the monster can attack into the tile adjacent to them in the specified direction, false otherwise.",
    )

    CanAiMonsterMoveInDirection = Symbol(
        None,
        None,
        None,
        "Checks whether an AI-controlled monster can move in the specified direction.\nAccounts for walls, other monsters on the target position and IQ skills that might prevent a monster from moving into a specific location, such as House Avoider, Trap Avoider or Lava Evader.\n\nr0: Entity pointer\nr1: Direction\nr2: [output] True if movement was not possible because there was another monster on the target tile, false otherwise.\nreturn: True if the monster can move in the specified direction, false otherwise.",
    )

    ShouldMonsterRunAway = Symbol(
        None,
        None,
        None,
        "Checks if a monster should run away from other monsters\n\nr0: Entity pointer\nreturn: True if the monster should run away, false otherwise",
    )

    ShouldMonsterRunAwayVariation = Symbol(
        None,
        None,
        None,
        "Calls ShouldMonsterRunAway and returns its result. It also calls another function if the result was true.\n\nr0: Entity pointer\nr1: ?\nreturn: Result of the call to ShouldMonsterRunAway",
    )

    SafeguardIsActive = Symbol(
        None,
        None,
        None,
        "Checks if the monster is under the effect of Safeguard.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to log a message\nreturn: bool",
    )

    LeafGuardIsActive = Symbol(
        None,
        None,
        None,
        "Checks if the monster is protected by the ability Leaf Guard.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to log a message\nreturn: bool",
    )

    IsProtectedFromStatDrops = Symbol(
        None,
        None,
        None,
        "Checks if the target monster is protected from getting their stats dropped by the user.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to log a message\nreturn: bool",
    )

    NoGastroAcidStatus = Symbol(
        None,
        None,
        None,
        "Checks if a monster does not have the Gastro Acid status.\n\nr0: entity pointer\nreturn: bool",
    )

    AbilityIsActive = Symbol(
        None,
        None,
        None,
        "Checks if a monster has a certain ability that isn't disabled by Gastro Acid.\n\nr0: entity pointer\nr1: ability ID\nreturn: bool",
    )

    AbilityIsActiveVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for AbilityIsActive.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nr0: entity pointer\nr1: ability ID\nreturn: bool",
    )

    OtherMonsterAbilityIsActive = Symbol(
        None,
        None,
        None,
        "Checks if there are any other monsters on the floor besides the user that have the specified ability active, subject to the user being on the floor.\n\nIt also seems like there might be some other range or validity check, so this might not actually check ALL other monsters?\n\nr0: user entity pointer\nr1: ability ID\nreturn: bool",
    )

    LevitateIsActive = Symbol(
        None,
        None,
        None,
        "Checks if a monster is levitating (has the effect of Levitate and Gravity is not active).\n\nr0: pointer to entity\nreturn: bool",
    )

    MonsterIsType = Symbol(
        None,
        None,
        None,
        "Checks if a monster is a given type.\n\nr0: entity pointer\nr1: type ID\nreturn: bool",
    )

    IsTypeAffectedByGravity = Symbol(
        None,
        None,
        None,
        "Checks if Gravity is active and that the given type is affected (i.e., Flying type).\n\nr0: target entity pointer (unused)\nr1: type ID\nreturn: bool",
    )

    HasTypeAffectedByGravity = Symbol(
        None,
        None,
        None,
        "Checks if Gravity is active and that the given monster is of an affected type (i.e., Flying type).\n\nr0: target entity pointer\nr1: type ID\nreturn: bool",
    )

    CanSeeInvisibleMonsters = Symbol(
        None,
        None,
        None,
        "Returns whether a certain monster can see other invisible monsters.\nTo be precise, this function returns true if the monster is holding Goggle Specs or if it has the status status::STATUS_EYEDROPS.\n\nr0: Entity pointer\nreturn: True if the monster can see invisible monsters.",
    )

    HasDropeyeStatus = Symbol(
        None,
        None,
        None,
        "Returns whether a certain monster is under the effect of status::STATUS_DROPEYE.\n\nr0: Entity pointer\nreturn: True if the monster has dropeye status.",
    )

    IqSkillIsEnabled = Symbol(
        None,
        None,
        None,
        "Checks if a monster has a certain IQ skill enabled.\n\nr0: entity pointer\nr1: IQ skill ID\nreturn: bool",
    )

    UpdateIqSkills = Symbol(
        None,
        None,
        None,
        "Updates the IQ skill flags of a monster.\n\nIf the monster is a team member, copies monster::iq_skill_menu_flags to monster::iq_skill_flags. If the monster is an enemy, enables all the IQ skills it can learn (except a few that are only enabled in enemies that have a certain amount of IQ).\nIf the monster is an enemy, it also sets its tactic to TACTIC_GO_AFTER_FOES.\nCalled after exiting the IQ skills menu or after an enemy spawns.\n\nr0: monster pointer",
    )

    GetMoveTypeForMonster = Symbol(
        None,
        None,
        None,
        "Check the type of a move when used by a certain monster. Accounts for special cases such as Hidden Power, Weather Ball, the regular attack...\n\nr0: Entity pointer\nr1: Pointer to move data\nreturn: Type of the move",
    )

    GetMovePower = Symbol(
        None,
        None,
        None,
        "Gets the power of a move, factoring in Ginseng/Space Globe boosts.\n\nr0: user pointer\nr1: move pointer\nreturn: move power",
    )

    UpdateStateFlags = Symbol(
        None,
        None,
        None,
        "Updates monster::state_flags and monster::prev_state_flags with new values.\n\nr0: monster pointer\nr1: bitmask for bits to update\nr2: whether to set the bits indicated by the mask to 1 or 0\nreturn: whether or not any of the masked bits changed from the previous state",
    )

    IsProtectedFromNegativeStatus = Symbol(
        None,
        None,
        None,
        "Checks if the target monster is protected from getting a negative status condition.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to log a message\nreturn: bool",
    )

    AddExpSpecial = Symbol(
        None,
        None,
        None,
        "Adds to a monster's experience points, subject to experience boosting effects.\n\nThis function appears to be called only under special circumstances. Possibly when granting experience from damage (e.g., Joy Ribbon)?\n\nInterestingly, the parameter in r0 isn't actually used. This might be a compiler optimization to avoid shuffling registers, since this function might be called alongside lots of other functions that have both the attacker and defender as the first two arguments.\n\nr0: attacker pointer\nr1: defender pointer\nr2: base experience gain, before boosts",
    )

    EnemyEvolution = Symbol(
        None,
        None,
        None,
        "Checks if any enemies on the floor should evolve and attempts to evolve it. The\nentity pointer passed seems to get replaced by a generic placeholder entity if the\nentity pointer passed is invalid.\n\nr0: entity pointer",
    )

    LevelUpItemEffect = Symbol(
        None,
        None,
        None,
        "Attempts to level up the target. Calls LevelUp with a few extra checks and messages\nfor using as an item. Used for the Joy Seed and Golden Seed.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: number of levels\nr3: bool message flag?\nstack[0]: bool show level up dialogue (for example 'Hey, I leveled up!' with a portrait)?",
    )

    TryDecreaseLevel = Symbol(
        None,
        None,
        None,
        "Decrease the target monster's level if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: number of levels to decrease\nreturn: success flag",
    )

    LevelUp = Symbol(
        None,
        None,
        None,
        "Attempts to level up the target. Fails if the target's level can't be raised. The show level up dialogue bool does nothing for monsters not on the team.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: bool message flag?\nr3: bool show level up dialogue (for example 'Hey, I leveled up!' with a portrait)?\nreturn: success flag",
    )

    GetMonsterMoves = Symbol(
        None,
        None,
        None,
        "Determines the moveset of a newly spawned monster given its species and level.\n\nThe function loops the monster's learnset, adding moves to the list in level-up order. Once all four slots are filled up, a random existing move gets replaced to make room for the new one. This means that the monster will always have the latest move it can learn given its level.\n\nr0: [output] Pointer to move ID list (4 entries, 2 bytes each)\nr1: Monster ID\nr2: Monster level",
    )

    EvolveMonster = Symbol(
        None,
        None,
        None,
        "Makes the specified monster evolve into the specified species. Has a special case when\na monster evolves into Ninjask and tries to spawn a Shedinja as well.\n\nr0: user entity pointer?\nr1: target pointer to the entity to evolve\nr2: Species to evolve into",
    )

    ChangeMonsterAnimation = Symbol(
        None,
        None,
        None,
        "Changes the animation a monster is currently playing. Optionally changes their direction as well.\n\nDoes nothing if the provided entity is not a monster.\n\nr0: Entity pointer\nr1: ID of the animation to set\nr2: Direction to turn the monster in, or DIR_NONE to keep the current direction",
    )

    GetIdleAnimationId = Symbol(
        None,
        None,
        None,
        "Returns the animation id to be applied to a monster that is currently idling.\n\nReturns a different animation for monsters with the sleep, napping, nightmare or bide status, as well as for sudowoodo and for monsters with infinite sleep turns (0x7F).\n\nr0: pointer to entity\nreturn: animation ID",
    )

    DisplayActions = Symbol(
        None,
        None,
        None,
        "Graphically displays any pending actions that have happened but haven't been shown on screen yet. All actions are displayed at the same time. For example, this delayed display system is used to display multiple monsters moving at once even though they take turns sequentially.\n\nr0: Pointer to an entity. Can be null.\nreturns: Seems to be true if there were any pending actions to display.",
    )

    CheckNonLeaderTile = Symbol(
        None,
        None,
        None,
        "Similar to CheckLeaderTile, but for other monsters.\n\nUsed both for enemies and team members.\n\nr0: Entity pointer",
    )

    EndNegativeStatusCondition = Symbol(
        None,
        None,
        None,
        "Cures the target's negative status conditions. The game rarely (if not never) calls\nthis function with the bool to remove the wrapping status false.\n\nr0: pointer to user\nr1: pointer to target\nr2: bool play animation\nr3: bool log failure message\nstack[0]: bool remove wrapping status\nreturn: bool succesfully removed negative status",
    )

    EndNegativeStatusConditionWrapper = Symbol(
        None,
        None,
        None,
        "Calls EndNegativeStatusCondition with remove wrapping status false.\n\nr0: pointer to user\nr1: pointer to target\nr2: bool play animation\nr3: bool log failure message\nreturn: bool succesfully removed negative status",
    )

    TransferNegativeStatusCondition = Symbol(
        None,
        None,
        None,
        "Transfers all negative status conditions the user has and gives then to the target.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    EndSleepClassStatus = Symbol(
        None,
        None,
        None,
        "Cures the target's sleep, sleepless, nightmare, yawn or napping status due to the action of the user, and prints the event to the log.\n\nr0: pointer to user\nr1: pointer to target",
    )

    EndBurnClassStatus = Symbol(
        None,
        None,
        None,
        "Cures the target's burned, poisoned, badly poisoned or paralysis status due to the action of the user, and prints the event to the log.\n\nr0: pointer to user\nr1: pointer to target",
    )

    EndFrozenClassStatus = Symbol(
        None,
        None,
        None,
        "Cures the target's freeze, shadow hold, ingrain, petrified, constriction or wrap (both as user and as target) status due to the action of the user.\n\nr0: pointer to user\nr1: pointer to target\nr2: if true, the event will be printed to the log",
    )

    EndCringeClassStatus = Symbol(
        None,
        None,
        None,
        "Cures the target's cringe, confusion, cowering, pause, taunt, encore or infatuated status due to the action of the user, and prints the event to the log.\n\nr0: pointer to user\nr1: pointer to target",
    )

    EndReflectClassStatus = Symbol(
        None,
        None,
        None,
        "Removes the target's reflect, safeguard, light screen, counter, magic coat, wish, protect, mirror coat, endure, mini counter?, mirror move, conversion 2, vital throw, mist, metal burst, aqua ring or lucky chant status due to the action of the user, and prints the event to the log.\n\nr0: pointer to user\nr1: pointer to target",
    )

    TryRemoveSnatchedMonsterFromDungeonStruct = Symbol(
        None,
        None,
        None,
        "If the target is afflicted with snatch, change dungeon::snatch_monster and dungeon::snatch_status_unique_id back\nto NULL and 0 respectively. This function does not actually remove the status and visual flags for snatch from\nthe monster, it simply removes it from the dungeon struct. After calling, the user should ensure the monster\ndoes not still have the snatch status.\n\nr0: pointer to user\nr1: pointer to target",
    )

    EndCurseClassStatus = Symbol(
        None,
        None,
        None,
        "Removes the target's curse (1), decoy (2), snatch (3), gastro acid (4), heal block (5), or embargo (6) status\ndue to the action of the user, and prints the event to the log.\n\nr0: pointer to user\nr1: pointer to target\nr2: curse class status being afflicted after (0 is the status is only being removed)\nr3: flag to log a message",
    )

    EndLeechSeedClassStatus = Symbol(
        None,
        None,
        None,
        "Cures the target's leech seed or destiny bond status due to the action of the user, and prints the event to the log.\n\nr0: pointer to user\nr1: pointer to target",
    )

    EndSureShotClassStatus = Symbol(
        None,
        None,
        None,
        "Removes the target's sure shot, whiffer, set damage or focus energy status due to the action of the user, and prints the event to the log.\n\nr0: pointer to user\nr1: pointer to target",
    )

    EndInvisibleClassStatus = Symbol(
        None,
        None,
        None,
        "Removes the target's invisible, transformed, mobile, or slip status due to the action of the user, and prints\nthe event to the log.\n\nr0: pointer to user\nr1: pointer to target\nr2: flag to not log a message when removing slip status",
    )

    EndBlinkerClassStatus = Symbol(
        None,
        None,
        None,
        "Removes the target's blinker, cross-eyed, eyedrops, or dropeye status due to the action of the user, and\nprints the event to the log.\n\nr0: pointer to user\nr1: pointer to target",
    )

    EndMuzzledStatus = Symbol(
        None,
        None,
        None,
        "Removes the target's muzzled status due to the action of the user, and prints the event to the log.\n\nr0: pointer to user\nr1: pointer to target",
    )

    EndMiracleEyeStatus = Symbol(
        None,
        None,
        None,
        "Removes the target's miracle eye status due to the action of the user, and prints the event to the log.\n\nr0: pointer to user\nr1: pointer to target",
    )

    EndMagnetRiseStatus = Symbol(
        None,
        None,
        None,
        "Removes the target's magnet rise status due to the action of the user, and prints the event to the log.\n\nr0: pointer to user\nr1: pointer to target",
    )

    TransferNegativeBlinkerClassStatus = Symbol(
        None,
        None,
        None,
        "Tries to transfer the negative blinker class status conditions from the user to\nthe target.\n\nr0: user entity pointer\nr1: target entity pointer\nreturn: Whether or not the status could be transferred",
    )

    EndFrozenStatus = Symbol(
        None,
        None,
        None,
        "Cures the target's freeze status due to the action of the user.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    EndProtectStatus = Symbol(
        None,
        None,
        None,
        "Ends the target's protect status due to the action of the user.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryRestoreRoostTyping = Symbol(
        None,
        None,
        None,
        "Tries to restore the target's original typings before the Roost effect took place. Does nothing if the target\nis not affected by Roost.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryTriggerMonsterHouse = Symbol(
        None,
        None,
        None,
        "Triggers a Monster House for an entity, if the right conditions are met.\n\nConditions: entity is valid and on the team, the tile is a Monster House tile, and the Monster House hasn't already been triggered.\n\nThis function sets the monster_house_triggered flag on the dungeon struct, spawns a bunch of enemies around the triggering entity (within a 4 tile radius), and handles the 'dropping down' animation for these enemies. If the allow outside enemies flag is set, the enemy spawns can be on any free tile (no monster) with open terrain, including in hallways. Otherwise, spawns are confined within the room boundaries.\n\nr0: entity for which the Monster House should be triggered\nr1: allow outside enemies flag (in practice this is always set to dungeon_generation_info::force_create_monster_house)",
    )

    ShouldMonsterFollowLeader = Symbol(
        None,
        None,
        None,
        "Checks if the monster should follow the leader. Always returns false for enemy monsters.\nThis function may actually be should monster target leader position.\n\nr0: Pointer to monster\nreturn: bool",
    )

    RunMonsterAi = Symbol(
        None,
        None,
        None,
        "Runs the AI for a single monster to determine whether the monster can act and which action it should perform if so\n\nr0: Pointer to monster\nr1: ?",
    )

    ApplyDamageAndEffects = Symbol(
        None,
        None,
        None,
        "Calls ApplyDamage, then performs various 'post-damage' effects such as counter damage, statuses from abilities that activate on contact, and probably some other stuff.\n\nNote that this doesn't include the effect of Illuminate, which is specifically handled elsewhere.\n\nr0: attacker pointer\nr1: defender pointer\nr2: damage_data pointer\nr3: False Swipe flag (see ApplyDamage)\nstack[0]: experience flag (see ApplyDamage)\nstack[1]: Damage source (see HandleFaint)\nstack[2]: defender response flag. If true, the defender can respond to the attack with various effects. If false, the only post-damage effect that can happen is the Rage attack boost.",
    )

    ApplyDamage = Symbol(
        None,
        None,
        None,
        "Applies damage to a monster. Displays the damage animation, lowers its health and handles reviving if applicable.\nThe EU version has some additional checks related to printing fainting messages under specific circumstances.\n\nr0: Attacker pointer\nr1: Defender pointer\nr2: Pointer to the damage_data struct that contains info about the damage to deal\nr3: False Swipe flag, causes the defender's HP to be set to 1 if it would otherwise have been 0\nstack[0]: experience flag, controls whether or not experience will be granted upon a monster fainting, and whether enemy evolution might be triggered\nstack[1]: Damage source (see HandleFaint)\nreturn: True if the target fainted (reviving does not count as fainting)",
    )

    AftermathCheck = Symbol(
        None,
        None,
        None,
        "Checks if the defender has the Aftermath ability and tries to activate it if so (50% chance).\n\nThe ability won't trigger if the damage source is DAMAGE_SOURCE_EXPLOSION.\n\nr0: Attacker pointer\nr1: Defender pointer\nr2: Damage source\nreturn: True if Aftermath was activated, false if it wasn't",
    )

    GetTypeMatchupBothTypes = Symbol(
        None,
        None,
        None,
        "Gets the type matchup for a given combat interaction, accounting for both of the user's types.\n\nCalls GetTypeMatchup twice and combines the result.\n\nr0: attacker pointer\nr1: defender pointer\nr2: attack type\nreturn: enum type_matchup",
    )

    ScrappyShouldActivate = Symbol(
        None,
        None,
        None,
        "Checks whether Scrappy should activate.\n\nScrappy activates when the ability is active on the attacker, the move type is Normal or Fighting, and the defender is a Ghost type.\n\nr0: attacker pointer\nr1: defender pointer\nr2: move type ID\nreturn: bool",
    )

    IsTypeIneffectiveAgainstGhost = Symbol(
        None,
        None,
        None,
        "Checks whether a type is normally ineffective against Ghost, i.e., it's Normal or Fighting.\n\nr0: type ID\nreturn: bool",
    )

    GhostImmunityIsActive = Symbol(
        None,
        None,
        None,
        "Checks whether the defender's typing would give it Ghost immunities.\n\nThis only checks one of the defender's types at a time. It checks whether the defender has the exposed status and whether the attacker has the Scrappy-like exclusive item effect, but does NOT check whether the attacker has the Scrappy ability.\n\nr0: attacker pointer\nr1: defender pointer\nr2: defender type index (0 the defender's first type, 1 for the defender's second type)\nreturn: bool",
    )

    GetTypeMatchup = Symbol(
        None,
        None,
        None,
        "Gets the type matchup for a given combat interaction.\n\nNote that the actual monster's types on the attacker and defender pointers are not used; the pointers are only used to check conditions. The actual type matchup table lookup is done solely using the attack and target type parameters.\n\nThis factors in some conditional effects like exclusive items, statuses, etc. There's some weirdness with the Ghost type; see the comment for struct type_matchup_table.\n\nr0: attacker pointer\nr1: defender pointer\nr2: target type index (0 the target's first type, 1 for the target's second type)\nr3: attack type\nreturn: enum type_matchup",
    )

    CalcTypeBasedDamageEffects = Symbol(
        None,
        None,
        None,
        "Calculates type-based effects on damage.\n\nLoosely, this includes type matchup effects (including modifications due to abilities, IQ skills, and exclusive items), STAB, pinch abilities like Overgrow, weather/floor condition effects on certain types, and miscellaneous effects like Charge.\n\nr0: [output] damage multiplier due to type effects.\nr1: attacker pointer\nr2: defender pointer\nr3: attack power\nstack[0]: attack type\nstack[1]: [output] struct containing info about the damage calculation (only the critical_hit, type_matchup, and field_0xF fields are modified)\nstack[2]: flag for whether Erratic Player and Technician effects should be excluded. CalcDamage only passes in true if the move is the regular attack or a projectile.\nreturn: whether or not the Type-Advantage Master IQ skill should activate if the attacker has it. In practice, this corresponds to when the attack is super-effective, but technically true is also returned when the defender is an invalid entity.",
    )

    CalcDamage = Symbol(
        None,
        None,
        None,
        "The damage calculation function.\n\nAt a high level, the damage formula is:\n  M * [(153/256)*(A + P) - 0.5*D + 50*ln(10*[L + (A - D)/8 + 50]) - 311]\nwhere:\n  - A is the offensive stat (attack or special attack) with relevant modifiers applied (stat stages, certain items, certain abilities, etc.)\n  - D is the defensive stat (defense or special defense) with relevant modifiers applied (stat stages, certain items, certain abilities, etc.)\n  - L is the attacker's level\n  - P is the move power with relevant modifiers applied\n  - M is an aggregate damage multiplier from a variety of things, such as type-effectiveness, STAB, critical hits (which are also rolled in this function), certain items, certain abilities, certain statuses, etc.\n\nThe calculations are done primarily with 64-bit fixed point arithmetic, and a bit of 32-bit fixed point arithmetic. There's also rounding/truncation/clamping at various steps in the process.\n\nr0: attacker pointer\nr1: defender pointer\nr2: attack type\nr3: attack power\nstack[0]: crit chance\nstack[1]: [output] struct containing info about the damage calculation\nstack[2]: damage multiplier (as a binary fixed-point number with 8 fraction bits)\nstack[3]: move ID\nstack[4]: flag to account for certain effects (Flash Fire, Reflect, Light Screen, aura bows, Def. Scarf, Zinc Band). Only ever set to false when computing recoil damage for Jump Kick/Hi Jump Kick missing, which is based on the damage that would have been done if the move didn't miss.",
    )

    ApplyDamageAndEffectsWrapper = Symbol(
        None,
        None,
        None,
        "A wrapper for ApplyDamageAndEffects used for applying damage from sources such as statuses, traps, liquid ooze,\nhunger, and possibly more.\n\nr0: monster entity pointer\nr1: damage amount\nr2: damage message\nr3: damage source",
    )

    CalcRecoilDamageFixed = Symbol(
        None,
        None,
        None,
        "Appears to calculate recoil damage to a monster.\n\nThis function wraps CalcDamageFixed using the monster as both the attacker and the defender, after doing some basic checks (like if the monster is already at 0 HP) and applying a boost from the Reckless ability if applicable.\n\nr0: entity pointer\nr1: fixed damage\nr2: ?\nr3: [output] struct containing info about the damage calculation\nstack[0]: move ID (interestingly, this doesn't seem to be used by the function)\nstack[1]: attack type\nstack[2]: damage source\nstack[3]: damage message\nothers: ?",
    )

    CalcDamageFixed = Symbol(
        None,
        None,
        None,
        "Appears to calculate damage from a fixed-damage effect.\n\nr0: attacker pointer\nr1: defender pointer\nr2: fixed damage\nr3: experience flag (see ApplyDamage)\nstack[0]: [output] struct containing info about the damage calculation\nstack[1]: attack type\nstack[2]: move category\nstack[3]: damage source\nstack[4]: damage message\nothers: ?",
    )

    CalcDamageFixedNoCategory = Symbol(
        None,
        None,
        None,
        "A wrapper around CalcDamageFixed with the move category set to none.\n\nr0: attacker pointer\nr1: defender pointer\nr2: fixed damage\nr3: experience flag (see ApplyDamage)\nstack[0]: [output] struct containing info about the damage calculation\nstack[1]: attack type\nstack[2]: damage source\nstack[3]: damage message\nothers: ?",
    )

    CalcDamageFixedWrapper = Symbol(
        None,
        None,
        None,
        "A wrapper around CalcDamageFixed.\n\nr0: attacker pointer\nr1: defender pointer\nr2: fixed damage\nr3: experience flag (see ApplyDamage)\nstack[0]: [output] struct containing info about the damage calculation\nstack[1]: attack type\nstack[2]: move category\nstack[3]: damage source\nstack[4]: damage message\nothers: ?",
    )

    UpdateShopkeeperModeAfterAttack = Symbol(
        None,
        None,
        None,
        "Updates the shopkeeper mode of a monster in response to being struck by an attack.\n\nIf the defender is in normal shopkeeper mode (not aggressive), nothing happens. Otherwise, the mode is set to SHOPKEEPER_MODE_ATTACK_TEAM if the attacker is a team member, or SHOPKEEPER_MODE_ATTACK_ENEMIES otherwise.\n\nr0: attacker pointer\nr1: defender pointer",
    )

    UpdateShopkeeperModeAfterTrap = Symbol(
        None,
        None,
        None,
        "Updates the shopkeeper mode of a monster in response to stepping on a trap.\n\nIf in the normal shopkeeper mode (not aggressive), nothing happens. Otherwise, the mode is set to SHOPKEEPER_MODE_ATTACK_TEAM if the trap is from a team member or SHOPKEEPER_MODE_ATTACK_ENEMIES otherwise.\n\nr0: shopkeeper pointer\nr1: bool non team member trap",
    )

    ResetDamageCalcDiagnostics = Symbol(
        None,
        None,
        None,
        "Resets the damage calculation diagnostic info stored on the dungeon struct. Called unconditionally at the start of CalcDamage.\n\nNo params.",
    )

    SpecificRecruitCheck = Symbol(
        None,
        None,
        None,
        "Checks if a specific monster can be recruited. Called by RecruitCheck.\n\nWill return false if dungeon::recruiting_enabled is false, if the monster is Mew and dungeon::dungeon_objective is OBJECTIVE_RESCUE or if the monster is any of the special Deoxys forms or any of the 3 regis.\nIf this function returns false, RecruitCheck will return false as well.\n\nr0: Monster ID\nreturn: True if the monster can be recruited",
    )

    RecruitCheck = Symbol(
        None,
        None,
        None,
        "Determines if a defeated enemy will attempt to join the team\n\nr0: user entity pointer\nr1: target entity pointer\nreturn: True if the target will attempt to join the team",
    )

    TryRecruit = Symbol(
        None,
        None,
        None,
        "Asks the player if they would like to recruit the enemy that was just defeated and handles the recruitment if they accept.\n\nr0: user entity pointer\nr1: monster to recruit entity pointer\nreturn: True if the monster was recruited, false if it wasn't",
    )

    TrySpawnMonsterAndTickSpawnCounter = Symbol(
        None,
        None,
        None,
        "First ticks up the spawn counter, and if it's equal or greater than the spawn cooldown, it will try to spawn an enemy if the number of enemies is below the spawn cap.\n\nIf the spawn counter is greater than 900, it will instead perform the special spawn caused by the ability Illuminate.\n\nNo params.",
    )

    TryNonLeaderItemPickUp = Symbol(
        None,
        None,
        None,
        "Similar to TryLeaderItemPickUp, but for other monsters.\n\nUsed both for enemies and team members.\n\nr0: entity pointer",
    )

    AuraBowIsActive = Symbol(
        None,
        None,
        None,
        "Checks if a monster is holding an aura bow that isn't disabled by Klutz.\n\nr0: entity pointer\nreturn: bool",
    )

    ExclusiveItemOffenseBoost = Symbol(
        None,
        None,
        None,
        "Gets the exclusive item boost for attack/special attack for a monster\n\nr0: entity pointer\nr1: move category index (0 for physical, 1 for special)\nreturn: boost",
    )

    ExclusiveItemDefenseBoost = Symbol(
        None,
        None,
        None,
        "Gets the exclusive item boost for defense/special defense for a monster\n\nr0: entity pointer\nr1: move category index (0 for physical, 1 for special)\nreturn: boost",
    )

    TeamMemberHasItemActive = Symbol(
        None,
        None,
        None,
        "Checks if any team member is holding a certain item and puts them into the array given.\n\nr0: [output] pointer to array of monsters (expected to have space for at least 4 pointers)\nr1: item ID\nreturn: number of team members with the item active",
    )

    TeamMemberHasExclusiveItemEffectActive = Symbol(
        None,
        None,
        None,
        "Checks if any team member is under the effects of a certain exclusive item effect.\n\nr0: exclusive item effect ID\nreturn: bool",
    )

    TrySpawnEnemyItemDrop = Symbol(
        None,
        None,
        None,
        "Determine what item a defeated enemy should drop, if any, then (probably?) spawn that item underneath them.\n\nThis function is called at the time when an enemy is defeated from ApplyDamage.\n\nr0: attacker entity (who defeated the enemy)\nr1: defender entity (who was defeated)",
    )

    TickNoSlipCap = Symbol(
        None,
        None,
        None,
        "Checks if the entity is a team member and holds the No-Slip Cap, and if so attempts to make one item in the bag sticky.\n\nr0: pointer to entity",
    )

    TickStatusAndHealthRegen = Symbol(
        None,
        None,
        None,
        "Applies the natural HP regen effect by taking modifiers into account (Poison Heal, Heal Ribbon, weather-related regen). Then it ticks down counters for volatile status effects, and heals them if the counter reached zero.\n\nr0: pointer to entity",
    )

    InflictSleepStatusSingle = Symbol(
        None,
        None,
        None,
        "This is called by TryInflictSleepStatus.\n\nr0: entity pointer\nr1: number of turns",
    )

    TryInflictSleepStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Sleep status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: number of turns\nr3: flag to log a message on failure",
    )

    IsProtectedFromSleepClassStatus = Symbol(
        None,
        None,
        None,
        "Checks if the monster is immune to sleep class status conditions.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: ignore safeguard\nr3: ignore other protections (exclusive items + leaf guard)\nstack[0]: flag to log a message on failure\nreturn: bool",
    )

    TryInflictNightmareStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Nightmare status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: number of turns",
    )

    TryInflictNappingStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Napping status condition (from Rest) on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: number of turns",
    )

    TryInflictYawningStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Yawning status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: number of turns",
    )

    TryInflictSleeplessStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Sleepless status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictPausedStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Paused status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: ?\nr3: number of turns\nstack[0]: flag to log a message on failure\nstack[1]: flag to only perform the check for inflicting without actually inflicting\nreturn: Whether or not the status could be inflicted",
    )

    TryInflictInfatuatedStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Infatuated status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to log a message on failure\nr3: flag to only perform the check for inflicting without actually inflicting\nreturn: Whether or not the status could be inflicted",
    )

    TryInflictBurnStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Burn status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to apply some special effect alongside the burn?\nr3: flag to log a message on failure\nstack[0]: flag to only perform the check for inflicting without actually inflicting\nreturn: Whether or not the status could be inflicted",
    )

    TryInflictBurnStatusWholeTeam = Symbol(
        None,
        None,
        None,
        "Inflicts the Burn status condition on all team members if possible.\n\nNo params.",
    )

    TryInflictPoisonedStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Poisoned status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to log a message on failure\nr3: flag to only perform the check for inflicting without actually inflicting\nreturn: Whether or not the status could be inflicted",
    )

    TryInflictBadlyPoisonedStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Badly Poisoned status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to log a message on failure\nr3: flag to only perform the check for inflicting without actually inflicting\nreturn: Whether or not the status could be inflicted",
    )

    TryInflictFrozenStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Frozen status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to log a message on failure",
    )

    TryInflictConstrictionStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Constriction status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: animation ID\nr3: flag to log a message on failure",
    )

    TryInflictShadowHoldStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Shadow Hold (AKA Immobilized) status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to only perform the check for inflicting without actually inflicting",
    )

    TryInflictIngrainStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Ingrain status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictWrappedStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Wrapped status condition on a target monster if possible.\n\nThis also gives the user the Wrap status (Wrapped around foe).\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    FreeOtherWrappedMonsters = Symbol(
        None,
        None,
        None,
        "Frees from the wrap status all monsters which are wrapped by/around the monster passed as parameter.\n\nr0: pointer to entity",
    )

    TryInflictPetrifiedStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Petrified status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    LowerOffensiveStat = Symbol(
        None,
        None,
        None,
        "Lowers the specified offensive stat on the target monster.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: stat index\nr3: number of stages\nstack[0]: flag to check for being protected from stat drops\nstack[1]: flag to log a message on failure for IsProtectedFromStatDrops",
    )

    LowerDefensiveStat = Symbol(
        None,
        None,
        None,
        "Lowers the specified defensive stat on the target monster.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: stat index\nr3: number of stages\nstack[0]: flag to check for being protected from stat drops\nstack[1]: flag to log a message on failure for IsProtectedFromStatDrops",
    )

    BoostOffensiveStat = Symbol(
        None,
        None,
        None,
        "Boosts the specified offensive stat on the target monster.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: stat index\nr3: number of stages",
    )

    BoostDefensiveStat = Symbol(
        None,
        None,
        None,
        "Boosts the specified defensive stat on the target monster.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: stat index\nr3: number of stages",
    )

    FlashFireShouldActivate = Symbol(
        None,
        None,
        None,
        "Checks whether Flash Fire should activate, assuming the defender is being hit by a Fire-type move.\n\nThis checks that the defender is valid and Flash Fire is active, and that Normalize isn't active on the attacker.\n\nr0: attacker pointer\nr1: defender pointer\nreturn: 2 if Flash Fire should activate and raise the defender's boost level, 1 if Flash Fire should activate but the defender's boost level is maxed out, 0 otherwise.",
    )

    ActivateFlashFire = Symbol(
        None,
        None,
        None,
        "Actually applies the Flash Fire boost with a message log and animation. Passes the same monster for attacker and\ndefender, but the attacker goes unused.\n\nr0: attacker pointer?\nr1: defender pointer",
    )

    ApplyOffensiveStatMultiplier = Symbol(
        None,
        None,
        None,
        "Applies a multiplier to the specified offensive stat on the target monster.\n\nThis affects struct monster_stat_modifiers::offensive_multipliers, for moves like Charm and Memento.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: stat index\nr3: multiplier\nstack[0]: ?",
    )

    ApplyDefensiveStatMultiplier = Symbol(
        None,
        None,
        None,
        "Applies a multiplier to the specified defensive stat on the target monster.\n\nThis affects struct monster_stat_modifiers::defensive_multipliers, for moves like Screech.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: stat index\nr3: multiplier\nstack[0]: ?",
    )

    BoostHitChanceStat = Symbol(
        None,
        None,
        None,
        "Boosts the specified hit chance stat (accuracy or evasion) on the target monster.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: stat index",
    )

    LowerHitChanceStat = Symbol(
        None,
        None,
        None,
        "Lowers the specified hit chance stat (accuracy or evasion) on the target monster.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: stat index\nr3: ? (Irdkwia's notes say this is the number of stages, but I'm pretty sure that's incorrect)",
    )

    TryInflictCringeStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Cringe status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to log a message on failure\nr3: flag to only perform the check for inflicting without actually inflicting\nreturn: Whether or not the status could be inflicted",
    )

    TryInflictParalysisStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Paralysis status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to log a message on failure\nr3: flag to only perform the check for inflicting without actually inflicting\nreturn: Whether or not the status could be inflicted",
    )

    BoostSpeed = Symbol(
        None,
        None,
        None,
        "Boosts the speed of the target monster.\n\nIf the number of turns specified is 0, a random turn count will be selected using the default SPEED_BOOST_TURN_RANGE.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: number of stages\nr3: number of turns\nstack[0]: flag to log a message on failure",
    )

    BoostSpeedOneStage = Symbol(
        None,
        None,
        None,
        "A wrapper around BoostSpeed with the number of stages set to 1.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: number of turns\nr3: flag to log a message on failure",
    )

    LowerSpeed = Symbol(
        None,
        None,
        None,
        "Lowers the speed of the target monster.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: number of stages\nr3: flag to log a message on failure",
    )

    TrySealMove = Symbol(
        None,
        None,
        None,
        "Seals one of the target monster's moves. The move to be sealed is randomly selected.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to log a message on failure\nreturn: Whether or not a move was sealed",
    )

    BoostOrLowerSpeed = Symbol(
        None,
        None,
        None,
        "Randomly boosts or lowers the speed of the target monster by one stage with equal probability.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    ResetHitChanceStat = Symbol(
        None,
        None,
        None,
        "Resets the specified hit chance stat (accuracy or evasion) back to normal on the target monster.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: stat index\nr3: ?",
    )

    ExclusiveItemEffectIsActiveWithLogging = Symbol(
        None,
        None,
        None,
        "Calls ExclusiveItemEffectIsActive, then logs the specified message if indicated.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: whether a message should be logged if the effect is active\nr3: message ID to be logged if the effect is active\nstack[0]: exclusive item effect ID\nreturn: bool, same as ExclusiveItemEffectIsActive",
    )

    TryActivateQuickFeet = Symbol(
        None,
        None,
        None,
        "Activate the Quick Feet ability on the defender, if the monster has it and it's active.\n\nr0: attacker pointer\nr1: defender pointer\nreturn: bool, whether or not the ability was activated",
    )

    TryInflictTerrifiedStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Terrified status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictGrudgeStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Grudge status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to log a message\nreturn: Whether or not the status could be inflicted",
    )

    TryInflictConfusedStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Confused status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to log a message on failure\nr3: flag to only perform the check for inflicting without actually inflicting\nreturn: Whether or not the status could be inflicted",
    )

    TryInflictCoweringStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Cowering status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to log a message on failure\nr3: flag to only perform the check for inflicting without actually inflicting\nreturn: Whether or not the status could be inflicted",
    )

    TryRestoreHp = Symbol(
        None,
        None,
        None,
        "Restore HP of the target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: HP to restore\nreturn: success flag",
    )

    TryIncreaseHp = Symbol(
        None,
        None,
        None,
        "Restore HP and possibly boost max HP of the target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: HP to restore\nr3: max HP boost\nstack[0]: flag to log a message on failure\nreturn: Success flag",
    )

    RevealItems = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    RevealStairs = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    RevealEnemies = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictLeechSeedStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Leech Seed status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to log a message on failure\nr3: flag to only perform the check for inflicting without actually inflicting\nreturn: Whether or not the status could be inflicted",
    )

    TryInflictDestinyBondStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Destiny Bond status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictSureShotStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Sure Shot status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictWhifferStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Whiffer status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictSetDamageStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Set Damage status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictFocusEnergyStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Focus Energy status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictDecoyStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Decoy status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nreturn: Whether or not the status could be inflicted",
    )

    TryInflictCurseStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Curse status condition on a target monster if possible and if the user is\na ghost type. Otherwise, just boost the user's defense and attack then lower the user's\nspeed.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictSnatchStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Snatch status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictTauntStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Taunt status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nreturn: Whether or not the status could be inflicted",
    )

    TryInflictStockpileStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Stockpile condition on a target monster if possible. Won't boost the level\nof stockpiling above 3.\n\nr0: user entity pointer\nr1: target entity pointer\nreturn: Whether or not the status could be inflicted or boosted",
    )

    TryInflictInvisibleStatus = Symbol(
        None,
        None,
        None,
        "Attempts to turn the target invisible.\n\nThe user pointer is only used when calling LogMessage functions.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictPerishSongStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Perish Song status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to only perform the check for inflicting without actually inflicting\nreturn: Whether or not the status could be inflicted",
    )

    TryInflictEncoreStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Encore status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to only perform the check for inflicting without actually inflicting\nreturn: Whether or not the status could be inflicted",
    )

    TryDecreaseBelly = Symbol(
        None,
        None,
        None,
        "Tries to reduce the belly size of the target. Only when max belly shrink is 0, the\ncurrent belly is reduced by belly to lose. If both are non-zero, only the max belly\nshrink is applied.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: belly to lose\nr3: max belly shrink",
    )

    TryIncreaseBelly = Symbol(
        None,
        None,
        None,
        "Restore belly and possibly boost max belly of the target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: belly to restore\nr3: max belly boost (if belly is full)\nstack[0]: flag to log a message",
    )

    TryInflictMuzzledStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Muzzled status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to only perform the check for inflicting without actually inflicting\nreturn: Whether or not the status could be inflicted",
    )

    TryTransform = Symbol(
        None,
        None,
        None,
        "Attempts to transform the target into the species of a random monster contained in the list returned by MonsterSpawnListPartialCopy.\n\nThe user pointer is only used when calling LogMessage functions.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictMobileStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Mobile status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictExposedStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Exposed status condition on a target monster if possible. Only applies to\nGhost types and monsters with raised evasion. If the animation effect ID is 0,\ndefaults to animation ID 0xE (this fallback animation likely can't be seen in normal\nplay).\n\nr0: user entity pointer\nr1: target entity pointer\nr2: animation effect ID\nr3: flag to only perform the check for inflicting without actually inflicting\nreturn: Whether or not the status could be inflicted",
    )

    TryActivateIdentifyCondition = Symbol(
        None,
        None,
        None,
        "Sets the flag for the identify orb which causes monsters holding items to be shown with\na blue exclamation mark status icon.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictBlinkerStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Blinker status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to only perform the check for inflicting without actually inflicting\nr3: flag to log a message on failure\nreturn: Whether or not the status could be inflicted",
    )

    IsBlinded = Symbol(
        None,
        None,
        None,
        "Returns true if the monster has the blinded status (see statuses::blinded), or if it is not the leader and is holding Y-Ray Specs.\n\nr0: pointer to entity\nr1: flag for whether to check for the held item\nreturn: bool",
    )

    TryInflictCrossEyedStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Cross-Eyed status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to only perform the check for inflicting without actually inflicting\nreturn: Whether or not the status could be inflicted",
    )

    TryInflictEyedropStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Eyedrop status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictSlipStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Slip status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nreturn: Whether or not the status could be inflicted",
    )

    TryInflictDropeyeStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Dropeye status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nreturn: Whether or not the status could be inflicted",
    )

    RestoreAllMovePP = Symbol(
        None,
        None,
        None,
        "Restores the PP of all the target's moves by the specified amount.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: PP to restore\nr3: flag to suppress message logging",
    )

    RestoreOneMovePP = Symbol(
        None,
        None,
        None,
        "Restores the PP the target's move in the specified move slot by the specified amount.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: move index\nr3: PP to restore\nstack[0]: flag to log message",
    )

    RestoreRandomMovePP = Symbol(
        None,
        None,
        None,
        "Restores the PP of a random one of the target's moves by the specified amount.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: PP to restore\nr3: flag to log message",
    )

    ApplyProteinEffect = Symbol(
        None,
        None,
        None,
        "Tries to boost the target's attack stat.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: attack boost",
    )

    ApplyCalciumEffect = Symbol(
        None,
        None,
        None,
        "Tries to boost the target's special attack stat.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: special attack boost",
    )

    ApplyIronEffect = Symbol(
        None,
        None,
        None,
        "Tries to boost the target's defense stat.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: defense boost",
    )

    ApplyZincEffect = Symbol(
        None,
        None,
        None,
        "Tries to boost the target's special defense stat.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: special defense boost",
    )

    TryInflictLongTossStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Long Toss status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictPierceStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Pierce status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictGastroAcidStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Gastro Acid status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to log message\nr3: flag to only perform the check for inflicting without actually inflicting\nreturn: Whether or not the status could be inflicted",
    )

    SetAquaRingHealingCountdownTo4 = Symbol(
        None,
        None,
        None,
        "Sets the countdown for Aqua Ring healing countdown to a global value (0x4).\n\nr0: pointer to entity",
    )

    ApplyAquaRingHealing = Symbol(
        None,
        None,
        None,
        "Applies the passive healing gained from the Aqua Ring status.\n\nr0: pointer to entity",
    )

    TryInflictAquaRingStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Aqua Ring status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictLuckyChantStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Lucky Chant status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictHealBlockStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Heal Block status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to log message\nr3: flag to only perform the check for inflicting without actually inflicting\nreturn: Whether or not the status could be inflicted",
    )

    MonsterHasEmbargoStatus = Symbol(
        None,
        None,
        None,
        "Returns true if the monster has the Embargo status condition.\n\nr0: pointer to entity\nreturn: bool",
    )

    LogItemBlockedByEmbargo = Symbol(
        None,
        None,
        None,
        "Logs the error message when the usage of an item is blocked by Embargo.\n\nr0: pointer to entity",
    )

    TryInflictEmbargoStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Embargo status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to log message\nr3: flag to only perform the check for inflicting without actually inflicting\nreturn: Whether or not the status could be inflicted",
    )

    TryInflictMiracleEyeStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Miracle Eye status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: flag to only perform the check for inflicting without actually inflicting",
    )

    TryInflictMagnetRiseStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Magnet Rise status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    IsFloating = Symbol(
        None,
        None,
        None,
        "Checks if a monster is currently floating for reasons other than its typing or ability.\n\nIn particular, this checks for Gravity and Magnet Rise.\n\nr0: entity pointer\nreturn: bool",
    )

    TryInflictSafeguardStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Safeguard status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictMistStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Mist status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictWishStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Wish status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictMagicCoatStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Magic Coat status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictLightScreenStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Light Screen status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictReflectStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Reflect status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictProtectStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Protect status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictMirrorCoatStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Mirror Coat status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictEndureStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Endure status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictMirrorMoveStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Mirror Move status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictConversion2Status = Symbol(
        None,
        None,
        None,
        "Inflicts the Conversion2 status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryInflictVitalThrowStatus = Symbol(
        None,
        None,
        None,
        "Inflicts the Vital Throw status condition on a target monster if possible.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    TryResetStatChanges = Symbol(
        None,
        None,
        None,
        "Tries to reset the stat changes of the defender.\n\nr0: attacker entity pointer\nr1: defender entity pointer\nr3: bool to force animation",
    )

    MirrorMoveIsActive = Symbol(
        None,
        None,
        None,
        "Checks if the monster is under the effect of Mirror Move.\n\nReturns 1 if the effects is a status, 2 if it comes from an exclusive item, 0 otherwise.\n\nr0: pointer to entity\nreturn: int",
    )

    MistIsActive = Symbol(
        None,
        None,
        None,
        "Checks if the monster is under the effect of Mist.\n\nReturns 1 if the effects is a status, 2 if it comes from an exclusive item, 0 otherwise.\n\nr0: pointer to entity\nreturn: int",
    )

    Conversion2IsActive = Symbol(
        None,
        None,
        None,
        "Checks if the monster is under the effect of Conversion 2 (its type was changed).\n\nReturns 1 if the effects is a status, 2 if it comes from an exclusive item, 0 otherwise.\n\nr0: pointer to entity\nreturn: int",
    )

    AiConsiderMove = Symbol(
        None,
        None,
        None,
        "The AI uses this function to check if a move has any potential targets, to calculate the list of potential targets and to calculate the move's special weight.\nThis weight will be higher if the pokémon has weak-type picker and the target is weak to the move (allies only, enemies always get a result of 1 even if the move is super effective). More things could affect the result.\nThis function also sets the flag can_be_used on the ai_possible_move struct if it makes sense to use it.\nMore research is needed. There's more documentation about this special weight. Does all the documented behavior happen in this function?\n\nr0: ai_possible_move struct for this move\nr1: Entity pointer\nr2: Move pointer\nreturn: Move's calculated special weight",
    )

    TryAddTargetToAiTargetList = Symbol(
        None,
        None,
        None,
        "Checks if the specified target is eligible to be targeted by the AI and if so adds it to the list of targets. This function also fills an array that seems to contain the directions in which the user should turn to look at each of the targets in the list, as well as a third unknown array.\n\nr0: Number of existing targets in the list\nr1: Move's AI range field\nr2: User entity pointer\nr3: Target entity pointer\nstack[0]: Move pointer\nstack[1]: check_all_conditions parameter to pass to IsAiTargetEligible\nreturn: New number of targets in the target list",
    )

    IsAiTargetEligible = Symbol(
        None,
        None,
        None,
        "Checks if a given target is eligible to be targeted by the AI with a certain move\n\nr0: Move's AI range field\nr1: User entity pointer\nr2: Target entity pointer\nr3: Move pointer\nstack[0]: True to check all the possible move_ai_condition values, false to only check for move_ai_condition::AI_CONDITION_RANDOM (if the move has a different ai condition, the result will be false).\nreturn: True if the target is eligible, false otherwise",
    )

    IsTargetInRange = Symbol(
        None,
        None,
        None,
        "Returns true if the target is within range of the user's move, false otherwise.\n\nIf the user does not have Course Checker, it simply checks if the distance between user and target is less or equal than the move range.\nOtherwise, it will iterate through all tiles in the direction specified, checking for walls or other monsters in the way, and return false if they are found.\n\nr0: user pointer\nr1: target pointer\nr2: direction ID\nr3: move range (in number of tiles)",
    )

    ShouldUsePp = Symbol(
        None,
        None,
        None,
        "Checks if a monster should use PP when using a move. It also displays the corresponding animation if PP Saver triggers and prints the required messages to the message log.\n\nr0: entity pointer\nreturn: True if the monster should not use PP, false if it should.",
    )

    GetEntityMoveTargetAndRange = Symbol(
        None,
        None,
        None,
        "Gets the move target-and-range field when used by a given entity. See struct move_target_and_range in the C headers.\n\nr0: entity pointer\nr1: move pointer\nr2: AI flag (same as GetMoveTargetAndRange)\nreturn: move target and range",
    )

    GetEntityNaturalGiftInfo = Symbol(
        None,
        None,
        None,
        "Gets the relevant entry in NATURAL_GIFT_ITEM_TABLE based on the entity's held item, if possible.\n\nr0: entity pointer\nreturn: pointer to a struct natural_gift_item_info, or null if none was found",
    )

    GetEntityWeatherBallType = Symbol(
        None,
        None,
        None,
        "Gets the current Weather Ball type for the given entity, based on the apparent weather.\n\nr0: entity pointer\nreturn: type ID",
    )

    ActivateMotorDrive = Symbol(
        None,
        None,
        None,
        "Displays the message and applies the speed boost for the ability Motor Drive.\n\nr0: monster pointer",
    )

    TryActivateFrisk = Symbol(
        None,
        None,
        None,
        "Tries to activate the Frisk ability on the defender. The attacker has to be on the team and the defender has to be\nholding an item or be able to drop a treasure box.\n\nr0: attacker pointer\nr1: defender pointer",
    )

    TryActivateBadDreams = Symbol(
        None,
        None,
        None,
        "Tries to apply the damage from Bad Dreams to all sleeping monsters in the room.\n\nr0: monster pointer",
    )

    ActivateStench = Symbol(
        None,
        None,
        None,
        "Activate the Stench ability on the monster.\n\nr0: monster pointer",
    )

    TryActivateSteadfast = Symbol(
        None,
        None,
        None,
        "Activate the Steadfast ability on the defender, if the monster has it and it's active.\n\nr0: attacker pointer\nr1: defender pointer",
    )

    IsInSpawnList = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: spawn_list_ptr\nr1: monster ID\nreturn: bool",
    )

    ChangeShayminForme = Symbol(
        None,
        None,
        None,
        "forme:\n  1: change from Land to Sky\n  2: change from Sky to Land\nresult:\n  0: not Shaymin\n  1: not correct Forme\n  2: frozen\n  3: ok\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: Target\nr1: forme\nreturn: result",
    )

    ApplyItemEffect = Symbol(
        None,
        None,
        None,
        "Seems to apply an item's effect via a giant switch statement?\n\nr3: attacker pointer\nstack[0]: defender pointer\nstack[1]: thrown item pointer\nothers: ?",
    )

    ApplyCheriBerryEffect = Symbol(
        None,
        None,
        None,
        "Tries to heal the paralysis status condition. Prints a message on failure.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    ApplyPechaBerryEffect = Symbol(
        None,
        None,
        None,
        "Tries to heal the poisoned and badly poisoned status condition. Prints a message on\nfailure.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    ApplyRawstBerryEffect = Symbol(
        None,
        None,
        None,
        "Tries to heal the burn status condition. Prints a message on failure.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    ApplyHungerSeedEffect = Symbol(
        None,
        None,
        None,
        "Empties the targets belly to cause Hungry Pal status in non-leader monsters and\nFamished in the leader monster.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    ApplyVileSeedEffect = Symbol(
        None,
        None,
        None,
        "Reduces the targets defense and special defense stages to the lowest level.\n\nr0: attacker pointer\nr1: defender pointer",
    )

    ApplyViolentSeedEffect = Symbol(
        None,
        None,
        None,
        "Boosts the target's offensive stats stages to the max.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    ApplyGinsengEffect = Symbol(
        None,
        None,
        None,
        "Boosts the power of the move at the top of the target's Move List. Appears to have a\nleftover check to boost the power of a move by 3 instead of 1 that always fails because\nthe chance is 0.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    ApplyBlastSeedEffect = Symbol(
        None,
        None,
        None,
        "If thrown, unfreeze and deal fixed damage to the defender. If not thrown, try to find \na monster in front of the attacker. If a monster is found unfreeze and dedal fixed \ndamage to the defender. Appears to have a leftover check for if the current fixed room is a boss fight and loads a different pointer for the damage when used in a boss room.\nHowever, this isn't noticeable because both the normal and boss damage is the same.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: bool thrown",
    )

    ApplyGummiBoostsDungeonMode = Symbol(
        None,
        None,
        None,
        "Applies the IQ and possible stat boosts from eating a Gummi to the target monster.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: Gummi type ID\nr3: Stat boost amount, if a random stat boost occurs",
    )

    CanMonsterUseItem = Symbol(
        None,
        None,
        None,
        "Checks whether a monster can use a certain item.\n\nReturns false if the item is sticky, or if the monster is under the STATUS_MUZZLED status and the item is edible.\nAlso prints failure messages if required.\n\nr0: Monster entity pointer\nr1: Item pointer\nreturn: True if the monster can use the item, false otherwise",
    )

    ApplyGrimyFoodEffect = Symbol(
        None,
        None,
        None,
        "Randomly inflicts poison, shadow hold, burn, paralysis, or an offensive stat debuff\nto the target. If the survivalist iq skill or gluttony ability is active, the target\nhas a 50% chance not to be affected.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    ApplyMixElixirEffect = Symbol(
        None,
        None,
        None,
        "If the target monster is a Linoone, restores all the PP of all the target's moves.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    ApplyDoughSeedEffect = Symbol(
        None,
        None,
        None,
        "If the target monster is a team member, set dough_seed_extra_poke_flag to true to \nmake extra poke spawn on the next floor. Otherwise, do nothing.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    ApplyViaSeedEffect = Symbol(
        None,
        None,
        None,
        "Tries to randomly teleport the target with a message for eating the seed.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    ApplyGravelyrockEffect = Symbol(
        None,
        None,
        None,
        "Restores 10 hunger to the target and will raise the target's IQ if they are a bonsly\nor sudowoodo.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    ApplyGonePebbleEffect = Symbol(
        None,
        None,
        None,
        "Causes a few visual effects, temporarily changes the dungeon music to the Goodnight\ntrack, and gives the target the enduring status.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    ApplyGracideaEffect = Symbol(
        None,
        None,
        None,
        "If the target is Shaymin, attempt to change the target's form to Shaymin Sky Forme. Otherwise, do nothing.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    ShouldTryEatItem = Symbol(
        None,
        None,
        None,
        "Checks if a given item should be eaten by the TryEatItem effect.\n\nReturns false if the ID is lower than 0x45, greater than 0x8A or if it's listed in the EAT_ITEM_EFFECT_IGNORE_LIST array.\n\nr0: Item ID\nreturn: True if the item should be eaten by TryEatItem.",
    )

    GetMaxPpWrapper = Symbol(
        None,
        None,
        None,
        "Gets the maximum PP for a given move. A wrapper around the function in the ARM 9 binary.\n\nr0: move pointer\nreturn: max PP for the given move, capped at 99",
    )

    MoveIsNotPhysical = Symbol(
        None,
        None,
        None,
        "Checks if a move isn't a physical move.\n\nr0: move ID\nreturn: bool",
    )

    CategoryIsNotPhysical = Symbol(
        None,
        None,
        None,
        "Checks that a move category is not CATEGORY_PHYSICAL.\n\nr0: move category ID\nreturn: bool",
    )

    TryDrought = Symbol(
        None,
        None,
        None,
        "Attempts to drain all water from the current floor.\n\nFails if orbs are disabled on the floor or if the current tileset has the is_water_tileset flag set.\n\nr0: user pointer",
    )

    TryPounce = Symbol(
        None,
        None,
        None,
        "Makes the target monster execute the Pounce action in a given direction if possible.\n\nIf the direction ID is 8, the target will pounce in the direction it's currently facing.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: direction ID",
    )

    TryBlowAway = Symbol(
        None,
        None,
        None,
        "Blows away the target monster in a given direction if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: direction ID",
    )

    TryExplosion = Symbol(
        None,
        None,
        None,
        "Creates an explosion if possible.\n\nThe target monster is considered the source of the explosion.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: coordinates where the explosion should take place (center)\nr3: explosion radius (only works correctly with 1 and 2)\nstack[0]: damage type\nstack[1]: damage source",
    )

    TryAftermathExplosion = Symbol(
        None,
        None,
        None,
        "Creates the explosion for the ability aftermath if possible.\n\nThe target monster is considered the source of the explosion.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: coordinates where the explosion should take place (center)\nr3: explosion radius (only works correctly with 1 and 2)\nstack[0]: damage type\nstack[1]: damage source (normally DAMAGE_SOURCE_EXPLOSION)",
    )

    TryWarp = Symbol(
        None,
        None,
        None,
        "Makes the target monster warp if possible.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: warp type\nr3: position (if warp type is position-based)",
    )

    EnsureCanStandCurrentTile = Symbol(
        None,
        None,
        None,
        "Checks that the given monster is standing on a tile it can stand on given its movement type, and warps it to a random location if it's not.\n\nr0: Entity pointer",
    )

    TryActivateNondamagingDefenderAbility = Symbol(
        None,
        None,
        None,
        "Applies the effects of a defender's ability on an attacker. After a move is used,\nthis function is called to see if any of the bitflags for an ability were set and\napplies the corresponding effect. (The way leech seed removes certain statuses is\nalso handled here.)\n\nr0: entity pointer",
    )

    TryActivateNondamagingDefenderExclusiveItem = Symbol(
        None,
        None,
        None,
        "Applies the effects of a defender's item on an attacker. After a move is used,\nthis function is called to see if any of the bitflags for an item were set and\napplies the corresponding effect.\n\nr0: attacker entity pointer\nr1: defender entity pointer",
    )

    GetMoveRangeDistance = Symbol(
        None,
        None,
        None,
        "Returns the maximum reach distance of a move, based on its AI range value.\n\nIf the move doesn't have an AI range value of RANGE_FRONT_10, RANGE_FRONT_WITH_CORNER_CUTTING or RANGE_FRONT_2_WITH_CORNER_CUTTING, returns 0.\nIf r2 is true, the move is a two-turn move and the user isn't charging said move, returns 0.\n\nr0: User entity pointer\nr1: Move pointer\nr2: True to perform the two-turn move check\nreturn: Maximum reach distance of the move, in tiles.",
    )

    MoveHitCheck = Symbol(
        None,
        None,
        None,
        "Determines if a move used hits or misses the target. It gets called twice per target, once with r3 = false and a second time with r3 = true.\n\nr0: Attacker\nr1: Defender\nr2: Pointer to move data\nr3: False if the move's first accuracy (accuracy1) should be used, true if its second accuracy (accuracy2) should be used instead.\nstack[0]: If true, always hit if the attacker and defender are the same. Otherwise, moves can miss no matter what the attacker and defender are.\nreturns: True if the move hits, false if it misses.",
    )

    IsHyperBeamVariant = Symbol(
        None,
        None,
        None,
        "Checks if a move is a Hyper Beam variant that requires a a turn to recharge.\n\nInclude moves: Frenzy Plant, Hydro Cannon, Hyper Beam, Blast Burn, Rock Wrecker, Giga Impact, Roar of Time\n\nr0: move\nreturn: bool",
    )

    IsChargingTwoTurnMove = Symbol(
        None,
        None,
        None,
        "Checks if a monster is currently charging the specified two-turn move.\n\nr0: User entity pointer\nr1: Move pointer\nreturn: True if the user is charging the specified two-turn move, false otherwise.",
    )

    HasMaxGinsengBoost99 = Symbol(
        None,
        None,
        None,
        "Checks if a move has a max Ginseng boost value of 99\n\nr0: Move\nreturn: True if the move's max Ginseng boost is 99, false otherwise.",
    )

    TwoTurnMoveForcedMiss = Symbol(
        None,
        None,
        None,
        "Checks if a move should miss a monster due to the monster being in the middle of Fly, Bounce, Dive, Dig, Shadow Force, or some other two-turn move that grants pseudo-invincibility.\n\nr0: entity pointer\nr1: move\nreturn: true if the move should miss",
    )

    DungeonRandOutcomeUserTargetInteraction = Symbol(
        None,
        None,
        None,
        "Like DungeonRandOutcome, but specifically for user-target interactions.\n\nThis modifies the underlying random process depending on factors like Serene Grace, and whether or not either entity has fainted.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: base success percentage (100*p). 0 is treated specially and guarantees success.\nreturns: True if the random check passed, false otherwise.",
    )

    DungeonRandOutcomeUserAction = Symbol(
        None,
        None,
        None,
        "Like DungeonRandOutcome, but specifically for user actions.\n\nThis modifies the underlying random process to factor in Serene Grace (and checks whether the user is a valid entity).\n\nr0: entity pointer\nr1: base success percentage (100*p). 0 is treated specially and guarantees success.\nreturns: True if the random check passed, false otherwise.",
    )

    CanAiUseMove = Symbol(
        None,
        None,
        None,
        "Checks if an AI-controlled monster can use a move.\nWill return false if the any of the flags move::f_exists, move::f_subsequent_in_link_chain or move::f_disabled is true. The function does not check if the flag move::f_enabled_for_ai is set. This function also returns true if the call to CanMonsterUseMove is true.\nThe function contains a loop that is supposed to check other moves after the specified one, but the loop breaks after it finds a move that isn't linked, which is always true given the checks in place at the start of the function.\n\nr0: Entity pointer\nr1: Move index\nr2: extra_checks parameter when calling CanMonsterUseMove\nreturn: True if the AI can use the move (not accounting for move::f_enabled_for_ai)",
    )

    CanMonsterUseMove = Symbol(
        None,
        None,
        None,
        "Checks if a monster can use the given move.\nWill always return true for the regular attack. Will return false if the move if the flag move::f_disabled is true, if the flag move::f_sealed is true. More things will be checked if the extra_checks parameter is true.\n\nr0: Entity pointer\nr1: Move pointer\nr2: True to check whether the move is out of PP, whether it can be used under the taunted status and whether the encore status prevents using the move\nreturn: True if the monster can use the move, false otherwise.",
    )

    UpdateMovePp = Symbol(
        None,
        None,
        None,
        "Updates the PP of any moves that were used by a monster, if PP should be consumed.\n\nr0: entity pointer\nr1: flag for whether or not PP should be consumed",
    )

    GetDamageSourceWrapper = Symbol(
        None,
        None,
        None,
        "Wraps GetDamageSource (in arm9) for a move info struct rather than a move ID.\n\nr0: move info pointer\nr1: item ID\nreturn: damage source",
    )

    LowerSshort = Symbol(
        None,
        None,
        None,
        "Gets the lower 2 bytes of a 4-byte number and interprets it as a signed short.\n\nr0: 4-byte number x\nreturn: (short) x",
    )

    PlayMoveAnimation = Symbol(
        None,
        None,
        None,
        "Handles the process of getting and playing all the animations for a move. Waits\nuntil the animation has no more frames before returning.\n\nr0: Pointer to the entity that used the move\nr1: Pointer to the entity that is the target\nr2: Move pointer\nr3: position",
    )

    GetMoveAnimationId = Symbol(
        None,
        None,
        None,
        "Returns the move animation ID that should be played for a move.\nIt contains a check for weather ball. After that, if the parameter should_play_alternative_animation is false, the move ID is returned. If it's true, there's a bunch of manual ID checks that result on a certain hardcoded return value.\n\nr0: Move ID\nr1: Apparent weather for the monster who used the move\nr2: Result of ShouldMovePlayADifferentAnimation\nreturn: Move animation ID",
    )

    ShouldMovePlayAlternativeAnimation = Symbol(
        None,
        None,
        None,
        "Checks whether a moved used by a monster should play its alternative animation. Includes checks for Curse, Snore, Sleep Talk, Solar Beam and 2-turn moves.\n\nr0: Pointer to the entity that used the move\nr1: Move pointer\nreturn: True if the move should play its alternative animation",
    )

    ExecuteMoveEffect = Symbol(
        None,
        None,
        None,
        "Handles the effects that happen after a move is used. Includes a loop that is run for each target, mutiple ability checks and the giant switch statement that executes the effect of the move used given its ID.\n\nr0: pointer to some struct\nr1: attacker pointer\nr2: pointer to move data\nr3: ?\nstack[0]: ?",
    )

    DoMoveDamageInlined = Symbol(
        None,
        None,
        None,
        "Exactly the same as DoMoveDamage, except it appears DealDamage was inlined.\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: item ID\nreturn: whether or not damage was dealt",
    )

    DealDamage = Symbol(
        None,
        None,
        None,
        "Deals damage from a move or item used by an attacking monster on a defending monster.\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: damage multiplier (as a binary fixed-point number with 8 fraction bits)\nstack[0]: item ID\nreturn: amount of damage dealt",
    )

    DealDamageWithTypeAndPowerBoost = Symbol(
        None,
        None,
        None,
        "Same as DealDamage, except with an explicit move type and a base power boost.\n\nr0: attacker pointer\nr1: defender pointer\nr2: move\nr3: damage multiplier (as a binary fixed-point number with 8 fraction bits)\nstack[0]: item ID\nstack[1]: move type\nstack[2]: base power boost\nreturn: amount of damage dealt",
    )

    DealDamageProjectile = Symbol(
        None,
        None,
        None,
        "Deals damage from a variable-damage projectile.\n\nr0: entity pointer 1?\nr1: entity pointer 2?\nr2: move pointer\nr3: move power\nstack[0]: damage multiplier (as a binary fixed-point number with 8 fraction bits)\nstack[1]: item ID of the projectile\nreturn: Calculated damage",
    )

    DealDamageWithType = Symbol(
        None,
        None,
        None,
        "Same as DealDamage, except with an explicit move type.\n\nr0: attacker pointer\nr1: defender pointer\nr2: move type\nr3: move\nstack[0]: damage multiplier (as a binary fixed-point number with 8 fraction bits)\nstack[1]: item ID\nreturn: amount of damage dealt",
    )

    PerformDamageSequence = Symbol(
        None,
        None,
        None,
        "Performs the 'damage sequence' given the results of the damage calculation. This includes running the accuracy roll with MoveHitCheck, calling ApplyDamageAndEffects, and some other miscellaneous bits of state bookkeeping (including handling the effects of Illuminate).\n\nThis is the last function called by DealDamage. The result of this call is the return value of DealDamage and its relatives.\n\nr0: Attacker pointer\nr1: Defender pointer\nr2: Move pointer\nr3: [output] struct containing info about the damage calculation\nstack[0]: Damage source\nreturn: Calculated damage",
    )

    StatusCheckerCheck = Symbol(
        None,
        None,
        None,
        "Determines if using a given move against its intended targets would be redundant because all of them already have the effect caused by said move.\n\nr0: Pointer to the entity that is considering using the move\nr1: Move pointer\nreturn: True if it makes sense to use the move, false if it would be redundant given the effects it causes and the effects that all the targets already have.",
    )

    GetApparentWeather = Symbol(
        None,
        None,
        None,
        "Get the weather, as experienced by a specific entity.\n\nr0: entity pointer\nreturn: weather ID",
    )

    TryWeatherFormChange = Symbol(
        None,
        None,
        None,
        "Tries to change a monster into one of its weather-related alternative forms. Applies to Castform and Cherrim, and checks for their unique abilities.\n\nr0: pointer to entity",
    )

    ActivateSportCondition = Symbol(
        None,
        None,
        None,
        "Activates the Mud Sport or Water Sport condition on the dungeon floor for some number of turns.\n\nr0: water sport flag (false for Mud Sport, true for Water Sport)",
    )

    TryActivateWeather = Symbol(
        None,
        None,
        None,
        "Tries to change the weather based upon the information for each weather type in the\ndungeon struct. Returns whether the weather was succesfully changed or not.\n\nr0: bool to log message and play animation?\nr1: bool to force weather change and animation?\nreturn: True if the weather changed",
    )

    DigitCount = Symbol(
        None,
        None,
        None,
        "Counts the number of digits in a nonnegative integer.\n\nIf the number is negative, it is cast to a uint16_t before counting digits.\n\nr0: int\nreturn: number of digits in int",
    )

    LoadTextureUi = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nNo params."
    )

    DisplayNumberTextureUi = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: x position\nr1: y position\nr2: number\nr3: ally_mode\nreturn: xsize",
    )

    DisplayCharTextureUi = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: render_3d_element_64\nr1: x position\nr2: y position\nr3: char_id\nstack[0]: ?\nreturn: ?",
    )

    DisplayUi = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nNo params."
    )

    GetTile = Symbol(
        None,
        None,
        None,
        "Get the tile at some position. If the coordinates are out of bounds, returns a default tile.\n\nr0: x position\nr1: y position\nreturn: tile pointer",
    )

    GetTileSafe = Symbol(
        None,
        None,
        None,
        "Get the tile at some position. If the coordinates are out of bounds, returns a pointer to a copy of the default tile.\n\nr0: x position\nr1: y position\nreturn: tile pointer",
    )

    IsFullFloorFixedRoom = Symbol(
        None,
        None,
        None,
        "Checks if the current fixed room on the dungeon generation info corresponds to a fixed, full-floor layout.\n\nThe first non-full-floor fixed room is 0xA5, which is for Sealed Chambers.\n\nreturn: bool",
    )

    IsCurrentTilesetBackground = Symbol(
        None,
        None,
        None,
        "Calls IsBackgroundTileset with the current tileset ID\n\nreturn: True if the current dungeon tileset is a background, false if it's a regular tileset.",
    )

    TrySpawnGoldenChamber = Symbol(
        None,
        None,
        None,
        "Changes the tileset and fixed room id of the floor for the Golden Chamber if the floor should be a\nGolden Chamber.\n\nNo params.",
    )

    CountItemsOnFloorForAcuteSniffer = Symbol(
        None,
        None,
        None,
        "Counts the number of items on the floor by checking every tile for an item and stores it into\ndungeon::item_sniffer_item_count\n\nNo params.",
    )

    GetStairsSpawnPosition = Symbol(
        None,
        None,
        None,
        "Gets the spawn position for the stairs and stores it at the passed pointers.\n\nr0: [output] pointer to x coordinate\nr1: [output] pointer to y coordinate",
    )

    PositionIsOnStairs = Symbol(
        None,
        None,
        None,
        "Checks if this location is on top of the staircase. In the game it is only used to check if an outlaw has reached\nthe staircase.\n\nr0: x coordinate\nr1: y coordinate\nreturn: bool",
    )

    GetStairsRoom = Symbol(
        None,
        None,
        None,
        "Returns the index of the room that contains the stairs\n\nreturn: Room index",
    )

    GetDefaultTileTextureId = Symbol(
        None,
        None,
        None,
        "Returns the texture_id of the default tile?\n\nreturn: texture_id",
    )

    DetermineAllTilesWalkableNeighbors = Symbol(
        None,
        None,
        None,
        "Evaluates the walkable_neighbor_flags for all tiles.\n\nNo params.",
    )

    DetermineTileWalkableNeighbors = Symbol(
        None,
        None,
        None,
        "Evaluates the walkable_neighbor_flags for the this tile by checking the 8 adjacent tiles.\n\nr0: x coordinate\nr1: y coordinate",
    )

    UpdateTrapsVisibility = Symbol(
        None,
        None,
        None,
        "Exact purpose unknown. Gets called whenever a trap tile is shown or hidden.\n\nNo params.",
    )

    DrawTileGrid = Symbol(
        None,
        None,
        None,
        "Draws a grid on the nearby walkable tiles. Triggered by pressing Y.\n\nr0: Coordinates of the entity around which the grid will be drawn\nr1: ?\nr2: ?\nr3: ?",
    )

    HideTileGrid = Symbol(
        None,
        None,
        None,
        "Hides the grid on the nearby walkable tiles. Triggered by releasing Y.\n\nNo params.",
    )

    DiscoverMinimap = Symbol(
        None,
        None,
        None,
        "Discovers the tiles around the specified position on the minimap.\n\nThe discovery radius depends on the visibility range of the floor. If display_data::blinded is true, the function returns early without doing anything.\n\nr0: Position around which the map should be discovered",
    )

    PositionHasItem = Symbol(
        None,
        None,
        None,
        "Checks if the tile at the position has an item on it.\n\nr0: Position to check\nreturn: bool",
    )

    PositionHasMonster = Symbol(
        None,
        None,
        None,
        "Checks if the tile at the position has a monster on it.\n\nr0: Position to check\nreturn: bool",
    )

    TrySmashWall = Symbol(
        None,
        None,
        None,
        "Checks if the tile at the position is a wall. If so, smash it (turn it into a floor tile), play an animation\n\nr0: Wall position to smash\nreturn: bool",
    )

    IsWaterTileset = Symbol(
        None,
        None,
        None,
        "Returns flag tileset_property::is_water_tileset for the current tileset\n\nreturn: True if the current tileset is a water tileset",
    )

    GetRandomSpawnMonsterID = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nreturn: monster ID?",
    )

    NearbyAllyIqSkillIsEnabled = Symbol(
        None,
        None,
        None,
        "Appears to check whether or not the given monster has any allies nearby (within 1 tile) that have the given IQ skill active.\n\nr0: entity pointer\nr1: IQ skill ID\nreturn: bool",
    )

    ResetGravity = Symbol(
        None,
        None,
        None,
        "Resets gravity (and the byte after it?) in the dungeon struct back to 0.\n\nNo params.",
    )

    GravityIsActive = Symbol(
        None, None, None, "Checks if gravity is active on the floor.\n\nreturn: bool"
    )

    TryActivateGravity = Symbol(
        None,
        None,
        None,
        "Attempts to activate Gravity for this dungeon floor.\n\nreturn: whether or not gravity was activated",
    )

    ShouldBoostKecleonShopSpawnChance = Symbol(
        None,
        None,
        None,
        "Gets the boost_kecleon_shop_spawn_chance field on the dungeon struct.\n\nreturn: bool",
    )

    SetShouldBoostKecleonShopSpawnChance = Symbol(
        None,
        None,
        None,
        "Sets the boost_kecleon_shop_spawn_chance field on the dungeon struct to the given value.\n\nr0: bool to set the flag to",
    )

    UpdateShouldBoostKecleonShopSpawnChance = Symbol(
        None,
        None,
        None,
        "Sets the boost_kecleon_shop_spawn_chance field on the dungeon struct depending on if a team member has the exclusive item effect for more kecleon shops.\n\nNo params.",
    )

    SetDoughSeedFlag = Symbol(
        None,
        None,
        None,
        "Sets the dough_seed_extra_money_flag field on the dungeon struct to the given value.\n\nr0: bool to set the flag to",
    )

    TrySpawnDoughSeedPoke = Symbol(
        None,
        None,
        None,
        "Checks the dough_seed_extra_money_flag field on the dungeon struct and tries to spawn\nextra poke if it is set.\n\nNo params.",
    )

    IsSecretBazaar = Symbol(
        None,
        None,
        None,
        "Checks if the current floor is the Secret Bazaar.\n\nreturn: bool",
    )

    ShouldBoostHiddenStairsSpawnChance = Symbol(
        None,
        None,
        None,
        "Gets the boost_hidden_stairs_spawn_chance field on the dungeon struct.\n\nreturn: bool",
    )

    SetShouldBoostHiddenStairsSpawnChance = Symbol(
        None,
        None,
        None,
        "Sets the boost_hidden_stairs_spawn_chance field on the dungeon struct to the given value.\n\nr0: bool to set the flag to",
    )

    UpdateShouldBoostHiddenStairsSpawnChance = Symbol(
        None,
        None,
        None,
        "Sets the boost_hidden_stairs_spawn_chance field on the dungeon struct depending on if a team member has the exclusive item effect for more hidden stairs.\n\nNo params.",
    )

    IsSecretRoom = Symbol(
        None,
        None,
        None,
        "Checks if the current floor is the Secret Room fixed floor (from hidden stairs).\n\nreturn: bool",
    )

    IsSecretFloor = Symbol(
        None,
        None,
        None,
        "Checks if the current floor is a secret bazaar or a secret room.\n\nreturn: bool",
    )

    GetCurrentHiddenStairsType = Symbol(
        None,
        None,
        None,
        "Checks if the current floor is a secret bazaar or a secret room and returns which one it is.\n\nreturn: enum hidden_stairs_type",
    )

    HiddenStairsPresent = Symbol(
        None,
        None,
        None,
        "Checks if the hidden stairs are present on this floor.\n\nThe function checks that dungeon_generation_info::hidden_stairs_pos isn't (-1, -1)\n\nreturn: True if the hidden stairs are present on this floor, false otherwise.",
    )

    HiddenStairsTrigger = Symbol(
        None,
        None,
        None,
        "Called whenever the leader steps on the hidden stairs.\n\nIf the stairs hadn't been revealed yet, plays the corresponding animation.\n\nr0: True to display a message if the stairs are revealed, false to omit it.",
    )

    GetDungeonGenInfoUnk0C = Symbol(
        None, None, None, "return: dungeon_generation_info::field_0xc"
    )

    GetMinimapData = Symbol(
        None,
        None,
        None,
        "Returns a pointer to the minimap_display_data struct in the dungeon struct.\n\nreturn: minimap_display_data*",
    )

    DrawMinimapTile = Symbol(
        None,
        None,
        None,
        "Draws a single tile on the minimap.\n\nr0: X position\nr1: Y position",
    )

    UpdateMinimap = Symbol(
        None, None, None, "Graphically updates the minimap\n\nNo params."
    )

    SetMinimapDataE447 = Symbol(
        None,
        None,
        None,
        "Sets minimap_display_data::field_0xE447 to the specified value\n\nr0: Value to set the field to",
    )

    GetMinimapDataE447 = Symbol(
        None,
        None,
        None,
        "Exclusive to the EU ROM. Returns minimap_display_data::field_0xE447.\n\nreturn: minimap_display_data::field_0xE447",
    )

    SetMinimapDataE448 = Symbol(
        None,
        None,
        None,
        "Sets minimap_display_data::field_0xE448 to the specified value\n\nr0: Value to set the field to",
    )

    InitWeirdMinimapMatrix = Symbol(
        None,
        None,
        None,
        "Initializes the matrix at minimap_display_data+0xE000. Seems to overflow said matrix when doing so.\n\nNo params.",
    )

    InitMinimapDisplayTile = Symbol(
        None,
        None,
        None,
        "Used to initialize an instance of struct minimap_display_tile\n\nr0: Pointer to struct to init\nr1: Seems to be a pointer to the file that stores minimap icons or something like that",
    )

    LoadFixedRoomDataVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for LoadFixedRoomData.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nNo params.",
    )

    UnloadFixedRoomData = Symbol(
        None,
        None,
        None,
        "Unloads fixed room data from the buffer pointed to by FIXED_ROOM_DATA_PTR, then clears the pointer.\n\nAlso clears dungeon::unk_fixed_room_pointer.\n\nNo params.",
    )

    IsNormalFloor = Symbol(
        None,
        None,
        None,
        "Checks if the current floor is a normal layout.\n\n'Normal' means any layout that is NOT one of the following:\n- Hidden stairs floors\n- Golden Chamber\n- Challenge Request floor\n- Outlaw hideout\n- Treasure Memo floor\n- Full-room fixed floors (ID < 0xA5) [0xA5 == Sealed Chamber]\n\nreturn: bool",
    )

    GenerateFloor = Symbol(
        None,
        None,
        None,
        "This is the master function that generates the dungeon floor.\n\nVery loosely speaking, this function first tries to generate a valid floor layout. Then it tries to spawn entities in a valid configuration. Finally, it performs cleanup and post-processing depending on the dungeon.\n\nIf a spawn configuration is invalid, the entire floor layout is scrapped and regenerated. If the generated floor layout is invalid 10 times in a row, or a valid spawn configuration isn't generated within 10 attempts, the generation algorithm aborts and the default one-room Monster House floor is generated as a fallback.\n\nNo params.",
    )

    GetTileTerrain = Symbol(
        None,
        None,
        None,
        "Gets the terrain type of a tile.\n\nr0: tile pointer\nreturn: terrain ID",
    )

    DungeonRand100 = Symbol(
        None,
        None,
        None,
        "Compute a pseudorandom integer on the interval [0, 100) using the dungeon PRNG.\n\nreturn: pseudorandom integer",
    )

    ClearHiddenStairs = Symbol(
        None,
        None,
        None,
        "Clears the tile (terrain and spawns) on which Hidden Stairs are spawned, if applicable.\n\nNo params.",
    )

    FlagHallwayJunctions = Symbol(
        None,
        None,
        None,
        "Sets the junction flag (bit 3 of the terrain flags) on any hallway junction tiles in some range [x0, x1), [y0, y1). This leaves tiles within rooms untouched.\n\nA hallway tile is considered a junction if it has at least 3 cardinal neighbors with open terrain.\n\nr0: x0\nr1: y0\nr2: x1\nr3: y1",
    )

    GenerateStandardFloor = Symbol(
        None,
        None,
        None,
        "Generate a standard floor with the given parameters.\n\nBroadly speaking, a standard floor is generated as follows:\n1. Generating the grid\n2. Creating a room or hallway anchor in each grid cell\n3. Creating hallways between grid cells\n4. Generating special features (maze room, Kecleon shop, Monster House, extra hallways, room imperfections, secondary structures)\n\nr0: grid size x\nr1: grid size y\nr2: floor properties",
    )

    GenerateOuterRingFloor = Symbol(
        None,
        None,
        None,
        "Generates a floor layout with a 4x2 grid of rooms, surrounded by an outer ring of hallways.\n\nr0: floor properties",
    )

    GenerateCrossroadsFloor = Symbol(
        None,
        None,
        None,
        "Generates a floor layout with a mesh of hallways on the interior 3x2 grid, surrounded by a boundary of rooms protruding from the interior like spikes, excluding the corner cells.\n\nr0: floor properties",
    )

    GenerateLineFloor = Symbol(
        None,
        None,
        None,
        "Generates a floor layout with 5 grid cells in a horizontal line.\n\nr0: floor properties",
    )

    GenerateCrossFloor = Symbol(
        None,
        None,
        None,
        "Generates a floor layout with 5 rooms arranged in a cross ('plus sign') formation.\n\nr0: floor properties",
    )

    GenerateBeetleFloor = Symbol(
        None,
        None,
        None,
        "Generates a floor layout in a 'beetle' formation, which is created by taking a 3x3 grid of rooms, connecting the rooms within each row, and merging the central column into one big room.\n\nr0: floor properties",
    )

    MergeRoomsVertically = Symbol(
        None,
        None,
        None,
        "Merges two vertically stacked rooms into one larger room.\n\nr0: x grid coordinate of the rooms to merge\nr1: y grid coordinate of the upper room\nr2: dy, where the lower room has a y grid coordinate of y+dy\nr3: grid to update",
    )

    GenerateOuterRoomsFloor = Symbol(
        None,
        None,
        None,
        "Generates a floor layout with a ring of rooms on the grid boundary and nothing in the interior.\n\nNote that this function is bugged, and won't properly connect all the rooms together for grid_size_x < 4.\n\nr0: grid size x\nr1: grid size y\nr2: floor properties",
    )

    IsNotFullFloorFixedRoom = Symbol(
        None,
        None,
        None,
        "Checks if a fixed room ID does not correspond to a fixed, full-floor layout.\n\nThe first non-full-floor fixed room is 0xA5, which is for Sealed Chambers.\n\nr0: fixed room ID\nreturn: bool",
    )

    GenerateFixedRoom = Symbol(
        None,
        None,
        None,
        "Handles fixed room generation if the floor contains a fixed room.\n\nr0: fixed room ID\nr1: floor properties\nreturn: bool",
    )

    GenerateOneRoomMonsterHouseFloor = Symbol(
        None,
        None,
        None,
        "Generates a floor layout with just a large, one-room Monster House.\n\nThis is the default layout if dungeon generation fails.\n\nNo params.",
    )

    GenerateTwoRoomsWithMonsterHouseFloor = Symbol(
        None,
        None,
        None,
        "Generate a floor layout with two rooms (left and right), one of which is a Monster House.\n\nNo params.",
    )

    GenerateExtraHallways = Symbol(
        None,
        None,
        None,
        "Generate extra hallways on the floor via a series of random walks.\n\nEach random walk starts from a random tile in a random room, leaves the room in a random cardinal direction, and from there tunnels through obstacles through a series of random turns, leaving open terrain in its wake. The random walk stops when it reaches open terrain, goes out of bounds, or reaches an impassable obstruction.\n\nr0: grid to update\nr1: grid size x\nr2: grid size y\nr3: number of extra hallways to generate",
    )

    GetGridPositions = Symbol(
        None,
        None,
        None,
        "Get the grid cell positions for a given set of floor grid dimensions.\n\nr0: [output] pointer to array of the starting x coordinates of each grid column\nr1: [output] pointer to array of the starting y coordinates of each grid row\nr2: grid size x\nr3: grid size y",
    )

    InitDungeonGrid = Symbol(
        None,
        None,
        None,
        "Initialize a dungeon grid with defaults.\n\nThe grid is an array of grid cells stored in column-major order (such that grid cells with the same x value are stored contiguously), with a fixed column size of 15. If the grid size in the y direction is less than this, the last (15 - grid_size_y) entries of each column will be uninitialized.\n\nNote that the grid size arguments define the maximum size of the grid from a programmatic standpoint. However, grid cells can be invalidated if they exceed the configured floor size in the dungeon generation status struct. Thus, the dimensions of the ACTIVE grid can be smaller.\n\nr0: [output] grid (expected to have space for at least (15*(grid_size_x-1) + grid_size_y) dungeon grid cells)\nr1: grid size x\nr2: grid size y",
    )

    AssignRooms = Symbol(
        None,
        None,
        None,
        "Randomly selects a subset of grid cells to become rooms.\n\nThe given number of grid cells will become rooms. If any of the selected grid cells are invalid, fewer rooms will be generated. The number of rooms assigned will always be at least 2 and never exceed 36.\n\nCells not marked as rooms will become hallway anchors. A hallway anchor is a single tile in a non-room grid cell to which hallways will be connected later, thus 'anchoring' hallway generation.\n\nr0: grid to update\nr1: grid size x\nr2: grid size y\nr3: number of rooms; if positive, a random value between [n_rooms, n_rooms+2] will be used. If negative, |n_rooms| will be used exactly.",
    )

    CreateRoomsAndAnchors = Symbol(
        None,
        None,
        None,
        "Creates rooms and hallway anchors in each grid cell as designated by AssignRooms.\n\nThis function creates a rectangle of open terrain for each room (with some margin relative to the grid cell border). A single open tile is created in hallway anchor cells, and a hallway anchor indicator is set for later reference.\n\nr0: grid to update\nr1: grid size x\nr2: grid size y\nr3: array of the starting x coordinates of each grid column\nstack[0]: array of the starting y coordinates of each grid row\nstack[1]: room bitflags; only uses bit 2 (mask: 0b100), which enables room imperfections",
    )

    GenerateSecondaryStructures = Symbol(
        None,
        None,
        None,
        "Try to generate secondary structures in flagged rooms.\n\nIf a valid room with no special features is flagged to have a secondary structure, try to generate a random one in the room, based on the result of a dice roll:\n  0: no secondary structure\n  1: maze, or a central water/lava 'plus sign' as fallback, or a single water/lava tile in the center as a second fallback\n  2: checkerboard pattern of water/lava\n  3: central pool of water/lava\n  4: central 'island' with items and a Warp Tile, surrounded by a 'moat' of water/lava\n  5: horizontal or vertical divider of water/lava splitting the room in two\n\nIf the room isn't the right shape, dimension, or otherwise doesn't support the selected secondary structure, it is left untouched.\n\nr0: grid to update\nr1: grid size x\nr2: grid size y",
    )

    AssignGridCellConnections = Symbol(
        None,
        None,
        None,
        "Randomly assigns connections between adjacent grid cells.\n\nConnections are created via a random walk with momentum, starting from the grid cell at (cursor x, cursor y). A connection is drawn in a random direction from the current cursor, and this process is repeated a certain number of times (the 'floor connectivity' specified in the floor properties). The direction of the random walk has 'momentum'; there's a 50% chance it will be the same as the previous step (or rotated counterclockwise if on the boundary). This helps to reduce the number of dead ends and forks in the road caused by the random walk 'doubling back' on itself.\n\nIf dead ends are disabled in the floor properties, there is an additional phase to remove dead end hallway anchors (only hallway anchors, not rooms) by drawing additional connections. Note that the actual implementation contains a bug: the grid cell validity checks use the wrong index, so connections may be drawn to invalid cells.\n\nr0: grid to update\nr1: grid size x\nr2: grid size y\nr3: cursor x\nstack[0]: cursor y\nstack[1]: floor properties",
    )

    CreateGridCellConnections = Symbol(
        None,
        None,
        None,
        "Create grid cell connections either by creating hallways or merging rooms.\n\nWhen creating a hallway connecting a hallway anchor, the exact anchor coordinates are used as the endpoint. When creating a hallway connecting a room, a random point on the room edge facing the hallway is used as the endpoint. The grid cell boundaries are used as the middle coordinates for kinks (see CreateHallway).\n\nIf room merging is enabled, there is a 9.75% chance that two connected rooms will be merged into a single larger room (9.75% comes from two 5% rolls, one for each of the two rooms being merged). A room can only participate in a merge once.\n\nr0: grid to update\nr1: grid size x\nr2: grid size y\nr3: array of the starting x coordinates of each grid column\nstack[0]: array of the starting y coordinates of each grid row\nstack[1]: disable room merging flag",
    )

    GenerateRoomImperfections = Symbol(
        None,
        None,
        None,
        "Attempt to generate room imperfections for each room in the floor layout, if enabled.\n\nEach room has a 40% chance of having imperfections if its grid cell is flagged to allow room imperfections. Imperfections are generated by randomly growing the walls of the room inwards for a certain number of iterations, starting from the corners.\n\nr0: grid to update\nr1: grid size x\nr2: grid size y",
    )

    CreateHallway = Symbol(
        None,
        None,
        None,
        "Create a hallway between two points.\n\nIf the two points share no coordinates in common (meaning the line connecting them is diagonal), a 'kinked' hallway is created, with the kink at a specified 'middle' coordinate (in practice the grid cell boundary). For example, with a kinked horizontal hallway, there are two horizontal lines extending out from the endpoints, connected by a vertical line on the middle x coordinate.\n\nIf a hallway would intersect with an existing open tile (like an existing hallway), the hallway will only be created up to the point where it intersects with the open tile.\n\nr0: x0\nr1: y0\nr2: x1\nr3: y1\nstack[0]: vertical flag (true for vertical hallway, false for horizontal)\nstack[1]: middle x coordinate for kinked horizontal hallways\nstack[2]: middle y coordinate for kinked vertical hallways",
    )

    EnsureConnectedGrid = Symbol(
        None,
        None,
        None,
        "Ensure the grid forms a connected graph (all valid cells are reachable) by adding hallways to unreachable grid cells.\n\nIf a grid cell cannot be connected for some reason, remove it entirely.\n\nr0: grid to update\nr1: grid size x\nr2: grid size y\nr3: array of the starting x coordinates of each grid column\nstack[0]: array of the starting y coordinates of each grid row",
    )

    SetTerrainObstacleChecked = Symbol(
        None,
        None,
        None,
        "Set the terrain of a specific tile to be an obstacle (wall or secondary terrain).\n\nSecondary terrain (water/lava) can only be placed in the specified room. If the tile room index does not match, a wall will be placed instead.\n\nr0: tile pointer\nr1: use secondary terrain flag (true for water/lava, false for wall)\nr2: room index",
    )

    FinalizeJunctions = Symbol(
        None,
        None,
        None,
        "Finalizes junction tiles by setting the junction flag (bit 3 of the terrain flags) and ensuring open terrain.\n\nNote that this implementation is slightly buggy. This function scans tiles left-to-right, top-to-bottom, and identifies junctions as any open, non-hallway tile (room_index != 0xFF) adjacent to an open, hallway tile (room_index == 0xFF). This interacts poorly with hallway anchors (room_index == 0xFE). This function sets the room index of any hallway anchors to 0xFF within the same loop, so a hallway anchor may or may not be identified as a junction depending on the orientation of connected hallways.\n\nFor example, in the following configuration, the 'o' tile would be marked as a junction because the neighboring hallway tile to its left comes earlier in iteration, while the 'o' tile still has the room index 0xFE, causing the algorithm to mistake it for a room tile:\n  xxxxx\n  ---ox\n  xxx|x\n  xxx|x\nHowever, in the following configuration, the 'o' tile would NOT be marked as a junction because it comes earlier in iteration than any of its neighboring hallway tiles, so its room index is set to 0xFF before it can be marked as a junction. This is actually the ONLY possible configuration where a hallway anchor will not be marked as a junction.\n  xxxxx\n  xo---\n  x|xxx\n  x|xxx\n\nNo params.",
    )

    GenerateKecleonShop = Symbol(
        None,
        None,
        None,
        "Possibly generate a Kecleon shop on the floor.\n\nA Kecleon shop will be generated with a probability determined by the Kecleon shop spawn chance parameter. A Kecleon shop will be generated in a random room that is valid, connected, has no other special features, and has dimensions of at least 5x4. Kecleon shops will occupy the entire room interior, leaving a one tile margin from the room walls.\n\nr0: grid to update\nr1: grid size x\nr2: grid size y\nr3: Kecleon shop spawn chance (percentage from 0-100)",
    )

    GenerateMonsterHouse = Symbol(
        None,
        None,
        None,
        "Possibly generate a Monster House on the floor.\n\nA Monster House will be generated with a probability determined by the Monster House spawn chance parameter, and only if the current floor can support one (no non-Monster-House outlaw missions or special floor types). A Monster House will be generated in a random room that is valid, connected, and is not a merged or maze room.\n\nr0: grid to update\nr1: grid size x\nr2: grid size y\nr3: Monster House spawn chance (percentage from 0-100)",
    )

    GenerateMazeRoom = Symbol(
        None,
        None,
        None,
        "Possibly generate a maze room on the floor.\n\nA maze room will be generated with a probability determined by the maze room chance parameter. A maze will be generated in a random room that is valid, connected, has odd dimensions, and has no other features.\n\nr0: grid to update\nr1: grid size x\nr2: grid size y\nr3: maze room chance (percentage from 0-100)",
    )

    GenerateMaze = Symbol(
        None,
        None,
        None,
        "Generate a maze room within a given grid cell.\n\nA 'maze' is generated within the room using a series of random walks to place obstacle terrain (walls or secondary terrain) in a maze-like arrangement. 'Maze lines' (see GenerateMazeLine) are generated using every other tile around the room's border, as well as every other interior tile, as a starting point. This ensures that there are stripes of walkable open terrain surrounded by stripes of obstacles (the maze walls).\n\nr0: grid cell pointer\nr1: use secondary terrain flag (true for water/lava, false for walls)",
    )

    GenerateMazeLine = Symbol(
        None,
        None,
        None,
        "Generate a 'maze line' from a given starting point, within the given bounds.\n\nA 'maze line' is a random walk starting from (x0, y0). The random walk proceeds with a stride of 2 in a random direction, laying down obstacles as it goes. The random walk terminates when it gets trapped and there are no more neighboring tiles that are open and in-bounds.\n\nr0: x0\nr1: y0\nr2: xmin\nr3: ymin\nstack[0]: xmax\nstack[1]: ymax\nstack[2]: use secondary terrain flag (true for water/lava, false for walls)\nstack[3]: room index",
    )

    SetSpawnFlag5 = Symbol(
        None,
        None,
        None,
        "Set spawn flag 5 (0b100000 or 0x20) on all tiles in a room.\n\nr0: grid cell",
    )

    IsNextToHallway = Symbol(
        None,
        None,
        None,
        "Checks if a tile position is either in a hallway or next to one.\n\nr0: x\nr1: y\nreturn: bool",
    )

    ResolveInvalidSpawns = Symbol(
        None,
        None,
        None,
        "Resolve invalid spawn flags on tiles.\n\nSpawn flags can be invalid due to terrain. For example, traps can't spawn on obstacles. Spawn flags can also be invalid due to multiple being set on a single tile, in which case one will take precedence. For example, stair spawns trump trap spawns.\n\nNo params.",
    )

    ConvertSecondaryTerrainToChasms = Symbol(
        None,
        None,
        None,
        "Converts all secondary terrain tiles (water/lava) to chasms.\n\nNo params.",
    )

    EnsureImpassableTilesAreWalls = Symbol(
        None,
        None,
        None,
        "Ensures all tiles with the impassable flag are walls.\n\nNo params.",
    )

    InitializeTile = Symbol(
        None, None, None, "Initialize a tile struct.\n\nr0: tile pointer"
    )

    ResetFloor = Symbol(
        None,
        None,
        None,
        "Resets the floor in preparation for a floor generation attempt.\n\nResets all tiles, resets the border to be impassable, and clears entity spawns.\n\nNo params.",
    )

    PosIsOutOfBounds = Symbol(
        None,
        None,
        None,
        "Checks if a position (x, y) is out of bounds on the map: !((0 <= x <= 55) && (0 <= y <= 31)).\n\nr0: x\nr1: y\nreturn: bool",
    )

    ShuffleSpawnPositions = Symbol(
        None,
        None,
        None,
        "Randomly shuffle an array of spawn positions.\n\nr0: spawn position array containing bytes {x1, y1, x2, y2, ...}\nr1: number of (x, y) pairs in the spawn position array",
    )

    MarkNonEnemySpawns = Symbol(
        None,
        None,
        None,
        "Mark tiles for all non-enemy entities, which includes stairs, items, traps, and the player. Note that this only marks tiles; actual spawning is handled later.\n\nMost entities are spawned randomly on a subset of permissible tiles.\n\nStairs are spawned if they don't already exist on the floor, and hidden stairs of the specified type are also spawned if configured as long as there are at least 2 floors left in the dungeon. Stairs can spawn on any tile that has open terrain, is in a room, isn't in a Kecleon shop, doesn't already have an enemy spawn, isn't a hallway junction, and isn't a special tile like a Key door.\n\nItems are spawned both normally in rooms, as well as in walls and Monster Houses. Normal items can spawn on any tile that has open terrain, is in a room, isn't in a Kecleon shop or Monster House, isn't a hallway junction, and isn't a special tile like a Key door. Buried items can spawn on any wall tile. Monster House items can spawn on any Monster House tile that isn't in a Kecleon shop and isn't a hallway junction.\n\nTraps are similarly spawned both normally in rooms, as well as in Monster Houses. Normal traps can spawn on any tile that has open terrain, is in a room, isn't in a Kecleon shop, doesn't already have an item or enemy spawn, and isn't a special tile like a Key door. Monster House traps follow the same conditions as Monster House items.\n\nThe player can spawn on any tile that has open terrain, is in a room, isn't in a Kecleon shop, isn't a hallway junction, doesn't already have an item, enemy, or trap spawn, and isn't a special tile like a Key door.\n\nr0: floor properties\nr1: empty Monster House flag. An empty Monster House is one with no items or traps, and only a small number of enemies.",
    )

    MarkEnemySpawns = Symbol(
        None,
        None,
        None,
        "Mark tiles for all enemies, which includes normal enemies and those in Monster Houses. Note that this only marks tiles; actual spawning is handled later in SpawnInitialMonsters.\n\nNormal enemies can spawn on any tile that has open terrain, isn't in a Kecleon shop, doesn't already have another entity spawn, and isn't a special tile like a Key door.\n\nMonster House enemies can spawn on any Monster House tile that isn't in a Kecleon shop, isn't where the player spawns, and isn't a special tile like a Key door.\n\nr0: floor properties\nr1: empty Monster House flag. An empty Monster House is one with no items or traps, and only a small number of enemies.",
    )

    SetSecondaryTerrainOnWall = Symbol(
        None,
        None,
        None,
        "Set a specific tile to have secondary terrain (water/lava), but only if it's a passable wall.\n\nr0: tile pointer",
    )

    GenerateSecondaryTerrainFormations = Symbol(
        None,
        None,
        None,
        "Generate secondary terrain (water/lava) formations.\n\nThis includes 'rivers' that flow from top-to-bottom (or bottom-to-top), as well as 'lakes' both standalone and after rivers. Water/lava formations will never cut through rooms, but they can pass through rooms to the opposite side.\n\nRivers are generated by a top-down or bottom-up random walk that ends when existing secondary terrain is reached or the walk goes out of bounds. Some rivers also end prematurely in a lake. Lakes are a large collection of secondary terrain generated around a central point.\n\nr0: bit index to test in the floor properties room flag bitvector (formations are only generated if the bit is set)\nr1: floor properties",
    )

    StairsAlwaysReachable = Symbol(
        None,
        None,
        None,
        "Checks that the stairs are reachable from every walkable tile on the floor.\n\nThis runs a graph traversal algorithm that is very similar to breadth-first search (the order in which nodes are visited is slightly different), starting from the stairs. If any tile is walkable but wasn't reached by the traversal algorithm, then the stairs must not be reachable from that tile.\n\nr0: x coordinate of the stairs\nr1: y coordinate of the stairs\nr2: flag to always return true, but set a special bit on all walkable tiles that aren't reachable from the stairs\nreturn: bool",
    )

    GetNextFixedRoomAction = Symbol(
        None,
        None,
        None,
        "Returns the next action that needs to be performed when spawning a fixed room tile.\n\nreturn: Next action ID",
    )

    ConvertWallsToChasms = Symbol(
        None, None, None, "Converts all wall tiles to chasms.\n\nNo params."
    )

    ResetInnerBoundaryTileRows = Symbol(
        None,
        None,
        None,
        "Reset the inner boundary tile rows (y == 1 and y == 30) to their initial state of all wall tiles, with impassable walls at the edges (x == 0 and x == 55).\n\nNo params.",
    )

    ResetImportantSpawnPositions = Symbol(
        None,
        None,
        None,
        "Resets important spawn positions (the player, stairs, and hidden stairs) back to their default values.\n\nr0: dungeon generation info pointer (a field on the dungeon struct)",
    )

    SpawnStairs = Symbol(
        None,
        None,
        None,
        "Spawn stairs at the given location.\n\nIf the hidden stairs type is something other than HIDDEN_STAIRS_NONE, hidden stairs of the specified type will be spawned instead of normal stairs.\n\nIf spawning normal stairs and the current floor is a rescue floor, the room containing the stairs will be converted into a Monster House.\n\nIf attempting to spawn hidden stairs but the spawn is blocked, the floor generation status's hidden stairs spawn position will be updated, but it won't be transferred to the dungeon generation info struct.\n\nr0: position (two-byte array for {x, y})\nr1: dungeon generation info pointer (a field on the dungeon struct)\nr2: hidden stairs type",
    )

    GetHiddenStairsType = Symbol(
        None,
        None,
        None,
        "Gets the hidden stairs type for a given floor.\n\nThis function reads the floor properties and resolves any randomness (such as HIDDEN_STAIRS_RANDOM_SECRET_BAZAAR_OR_SECRET_ROOM and the floor_properties::hidden_stairs_spawn_chance) into a concrete hidden stairs type.\n\nr0: dungeon generation info pointer\nr1: floor properties pointer\nreturn: enum hidden_stairs_type",
    )

    GetFinalKecleonShopSpawnChance = Symbol(
        None,
        None,
        None,
        "Gets the kecleon shop spawn chance for the floor.\n\nWhen dungeon::boost_kecleon_shop_spawn_chance is false, returns the same value as the input. When it's true, returns the input (chance * 1.2).\n\nr0: base kecleon shop spawn chance, floor_properties::kecleon_shop_spawn_chance\nreturn: int",
    )

    ResetHiddenStairsSpawn = Symbol(
        None,
        None,
        None,
        "Resets hidden stairs spawn information for the floor. This includes the position on the floor generation status as well as the flag indicating whether the spawn was blocked.\n\nNo params.",
    )

    PlaceFixedRoomTile = Symbol(
        None,
        None,
        None,
        "Used to spawn a single tile when generating a fixed room. The tile might contain an item or a monster.\n\nr0: Pointer to the tile to spawn\nr1: Fixed room action to perform. Controls what exactly will be spawned. The action is actually 12 bits long, the highest 4 bits are used as a parameter that represents a direction (for example, when spawning a monster).\nr2: Tile X position\nr3: Tile Y position",
    )

    FixedRoomActionParamToDirection = Symbol(
        None,
        None,
        None,
        "Converts the parameter stored in a fixed room action value to a direction ID.\n\nThe conversion is performed by subtracting 1 to the value. If the parameter had a value of 0, DIR_NONE is returned.\n\nr0: Parameter value\nreturn: Direction",
    )

    ApplyKeyEffect = Symbol(
        None,
        None,
        None,
        "Attempts to open a locked door in front of the target if a locked door has not already\nbeen open on the floor.\n\nr0: user entity pointer\nr1: target entity pointer",
    )

    LoadFixedRoomData = Symbol(
        None,
        None,
        None,
        "Loads fixed room data from BALANCE/fixed.bin into the buffer pointed to by FIXED_ROOM_DATA_PTR.\n\nNo params.",
    )

    LoadFixedRoom = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OpenFixedBin = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nNo params."
    )

    CloseFixedBin = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nNo params."
    )

    AreOrbsAllowed = Symbol(
        None,
        None,
        None,
        "Checks if orbs are usable in the given fixed room.\n\nAlways true if not a full-floor fixed room.\n\nr0: fixed room ID\nreturn: bool",
    )

    AreTileJumpsAllowed = Symbol(
        None,
        None,
        None,
        "Checks if tile jumps (warping, being blown away, and leaping) are allowed in the given fixed room.\n\nAlways true if not a full-floor fixed room.\n\nr0: fixed room ID\nreturn: bool",
    )

    AreTrawlOrbsAllowed = Symbol(
        None,
        None,
        None,
        "Checks if Trawl Orbs work in the given fixed room.\n\nAlways true if not a full-floor fixed room.\n\nr0: fixed room ID\nreturn: bool",
    )

    AreOrbsAllowedVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for InitMemAllocTable.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nr0: fixed room ID\nreturn: bool",
    )

    AreLateGameTrapsEnabled = Symbol(
        None,
        None,
        None,
        "Check if late-game traps (Summon, Pitfall, and Pokémon traps) work in the given fixed room.\n\nOr disabled? This function, which Irdkwia's notes label as a disable check, check the struct field labeled in End's notes as an enable flag.\n\nr0: fixed room ID\nreturn: bool",
    )

    AreMovesEnabled = Symbol(
        None,
        None,
        None,
        "Checks if moves (excluding the regular attack) are usable in the given fixed room.\n\nr0: fixed room ID\nreturn: bool",
    )

    IsRoomIlluminated = Symbol(
        None,
        None,
        None,
        "Checks if the given fixed room is fully illuminated.\n\nr0: fixed room ID\nreturn: bool",
    )

    GetMatchingMonsterId = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: monster ID\nr1: ?\nr2: ?\nreturn: monster ID",
    )

    GenerateItemExplicit = Symbol(
        None,
        None,
        None,
        "Initializes an item struct with the given information.\n\nThis calls InitStandardItem, then explicitly sets the quantity and stickiness. If quantity == 0 for Poké, GenerateCleanItem is used instead.\n\nr0: pointer to item to initialize\nr1: item ID\nr2: quantity\nr3: sticky flag",
    )

    GenerateAndSpawnItem = Symbol(
        None,
        None,
        None,
        "A convenience function that generates an item with GenerateItemExplicit, then spawns it with SpawnItem.\n\nIf the check-in-bag flag is set and the player's bag already contains an item with the given ID, a Reviver Seed will be spawned instead.\n\nIt seems like this function is only ever called in one place, with an item ID of 0x49 (Reviver Seed).\n\nr0: item ID\nr1: x position\nr2: y position\nr3: quantity\nstack[0]: sticky flag\nstack[1]: check-in-bag flag",
    )

    IsHiddenStairsFloor = Symbol(
        None,
        None,
        None,
        "Checks if the current floor is either the Secret Bazaar or a Secret Room.\n\nreturn: bool",
    )

    IsSecretBazaarVeneer = Symbol(
        None,
        None,
        None,
        "Likely a linker-generated veneer for IsSecretBazaar.\n\nSee https://developer.arm.com/documentation/dui0474/k/image-structure-and-generation/linker-generated-veneers/what-is-a-veneer-\n\nreturn: bool",
    )

    GenerateStandardItem = Symbol(
        None,
        None,
        None,
        "Wrapper around GenerateItem with quantity set to 0\n\nr0: pointer to item to initialize\nr1: item ID\nr2: stickiness type",
    )

    GenerateCleanItem = Symbol(
        None,
        None,
        None,
        "Wrapper around GenerateItem with quantity set to 0 and stickiness type set to SPAWN_STICKY_NEVER.\n\nr0: pointer to item to initialize\nr1: item ID",
    )

    TryLeaderItemPickUp = Symbol(
        None,
        None,
        None,
        "Checks the tile at the specified position and determines if the leader should pick up an item.\n\nr0: position\nr1: flag for whether or not a message should be logged upon the leader failing to obtain the item",
    )

    SpawnItem = Symbol(
        None,
        None,
        None,
        "Spawns an item on the floor. Fails if there are more than 64 items already on the floor.\n\nThis calls SpawnItemEntity, fills in the item info struct, sets the entity to be visible, binds the entity to the tile it occupies, updates the n_items counter on the dungeon struct, and various other bits of bookkeeping.\n\nr0: position\nr1: item pointer\nr2: some flag?\nreturn: success flag",
    )

    RemoveGroundItem = Symbol(
        None,
        None,
        None,
        "Removes an item lying on the ground.\n\nAlso updates dungeon::n_items.\n\nr0: Position where the item is located\nr1: If true, update dungeon::poke_buy_kecleon_shop and dungeon::poke_sold_kecleon_shop",
    )

    SpawnDroppedItemWrapper = Symbol(
        None,
        None,
        None,
        "Wraps SpawnDroppedItem in a more convenient interface.\n\nr0: entity\nr1: position\nr2: item\nr3: ?",
    )

    SpawnDroppedItem = Symbol(
        None,
        None,
        None,
        "Used to spawn an item that was thrown or dropped, with a log message.\n\nDetermines where exactly the item will land, if it bounces on a trap, etc.\nUsed for thrown items that hit a wall, for certain enemy drops (such as Unown stones or Treasure Boxes), for certain moves (like Pay Day and Knock Off), and possibly other things.\n\nr0: entity that dropped or threw the item\nr1: item entity. Contains the coordinates where the item should try to land first.\nr2: item info\nr3: ?\nstack[0]: pointer to int16_t[2] for x/y direction (corresponding to DIRECTIONS_XY)\nstack[1]: ?",
    )

    TryGenerateUnownStoneDrop = Symbol(
        None,
        None,
        None,
        "Determine if a defeated monster should drop a Unown Stone, and generate the item if so.\n\nChecks that the current dungeon isn't a Marowak Dojo training maze, and that the monster is an Unown. If so, there's a 21% chance that an Unown Stone will be generated.\n\nr0: [output] item\nr1: monster ID\nreturn: whether or not an Unown Stone was generated",
    )

    HasHeldItem = Symbol(
        None,
        None,
        None,
        "Checks if a monster has a certain held item.\n\nr0: entity pointer\nr1: item ID\nreturn: bool",
    )

    GenerateMoneyQuantity = Symbol(
        None,
        None,
        None,
        "Set the quantity code on an item (assuming it's Poké), given some maximum acceptable money amount.\n\nr0: item pointer\nr1: max money amount (inclusive)",
    )

    CheckTeamItemsFlags = Symbol(
        None,
        None,
        None,
        "Checks whether any of the items in the bag or any of the items carried by team members has any of the specified flags set in its flags field.\n\nr0: Flag(s) to check (0 = f_exists, 1 = f_in_shop, 2 = f_unpaid, etc.)\nreturn: True if any of the items of the team has the specified flags set, false otherwise.",
    )

    AddHeldItemToBag = Symbol(
        None,
        None,
        None,
        "Adds the monster's held item to the bag. This is only called on monsters on the exploration team.\nmonster::is_not_team_member should be checked to be false before calling.\n\nr0: monster pointer",
    )

    RemoveEmptyItemsInBagWrapper = Symbol(
        None,
        None,
        None,
        "Calls RemoveEmptyItemsInBag, then some other function that seems to update the minimap, the map surveyor flag, and other stuff.\n\nNo params.",
    )

    GenerateItem = Symbol(
        None,
        None,
        None,
        "Initializes an item struct with the given information.\n\nThis wraps InitItem, but with extra logic to resolve the item's stickiness. It also calls GenerateMoneyQuantity for Poké.\n\nr0: pointer to item to initialize\nr1: item ID\nr2: quantity\nr3: stickiness type (enum gen_item_stickiness)",
    )

    DoesProjectileHitTarget = Symbol(
        None,
        None,
        None,
        "Determines if a hurled projectile will impact on a target or if the target will dodge it instead.\n\nContains a random chance using THROWN_ITEM_HIT_CHANCE, as well as some additional checks involving certain items (Whiff Specs, Lockon Specs and Dodge Scarf), exclusive item effects (EXCLUSIVE_EFF_THROWN_ITEM_PROTECTION) or pokémon (Kecleon, clients, secret bazaar NPCs).\n\nr0: Monster that throws the item\nr1: Target monster\nreturn: True if the item impacts on the target, false if the target dodges the item.",
    )

    DisplayFloorCard = Symbol(
        None,
        None,
        None,
        "Dispatches the splash screen between floors showing the dungeon name and the current floor.\n\nFirst it checks whether the current floor is a secret bazaar or secret room, then it calls HandleFloorCard.\n\nr0: Duration in frames",
    )

    HandleFloorCard = Symbol(
        None,
        None,
        None,
        "Handles the display of the splash screen between floors showing the dungeon name and the current floor.\n\nSeems to enter a loop where it calls AdvanceFrame until the desired number of frames is waited or A is pressed.\n\nr0: dungeon_id\nr1: floor\nr2: duration\nr3: enum hidden_stairs_type",
    )

    CheckActiveChallengeRequest = Symbol(
        None,
        None,
        None,
        "Checks if there's an active challenge request on the current dungeon.\n\nreturn: True if there's an active challenge request on the current dungeon in the list of missions.",
    )

    GetMissionDestination = Symbol(
        None,
        None,
        None,
        "Returns the current mission destination on the dungeon struct.\n\nreturn: &dungeon::mission_destination",
    )

    IsOutlawOrChallengeRequestFloor = Symbol(
        None,
        None,
        None,
        "Checks if the current floor is an active mission destination of type MISSION_TAKE_ITEM_FROM_OUTLAW, MISSION_ARREST_OUTLAW or MISSION_CHALLENGE_REQUEST.\n\nreturn: bool",
    )

    IsDestinationFloor = Symbol(
        None,
        None,
        None,
        "Checks if the current floor is a mission destination floor.\n\nreturn: bool",
    )

    IsCurrentMissionType = Symbol(
        None,
        None,
        None,
        "Checks if the current floor is an active mission destination of a given type (and any subtype).\n\nr0: mission type\nreturn: bool",
    )

    IsCurrentMissionTypeExact = Symbol(
        None,
        None,
        None,
        "Checks if the current floor is an active mission destination of a given type and subtype.\n\nr0: mission type\nr1: mission subtype\nreturn: bool",
    )

    IsOutlawMonsterHouseFloor = Symbol(
        None,
        None,
        None,
        "Checks if the current floor is a mission destination for a Monster House outlaw mission.\n\nreturn: bool",
    )

    IsGoldenChamber = Symbol(
        None,
        None,
        None,
        "Checks if the current floor is a Golden Chamber floor.\n\nreturn: bool",
    )

    IsLegendaryChallengeFloor = Symbol(
        None,
        None,
        None,
        "Checks if the current floor is a boss floor for a Legendary Challenge Letter mission.\n\nreturn: bool",
    )

    IsJirachiChallengeFloor = Symbol(
        None,
        None,
        None,
        "Checks if the current floor is the boss floor in Star Cave Pit for Jirachi's Challenge Letter mission.\n\nreturn: bool",
    )

    IsDestinationFloorWithMonster = Symbol(
        None,
        None,
        None,
        "Checks if the current floor is a mission destination floor with a special monster.\n\nSee FloorHasMissionMonster for details.\n\nreturn: bool",
    )

    LoadMissionMonsterSprites = Symbol(
        None,
        None,
        None,
        "Loads the sprites of monsters that appear on the current floor because of a mission, if applicable.\n\nThis includes monsters to be rescued, outlaws and its minions.\n\nNo params.",
    )

    MissionTargetEnemyIsDefeated = Symbol(
        None,
        None,
        None,
        "Checks if the target enemy of the mission on the current floor has been defeated.\n\nreturn: bool",
    )

    SetMissionTargetEnemyDefeated = Symbol(
        None,
        None,
        None,
        "Set the flag for whether or not the target enemy of the current mission has been defeated.\n\nr0: new flag value",
    )

    IsDestinationFloorWithFixedRoom = Symbol(
        None,
        None,
        None,
        "Checks if the current floor is a mission destination floor with a fixed room.\n\nThe entire floor can be a fixed room layout, or it can just contain a Sealed Chamber.\n\nreturn: bool",
    )

    GetItemToRetrieve = Symbol(
        None,
        None,
        None,
        "Get the ID of the item that needs to be retrieve on the current floor for a mission, if one exists.\n\nreturn: item ID",
    )

    GetItemToDeliver = Symbol(
        None,
        None,
        None,
        "Get the ID of the item that needs to be delivered to a mission client on the current floor, if one exists.\n\nreturn: item ID",
    )

    GetSpecialTargetItem = Symbol(
        None,
        None,
        None,
        "Get the ID of the special target item for a Sealed Chamber or Treasure Memo mission on the current floor.\n\nreturn: item ID",
    )

    IsDestinationFloorWithItem = Symbol(
        None,
        None,
        None,
        "Checks if the current floor is a mission destination floor with a special item.\n\nThis excludes missions involving taking an item from an outlaw.\n\nreturn: bool",
    )

    IsDestinationFloorWithHiddenOutlaw = Symbol(
        None,
        None,
        None,
        "Checks if the current floor is a mission destination floor with a 'hidden outlaw' that behaves like a normal enemy.\n\nreturn: bool",
    )

    IsDestinationFloorWithFleeingOutlaw = Symbol(
        None,
        None,
        None,
        "Checks if the current floor is a mission destination floor with a 'fleeing outlaw' that runs away.\n\nreturn: bool",
    )

    GetMissionTargetEnemy = Symbol(
        None,
        None,
        None,
        "Get the monster ID of the target enemy to be defeated on the current floor for a mission, if one exists.\n\nreturn: monster ID",
    )

    GetMissionEnemyMinionGroup = Symbol(
        None,
        None,
        None,
        "Get the monster ID of the specified minion group on the current floor for a mission, if it exists.\n\nNote that a single minion group can correspond to multiple actual minions of the same species. There can be up to 2 minion groups.\n\nr0: minion group index (0-indexed)\nreturn: monster ID",
    )

    SetTargetMonsterNotFoundFlag = Symbol(
        None,
        None,
        None,
        "Sets dungeon::target_monster_not_found_flag to the specified value.\n\nr0: Value to set the flag to",
    )

    GetTargetMonsterNotFoundFlag = Symbol(
        None,
        None,
        None,
        "Gets the value of dungeon::target_monster_not_found_flag.\n\nreturn: dungeon::target_monster_not_found_flag",
    )

    FloorHasMissionMonster = Symbol(
        None,
        None,
        None,
        "Checks if a given floor is a mission destination with a special monster, either a target to rescue or an enemy to defeat.\n\nMission types with a monster on the destination floor:\n- Rescue client\n- Rescue target\n- Escort to target\n- Deliver item\n- Search for target\n- Take item from outlaw\n- Arrest outlaw\n- Challenge Request\n\nr0: mission destination info pointer\nreturn: bool",
    )

    GenerateMissionEggMonster = Symbol(
        None,
        None,
        None,
        "Generates the monster ID in the egg from the given mission. Uses the base form of the monster.\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: mission struct",
    )

    LogMessageByIdWithPopupCheckParticipants = Symbol(
        None,
        None,
        None,
        "Logs the appropriate message based on the participating entites; this function calls LogMessageByIdWithPopupCheckUserTarget is both the user and target pointers are non-null, otherwise it calls LogMessageByIdWithPopupCheckUser if the user pointer is non-null, otherwise doesn't log anything.\n\nThis function also seems to set some global table entry to some value?\n\nr0: user entity pointer\nr1: target entity pointer\nr2: message ID\nr3: index into some table?\nstack[0]: value to set at the table index specified by r3?",
    )

    LogMessageByIdWithPopupCheckUser = Symbol(
        None,
        None,
        None,
        "Logs a message in the message log alongside a message popup, if the user hasn't fainted.\n\nr0: user entity pointer\nr1: message ID",
    )

    LogMessageWithPopupCheckUser = Symbol(
        None,
        None,
        None,
        "Logs a message in the message log alongside a message popup, if the user hasn't fainted.\n\nr0: user entity pointer\nr1: message string",
    )

    LogMessageByIdQuiet = Symbol(
        None,
        None,
        None,
        "Logs a message in the message log (but without a message popup).\n\nr0: user entity pointer\nr1: message ID",
    )

    LogMessageQuiet = Symbol(
        None,
        None,
        None,
        "Logs a message in the message log (but without a message popup).\n\nr0: user entity pointer\nr1: message string",
    )

    LogMessageByIdWithPopupCheckUserTarget = Symbol(
        None,
        None,
        None,
        "Logs a message in the message log alongside a message popup, if some user check passes and the target hasn't fainted.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: message ID",
    )

    LogMessageWithPopupCheckUserTarget = Symbol(
        None,
        None,
        None,
        "Logs a message in the message log alongside a message popup, if some user check passes and the target hasn't fainted.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: message string",
    )

    LogMessageByIdQuietCheckUserTarget = Symbol(
        None,
        None,
        None,
        "Logs a message in the message log (but without a message popup), if some user check passes and the target hasn't fainted.\n\nr0: user entity pointer\nr1: target entity pointer\nr2: message ID",
    )

    LogMessageByIdWithPopupCheckUserUnknown = Symbol(
        None,
        None,
        None,
        "Logs a message in the message log alongside a message popup, if the user hasn't fainted and some other unknown check.\n\nr0: user entity pointer\nr1: ?\nr2: message ID",
    )

    LogMessageByIdWithPopup = Symbol(
        None,
        None,
        None,
        "Logs a message in the message log alongside a message popup.\n\nr0: user entity pointer\nr1: message ID",
    )

    LogMessageWithPopup = Symbol(
        None,
        None,
        None,
        "Logs a message in the message log alongside a message popup.\n\nr0: user entity pointer\nr1: message string",
    )

    LogMessage = Symbol(
        None,
        None,
        None,
        "Logs a message in the message log.\n\nr0: user entity pointer\nr1: message string\nr2: bool, whether or not to present a message popup",
    )

    LogMessageById = Symbol(
        None,
        None,
        None,
        "Logs a message in the message log.\n\nr0: user entity pointer\nr1: message ID\nr2: bool, whether or not to present a message popup",
    )

    InitPortraitDungeon = Symbol(
        None,
        None,
        None,
        "Initialize the portrait params structure for the given monster and expression\n\nr0: pointer the portrait params data structure to initialize\nr1: monster id\nr2: emotion id",
    )

    OpenMessageLog = Symbol(
        None, None, None, "Opens the message log window.\n\nr0: ?\nr1: ?"
    )

    RunDungeonMode = Symbol(
        None,
        None,
        None,
        "This appears to be the top-level function for running dungeon mode.\n\nIt gets called by MainGame right after doing the dungeon fade transition, and once it exits, the dungeon results are processed.\n\nThis function is presumably in charge of allocating the dungeon struct, setting it up, launching the dungeon engine, etc.",
    )

    StartFadeDungeon = Symbol(
        None,
        None,
        None,
        "Initiates a screen fade in dungeon mode.\n\nSets the fields of the dungeon_fade struct to appropriate values given in the args.\n\nr0: Dungeon fade struct\nr1: Change of brightness per frame\nr2: Fade type",
    )

    StartFadeDungeonWrapper = Symbol(
        None,
        None,
        None,
        "Calls StartFadeDungeon to initiate a screen fade in dungeon mode.\n\nSets the status field in the dungeon_fades struct to the fade type, then uses a switch-case to create a mapping of the status enums to different ones for some reason. This mapped value is then used in the StartFadeDungeon call.\n\nr0: Fade type\nr1: Change of brightness per frame\nr2: Screen to fade",
    )

    HandleFadesDungeon = Symbol(
        None,
        None,
        None,
        "Gets called every frame for both screens in dungeon mode. Handles the status of the screen fades.\n\nr0: enum screen",
    )

    HandleFadesDungeonBothScreens = Symbol(
        None, None, None, "Calls HandleFadesDungeon for both screens.\n\nNo params."
    )

    DisplayFloorTip = Symbol(
        None,
        None,
        None,
        "Display the dungeon tip that displays on floor change, based on which tips have already been displayed.\n\nNo params.\n\nreturn: 1 if a tip has been displayed, 0 otherwise",
    )

    DisplayItemTip = Symbol(
        None,
        None,
        None,
        "Display the dungeon tip if not already displayed matching the (presumably newly acquired) item\n\nr0: item id\nreturn: 1 if a tip has been displayed, 0 otherwise",
    )

    DisplayDungeonTip = Symbol(
        None,
        None,
        None,
        "Checks if a given dungeon tip should be displayed at the start of a floor and if so, displays it. Called up to 4 times at the start of each new floor, with a different r0 parameter each time.\n\nr0: Pointer to the message_tip struct of the message that should be displayed\nr1: True to log the message in the message log\n\nreturn: 1 if the message has been displayed, 0 if it wasn’t",
    )

    SetBothScreensWindowColorToDefault = Symbol(
        None,
        None,
        None,
        "This changes the palettes of windows in both screens to an appropiate value depending on the playthrough\nIf you're in a special episode, they turn green , otherwise, they turn blue or pink depending on your character's sex\n\nNo params",
    )

    GetPersonalityIndex = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: monster pointer\nreturn: ?",
    )

    DisplayMessage = Symbol(
        None,
        None,
        None,
        "Displays a message in a dialogue box that optionally waits for player input before closing.\n\nr0: pointer to the structure representing the desired state of the portrait\nr1: ID of the string to display\nr2: True to wait for player input before closing the dialogue box, false to close it automatically once all the characters get printed.",
    )

    DisplayMessage2 = Symbol(None, None, None, "Very similar to DisplayMessage")

    YesNoMenu = Symbol(
        None,
        None,
        None,
        "Opens a menu where the user can choose 'Yes' or 'No' and waits for input before returning.\n\nr0: ?\nr1: ID of the string to display in the textbox\nr2: Option that the cursor will be on by default. 0 for 'Yes', 1 for 'No'\nr3: ?\nreturn: True if the user chooses 'Yes', false if the user chooses 'No'",
    )

    DisplayMessageInternal = Symbol(
        None,
        None,
        None,
        "Called by DisplayMessage. Seems to be the function that handles the display of the dialogue box. It won't return until all the characters have been written and after the player manually closes the dialogue box (if the corresponding parameter was set).\n\nr0: ID of the string to display\nr1: True to wait for player input before closing the dialogue box, false to close it automatically once all the characters get printed.\nr2: pointer to the structure representing the desired state of the portrait\nr3: ?\nstack[0]: ?\nstack[1]: ?",
    )

    OpenMenu = Symbol(
        None,
        None,
        None,
        "Opens a menu. The menu to open depends on the specified parameter.\n\nIt looks like the function takes a parameter in r0, but doesn't use it. r1 doesn't even get set when this function is called.\n\nr0: (?) Unused by the function. Seems to be 1 byte long.\nr1: (?) Unused by the function. Seems to be 1 byte long.\nr2: True to open the bag menu, false to open the main dungeon menu",
    )

    OthersMenuLoop = Symbol(
        None,
        None,
        None,
        "Called on each frame while the in-dungeon 'others' menu is open.\n\nIt contains a switch to determine whether an option has been chosen or not and a second switch that determines what to do depending on which option was chosen.\n\nreturn: int (Actually, this is probably some sort of enum shared by all the MenuLoop functions)",
    )

    OthersMenu = Symbol(
        None,
        None,
        None,
        "Called when the in-dungeon 'others' menu is open. Does not return until the menu is closed.\n\nreturn: Always 0",
    )


class NaItcmOverlay29Data:

    DUNGEON_STRUCT_SIZE = Symbol(
        None, None, None, "Size of the dungeon struct (0x2CB14)"
    )

    MAX_HP_CAP = Symbol(
        None, None, None, "The maximum amount of HP a monster can have (999)."
    )

    OFFSET_OF_DUNGEON_FLOOR_PROPERTIES = Symbol(
        None,
        None,
        None,
        "Offset of the floor properties field in the dungeon struct (0x286B2)",
    )

    SPAWN_RAND_MAX = Symbol(
        None,
        None,
        None,
        "Equal to 10,000 (0x2710). Used as parameter for DungeonRandInt to generate the random number which determines the entity to spawn.",
    )

    DUNGEON_PRNG_LCG_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The multiplier shared by all of the dungeon PRNG's LCGs, 1566083941 (0x5D588B65).",
    )

    DUNGEON_PRNG_LCG_INCREMENT_SECONDARY = Symbol(
        None,
        None,
        None,
        "The increment for the dungeon PRNG's secondary LCGs, 2531011 (0x269EC3). This happens to be the same increment that the Microsoft Visual C++ runtime library uses in its implementation of the rand() function.",
    )

    KECLEON_FEMALE_ID = Symbol(
        None,
        None,
        None,
        "0x3D7 (983). Used when spawning Kecleon on an even numbered floor.",
    )

    KECLEON_MALE_ID = Symbol(
        None,
        None,
        None,
        "0x17F (383). Used when spawning Kecleon on an odd numbered floor.",
    )

    MSG_ID_SLOW_START = Symbol(
        None,
        None,
        None,
        "ID of the message printed when a monster has the ability Slow Start at the beginning of the floor.",
    )

    EXPERIENCE_POINT_GAIN_CAP = Symbol(
        None,
        None,
        None,
        "A cap on the experience that can be given to a monster in one call to AddExpSpecial",
    )

    JUDGMENT_MOVE_ID = Symbol(
        None, None, None, "Move ID for Judgment (0x1D3)\n\ntype: enum move_id"
    )

    REGULAR_ATTACK_MOVE_ID = Symbol(
        None, None, None, "Move ID for the regular attack (0x163)\n\ntype: enum move_id"
    )

    DEOXYS_ATTACK_ID = Symbol(
        None,
        None,
        None,
        "Monster ID for Deoxys in Attack Forme (0x1A3)\n\ntype: enum monster_id",
    )

    DEOXYS_SPEED_ID = Symbol(
        None,
        None,
        None,
        "Monster ID for Deoxys in Speed Forme (0x1A5)\n\ntype: enum monster_id",
    )

    GIRATINA_ALTERED_ID = Symbol(
        None,
        None,
        None,
        "Monster ID for Giratina in Altered Forme (0x211)\n\ntype: enum monster_id",
    )

    PUNISHMENT_MOVE_ID = Symbol(
        None, None, None, "Move ID for Punishment (0x1BD)\n\ntype: enum move_id"
    )

    OFFENSE_STAT_MAX = Symbol(
        None,
        None,
        None,
        "Cap on an attacker's modified offense (attack or special attack) stat after boosts. Used during damage calculation.",
    )

    PROJECTILE_MOVE_ID = Symbol(
        None,
        None,
        None,
        "The move ID of the special 'projectile' move (0x195)\n\ntype: enum move_id",
    )

    BELLY_LOST_PER_TURN = Symbol(
        None,
        None,
        None,
        "The base value by which belly is decreased every turn.\n\nIts raw value is 0x199A, which encodes a binary fixed-point number (16 fraction bits) with value (0x199A * 2^-16), and is the closest approximation to 0.1 representable in this number format.",
    )

    MONSTER_HEAL_HP_MAX = Symbol(
        None, None, None, "The maximum amount of HP a monster can have (999)."
    )

    MOVE_TARGET_AND_RANGE_SPECIAL_USER_HEALING = Symbol(
        None,
        None,
        None,
        "The move target and range code for special healing moves that target just the user (0x273).\n\ntype: struct move_target_and_range (+ padding)",
    )

    PLAIN_SEED_STRING_ID = Symbol(
        None, None, None, "The string ID for eating a Plain Seed (0xBE9)."
    )

    MAX_ELIXIR_PP_RESTORATION = Symbol(
        None,
        None,
        None,
        "The amount of PP restored per move by ingesting a Max Elixir (0x3E7).",
    )

    SLIP_SEED_FAIL_STRING_ID = Symbol(
        None, None, None, "The string ID for when eating the Slip Seed fails (0xC75)."
    )

    ROCK_WRECKER_MOVE_ID = Symbol(
        None, None, None, "The move ID for Rock Wrecker (453)."
    )

    CASTFORM_NORMAL_FORM_MALE_ID = Symbol(
        None, None, None, "Castform's male normal form ID (0x17B)"
    )

    CASTFORM_NORMAL_FORM_FEMALE_ID = Symbol(
        None, None, None, "Castform's female normal form ID (0x3D3)"
    )

    CHERRIM_SUNSHINE_FORM_MALE_ID = Symbol(
        None, None, None, "Cherrim's male sunshine form ID (0x1CD)"
    )

    CHERRIM_OVERCAST_FORM_FEMALE_ID = Symbol(
        None, None, None, "Cherrim's female overcast form ID (0x424)"
    )

    CHERRIM_SUNSHINE_FORM_FEMALE_ID = Symbol(
        None, None, None, "Cherrim's female sunshine form ID (0x425)"
    )

    FLOOR_GENERATION_STATUS_PTR = Symbol(
        None,
        None,
        None,
        "Pointer to the global FLOOR_GENERATION_STATUS\n\ntype: struct floor_generation_status*",
    )

    OFFSET_OF_DUNGEON_N_NORMAL_ITEM_SPAWNS = Symbol(
        None,
        None,
        None,
        "Offset of the (number of base items + 1) field on the dungeon struct (0x12AFA)",
    )

    DUNGEON_GRID_COLUMN_BYTES = Symbol(
        None,
        None,
        None,
        "The number of bytes in one column of the dungeon grid cell array, 450, which corresponds to a column of 15 grid cells.",
    )

    DEFAULT_MAX_POSITION = Symbol(
        None,
        None,
        None,
        "A large number (9999) to use as a default position for keeping track of min/max position values",
    )

    OFFSET_OF_DUNGEON_GUARANTEED_ITEM_ID = Symbol(
        None,
        None,
        None,
        "Offset of the guaranteed item ID field in the dungeon struct (0x2C9E8)",
    )

    FIXED_ROOM_TILE_SPAWN_TABLE = Symbol(
        None,
        None,
        None,
        "Table of tiles that can spawn in fixed rooms, pointed into by the FIXED_ROOM_TILE_SPAWN_TABLE.\n\nThis is an array of 11 4-byte entries containing info about one tile each. Info includes the trap ID if a trap, room ID, and flags.\n\ntype: struct fixed_room_tile_spawn_entry[11]",
    )

    TREASURE_BOX_1_ITEM_IDS = Symbol(
        None,
        None,
        None,
        "Item IDs for variant 1 of each of the treasure box items (ITEM_*_BOX_1).\n\ntype: struct item_id_16[12]",
    )

    FIXED_ROOM_REVISIT_OVERRIDES = Symbol(
        None,
        None,
        None,
        "Table of fixed room IDs, which if nonzero, overrides the normal fixed room ID for a floor (which is used to index the table) if the dungeon has already been cleared previously.\n\nOverrides are used to substitute different fixed room data for things like revisits to story dungeons.\n\ntype: struct fixed_room_id_8[256]",
    )

    FIXED_ROOM_MONSTER_SPAWN_TABLE = Symbol(
        None,
        None,
        None,
        "Table of monsters that can spawn in fixed rooms, pointed into by the FIXED_ROOM_ENTITY_SPAWN_TABLE.\n\nThis is an array of 120 4-byte entries containing info about one monster each. Info includes the monster ID, stats, and behavior type.\n\ntype: struct fixed_room_monster_spawn_entry[120]",
    )

    FIXED_ROOM_ITEM_SPAWN_TABLE = Symbol(
        None,
        None,
        None,
        "Table of items that can spawn in fixed rooms, pointed into by the FIXED_ROOM_ENTITY_SPAWN_TABLE.\n\nThis is an array of 63 8-byte entries containing one item ID each.\n\ntype: struct fixed_room_item_spawn_entry[63]",
    )

    FIXED_ROOM_ENTITY_SPAWN_TABLE = Symbol(
        None,
        None,
        None,
        "Table of entities (items, monsters, tiles) that can spawn in fixed rooms, which is indexed into by the main data structure for each fixed room.\n\nThis is an array of 269 entries. Each entry contains 3 pointers (one into FIXED_ROOM_ITEM_SPAWN_TABLE, one into FIXED_ROOM_MONSTER_SPAWN_TABLE, and one into FIXED_ROOM_TILE_SPAWN_TABLE), and represents the entities that can spawn on one specific tile in a fixed room.\n\ntype: struct fixed_room_entity_spawn_entry[269]",
    )

    STATUS_ICON_ARRAY_MUZZLED = Symbol(
        None,
        None,
        None,
        "Array of bit masks used to set monster::status_icon. Indexed by monster::statuses::muzzled * 8. See UpdateStatusIconFlags for details.",
    )

    STATUS_ICON_ARRAY_MAGNET_RISE = Symbol(
        None,
        None,
        None,
        "Array of bit masks used to set monster::status_icon. Indexed by monster::statuses::magnet_rise * 8. See UpdateStatusIconFlags for details.",
    )

    STATUS_ICON_ARRAY_MIRACLE_EYE = Symbol(
        None,
        None,
        None,
        "Array of bit masks used to set monster::status_icon. Indexed by monster::statuses::miracle_eye * 8. See UpdateStatusIconFlags for details.",
    )

    STATUS_ICON_ARRAY_LEECH_SEED = Symbol(
        None,
        None,
        None,
        "Array of bit masks used to set monster::status_icon. Indexed by monster::statuses::leech_seed * 8. See UpdateStatusIconFlags for details.",
    )

    STATUS_ICON_ARRAY_LONG_TOSS = Symbol(
        None,
        None,
        None,
        "Array of bit masks used to set monster::status_icon. Indexed by monster::statuses::long_toss * 8. See UpdateStatusIconFlags for details.",
    )

    STATUS_ICON_ARRAY_BLINDED = Symbol(
        None,
        None,
        None,
        "Array of bit masks used to set monster::status_icon. Indexed by monster::statuses::blinded * 8. See UpdateStatusIconFlags for details.",
    )

    STATUS_ICON_ARRAY_BURN = Symbol(
        None,
        None,
        None,
        "Array of bit masks used to set monster::status_icon. Indexed by monster::statuses::burn * 8. See UpdateStatusIconFlags for details.",
    )

    STATUS_ICON_ARRAY_SURE_SHOT = Symbol(
        None,
        None,
        None,
        "Array of bit masks used to set monster::status_icon. Indexed by monster::statuses::sure_shot * 8. See UpdateStatusIconFlags for details.",
    )

    STATUS_ICON_ARRAY_INVISIBLE = Symbol(
        None,
        None,
        None,
        "Array of bit masks used to set monster::status_icon. Indexed by monster::statuses::invisible * 8. See UpdateStatusIconFlags for details.",
    )

    STATUS_ICON_ARRAY_SLEEP = Symbol(
        None,
        None,
        None,
        "Array of bit masks used to set monster::status_icon. Indexed by monster::statuses::sleep * 8. See UpdateStatusIconFlags for details.",
    )

    STATUS_ICON_ARRAY_CURSE = Symbol(
        None,
        None,
        None,
        "Array of bit masks used to set monster::status_icon. Indexed by monster::statuses::curse * 8. See UpdateStatusIconFlags for details.",
    )

    STATUS_ICON_ARRAY_FREEZE = Symbol(
        None,
        None,
        None,
        "Array of bit masks used to set monster::status_icon. Indexed by monster::statuses::freeze * 8. See UpdateStatusIconFlags for details.",
    )

    STATUS_ICON_ARRAY_CRINGE = Symbol(
        None,
        None,
        None,
        "Array of bit masks used to set monster::status_icon. Indexed by monster::statuses::cringe * 8. See UpdateStatusIconFlags for details.",
    )

    STATUS_ICON_ARRAY_BIDE = Symbol(
        None,
        None,
        None,
        "Array of bit masks used to set monster::status_icon. Indexed by monster::statuses::bide * 8. See UpdateStatusIconFlags for details.",
    )

    STATUS_ICON_ARRAY_REFLECT = Symbol(
        None,
        None,
        None,
        "Array of bit masks used to set monster::status_icon. Indexed by monster::statuses::reflect * 8. See UpdateStatusIconFlags for details.",
    )

    DIRECTIONS_XY = Symbol(
        None,
        None,
        None,
        "An array mapping each direction index to its x and y displacements.\n\nDirections start with 0=down and proceed counterclockwise (see enum direction_id). Displacements for x and y are interleaved and encoded as 2-byte signed integers. For example, the first two integers are [0, 1], which correspond to the x and y displacements for the 'down' direction (positive y means down).",
    )

    DISPLACEMENTS_WITHIN_2_LARGEST_FIRST = Symbol(
        None,
        None,
        None,
        "An array of displacement vectors with max norm <= 2, ordered in descending order by norm.\n\nThe last element, (99, 99), is invalid and used as an end marker.\n\ntype: position[26]",
    )

    DISPLACEMENTS_WITHIN_2_SMALLEST_FIRST = Symbol(
        None,
        None,
        None,
        "An array of displacement vectors with max norm <= 2, ordered in ascending order by norm.\n\nThe last element, (99, 99), is invalid and used as an end marker.\n\ntype: position[26]",
    )

    DISPLACEMENTS_WITHIN_3 = Symbol(
        None,
        None,
        None,
        "An array of displacement vectors with max norm <= 3. The elements are vaguely in ascending order by norm, but not exactly.\n\nThe last element, (99, 99), is invalid and used as an end marker.\n\ntype: position[50]",
    )

    ITEM_CATEGORY_ACTIONS = Symbol(
        None,
        None,
        None,
        "Action ID associated with each item category. Used by GetItemAction.\n\nEach entry is 2 bytes long.",
    )

    FRACTIONAL_TURN_SEQUENCE = Symbol(
        None,
        None,
        None,
        "Read by certain functions that are called by RunFractionalTurn to see if they should be executed.\n\nArray is accessed via a pointer added to some multiple of fractional_turn, so that if the resulting memory location is zero, the function returns.",
    )

    BELLY_DRAIN_IN_WALLS_INT = Symbol(
        None,
        None,
        None,
        "The additional amount by which belly is decreased every turn when inside walls (integer part)",
    )

    BELLY_DRAIN_IN_WALLS_THOUSANDTHS = Symbol(
        None,
        None,
        None,
        "The additional amount by which belly is decreased every turn when inside walls (fractional thousandths)",
    )

    DAMAGE_MULTIPLIER_0_5 = Symbol(
        None,
        None,
        None,
        "A generic damage multiplier of 0.5 used in various places, as a 64-bit fixed-point number with 16 fraction bits.",
    )

    DAMAGE_MULTIPLIER_1_5 = Symbol(
        None,
        None,
        None,
        "A generic damage multiplier of 1.5 used in various places, as a 64-bit fixed-point number with 16 fraction bits.",
    )

    DAMAGE_MULTIPLIER_2 = Symbol(
        None,
        None,
        None,
        "A generic damage multiplier of 2 used in various places, as a 64-bit fixed-point number with 16 fraction bits.",
    )

    CLOUDY_DAMAGE_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The extra damage multiplier for non-Normal-type moves when the weather is Cloudy, as a 64-bit fixed-point number with 16 fraction bits (0.75).",
    )

    SOLID_ROCK_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The extra damage multiplier for super-effective moves when Solid Rock or Filter is active, as a 64-bit fixed-point number with 16 fraction bits (0.75).",
    )

    DAMAGE_FORMULA_MAX_BASE = Symbol(
        None,
        None,
        None,
        "The maximum value of the base damage formula (after DAMAGE_FORMULA_NON_TEAM_MEMBER_MODIFIER application, if relevant), as a 64-bit binary fixed-point number with 16 fraction bits (999).",
    )

    WONDER_GUARD_MULTIPLIER = Symbol(
        None,
        None,
        None,
        "The damage multiplier for moves affected by Wonder Guard, as a 64-bit fixed-point number with 16 fraction bits (0).",
    )

    DAMAGE_FORMULA_MIN_BASE = Symbol(
        None,
        None,
        None,
        "The minimum value of the base damage formula (after DAMAGE_FORMULA_NON_TEAM_MEMBER_MODIFIER application, if relevant), as a 64-bit binary fixed-point number with 16 fraction bits (1).",
    )

    TYPE_DAMAGE_NEGATING_EXCLUSIVE_ITEM_EFFECTS = Symbol(
        None,
        None,
        None,
        "List of exclusive item effects that negate damage of a certain type, terminated by a TYPE_NEUTRAL entry.\n\ntype: struct damage_negating_exclusive_eff_entry[28]",
    )

    TWO_TURN_MOVES_AND_STATUSES = Symbol(
        None,
        None,
        None,
        "List that matches two-turn move IDs to their corresponding status ID. The last entry is null.",
    )

    SPATK_STAT_IDX = Symbol(
        None,
        None,
        None,
        "The index (1) of the special attack entry in internal stat structs, such as the stat modifier array for a monster.",
    )

    ATK_STAT_IDX = Symbol(
        None,
        None,
        None,
        "The index (0) of the attack entry in internal stat structs, such as the stat modifier array for a monster.",
    )

    ROLLOUT_DAMAGE_MULT_TABLE = Symbol(
        None,
        None,
        None,
        "A table of damage multipliers for each successive hit of Rollout/Ice Ball. Each entry is a binary fixed-point number with 8 fraction bits.\n\ntype: int32_t[10]",
    )

    MAP_COLOR_TABLE = Symbol(
        None,
        None,
        None,
        "In order: white, black, red, green, blue, magenta, dark pink, chartreuse, light orange\n\nNote: unverified, ported from Irdkwia's notes\n\ntype: struct rgba[9]",
    )

    CORNER_CARDINAL_NEIGHBOR_IS_OPEN = Symbol(
        None,
        None,
        None,
        "An array mapping each (corner index, neighbor direction index) to whether or not that neighbor is expected to be open floor.\n\nCorners start with 0=top-left and proceed clockwise. Directions are enumerated as with DIRECTIONS_XY. The array is indexed by i=(corner_index * N_DIRECTIONS + direction). An element of 1 (0) means that starting from the specified corner of a room, moving in the specified direction should lead to an open floor tile (non-open terrain like a wall).\n\nNote that this array is only used for the cardinal directions. The elements at odd indexes are unused and unconditionally set to 0.\n\nThis array is used by the dungeon generation algorithm when generating room imperfections. See GenerateRoomImperfections.",
    )

    GUMMI_LIKE_STRING_IDS = Symbol(
        None,
        None,
        None,
        "List that holds the string IDs for how much a monster liked a gummi in decreasing order.",
    )

    GUMMI_IQ_STRING_IDS = Symbol(
        None,
        None,
        None,
        "List that holds the string IDs for how much a monster's IQ was raised by in decreasing order.",
    )

    DAMAGE_STRING_IDS = Symbol(
        None,
        None,
        None,
        "List that matches the damage_message ID to their corresponding string ID. The null entry at 0xE in the middle is for hunger. The last entry is null.",
    )

    DUNGEON_PTR = Symbol(
        None,
        None,
        None,
        "[Runtime] Pointer to the dungeon struct in dungeon mode.\n\nThis is a 'working copy' of DUNGEON_PTR_MASTER. The main dungeon engine uses this pointer (or rather pointers to this pointer) when actually running dungeon mode.\n\ntype: struct dungeon*",
    )

    DUNGEON_PTR_MASTER = Symbol(
        None,
        None,
        None,
        "[Runtime] Pointer to the dungeon struct in dungeon mode.\n\nThis is a 'master copy' of the dungeon pointer. The game uses this pointer when doing low-level memory work (allocation, freeing, zeroing). The normal DUNGEON_PTR is used for most other dungeon mode work.\n\ntype: struct dungeon*",
    )

    TOP_SCREEN_STATUS_PTR = Symbol(
        None,
        None,
        None,
        "[Runtime] Pointer for struct for handling the status of the top screen in dungeon mode.\n\ntype: struct top_screen_status",
    )

    LEADER_PTR = Symbol(
        None,
        None,
        None,
        "[Runtime] Pointer to the current leader of the team.\n\ntype: struct entity*",
    )

    DUNGEON_PRNG_STATE = Symbol(
        None,
        None,
        None,
        "[Runtime] The global PRNG state for dungeon mode, not including the current values in the secondary sequences.\n\nThis struct holds state for the primary LCG, as well as the current configuration controlling which LCG to use when generating random numbers. See DungeonRand16Bit for more information on how the dungeon PRNG works.\n\ntype: struct prng_state",
    )

    DUNGEON_PRNG_STATE_SECONDARY_VALUES = Symbol(
        None,
        None,
        None,
        "[Runtime] An array of 5 integers corresponding to the last value generated for each secondary LCG sequence.\n\nBased on the assembly, this appears to be its own global array, separate from DUNGEON_PRNG_STATE.",
    )

    LOADED_ATTACK_SPRITE_FILE_INDEX = Symbol(
        None,
        None,
        None,
        "[Runtime] The file index of the currently loaded attack sprite.\n\ntype: uint16_t",
    )

    LOADED_ATTACK_SPRITE_PACK_ID = Symbol(
        None,
        None,
        None,
        "[Runtime] The pack id of the currently loaded attack sprite. Should correspond to the id of m_attack.bin\n\ntype: enum pack_file_id",
    )

    EXCL_ITEM_EFFECTS_WEATHER_ATK_SPEED_BOOST = Symbol(
        None,
        None,
        None,
        "Array of IDs for exclusive item effects that increase attack speed with certain weather conditions.",
    )

    EXCL_ITEM_EFFECTS_WEATHER_MOVE_SPEED_BOOST = Symbol(
        None,
        None,
        None,
        "Array of IDs for exclusive item effects that increase movement speed with certain weather conditions.",
    )

    EXCL_ITEM_EFFECTS_WEATHER_NO_STATUS = Symbol(
        None,
        None,
        None,
        "Array of IDs for exclusive item effects that grant status immunity with certain weather conditions.",
    )

    EXCL_ITEM_EFFECTS_EVASION_BOOST = Symbol(
        None,
        None,
        None,
        "Array of IDs for exclusive item effects that grant an evasion boost with certain weather conditions.",
    )

    DEFAULT_TILE = Symbol(
        None,
        None,
        None,
        "The default tile struct.\n\nThis is just a struct full of zeroes, but is used as a fallback in various places where a 'default' tile is needed, such as when a grid index is out of range.\n\ntype: struct tile",
    )

    HIDDEN_STAIRS_SPAWN_BLOCKED = Symbol(
        None,
        None,
        None,
        "[Runtime] A flag for when Hidden Stairs could normally have spawned on the floor but didn't.\n\nThis is set either when the Hidden Stairs just happen not to spawn by chance, or when the current floor is a rescue or mission destination floor.\n\nThis appears to be part of a larger (8-byte?) struct. It seems like this value is at least followed by 3 bytes of padding and a 4-byte integer field.",
    )

    FIXED_ROOM_DATA_PTR = Symbol(
        None,
        None,
        None,
        "[Runtime] Pointer to decoded fixed room data loaded from the BALANCE/fixed.bin file.",
    )

    DUNGEON_FADES_PTR = Symbol(
        None,
        None,
        None,
        "[Runtime] Pointer to the dungeon fades struct that maintains the status of screen fades in dungeon mode.",
    )

    NECTAR_IQ_BOOST = Symbol(None, None, None, "IQ boost from ingesting Nectar.")


class NaItcmOverlay29Section:
    name = "overlay29"
    description = "The dungeon engine.\n\nThis is the 'main' overlay of dungeon mode. It controls most things that happen in a Mystery Dungeon, such as dungeon layout generation, dungeon menus, enemy AI, and generally just running each turn while within a dungeon."
    loadaddress = None
    length = None
    functions = NaItcmOverlay29Functions
    data = NaItcmOverlay29Data


class NaItcmOverlay3Functions:

    pass


class NaItcmOverlay3Data:

    pass


class NaItcmOverlay3Section:
    name = "overlay3"
    description = "Controls the Friend Rescue submenu within the top menu."
    loadaddress = None
    length = None
    functions = NaItcmOverlay3Functions
    data = NaItcmOverlay3Data


class NaItcmOverlay30Functions:

    WriteQuicksaveData = Symbol(
        None,
        None,
        None,
        "Function responsible for writing dungeon data when quicksaving.\n\nAmong other things, it contains a loop that goes through all the monsters in the current dungeon, copying their data to the buffer. The data is not copied as-is though, the game uses a reduced version of the monster struct containing only the minimum required data to resume the game later.\n\nr0: Pointer to buffer where data should be written\nr1: Buffer size. Seems to be 0x5800 (22 KB) when the function is called.",
    )


class NaItcmOverlay30Data:

    OVERLAY30_JP_STRING_1 = Symbol(None, None, None, "みさき様")

    OVERLAY30_JP_STRING_2 = Symbol(None, None, None, "やよい様")


class NaItcmOverlay30Section:
    name = "overlay30"
    description = "Controls quicksaving in dungeons."
    loadaddress = None
    length = None
    functions = NaItcmOverlay30Functions
    data = NaItcmOverlay30Data


class NaItcmOverlay31Functions:

    EntryOverlay31 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes\n\nNo params."
    )

    DrawDungeonMenuStatusWindow = Symbol(
        None,
        None,
        None,
        "Draws the contents shown in the main dungeon menu status window showing the player's belly, money, play time, etc.\n\nr0: int",
    )

    DungeonMenuSwitch = Symbol(
        None,
        None,
        None,
        "Note: unverified, ported from Irdkwia's notes\n\nr0: appears to be an index of some sort, probably the menu index based on the function name?",
    )

    MovesMenu = Symbol(
        None,
        None,
        None,
        "Displays a menu showing the moves of a monster. Does not return until the menu is closed.\n\nThis function does not get called when opening the leader's move menu.\n\nr0: Pointer to an action struct containing the index of the monster whose moves will be checked in the action_use_idx field.",
    )

    HandleMovesMenuWrapper0 = Symbol(
        None,
        None,
        None,
        "Sets some field on a struct to 0 and calls HandleMovesMenu.\n\nr0: struct pointer, see HandleMovesMenu\nr1: See HandleMovesMenu\nr2: See HandleMovesMenu\nr3: monster index, see HandleMovesMenu\nreturn: bool, see HandleMovesMenu",
    )

    HandleMovesMenuWrapper1 = Symbol(
        None,
        None,
        None,
        "Sets some field on a struct to 1 and calls HandleMovesMenu.\n\nr0: struct pointer, see HandleMovesMenu\nr1: See HandleMovesMenu\nr2: See HandleMovesMenu\nr3: monster index, see HandleMovesMenu\nreturn: bool, see HandleMovesMenu",
    )

    HandleMovesMenu = Symbol(
        None,
        None,
        None,
        "Handles the different options on the moves menu. Does not return until the menu is closed.\n\nThis function also takes care of updating the fields in the action_data struct it receives when a menu option is chosen.\n\nr0: Pointer to some struct that was created by a previous function. Contains a pointer to the monster whose moves are being displayed at offset 0x0.\nr1: ?\nr2: ?\nr3: Index of the monster whose moves are going to be displayed on the menu. Unused.\nreturn: True if the menu was closed without selecting anything, false if an option was chosen.",
    )

    TeamMenu = Symbol(
        None,
        None,
        None,
        "Called when the in-dungeon 'team' menu is open. Does not return until the menu is closed.\n\nNote that selecting certain options in this menu (such as viewing the details or the moves of a pokémon) counts as switching to a different menu, which causes the function to return.\n\nr0: Pointer to the leader's entity struct\nreturn: ?",
    )

    RestMenu = Symbol(
        None,
        None,
        None,
        "Called when the in-dungeon 'rest' menu is open. Does not return until the menu is closed.\n\nNo params.",
    )

    RecruitmentSearchMenuLoop = Symbol(
        None,
        None,
        None,
        "Called on each frame while the in-dungeon 'recruitment search' menu is open.\n\nreturn: int (Actually, this is probably some sort of enum shared by all the MenuLoop functions)",
    )

    HelpMenuLoop = Symbol(
        None,
        None,
        None,
        "Called on each frame while the in-dungeon 'help' menu is open.\n\nThe menu is still considered open while one of the help pages is being viewed, so this function keeps being called even after choosing an option.\n\nreturn: int (Actually, this is probably some sort of enum shared by all the MenuLoop functions)",
    )


class NaItcmOverlay31Data:

    DUNGEON_WINDOW_PARAMS_1 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_2 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_3 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_4 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_MAIN_MENU_ITEMS = Symbol(None, None, None, "")

    OVERLAY31_UNKNOWN_STRING_IDS = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY31_UNKNOWN_STRUCT__NA_2389E30 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_5 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_6 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_7 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_SUBMENU_ITEMS_1 = Symbol(None, None, None, "")

    DUNGEON_SUBMENU_ITEMS_2 = Symbol(None, None, None, "")

    DUNGEON_SUBMENU_ITEMS_3 = Symbol(None, None, None, "")

    DUNGEON_SUBMENU_ITEMS_4 = Symbol(None, None, None, "")

    OVERLAY31_UNKNOWN_STRUCT__NA_2389EF0 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_8 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_9 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_10 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_11 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_12 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_13 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY31_JP_STRING = Symbol(
        None, None, None, "\n\n----　 初期ポジション=%d　----- \n"
    )

    DUNGEON_WINDOW_PARAMS_14 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_15 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_16 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_17 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_18 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_19 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY31_UNKNOWN_STRUCT__NA_2389FE8 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_20 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_21 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_22 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_23 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_24 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_25 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_SUBMENU_ITEMS_5 = Symbol(None, None, None, "")

    DUNGEON_WINDOW_PARAMS_26 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY31_UNKNOWN_STRUCT__NA_238A144 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_27 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_28 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY31_UNKNOWN_STRUCT__NA_238A190 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_SUBMENU_ITEMS_6 = Symbol(None, None, None, "")

    DUNGEON_WINDOW_PARAMS_29 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_30 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_31 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    DUNGEON_WINDOW_PARAMS_32 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY31_RESERVED_SPACE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY31_UNKNOWN_POINTER__NA_238A260 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY31_UNKNOWN_VALUE__NA_238A264 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY31_UNKNOWN_POINTER__NA_238A268 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY31_UNKNOWN_POINTER__NA_238A26C = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY31_UNKNOWN_POINTER__NA_238A270 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY31_UNKNOWN_POINTER__NA_238A274 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY31_UNKNOWN_POINTER__NA_238A278 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY31_UNKNOWN_POINTER__NA_238A27C = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY31_UNKNOWN_POINTER__NA_238A280 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY31_UNKNOWN_POINTER__NA_238A284 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY31_UNKNOWN_POINTER__NA_238A288 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY31_UNKNOWN_POINTER__NA_238A28C = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )


class NaItcmOverlay31Section:
    name = "overlay31"
    description = "Controls the dungeon menu (during dungeon mode)."
    loadaddress = None
    length = None
    functions = NaItcmOverlay31Functions
    data = NaItcmOverlay31Data


class NaItcmOverlay32Functions:

    pass


class NaItcmOverlay32Data:

    pass


class NaItcmOverlay32Section:
    name = "overlay32"
    description = "Unused; all zeroes."
    loadaddress = None
    length = None
    functions = NaItcmOverlay32Functions
    data = NaItcmOverlay32Data


class NaItcmOverlay33Functions:

    pass


class NaItcmOverlay33Data:

    pass


class NaItcmOverlay33Section:
    name = "overlay33"
    description = "Unused; all zeroes."
    loadaddress = None
    length = None
    functions = NaItcmOverlay33Functions
    data = NaItcmOverlay33Data


class NaItcmOverlay34Functions:

    ExplorersOfSkyMain = Symbol(
        None,
        None,
        None,
        "The main function for Explorers of Sky.\n\nNote: unverified, ported from Irdkwia's notes\n\nr0: probably a game mode ID?\nreturn: probably a return code?",
    )


class NaItcmOverlay34Data:

    OVERLAY34_UNKNOWN_STRUCT__NA_22DD014 = Symbol(
        None,
        None,
        None,
        "1*0x4 + 3*0x4\n\nNote: unverified, ported from Irdkwia's notes",
    )

    START_MENU_ITEMS_CONFIRM = Symbol(None, None, None, "")

    OVERLAY34_UNKNOWN_STRUCT__NA_22DD03C = Symbol(
        None,
        None,
        None,
        "1*0x4 + 3*0x4\n\nNote: unverified, ported from Irdkwia's notes",
    )

    DUNGEON_DEBUG_MENU_ITEMS = Symbol(None, None, None, "")

    OVERLAY34_RESERVED_SPACE = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY34_UNKNOWN_POINTER__NA_22DD080 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY34_UNKNOWN_POINTER__NA_22DD084 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY34_UNKNOWN_POINTER__NA_22DD088 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY34_UNKNOWN_POINTER__NA_22DD08C = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )

    OVERLAY34_UNKNOWN_POINTER__NA_22DD090 = Symbol(
        None, None, None, "Note: unverified, ported from Irdkwia's notes"
    )


class NaItcmOverlay34Section:
    name = "overlay34"
    description = "Related to launching the game.\n\nThere are mention in the strings of logos like the ESRB logo. This only seems to be loaded during the ESRB rating splash screen, so this is likely the sole purpose of this overlay."
    loadaddress = None
    length = None
    functions = NaItcmOverlay34Functions
    data = NaItcmOverlay34Data


class NaItcmOverlay35Functions:

    pass


class NaItcmOverlay35Data:

    pass


class NaItcmOverlay35Section:
    name = "overlay35"
    description = "Unused; all zeroes."
    loadaddress = None
    length = None
    functions = NaItcmOverlay35Functions
    data = NaItcmOverlay35Data


class NaItcmOverlay4Functions:

    pass


class NaItcmOverlay4Data:

    pass


class NaItcmOverlay4Section:
    name = "overlay4"
    description = "Controls the Trade Items submenu within the top menu."
    loadaddress = None
    length = None
    functions = NaItcmOverlay4Functions
    data = NaItcmOverlay4Data


class NaItcmOverlay5Functions:

    pass


class NaItcmOverlay5Data:

    pass


class NaItcmOverlay5Section:
    name = "overlay5"
    description = "Controls the Trade Team submenu within the top menu."
    loadaddress = None
    length = None
    functions = NaItcmOverlay5Functions
    data = NaItcmOverlay5Data


class NaItcmOverlay6Functions:

    pass


class NaItcmOverlay6Data:

    pass


class NaItcmOverlay6Section:
    name = "overlay6"
    description = "Controls the Wonder Mail S submenu within the top menu."
    loadaddress = None
    length = None
    functions = NaItcmOverlay6Functions
    data = NaItcmOverlay6Data


class NaItcmOverlay7Functions:

    pass


class NaItcmOverlay7Data:

    pass


class NaItcmOverlay7Section:
    name = "overlay7"
    description = (
        "Controls the Nintendo WFC submenu within the top menu (under 'Other')."
    )
    loadaddress = None
    length = None
    functions = NaItcmOverlay7Functions
    data = NaItcmOverlay7Data


class NaItcmOverlay8Functions:

    pass


class NaItcmOverlay8Data:

    pass


class NaItcmOverlay8Section:
    name = "overlay8"
    description = (
        "Controls the Send Demo Dungeon submenu within the top menu (under 'Other')."
    )
    loadaddress = None
    length = None
    functions = NaItcmOverlay8Functions
    data = NaItcmOverlay8Data


class NaItcmOverlay9Functions:

    CreateJukeboxTrackMenu = Symbol(
        None,
        None,
        None,
        "Creates a window containing the track selection menu for the Sky Jukebox. Also see struct jukebox_track_menu.\n\nIf window_params is NULL, JUKEBOX_TRACK_MENU_DEFAULT_WINDOW_PARAMS will be used. Otherwise, it will be copied onto the window, ignoring the update and contents fields. If window_params::width and/or window_params::height are 0, they will be computed based on the contained text.\n\nIf window_extra_info is non-NULL, it will be copied onto the window. Note that window_extra_info can only be NULL if there are no window_flags set that require extra info.\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: simple_menu_id_item struct array, terminated with an item with string_id 0\nstack[0]: number of menu items\nreturn: window_id",
    )

    CloseJukeboxTrackMenu = Symbol(
        None,
        None,
        None,
        "Closes a window created with CreateJukeboxTrackMenu.\n\nr0: window_id",
    )

    IsJukeboxTrackMenuActive = Symbol(
        None,
        None,
        None,
        "This is a guess.\n\nChecks if the state of a jukebox track menu is something other than 7 or 8.\n\nr0: window_id\nreturn: bool",
    )

    UpdateJukeboxTrackMenu = Symbol(
        None,
        None,
        None,
        "Window update function for jukebox track menus.\n\nr0: window pointer",
    )

    CreatePlaybackControlsMenu = Symbol(
        None,
        None,
        None,
        "Creates a window containing the playback controls menu for a selected song. Also see struct playback_controls_menu.\n\nIf window_params is NULL, PLAYBACK_CONTROLS_MENU_DEFAULT_WINDOW_PARAMS will be used. Otherwise, it will be copied onto the window, ignoring the update and contents fields. If window_params::width and/or window_params::height are 0, they will be computed based on the contained text.\n\nIf window_extra_info is non-NULL, it will be copied onto the window. Note that window_extra_info can only be NULL if there are no window_flags set that require extra info.\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: ?\nstack[0]: simple_menu_id_item struct array 1, terminated with an item with string_id 0\nstack[1]: simple_menu_id_item struct array 2, terminated with an item with string_id 0\nreturn: window_id",
    )

    ClosePlaybackControlsMenu = Symbol(
        None,
        None,
        None,
        "Closes a window created with CreatePlaybackControlsMenu.\n\nr0: window_id",
    )

    IsPlaybackControlsMenuActive = Symbol(
        None,
        None,
        None,
        "This is a guess.\n\nChecks if the state of a playback controls menu is something other than 7 or 8.\n\nr0: window_id\nreturn: bool",
    )

    UpdatePlaybackControlsMenu = Symbol(
        None,
        None,
        None,
        "Window update function for playback controls menus.\n\nr0: window pointer",
    )

    CreateInputLockBox = Symbol(
        None,
        None,
        None,
        "Creates a window containing the 'Locked' text when inputs are locked while a song is playing. Also see struct input_lock_box.\n\nIf window_params is NULL, INPUT_LOCK_BOX_DEFAULT_WINDOW_PARAMS will be used. Otherwise, it will be copied onto the window, ignoring the update and contents fields. If window_params::height is 0, it will default to 2.\n\nIf window_extra_info is non-NULL, it will be copied onto the window. Note that window_extra_info can only be NULL if there are no window_flags set that require extra info.\n\nr0: window_params\nr1: window_flags\nr2: window_extra_info pointer\nr3: ?\nstack[0]: string ID\nreturn: window_id",
    )

    CloseInputLockBox = Symbol(
        None, None, None, "Closes a window created with InputLockBox.\n\nr0: window_id"
    )

    IsInputLockBoxActive = Symbol(
        None,
        None,
        None,
        "This is a guess.\n\nChecks if the state of an input lock box is not 4.\n\nr0: window_id\nreturn: bool",
    )

    UpdateInputLockBox = Symbol(
        None,
        None,
        None,
        "Window update function for input lock boxes.\n\nr0: window pointer",
    )


class NaItcmOverlay9Data:

    JUKEBOX_TRACK_MENU_DEFAULT_WINDOW_PARAMS = Symbol(
        None,
        None,
        None,
        "Default window_params for a jukebox_track_menu.\n\nNote that x_offset and y_offset refer to the right and bottom edges, since they will be paired with the x_offset_end and y_offset_end window flags in CreateJukeboxTrackMenu.\n\nAdditionally, width and height are 0, and will be computed in CreateJukeboxTrackMenu.",
    )

    PLAYBACK_CONTROLS_MENU_DEFAULT_WINDOW_PARAMS = Symbol(
        None,
        None,
        None,
        "Default window_params for a playback_controls_menu.\n\nNote that x_offset and y_offset refer to the right and bottom edges, since they will be paired with the x_offset_end and y_offset_end window flags in CreatePlaybackControlsMenu.\n\nAdditionally, width and height are 0, and will be computed in CreatePlaybackControlsMenu.",
    )

    INPUT_LOCK_BOX_DEFAULT_WINDOW_PARAMS = Symbol(
        None, None, None, "Default window_params for an input_lock_box."
    )

    TOP_MENU_RETURN_MUSIC_ID = Symbol(
        None,
        None,
        None,
        "Song playing in the main menu when returning from the Sky Jukebox.",
    )


class NaItcmOverlay9Section:
    name = "overlay9"
    description = "Controls the Sky Jukebox."
    loadaddress = None
    length = None
    functions = NaItcmOverlay9Functions
    data = NaItcmOverlay9Data


class NaItcmRamFunctions:

    pass


class NaItcmRamData:

    DEFAULT_MEMORY_ARENA_MEMORY = Symbol(
        None,
        None,
        None,
        "The memory region for the default memory arena.\n\nThe length is defined by DEFAULT_MEMORY_ARENA_SIZE.\n\nOne mode that uses this region for heap allocations is dungeon mode.",
    )

    GROUND_MEMORY_ARENA_2 = Symbol(
        None,
        None,
        None,
        "This is a memory subarena under DEFAULT_MEMORY_ARENA used for some things in ground mode.\n\nIt's used for user_flags 14.\n\nIncluding the allocator metadata, this arena occupies 0xB0000 bytes of space.\n\ntype: struct mem_arena",
    )

    GROUND_MEMORY_ARENA_2_BLOCKS = Symbol(
        None,
        None,
        None,
        "The block array for GROUND_MEMORY_ARENA_2.\n\ntype: struct mem_block[32]",
    )

    GROUND_MEMORY_ARENA_2_MEMORY = Symbol(
        None, None, None, "The memory region for GROUND_MEMORY_ARENA_2."
    )

    DUNGEON_COLORMAP_PTR = Symbol(
        None,
        None,
        None,
        "Pointer to a colormap used to render colors in a dungeon.\n\nThe colormap is a list of 4-byte RGB colors of the form {R, G, B, padding}, which the game indexes into when rendering colors. Some weather conditions modify the colormap, which is how the color scheme changes when it's, e.g., raining.",
    )

    DUNGEON_STRUCT = Symbol(
        None,
        None,
        None,
        "The dungeon context struct used for tons of stuff in dungeon mode. See struct dungeon in the C headers.\n\nThis struct never seems to be referenced directly, and is instead usually accessed via DUNGEON_PTR in overlay 29.\n\ntype: struct dungeon",
    )

    MOVE_DATA_TABLE = Symbol(
        None,
        None,
        None,
        "The move data table loaded directly from /BALANCE/waza_p.bin. See struct move_data_table in the C headers.\n\nPointed to by MOVE_DATA_TABLE_PTR in the ARM 9 binary.\n\ntype: struct move_data_table",
    )

    SOUND_MEMORY_ARENA = Symbol(
        None,
        None,
        None,
        "This is a memory subarena under DEFAULT_MEMORY_ARENA that seems to be used exclusively for sound data.\n\nIncluding allocator metadata, this subarena occupies 0x3C000 bytes of space within the default arena.\n\nIt's referenced by various sound functions like LoadDseFile, PlaySeLoad, and PlayBgm when allocating memory.\n\ntype: struct mem_arena",
    )

    SOUND_MEMORY_ARENA_BLOCKS = Symbol(
        None,
        None,
        None,
        "The block array for SOUND_MEMORY_ARENA.\n\ntype: struct mem_block[20]",
    )

    SOUND_MEMORY_ARENA_MEMORY = Symbol(
        None,
        None,
        None,
        "The memory region for SOUND_MEMORY_ARENA.\n\nThis region appears to be used for sound-related heap allocations, like when loading sound files into memory.",
    )

    FRAMES_SINCE_LAUNCH = Symbol(
        None,
        None,
        None,
        "Starts at 0 when the game is first launched, and continuously ticks up once per frame while the game is running.",
    )

    BAG_ITEMS = Symbol(
        None,
        None,
        None,
        "Array of item structs within the player's bag.\n\nWhile the game only allows a maximum of 48 items during normal play, it seems to read up to 50 item slots if filled.\n\ntype: struct item[50]",
    )

    BAG_ITEMS_PTR = Symbol(None, None, None, "Pointer to BAG_ITEMS.")

    STORAGE_ITEMS = Symbol(
        None,
        None,
        None,
        "Array of item IDs in the player's item storage.\n\nFor stackable items, the quantities are stored elsewhere, in STORAGE_ITEM_QUANTITIES.\n\ntype: struct item_id_16[1000]",
    )

    STORAGE_ITEM_QUANTITIES = Symbol(
        None,
        None,
        None,
        "Array of 1000 2-byte (unsigned) quantities corresponding to the item IDs in STORAGE_ITEMS.\n\nIf the corresponding item ID is not a stackable item, the entry in this array is unused, and will be 0.",
    )

    KECLEON_SHOP_ITEMS_PTR = Symbol(None, None, None, "Pointer to KECLEON_SHOP_ITEMS.")

    KECLEON_SHOP_ITEMS = Symbol(
        None,
        None,
        None,
        "Array of up to 8 items in the Kecleon Shop.\n\nIf there are fewer than 8 items, the array is expected to be null-terminated.\n\ntype: struct bulk_item[8]",
    )

    UNUSED_KECLEON_SHOP_ITEMS = Symbol(
        None,
        None,
        None,
        "Seems to be another array like KECLEON_SHOP_ITEMS, but don't actually appear to be used by the Kecleon Shop.",
    )

    KECLEON_WARES_ITEMS_PTR = Symbol(
        None, None, None, "Pointer to KECLEON_WARES_ITEMS."
    )

    KECLEON_WARES_ITEMS = Symbol(
        None,
        None,
        None,
        "Array of up to 4 items in Kecleon Wares.\n\nIf there are fewer than 4 items, the array is expected to be null-terminated.\n\ntype: struct bulk_item[4]",
    )

    UNUSED_KECLEON_WARES_ITEMS = Symbol(
        None,
        None,
        None,
        "Seems to be another array like KECLEON_WARES_ITEMS, but don't actually appear to be used by Kecleon Wares.",
    )

    MONEY_CARRIED = Symbol(
        None, None, None, "The amount of money the player is currently carrying."
    )

    MONEY_STORED = Symbol(
        None,
        None,
        None,
        "The amount of money the player currently has stored in the Duskull Bank.",
    )

    AUDIO_COMMANDS_BUFFER = Symbol(
        None,
        None,
        None,
        "Buffer used to store audio commands. 16 entries in total. Seems like entries are removed at some point (maybe after the commands are read or after they finish executing).",
    )

    CURSOR_16_SPRITE_ID = Symbol(
        None, None, None, "Id of the 'FONT/cursor_16.wan' sprite loaded in WAN_TABLE"
    )

    CURSOR_SPRITE_ID = Symbol(
        None, None, None, "Id of the 'FONT/cursor.wan' sprite loaded in WAN_TABLE"
    )

    CURSOR_ANIMATION_CONTROL = Symbol(
        None, None, None, "animation_control of 'FONT/cursor.wan'"
    )

    CURSOR_16_ANIMATION_CONTROL = Symbol(
        None, None, None, "animation_control of 'FONT/cursor_16.wan'"
    )

    ALERT_SPRITE_ID = Symbol(
        None, None, None, "Id of the 'FONT/alert.wan' sprite loaded in WAN_TABLE"
    )

    ALERT_ANIMATION_CONTROL = Symbol(
        None, None, None, "animation_control of 'FONT/alter.wan'"
    )

    SOUND_MEMORY_ARENA_PTR = Symbol(None, None, None, "Pointer to SOUND_MEMORY_ARENA.")

    WINDOW_LIST = Symbol(
        None,
        None,
        None,
        "Array of all window structs. Newly created window structs are taken from slots in this array.\n\nNote that this array isn't strictly ordered in any way. A newly created window will occupy the first available slot. If a window in an early slot is destroyed, windows that are still active in later slots won't be shifted back unless destroyed and recreated.\n\ntype: struct window_list",
    )

    LAST_NEW_MOVE = Symbol(
        None,
        None,
        None,
        "Move struct of the last new move introduced when learning a new move. Persists even after the move selection is made in the menu.\n\ntype: struct move",
    )

    SCRIPT_VARS_VALUES = Symbol(
        None,
        None,
        None,
        "The table of game variable values. Its structure is determined by SCRIPT_VARS.\n\nNote that with the script variable list defined in SCRIPT_VARS, the used length of this table is actually only 0x2B4. However, the real length of this table is 0x400 based on the game code.\n\ntype: struct script_var_value_table",
    )

    BAG_LEVEL = Symbol(
        None,
        None,
        None,
        "The player's bag level, which determines the bag capacity. This indexes directly into the BAG_CAPACITY_TABLE in the ARM9 binary.",
    )

    DEBUG_SPECIAL_EPISODE_NUMBER = Symbol(
        None,
        None,
        None,
        "The number of the special episode currently being played.\n\nThis backs the EXECUTE_SPECIAL_EPISODE_TYPE script variable.\n\ntype: struct special_episode_type_8",
    )

    KAOMADO_STREAM = Symbol(
        None,
        None,
        None,
        "The file stream utilized for all Kaomado portrait loads.\n\ntype: struct file_stream",
    )

    PENDING_DUNGEON_ID = Symbol(
        None,
        None,
        None,
        "The ID of the selected dungeon when setting off from the overworld.\n\nControls the text and map location during the 'map cutscene' just before entering a dungeon, as well as the actual dungeon loaded afterwards.\n\nThis field is actually part of a larger struct that also contains PENDING_STARTING_FLOOR.\n\ntype: struct dungeon_id_8",
    )

    PENDING_STARTING_FLOOR = Symbol(
        None,
        None,
        None,
        "The floor number to start from in the dungeon specified by PENDING_DUNGEON_ID.",
    )

    PLAY_TIME_SECONDS = Symbol(
        None, None, None, "The player's total play time in seconds."
    )

    PLAY_TIME_FRAME_COUNTER = Symbol(
        None,
        None,
        None,
        "Counts from 0-59 in a loop, with the play time being incremented by 1 second with each rollover.",
    )

    TEAM_NAME = Symbol(
        None,
        None,
        None,
        "The team name.\n\nA null-terminated string, with a maximum length of 10. Presumably encoded with the ANSI/Shift JIS encoding the game typically uses.\n\nThis is presumably part of a larger struct, together with other nearby data.",
    )

    LEVEL_UP_DATA_MONSTER_ID = Symbol(
        None,
        None,
        None,
        "ID of the monster whose level-up data is currently stored in LEVEL_UP_DATA_DECOMPRESS_BUFFER.",
    )

    LEVEL_UP_DATA_DECOMPRESS_BUFFER = Symbol(
        None,
        None,
        None,
        "Buffer used to stored a monster's decompressed level up data. Used by GetLvlUpEntry.\n\nExact size is a guess (100 levels * 12 bytes per entry = 1200 = 0x4B0).",
    )

    TEAM_MEMBER_TABLE = Symbol(
        None,
        None,
        None,
        "Table with all team members, persistent information about them, and information about which ones are currently active.\n\nSee the comments on struct team_member_table for more information.\n\ntype: struct team_member_table",
    )

    DRIVER_WORK = Symbol(None, None, None, "")

    DISP_MODE = Symbol(None, None, None, "")

    GXI_VRAM_LOCK_ID = Symbol(None, None, None, "")

    ENABLED_VRAM_BANKS = Symbol(
        None, None, None, "Bitset of enabled VRAM banks\n\ntype: vram_banks_set"
    )

    SUB_BG_EXT_PLTT = Symbol(None, None, None, "")

    CLR_IMG = Symbol(None, None, None, "")

    THREAD_INFO_STRUCT = Symbol(
        None, None, None, "thread_info struct that contains global state about threads"
    )

    FRAMES_SINCE_LAUNCH_TIMES_THREE = Symbol(
        None,
        None,
        None,
        "Starts at 0 when the game is first launched, and ticks up by 3 per frame while the game is running.",
    )

    GROUND_MEMORY_ARENA_1_PTR = Symbol(
        None, None, None, "Pointer to GROUND_MEMORY_ARENA_1."
    )

    GROUND_MEMORY_ARENA_2_PTR = Symbol(
        None, None, None, "Pointer to GROUND_MEMORY_ARENA_2."
    )

    LOCK_NOTIFY_ARRAY = Symbol(
        None,
        None,
        None,
        "Used to notify scripts waiting for a certain lock to unlock so they can resume their execution.\n\n1 byte per lock. Exact size isn't confirmed, it could potentially be longer.",
    )

    GROUND_MEMORY_ARENA_1 = Symbol(
        None,
        None,
        None,
        "This is a top-level memory arena used for some things in ground mode.\n\nIt's used for user_flags 8, 15, and 16.\n\nIncluding the allocator metadata, this arena occupies 0x64000 bytes of space.\n\ntype: struct mem_arena",
    )

    GROUND_MEMORY_ARENA_1_BLOCKS = Symbol(
        None,
        None,
        None,
        "The block array for GROUND_MEMORY_ARENA_1.\n\ntype: struct mem_block[52]",
    )

    GROUND_MEMORY_ARENA_1_MEMORY = Symbol(
        None, None, None, "The memory region for GROUND_MEMORY_ARENA_1."
    )

    SENTRY_DUTY_STRUCT = Symbol(None, None, None, "")

    TURNING_ON_THE_SPOT_FLAG = Symbol(
        None,
        None,
        None,
        "[Runtime] Flag for whether the player is turning on the spot (pressing Y).",
    )

    LOADED_ATTACK_SPRITE_DATA = Symbol(
        None,
        None,
        None,
        "[Runtime] Pointer to the dynamically allocated structure relating to the currently loaded attack sprite, in dungeon mode.\n\ntype: struct loaded_attack_sprite_data*",
    )

    ROLLOUT_ICE_BALL_MISSED = Symbol(
        None,
        None,
        None,
        "[Runtime] Appears to be set to true whenever a hit from Rollout or Ice Ball fails to deal damage.",
    )

    MULTIHIT_FATIGUE_MOVE_USED = Symbol(
        None,
        None,
        None,
        "[Runtime] Appears to be set to true whenever a multihit fatigue move deals damage.",
    )

    TWINEEDLE_HIT_TRACKER = Symbol(
        None,
        None,
        None,
        "[Runtime] Appears to be set to true whenever Twineedle hits and deals damage. So that even if the second attack misses, it will still try to poison the target.",
    )

    RAPID_SPIN_BINDING_REMOVAL = Symbol(
        None,
        None,
        None,
        "[Runtime] Appears to be set to true when using Rapid Spin to later remove any binding effects and Leech Seed.",
    )

    ROLLOUT_ICE_BALL_SUCCESSIVE_HITS = Symbol(
        None,
        None,
        None,
        "[Runtime] Seems to count the number of successive hits by Rollout or Ice Ball.",
    )

    MULTIHIT_MOVE_SUCCESSIVE_HITS = Symbol(
        None,
        None,
        None,
        "[Runtime] Seems to count the number of successive hits for multihit moves. This is used by Twineedle to check to attempt to apply Poison after the second attack.",
    )

    TRIPLE_KICK_SUCCESSIVE_HITS = Symbol(
        None,
        None,
        None,
        "[Runtime] Seems to count the number of successive hits by Triple Kick.",
    )

    METRONOME_NEXT_INDEX = Symbol(
        None,
        None,
        None,
        "[Runtime] The index into METRONOME_TABLE for the next usage of Metronome.",
    )

    FLOOR_GENERATION_STATUS = Symbol(
        None,
        None,
        None,
        "[Runtime] Status data related to generation of the current floor in a dungeon.\n\nThis data is populated as the dungeon floor is generated.\n\ntype: struct floor_generation_status",
    )


class NaItcmRamSection:
    name = "ram"
    description = "Main memory.\nData in this file aren't located in the ROM itself, and are instead constructs loaded at runtime.\n\nMore specifically, this file is a dumping ground for addresses that are useful to know about, but don't fall in the address ranges of any of the other files. Dynamically loaded constructs that do fall within the address range of a relevant binary should be listed in the corresponding YAML file of that binary, since it still has direct utility when reverse-engineering that particular binary."
    loadaddress = None
    length = None
    functions = NaItcmRamFunctions
    data = NaItcmRamData


class NaItcmSections:

    arm7 = NaItcmArm7Section

    arm9 = NaItcmArm9Section

    itcm = NaItcmItcmSection

    libs = NaItcmLibsSection

    move_effects = NaItcmMove_effectsSection

    overlay0 = NaItcmOverlay0Section

    overlay1 = NaItcmOverlay1Section

    overlay10 = NaItcmOverlay10Section

    overlay11 = NaItcmOverlay11Section

    overlay12 = NaItcmOverlay12Section

    overlay13 = NaItcmOverlay13Section

    overlay14 = NaItcmOverlay14Section

    overlay15 = NaItcmOverlay15Section

    overlay16 = NaItcmOverlay16Section

    overlay17 = NaItcmOverlay17Section

    overlay18 = NaItcmOverlay18Section

    overlay19 = NaItcmOverlay19Section

    overlay2 = NaItcmOverlay2Section

    overlay20 = NaItcmOverlay20Section

    overlay21 = NaItcmOverlay21Section

    overlay22 = NaItcmOverlay22Section

    overlay23 = NaItcmOverlay23Section

    overlay24 = NaItcmOverlay24Section

    overlay25 = NaItcmOverlay25Section

    overlay26 = NaItcmOverlay26Section

    overlay27 = NaItcmOverlay27Section

    overlay28 = NaItcmOverlay28Section

    overlay29 = NaItcmOverlay29Section

    overlay3 = NaItcmOverlay3Section

    overlay30 = NaItcmOverlay30Section

    overlay31 = NaItcmOverlay31Section

    overlay32 = NaItcmOverlay32Section

    overlay33 = NaItcmOverlay33Section

    overlay34 = NaItcmOverlay34Section

    overlay35 = NaItcmOverlay35Section

    overlay4 = NaItcmOverlay4Section

    overlay5 = NaItcmOverlay5Section

    overlay6 = NaItcmOverlay6Section

    overlay7 = NaItcmOverlay7Section

    overlay8 = NaItcmOverlay8Section

    overlay9 = NaItcmOverlay9Section

    ram = NaItcmRamSection
