# MMORPG Attribute & Fatigue System – Formula Reference

## 🧮 Attribute System (Finalized – Pre-Combat Integration)

### 1. Strength (STR)
- **Lifting Capacity**  
  ```
  Lifting Capacity = STR × 10 (kg)
  ```
- **Physical Damage Bonus**  
  *(Applies to all physical damage types: melee, ranged, etc.)*  
  ```
  Total Physical Damage = Base Weapon Damage + STR
  ```
- **Shield Damage Reduction** *(Varies by shield type)*  
  ```
  Damage Blocked = STR × Shield Multiplier
  ```
  - Buckler = STR × 1  
  - Small Shield = STR × 2  
  - Medium Shield = STR × 3  
  - Large Shield = STR × 4  
  - Tower Shield = STR × 5

### 2. Dexterity (DEX)
- **Base Chance to Hit**  
  *(Should include weapon accuracy, enemy evasion, skill modifiers, and buffs/debuffs)*  
  ```
  Base Hit Chance = DEX + Other Modifiers
  ```
- **Parry Chance**  
  ```
  Parry Chance = DEX + Other Modifiers
  ```
- **Block Chance** *(Passive if shield is equipped)*  
  ```
  Block Chance = DEX + Other Modifiers
  ```
- **Lockpicking Success**  
  ```
  Lockpicking Success = DEX+Lockpicking Skill Level-Lock Difficulty
  ```

### 3. Agility (AGI)
- **Dodge Chance**  
  ```
  Dodge Chance = AGI + Other Modifiers
  ```


### 4. Constitution (CON)
- **Base HP**  
  ```
  Base HP = CON × 100
  ```
-   ```
- **HP Recovery (Out of Combat)**  
  ```
  HP Recovery = (CON÷2)(HP/sec)
  ```
- **Poison/Disease Resistance**  
  ```
  Resistance Bonus = CON + Other Modifiers
  ```

### 5. Stamina (STA)
- **Activity Duration**
  - Normal Activities  
    ```
    Duration = STA(hours)
    ```
  - Moderate Activities  
    ```
    Duration = STA (minutes)
    ```
  - Heavy Activities  
    ```
    Duration = STA ÷ 2 (minutes)
    ```
- **Fatigue Recovery Rate**  
  ```
  Fatigue Recovery = 1 Fatigue per (STA × 10) seconds
  ```

### 6. Intelligence (INT)
- **XP/KP Gain Modifier**  
  ```
  XP/KP Gained = INT
  ```
- **Max Spell Rank Learnable**  
  ```
  Max Spell Rank = INT ÷ 2
  ```
- **Mana Pool**  
  ```
  Base MP = INT×100
  ```
- **Mana Recovery (Out of Combat)**  
  ```
  Mana Recovery = INT÷2(MP/sec)
  ```

### 7. Wisdom (WIS)
- **Spell Damage Bonus**  
  ```
  Total Spell Damage = Base + WIS
  ```
- **Mana Cost Reduction**  
  ```
  Final Mana Cost = Base-(WIS ÷ 10)
  ```

### 8. Willpower (WIL)
- **Mind-Affecting Spell Resistance**  
  ```
  Mind Resistance = Base + WIL (%)
  ```
- **Magic Resistance Bonus**  
  ```
  Magic Resistance = WIL ÷ 2 (%)
  ```

### 9. Charisma (CHA)
- **Success Rate for Charm, Fear, Taming, Intimidation**  
  ```
  Success Chance = Base Success Rate + CHA (%)
  ```

## 💤 Fatigue & Exhaustion System

- **Fatigue Accumulation**  
  ```
  Fatigue Gained = 1 per minute of overexertion
  ```
- **Fatigue Effects per Point**
  - Movement Speed:  
    ```
    −0.5% per Fatigue Point
    ```
  - Attribute Penalty:  
    ```
    −0.5% per Fatigue Point
    ```

- **Exhaustion Threshold**
  - At 10 Fatigue:  
    ```
    All Attributes = Base × 0.9
    ```
    - Applies 1 stack of the “Exhausted” debuff
  - At 10 Exhausted stacks:
    - Player is rendered unconscious
    - Forcefully logged out for 24 hours
    - Teleported to the nearest safe zone

## 👤 Character Creation Rules

- **Build Points Pool**  
  ```
  122 Build points available
  ```
  Build points are used to set starting attributtes and to select starting skills
- **Starting Attributes**  
  ```
 0 points per attribute
  ```
- **Attribute Cap**  
  ```
  Max per attribute = 50
  Minimum per attribute = 1
  ```

## ⚠️ Design Notes

- Several formulas reference “+ Other Modifiers” — these depend on:
  - Weapons, skills, buffs, and enemy defenses (e.g., dodge vs hit chance)
  - External resistance systems (poisons, magic)
- Agility’s mitigation values and block/dodge interaction will be revised after combat mechanics are finalized.

Climbing Skill = 10 + (DEX ÷ 2) + (AGI ÷ 2) + (Mountaineering bonus) + (Climb Walls Bonus) 